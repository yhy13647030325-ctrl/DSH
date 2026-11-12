#!/usr/bin/env node
/**
 * video-creation/probe/probe.mjs
 *
 * 视频输入探针：给一个视频文件，产出结构化画像 probe.json
 *   meta      元数据（时长/分辨率/帧率/码率/编码）
 *   scenes    场景切换点（ffmpeg scene detection）
 *   keyframes 关键帧 JPEG 序列（每场景 1 张）
 *   audio     分离音轨（wav）+ 是否有语音
 *   shots     推断镜头表
 *
 * 用法：
 *   node probe.mjs <video> [--out <dir>] [--scene-threshold 0.4] [--max-keyframes 40]
 *
 * 退出码：0 成功；1 参数/文件错误；2 ffmpeg 缺失；3 探针失败
 */
import { spawnSync, spawn } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";

const HERE = path.dirname(new URL(import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, "$1"));

// ---------------------------------------------------------------- ffmpeg 定位
function findTool(name, envVar) {
  if (process.env[envVar] && fs.existsSync(process.env[envVar])) return process.env[envVar];
  // PATH
  const w = process.platform === "win32" ? "where" : "which";
  const r = spawnSync(w, [name], { encoding: "utf8" });
  if (r.status === 0 && r.stdout) {
    const p = r.stdout.split(/\r?\n/).map(s => s.trim()).find(Boolean);
    if (p && fs.existsSync(p)) return p;
  }
  // 已知安装位置
  const candidates = process.platform === "win32"
    ? [
        `C:\\ffmpeg\\bin\\${name}.exe`,
        `C:\\Program Files\\ffmpeg\\bin\\${name}.exe`,
        path.join(os.homedir(), "AppData", "Local", "Microsoft", "WindowsApps", `${name}.exe`),
      ]
    : [`/usr/bin/${name}`, `/usr/local/bin/${name}`, `/opt/homebrew/bin/${name}`];
  for (const c of candidates) if (fs.existsSync(c)) return c;
  // 兜底：本项目 npm 装的 ffmpeg（优先 ffmpeg-static 6.0，其次 @ffmpeg-installer）
  const home = process.env.DSH_HOME || path.join(os.homedir(), ".dsh");
  const staticFirst = [
    path.join(home, "_work", "ffmpeg-tool", "node_modules", "ffmpeg-static", `${name}.exe`),
    path.join(home, "_work", "ffmpeg-tool", "node_modules",
      name === "ffmpeg" ? "@ffmpeg-installer" : "@ffprobe-installer", "win32-x64", `${name}.exe`),
  ];
  for (const c of staticFirst) if (fs.existsSync(c)) return c;
  // 再退一步：任意盘符的工作区
  const wsBase = path.resolve(HERE, "../../../_work/ffmpeg-tool/node_modules");
  const wsCandidates = [
    path.join(wsBase, "ffmpeg-static", `${name}.exe`),
    path.join(wsBase, name === "ffmpeg" ? "@ffmpeg-installer" : "@ffprobe-installer", "win32-x64", `${name}.exe`),
  ];
  for (const c of wsCandidates) if (fs.existsSync(c)) return c;
  return null;
}

// ---------------------------------------------------------------- 工具函数
function run(cmd, args, opts = {}) {
  const r = spawnSync(cmd, args, { encoding: "utf8", maxBuffer: 64 * 1024 * 1024, ...opts });
  return r;
}

function parseTimecode(tc) {
  // HH:MM:SS.ss -> seconds
  const m = /^(\d+):(\d+):(\d+(?:\.\d+)?)$/.exec(tc.trim());
  if (!m) return 0;
  return (+m[1]) * 3600 + (+m[2]) * 60 + parseFloat(m[3]);
}

// ---------------------------------------------------------------- 主流程
async function main() {
  const argv = process.argv.slice(2);
  const pos = [];
  const opts = { sceneThreshold: "0.4", maxKeyframes: "40", out: "" };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--out") opts.out = argv[++i];
    else if (a === "--scene-threshold") opts.sceneThreshold = argv[++i];
    else if (a === "--max-keyframes") opts.maxKeyframes = argv[++i];
    else if (a.startsWith("--")) { console.error("unknown flag", a); process.exit(1); }
    else pos.push(a);
  }
  const video = pos[0];
  if (!video) {
    console.error("usage: node probe.mjs <video> [--out dir] [--scene-threshold 0.4] [--max-keyframes 40]");
    process.exit(1);
  }
  const vpath = path.resolve(video);
  if (!fs.existsSync(vpath)) {
    console.error("文件不存在:", vpath);
    process.exit(1);
  }
  if (/^https?:\/\//i.test(video)) {
    console.error("拒绝处理 URL；probe 只接受本地文件。");
    process.exit(1);
  }

  const ffmpeg = findTool("ffmpeg", "FFMPEG_PATH");
  const ffprobe = findTool("ffprobe", "FFPROBE_PATH");
  if (!ffmpeg || !ffprobe) {
    console.error("ffmpeg/ffprobe 未找到。设置 FFMPEG_PATH/FFPROBE_PATH，或安装 ffmpeg。");
    process.exit(2);
  }

  const outDir = opts.out
    ? path.resolve(opts.out)
    : path.join(path.dirname(vpath), `probe-${path.basename(vpath, path.extname(video))}-${Date.now()}`);
  fs.mkdirSync(outDir, { recursive: true });
  const kfDir = path.join(outDir, "keyframes");
  fs.mkdirSync(kfDir, { recursive: true });

  console.log(`[probe] ffmpeg: ${ffmpeg}`);
  console.log(`[probe] 输入:   ${vpath}`);
  console.log(`[probe] 输出:   ${outDir}`);

  // ---- 1) 元数据
  const metaR = run(ffprobe, [
    "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", vpath
  ]);
  if (metaR.status !== 0) {
    console.error("ffprobe 失败:", metaR.stderr);
    process.exit(3);
  }
  const meta = JSON.parse(metaR.stdout);
  const vstream = (meta.streams || []).find(s => s.codec_type === "video");
  const astream = (meta.streams || []).find(s => s.codec_type === "audio");
  if (!vstream) {
    console.error("未找到视频流；可能不是视频文件。");
    process.exit(3);
  }

  const duration = parseFloat(meta.format.duration || vstream.duration || "0");
  const metaOut = {
    file: path.basename(vpath),
    sizeBytes: +meta.format.size || 0,
    container: meta.format.format_name,
    durationSec: +duration.toFixed(3),
    video: {
      codec: vstream.codec_name,
      width: vstream.width,
      height: vstream.height,
      fps: vstream.avg_frame_rate ? eval(vstream.avg_frame_rate) : null,
      pixFmt: vstream.pix_fmt,
    },
    audio: astream
      ? { codec: astream.codec_name, channels: astream.channels, sampleRate: astream.sample_rate }
      : null,
    bitrate: +meta.format.bit_rate || 0,
  };

  // ---- 2) 场景切换点
  const thr = parseFloat(opts.sceneThreshold);
  const sceneR = run(ffmpeg, [
    "-i", vpath, "-vf", `select='gt(scene,${thr})',showinfo`, "-an", "-f", "null", "-"
  ]);
  const sceneTimes = [];
  const sceneRe = /pts_time:([0-9.]+)/g;
  let mm;
  const sceneLog = (sceneR.stderr || "") + (sceneR.stdout || "");
  while ((mm = sceneRe.exec(sceneLog)) !== null) sceneTimes.push(parseFloat(mm[1]));

  // ---- 3) 关键帧（每场景 1 张，封顶 maxKeyframes）
  const maxKf = parseInt(opts.maxKeyframes, 10);
  const boundaries = [0, ...sceneTimes, duration].filter((v, i, a) => a.indexOf(v) === i).sort((a, b) => a - b);
  const shotMids = [];
  for (let i = 0; i < boundaries.length - 1; i++) {
    const mid = (boundaries[i] + boundaries[i + 1]) / 2;
    if (mid > 0) shotMids.push(mid);
  }
  const step = shotMids.length > maxKf ? Math.ceil(shotMids.length / maxKf) : 1;
  const keyframes = [];
  let idx = 0;
  for (let i = 0; i < shotMids.length; i += step) {
    const t = shotMids[i];
    const f = path.join(kfDir, `kf_${String(idx).padStart(3, "0")}_${t.toFixed(2)}s.jpg`);
    const r = run(ffmpeg, ["-ss", String(t), "-i", vpath, "-frames:v", "1", "-q:v", "3", "-y", f]);
    if (r.status === 0 && fs.existsSync(f)) {
      keyframes.push({ index: idx, timeSec: +t.toFixed(3), path: path.relative(outDir, f) });
      idx++;
    }
  }

  // ---- 4) 音轨分离
  let audio = null;
  if (astream) {
    const wav = path.join(outDir, "audio.wav");
    const r = run(ffmpeg, ["-i", vpath, "-vn", "-ac", "1", "-ar", "16000", "-y", wav]);
    if (r.status === 0 && fs.existsSync(wav)) {
      const st = fs.statSync(wav);
      audio = { path: path.relative(outDir, wav), bytes: st.size, hasAudioTrack: st.size > 1000 };
    } else {
      audio = { path: null, hasAudioTrack: false };
    }
  }

  // ---- 5) 镜头表（场景边界 + 关键帧映射）
  const shots = [];
  for (let i = 0; i < boundaries.length - 1; i++) {
    const s = boundaries[i], e = boundaries[i + 1];
    const kf = keyframes.find(k => k.timeSec > s && k.timeSec <= e);
    shots.push({
      index: i,
      startSec: +s.toFixed(3),
      endSec: +e.toFixed(3),
      durationSec: +(e - s).toFixed(3),
      keyframe: kf ? kf.path : null,
    });
  }

  const probe = {
    schemaVersion: 1,
    generatedAt: new Date().toISOString(),
    tool: { ffmpeg: ffmpeg, ffprobe: ffprobe },
    meta: metaOut,
    scenes: sceneTimes.map(t => +t.toFixed(3)),
    sceneThreshold: thr,
    keyframes,
    audio,
    shots,
    stats: {
      shotCount: shots.length,
      keyframeCount: keyframes.length,
      avgShotSec: shots.length ? +(duration / shots.length).toFixed(2) : 0,
    },
  };

  const pj = path.join(outDir, "probe.json");
  fs.writeFileSync(pj, JSON.stringify(probe, null, 2) + "\n", "utf8");

  // ---- 摘要
  console.log("");
  console.log(`[probe] 时长 ${metaOut.durationSec}s  ${metaOut.video.width}x${metaOut.video.height}@${metaOut.video.fps}  ${metaOut.video.codec}`);
  console.log(`[probe] 场景切换 ${sceneTimes.length} 处 → 推断 ${shots.length} 个镜头（平均 ${probe.stats.avgShotSec}s）`);
  console.log(`[probe] 关键帧 ${keyframes.length} 张 → ${path.relative(outDir, kfDir)}`);
  console.log(`[probe] 音轨 ${audio && audio.hasAudioTrack ? "已分离 audio.wav" : "无/未分离"}`);
  console.log(`[probe] 画像 → ${pj}`);
  console.log("");
  console.log("下一步：向用户确认意图 —— 复刻(replicate) / 改编(adapt) / 混剪(remix)");
}

main().catch(e => {
  console.error("[probe] 未预期错误:", e && e.message ? e.message : e);
  process.exit(3);
});
