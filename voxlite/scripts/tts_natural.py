#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""VoxLite 自然化配音管线：逐句 TTS -> 节奏起伏 -> 呼吸停顿 -> 音频后处理
同时输出与配音**逐句精确对齐**的字幕时间轴（不再手写猜时间）。

用法：
  python tts_natural.py --script script.json --voice zh-CN-XiaoxiaoNeural \
      --out narration.mp3 --subs subs.json [--raw]

script.json：
  [{"text":"一杯珍珠奶茶，到底藏了几块方糖？","rate":"-4%","gap":0.45,
    "style":"chat","degree":1.3}, ...]
  rate/gap 可省略，省略时按句型自动推断（疑问句放慢、长句加快）。
  style/degree 可省略，省略时按语义自动选情绪风格（疑问=chat、揭示=enthusiastic、
  转折=serious、惋惜=empathetic、安利=cheerful、平述=narration-relaxed）。
  注：情绪风格仅部分声音支持（XiaoxiaoNeural 最全，男声支持较少），
  若所选声音不支持该风格会自动降级为纯调速。
--raw 跳过音频后处理（用于 A/B 对照）
"""
import argparse, json, os, re, subprocess, sys, time

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
PY = sys.executable

# 后处理链：去浑浊 -> 提清晰 -> 压齿音 -> 压缩贴耳 -> 极轻空间 -> 响度标准化(-16 LUFS)
POST = ("highpass=f=85,"
        "equalizer=f=250:t=q:w=1.0:g=-2.5,"
        "equalizer=f=3200:t=q:w=1.4:g=3,"
        "equalizer=f=7500:t=q:w=2.0:g=-2.5,"
        "acompressor=threshold=-18dB:ratio=3:attack=8:release=180:makeup=2,"
        "aecho=0.88:0.88:22:0.055,"
        "loudnorm=I=-16:TP=-1.5:LRA=11")

VOICES = {
    "female_warm":  "zh-CN-XiaoxiaoNeural",   # 女声，温暖，通用科普
    "male_passion": "zh-CN-YunjianNeural",    # 男声，带劲，适合 Vox 讲解
    "male_sunny":   "zh-CN-YunxiNeural",      # 男声，阳光年轻
    "male_news":    "zh-CN-YunyangNeural",    # 男声，新闻播报感
    "female_lively": "zh-CN-XiaoyiNeural",    # 女声，活泼
}


# 情绪风格：按语义自动推断，制造「有表情」的播报腔（而非平铺直叙）
# 风格名均为 XiaoxiaoNeural 支持集合；男声支持较少，会自动降级
EMO_DEFAULT = {
    "chat": 1.3,            # 疑问/互动：好奇、带聊天气口
    "cheerful": 1.5,        # 安利/惊喜：明亮上扬
    "enthusiastic": 1.6,    # 揭示大数字/反转：兴奋着重
    "serious": 1.4,         # 转折/对比：严肃强调
    "empathetic": 1.5,      # 惋惜/风险预警：共情关切
    "sad": 1.5,             # 遗憾/下滑：低落
    "narration-relaxed": 1.2,  # 平述：松弛自然
}


def auto_emotion(text, idx, total):
    """按语义自动选情绪风格与强度；返回 (style, degree)

    优先级（避免误判）：
      1. 疑问句 → chat（好奇聊天气口）
      2. 损失/风险/惋惜/负面后果 → empathetic（共情关切）
      3. 建议/指南/限制/健康提醒（别超/应/须/世卫说…）→ serious（严肃强调）
      4. 安利/惊喜/正向 → cheerful
      5. 揭示大数字/反转 → enthusiastic
      6. 转折/对比 → serious
      7. 末句/平述 → narration-relaxed
    """
    if text.endswith(("？", "?")):
        return "chat", 1.3
    # 损失 / 风险 / 惋惜 / 负面后果
    if re.search(r"危害|风险|警告|小心|注意|危机|可惜|遗憾|下滑|下降|减少|亏损|衰落|失败|后果|"
                  r"预警|隐患|威胁|受损|崩|暴跌|缩水|超标|致癌|中毒|肥胖|蛀牙|患病|代价", text):
        return "empathetic", 1.4
    # 建议 / 指南 / 限制 / 健康提醒（「别超 25 克」「世卫说一天…」归这里）
    if re.search(r"建议|应该|应当|必须|别超|别喝|少喝|少|限制|控制|指南|标准|推荐量|"
                  r"每天|一天|世界卫生组织|世卫|权威|研究|实验|数据表明|提醒|警惕|勿|不宜|戒|改掉|远离", text):
        return "serious", 1.4
    if re.search(r"太棒|终于|推荐|值得|惊喜|惊人|突破|创下|点赞|厉害|赢了|赢|安利|必看|种草", text):
        return "cheerful", 1.5
    if re.search(r"足足|高达|整整|居然|竟然|突破|创下|相当于|暴增|猛增|暴涨|翻了|破|亿|万倍|翻倍", text):
        return "enthusiastic", 1.6
    if re.search(r"^而|但是|然而|其实|反而|不过|可是|对比|却|可这", text):
        return "serious", 1.4
    if idx == total - 1:
        return "narration-relaxed", 1.1
    return "narration-relaxed", 1.2


def xml_escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def auto_prosody(text, idx, total):
    """无显式参数时，按句型自动推断语速与停顿——整体偏快、节奏起伏、去播报腔"""
    if text.endswith(("？", "?")):
        return "-2%", 0.32                      # 悬念/提问：略慢 + 中停顿
    if re.search(r"\d|一|二|三|四|五|六|七|八|九|十|百|千|万|亿", text) and len(text) < 20:
        return "+0%", 0.28                      # 关键数字：常速强调（不拖）
    if idx == total - 1:
        return "+4%", 0.15                      # 收尾：稍快回稳
    if len(text) > 18:
        return "+14%", 0.20                     # 长铺垫：加快
    return "+12%", 0.22                         # 默认：偏快，去播报腔


def dur_of(path):
    out = subprocess.run([FF, "-i", path], capture_output=True).stderr.decode("utf-8", "ignore")
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0


def tts(voice, text, rate, out, style=None, degree=1.0, retries=4):
    base = [PY, "-m", "edge_tts", "--write-media", out]
    if style:
        ssml = (f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
                f'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="zh-CN">'
                f'<voice name="{voice}"><mstts:express-as style="{style}" '
                f'styledegree="{degree}"><prosody rate="{rate}">{xml_escape(text)}'
                f'</prosody></mstts:express-as></voice></speak>')
        args = base + ["--ssml", ssml]
    else:
        args = base + ["--voice", voice, f"--rate={rate}", "--text", text]
    for i in range(retries):
        r = subprocess.run(args, capture_output=True)
        if r.returncode == 0 and os.path.exists(out) and os.path.getsize(out) > 1000:
            return True
        # 所选声音不支持该风格 -> 丢掉 style 优雅降级（首轮即切换）
        if style and i == 0:
            args = base + ["--voice", voice, f"--rate={rate}", "--text", text]
        time.sleep(1.5 * (i + 1))               # edge-tts 会偶发限流，必须重试
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", required=True)
    ap.add_argument("--voice", default="zh-CN-XiaoxiaoNeural")
    ap.add_argument("--out", default="narration.mp3")
    ap.add_argument("--subs", default="subs.json")
    ap.add_argument("--raw", action="store_true")
    a = ap.parse_args()

    a.voice = VOICES.get(a.voice, a.voice)
    wd = os.path.dirname(os.path.abspath(a.out)) or "."
    os.chdir(wd)
    script = json.load(open(a.script, encoding="utf-8"))

    segs, timeline, cursor = [], [], 0.0
    for i, item in enumerate(script):
        txt = item["text"] if isinstance(item, dict) else str(item)
        d_rate, d_gap = auto_prosody(txt, i, len(script))
        rate = (item.get("rate") if isinstance(item, dict) else None) or d_rate
        gap = (item.get("gap") if isinstance(item, dict) else None) or d_gap
        style, degree = auto_emotion(txt, i, len(script))
        # 显式指定才覆盖；否则保留自动推断的情绪（否则 auto_emotion 全白做）
        style = (item.get("style") or item.get("emotion") or style) if isinstance(item, dict) else style
        degree = (item.get("degree") or degree) if isinstance(item, dict) else degree

        f = f"_seg{i:02d}.mp3"
        if not tts(a.voice, txt, rate, f, style=style, degree=degree):
            print(f"[fail] 第{i+1}句 TTS 失败: {txt[:14]}", file=sys.stderr)
            sys.exit(1)
        d = dur_of(f)
        segs.append((f, gap))
        # 字幕跟着音频走：开口即出，说完后多留 gap 便于阅读
        timeline.append({"start": round(cursor, 2),
                         "end": round(cursor + d + gap * 0.9, 2),
                         "text": txt})
        cursor += d + gap
        print(f"  [{i+1}/{len(script)}] {rate:>5} {style} gap={gap:.2f} {d:5.2f}s  {txt[:18]}")
        time.sleep(0.4)

    # 拼接：每句尾部补呼吸停顿
    ins, fl, labels = [], [], []
    for i, (f, gap) in enumerate(segs):
        ins += ["-i", f]
        fl.append(f"[{i}:a]apad=pad_dur={gap}[p{i}]")
        labels.append(f"[p{i}]")
    fl.append("".join(labels) + f"concat=n={len(segs)}:v=0:a=1[cat]")
    fl.append(f"[cat]{'anull' if a.raw else POST}[out]")

    cmd = [FF, "-y"] + ins + ["-filter_complex", ";".join(fl), "-map", "[out]",
                              "-c:a", "libmp3lame", "-b:a", "192k", os.path.basename(a.out)]
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode != 0:
        print(r.stderr.decode("utf-8", "ignore")[-2000:], file=sys.stderr)
        sys.exit(1)

    json.dump(timeline, open(a.subs, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"[ok] {a.out}  总时长 {cursor:.2f}s | 字幕轴 -> {a.subs}")
    print(f"[hint] 视频总长请按 {cursor:.1f}s 规划（或用 finalize.py 的 -shortest 对齐）")


if __name__ == "__main__":
    main()
