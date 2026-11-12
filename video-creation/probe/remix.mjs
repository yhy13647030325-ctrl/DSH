#!/usr/bin/env node
/**
 * video-creation/probe/remix.mjs
 *
 * 混剪：读 probe.json，按用户指定的镜头清单裁切 + 重排 + 拼接，可加转场与字幕。
 *
 * 用法：
 *   node remix.mjs <probe.json> --shots 0,2,1 [--out 输出.mp4]
 *                     [--transition fade] [--transition-dur 0.5]
 *                     [--subtitles 字幕.srt] [--scale 1280x720] [--mute]
 *
 * 例：
 *   node remix.mjs probe-out/probe.json --shots 2,0,1 --transition fade --out remix.mp4
 *     （把 3 个镜头倒序重排，加 0.5s 淡入淡出）
 *
 * 退出码：0 成功；1 参数；2 工具缺失；3 执行失败
 */
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";

function findTool(name, envVar) {
  if (process.env[envVar] && fs.existsSync(process.env[envVar])) return process.env[envVar];
  const w = process.platform === "win32" ? "where" : "which";
  const r = spawnSync(w, [name], { encoding: "utf8" });
  if (r.status === 0 && r.stdout) {
    const p = r.stdout.split(/\r?\n/).map(s => s.trim()).find(Boolean);
    if (p && fs.existsSync(p)) return p;
  }
  const home = process.env.DSH_HOME || path.join(os.homedir(), ".dsh");
  const staticFirst = [
    path.join(home, "_work", "ffmpeg-tool", "node_modules", "ffmpeg-static", `${name}.exe`),
    path.join(home, "_work", "ffmpeg-tool", "node_modules",
      name === "ffmpeg" ? "@ffmpeg-installer" : "@ffprobe-installer", "win32-x64", `${name}.exe`),
  ];
  for (const c of staticFirst) if (fs.existsSync(c)) return c;
  return null;
}

function parseArgs(argv) {
  const pos = [];
  const o = { shots: "", out: "", transition: "", transitionDur: "0.5", subtitles: "", scale: "", mute: false };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--shots") o.shots = argv[++i];
    else if (a === "--out") o.out = argv[++i];
    else if (a === "--transition") o.transition = argv[++i];
    else if (a === "--transition-dur") o.transitionDur = argv[++i];
    else if (a === "--subtitles") o.subtitles = argv[++i];
    else if (a === "--scale") o.scale = argv[++i];
    else if (a === "--mute") o.mute = true;
    else if (a.startsWith("--")) { console.error("unknown flag", a); process.exit(1); }
    else pos.push(a);
  }
  return { pos, o };
}

function main() {
  const { pos, o } = parseArgs(process.argv.slice(2));
  const probeFile = pos[0];
  if (!probeFile || !o.shots) {
    console.error("usage: node remix.mjs <probe.json> --shots 0,2,1 [--out x.mp4] [--transition fade] [--subtitles s.srt] [--scale WxH] [--mute]");
    process.exit(1);
  }
  const ffmpeg = findTool("ffmpeg", "FFMPEG_PATH");
  if (!ffmpeg) { console.error("ffmpeg 未找到"); process.exit(2); }

  const pp = path.resolve(probeFile);
  if (!fs.existsSync(pp)) { console.error("probe.json 不存在:", pp); process.exit(1); }
  const probe = JSON.parse(fs.readFileSync(pp, "utf8"));
  const baseDir = path.dirname(pp);
  const srcVideo = path.resolve(baseDir, "..", probe.meta.file);
  // meta.file 可能只是 basename；尝试在同级/上级找
  let video = srcVideo;
  if (!fs.existsSync(video)) {
    const alt = path.resolve(baseDir, probe.meta.file);
    if (fs.existsSync(alt)) video = alt;
    else { console.error("找不到源视频:", probe.meta.file); process.exit(1); }
  }

  const idx = o.shots.split(",").map(s => parseInt(s.trim(), 10)).filter(n => !isNaN(n));
  if (!idx.length) { console.error("--shots 为空"); process.exit(1); }
  for (const n of idx) {
    if (!probe.shots[n]) { console.error(`镜头 ${n} 不存在（共 ${probe.shots.length} 个）`); process.exit(1); }
  }

  const out = o.out ? path.resolve(o.out) : path.join(baseDir, `remix-${Date.now()}.mp4`);
  const dur = parseFloat(o.transitionDur);

  console.log(`[remix] 源:   ${video}`);
  console.log(`[remix] 镜头: ${idx.join(", ")}（原 ${probe.shots.length} 个中选 ${idx.length} 个）`);
  console.log(`[remix] 输出: ${out}`);

  // ---- 逐段裁切到临时目录（优先输出目录旁，避免系统 Temp 被沙箱拦截）
  const tmpDir = path.join(path.dirname(out), `_segments-${Date.now()}`);
  fs.mkdirSync(tmpDir, { recursive: true });
  const segs = [];
  idx.forEach((n, i) => {
    const s = probe.shots[n];
    const seg = path.join(tmpDir, `seg_${i}.mp4`);
    const args = ["-ss", String(s.startSec), "-t", String(s.durationSec), "-i", video];
    const vf = [];
    if (o.scale) vf.push(`scale=${o.scale.replace("x", ":")}`);
    if (vf.length) args.push("-vf", vf.join(","));
    args.push("-an", "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-y", seg);
    const r = spawnSync(ffmpeg, args, { encoding: "utf8" });
    if (r.status !== 0 || !fs.existsSync(seg)) {
      console.error(`[remix] 镜头 ${n} 裁切失败`);
      process.exit(3);
    }
    segs.push(seg);
    console.log(`[remix]   镜头 ${n}: ${s.startSec}s → ${s.endSec}s (${s.durationSec}s)`);
  });

  // ---- 拼接（带转场则用 xfade 链，否则 concat）
  let finalArgs;
  // ---- 拼接。转场分两档：
  //   fade → 用 fade 滤镜给每段头尾做淡入淡出后 concat（兼容旧 ffmpeg，无 xfade 依赖）
  //   xfade → 需要 ffmpeg 4.3+；运行时探测滤镜是否存在，不存在则自动降级为 fade
  let transitionMode = o.transition;
  if (transitionMode === "xfade") {
    const hasXfade = spawnSync(ffmpeg, ["-hide_banner", "-filters"], { encoding: "utf8" })
      .stdout.includes("xfade");
    if (!hasXfade) {
      console.warn("[remix] 当前 ffmpeg 不支持 xfade，自动降级为 fade 转场");
      transitionMode = "fade";
    }
  }

  if (transitionMode === "fade") {
    // 每段单独加 fade in/out，再 concat
    const faded = [];
    const fd = Math.min(dur, 0.5);
    segs.forEach((s, i) => {
      const f = path.join(tmpDir, `fade_${i}.mp4`);
      const r = spawnSync(ffmpeg, ["-i", s, "-vf",
        `fade=t=in:st=0:d=${fd},fade=t=out:st=${(probe.shots[idx[i]].durationSec - fd).toFixed(3)}:d=${fd}`,
        "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-y", f], { encoding: "utf8" });
      if (r.status === 0 && fs.existsSync(f)) faded.push(f);
      else faded.push(s);
    });
    const list = path.join(tmpDir, "list.txt");
    fs.writeFileSync(list, faded.map(s => `file '${s.replace(/\\/g, "/")}'`).join("\n"), "utf8");
    finalArgs = ["-f", "concat", "-safe", "0", "-i", list, "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p"];
  } else if (transitionMode === "xfade") {
    const inputs = [];
    segs.forEach(s => inputs.push("-i", s));
    const parts = [];
    let offset = 0;
    for (let i = 1; i < segs.length; i++) {
      const inPrev = i === 1 ? "0:v" : `x${i - 1}`;
      const inCur = `${i}:v`;
      const outLabel = i === segs.length - 1 ? "vout" : `x${i}`;
      offset += probe.shots[idx[i - 1]].durationSec - dur;
      parts.push(`[${inPrev}][${inCur}]xfade=transition=fade:duration=${dur}:offset=${offset.toFixed(3)}[${outLabel}]`);
    }
    finalArgs = [...inputs, "-filter_complex", parts.join(";"), "-map", "[vout]", "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p"];
  } else {
    const list = path.join(tmpDir, "list.txt");
    fs.writeFileSync(list, segs.map(s => `file '${s.replace(/\\/g, "/").replace(/'/g, "'\\''")}'`).join("\n"), "utf8");
    finalArgs = ["-f", "concat", "-safe", "0", "-i", list, "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p"];
  }

  // ---- 音频：保留原音轨（按镜头顺序裁切）或静音
  if (o.mute) {
    finalArgs.push("-an");
  } else if (probe.audio && probe.audio.hasAudioTrack) {
    // 简化：整体叠加原音频对应时间段
    const audioSegs = [];
    idx.forEach((n, i) => {
      const s = probe.shots[n];
      const aseg = path.join(tmpDir, `aseg_${i}.wav`);
      const r = spawnSync(ffmpeg, ["-ss", String(s.startSec), "-t", String(s.durationSec), "-i", video, "-vn", "-ac", "1", "-y", aseg], { encoding: "utf8" });
      if (r.status === 0 && fs.existsSync(aseg)) audioSegs.push(aseg);
    });
    if (audioSegs.length) {
      const alist = path.join(tmpDir, "alist.txt");
      fs.writeFileSync(alist, audioSegs.map(s => `file '${s.replace(/\\/g, "/")}'`).join("\n"), "utf8");
      const amix = path.join(tmpDir, "audio.wav");
      const r = spawnSync(ffmpeg, ["-f", "concat", "-safe", "0", "-i", alist, "-c", "copy", "-y", amix], { encoding: "utf8" });
      if (r.status === 0 && fs.existsSync(amix)) {
        // 音频输入必须插在所有视频输入之后、filter_complex/map 之前
        const fcAt = finalArgs.indexOf("-filter_complex");
        const mapAt = finalArgs.indexOf("-map");
        const cut = fcAt >= 0 ? fcAt : (mapAt >= 0 ? mapAt : finalArgs.length);
        const head = finalArgs.slice(0, cut);
        const tail = finalArgs.slice(cut);
        // 音频输入序号 = 视频段数（0..n-1），即 audioIdx
        const audioIdx = segs.length;
        finalArgs = [...head, "-i", amix, "-map", `${audioIdx}:a?`, "-c:a", "aac", "-shortest",
                     ...tail];
      }
    }
  }

  // ---- 字幕（烧录）
  if (o.subtitles && fs.existsSync(path.resolve(o.subtitles))) {
    const sub = path.resolve(o.subtitles).replace(/\\/g, "/").replace(/:/g, "\\:");
    finalArgs.push("-vf", `subtitles='${sub}'`);
  }

  finalArgs.push("-y", out);
  const r = spawnSync(ffmpeg, finalArgs, { encoding: "utf8", maxBuffer: 32 * 1024 * 1024 });
  // 清理临时
  try { fs.rmSync(tmpDir, { recursive: true, force: true }); } catch {}

  if (r.status !== 0 || !fs.existsSync(out)) {
    console.error("[remix] ffmpeg 失败:", (r.stderr || "").slice(-800));
    process.exit(3);
  }
  const sz = fs.statSync(out).size;
  console.log(`[remix] ✅ ${out}  (${(sz / 1024 / 1024).toFixed(2)} MB)`);
}

main();
