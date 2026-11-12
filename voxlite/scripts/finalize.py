#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""VoxEasy 成片终处理器：画幅归一化 + 安全区字幕 + 配音混流

解决四个高频事故：
  1. 关键帧比例不是 9:16（如 792x1160），发抖音被裁 / 加黑边
  2. 手写 drawtext 的 y 值拍脑袋，字幕踩进底部禁区被互动栏盖住
  3. 多行字幕各自带半透明底框，上下框互相压叠，观感脏乱
  4. 长句不换行，左右超出安全边距

字幕渲染走 libass（ASS 字幕），相比 drawtext 的优势：
  - 白字黑描边质量高（矢量描边，无锯齿），不需要底框
  - 多行行距由 libass 统一管理，永不重叠
  - MarginV 直接锁定底部安全边距
  - 支持关键词内联变色（文本里用 **词** 包裹即高亮为 Vox 黄）

用法：
  python finalize.py --video in.mp4 --audio narration.mp3 --out final.mp4 \
      --subs subs.json [--ratio 9:16] [--sub-style outline|box] [--check] [--strict-safe]

subs.json 格式： [{"start":0,"end":4,"text":"一句话字幕，**关键词**会变黄"}, ...]
--check 额外输出一版带安全区红框的自检文件（不要交付给用户）
安全区自检：默认每次都对 ASS 字幕做几何校验（顶部/底部禁区），越界仅警告；
            传 --strict-safe 则在越界时直接报错退出（CI/批量流水线自动拦截踩禁区成片）
"""
import argparse, json, os, re, subprocess, sys, shutil

import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()

RATIOS = {"9:16": (1080, 1920), "1:1": (1080, 1080), "16:9": (1920, 1080)}
# 安全区比例：顶部禁区 / 底部禁区 / 左右禁区
SAFE = {"9:16": (0.12, 0.20, 0.05), "1:1": (0.12, 0.18, 0.08), "16:9": (0.08, 0.12, 0.05)}

FONT_FILE = "msyhbd.ttc"      # 运行时由 find_cjk_font 覆盖为本地化拷贝文件名
FONT_NAME = "Microsoft YaHei"  # 运行时由 find_cjk_font 覆盖为探测到的字体名
PAD_COLOR = "0x14161A"         # 上下留白条颜色（深灰，替代难看的纯黑）
SAFE_GAP = 24                  # 字幕底边距离底部禁区红线的余量
MAX_CHARS = 16                 # 每行最大视觉宽度（1080 宽 / 54px 字号实测安全值）
PUNCT = "，。；！？、,.;!?：:"

# ASS 颜色为 &HBBGGRR&（BGR 顺序，与 HTML 相反）
C_WHITE = "&H00FFFFFF"
C_BLACK = "&H00000000"
C_SHADOW = "&H80000000"
C_VOX_YELLOW = "&H005EE4FF"    # #FFE45E 的 BGR 写法


def find_cjk_font():
    """跨平台探测中文字体，返回 (src_path, font_name)；找不到返回 (None, 兜底名)。

    libass/drawtext 在 fontsdir='.' 里按文件名找字，故 main 里会把探测到的系统字
    本地化拷贝进工作目录（Windows 盘符冒号会破坏 filter 语法，必须拷贝）。
    """
    candidates = [
        # Windows
        (r"C:\Windows\Fonts\msyhbd.ttc", "Microsoft YaHei"),
        (r"C:\Windows\Fonts\msyh.ttc", "Microsoft YaHei"),
        (r"C:\Windows\Fonts\simhei.ttf", "SimHei"),
        # macOS
        ("/System/Library/Fonts/PingFang.ttc", "PingFang SC"),
        ("/System/Library/Fonts/STHeiti Light.ttc", "STHeiti"),
        ("/Library/Fonts/Arial Unicode.ttf", "Arial Unicode MS"),
        # Linux
        ("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc", "Noto Sans CJK SC"),
        ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", "Noto Sans CJK SC"),
        ("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", "WenQuanYi Zen Hei"),
        ("/usr/share/fonts/truetype/arphic/uming.ttc", "AR PL UMing CN"),
    ]
    for path, name in candidates:
        if os.path.exists(path):
            return path, name
    return None, "Microsoft YaHei"


def vwidth(s: str) -> float:
    """视觉宽度：全角字符记 1，半角字符记 0.55"""
    return sum(1.0 if ord(c) > 0x2E80 else 0.55 for c in s)


def parse_segments(text: str):
    """解析 **词** 高亮：'一杯**奶茶**啊' -> [('一杯',False),('奶茶',True),('啊',False)]

    容错：未成对的 `**` 视为普通文本，不会把后续整段误判为高亮。
    例：'a**b**c**d'（3 个标记，最后一个未闭合）-> a 普通、b 高亮、'c**d' 普通。
    """
    marks = [m.start() for m in re.finditer(r"\*\*", text)]
    pairs, stack = [], []
    for pos in marks:
        if stack:
            pairs.append((stack.pop(), pos))
        else:
            stack.append(pos)          # 剩在栈里的未配对标记直接忽略
    pairs.sort()
    out, cursor = [], 0
    for s, e in pairs:
        if cursor < s:
            out.append((text[cursor:s], False))
        inner = text[s + 2:e]
        if inner:
            out.append((inner, True))
        cursor = e + 2
    if cursor < len(text):
        out.append((text[cursor:], False))
    return [(p, h) for p, h in out if p]


def split_segments(segs, pos: int):
    """在纯文本第 pos 个字符处把片段列表切成两半，不破坏高亮标记"""
    head, tail, cur = [], [], 0
    for txt, hl in segs:
        if cur >= pos:
            tail.append((txt, hl))
        elif cur + len(txt) <= pos:
            head.append((txt, hl))
        else:
            k = pos - cur
            head.append((txt[:k], hl))
            tail.append((txt[k:], hl))
        cur += len(txt)
    return head, tail


def hard_break(plain: str, limit: float) -> int:
    """在不超宽的最大位置硬切"""
    for i in range(len(plain) - 1, 0, -1):
        if vwidth(plain[:i]) <= limit:
            return i
    return len(plain)


def balanced_break(plain: str, limit: float) -> int:
    """两行场景：优先标点（保语义完整），并挑最接近中点的那个（两行更均衡）"""
    mid = len(plain) / 2
    cands = [i + 1 for i, c in enumerate(plain[:-1]) if c in PUNCT
             and vwidth(plain[:i + 1]) <= limit and vwidth(plain[i + 1:]) <= limit]
    return min(cands, key=lambda p: abs(p - mid)) if cands else hard_break(plain, limit)


def greedy_break(plain: str, limit: float) -> int:
    """多行场景：尽量填满当前行，优先落在标点后"""
    cut = hard_break(plain, limit)
    for i in range(cut, max(int(cut * 0.5), 1), -1):
        if plain[i - 1] in PUNCT:
            return i
    return cut


def layout(text: str, limit: float = MAX_CHARS, max_lines: int = 3):
    """把带 ** 高亮标记的文本排成多行片段列表，标记不会被断行切坏"""
    segs = parse_segments(text)
    plain = "".join(t for t, _ in segs)
    w = vwidth(plain)
    if w <= limit:
        return [segs]
    if w <= limit * 2:                       # 两行：优先均衡
        head, tail = split_segments(segs, balanced_break(plain, limit))
        return [head, tail]
    lines = []                               # 三行及以上：贪心填满
    while segs and len(lines) < max_lines:
        plain = "".join(t for t, _ in segs)
        if vwidth(plain) <= limit:
            lines.append(segs)
            segs = []
            break
        head, segs = split_segments(segs, greedy_break(plain, limit))
        lines.append(head)
    if segs:
        left = "".join(t for t, _ in segs)
        print(f"[warn] 字幕超过 {max_lines} 行，已截断：…{left[:12]}"
              f"（请精简文案，单句建议 ≤ {int(limit * max_lines)} 字）", file=sys.stderr)
    return lines


def ass_time(t: float) -> str:
    h = int(t // 3600)
    m = int(t % 3600 // 60)
    s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def render_ass_line(segs) -> str:
    """把片段列表渲染为 ASS 文本，高亮段落内联换成 Vox 黄"""
    out = []
    for txt, hl in segs:
        txt = txt.replace("{", "(").replace("}", ")").replace("\\", "/")
        out.append(f"{{\\c{C_VOX_YELLOW}}}{txt}{{\\c{C_WHITE}}}" if hl else txt)
    return "".join(out)


def build_ass(subs, W, H, ratio, path):
    """生成 ASS 字幕：白字黑描边，底边锁定在安全区之上"""
    _, bot, side = SAFE[ratio]
    fs = 54 if W >= 1080 else int(W / 20)
    outline = 5 if W >= 1080 else 3
    margin_v = int(H * bot) + SAFE_GAP        # 字幕底边到画面底部的距离
    margin_h = int(W * side) + 20             # 左右留白，比安全边距再收一点

    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Vox,{FONT_NAME},{fs},{C_WHITE},{C_WHITE},{C_BLACK},{C_SHADOW},-1,0,0,0,100,100,0.6,0,1,{outline},2,2,{margin_h},{margin_h},{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    # 每行输出为独立 Dialogue 并各自指定 MarginV：
    # libass 用 \N 换行时行距等于字体自然行高（实测仅 2px 间隙，描边会粘连），
    # 逐行定位可精确控制行距，同时把最后一行底边牢牢锁在安全线上。
    pitch = int(fs * 1.34)
    rows, max_lines = [], 1
    for s in subs:
        lines = layout(s["text"])
        max_lines = max(max_lines, len(lines))
        n = len(lines)
        for i, ln in enumerate(lines):
            mv = margin_v + (n - 1 - i) * pitch      # 多行向上生长
            rows.append(f"Dialogue: 0,{ass_time(s['start'])},{ass_time(s['end'])},"
                        f"Vox,,0,0,{mv},,{render_ass_line(ln)}")
    # 安全区几何自检（默认即跑，--strict-safe 时转为报错拦截）
    issues = []
    top_of_block = H - margin_v - pitch * (max_lines - 1)   # 最上行底边 y
    top_limit = H * SAFE[ratio][0]
    if top_of_block - fs < top_limit:
        issues.append(f"顶部禁区：字幕最上行顶边 {top_of_block - fs}px 已越过顶部禁区红线 {int(top_limit)}px")
    if margin_v < H * SAFE[ratio][1]:
        issues.append(f"底部禁区：字幕底边距 {margin_v}px 小于底部禁区 {int(H*SAFE[ratio][1])}px")
    for it in issues:
        print(f"[safe-zone][warn] {it}", file=sys.stderr)
    with open(path, "w", encoding="utf-8") as f:
        f.write(head + "\n".join(rows) + "\n")
    return fs, margin_v, outline, issues


def box_filters(subs, W, H, ratio):
    """降级方案：drawtext 白字黑描边（无底框，因此也不会重叠）"""
    _, bot, _ = SAFE[ratio]
    fs = 54 if W >= 1080 else int(W / 20)
    line_h = int(fs * 1.42)
    bottom_limit = H * (1 - bot) - SAFE_GAP
    parts = []
    for s in subs:
        lines = ["".join(t for t, _ in ln) for ln in layout(s["text"])]
        top_y = int(bottom_limit - len(lines) * line_h)
        for i, ln in enumerate(lines):
            esc = (ln.replace("\\", "").replace(":", "\\:")
                     .replace("'", "\u2019").replace("%", "\\%"))
            parts.append(
                f"drawtext=fontfile='{FONT_FILE}':text='{esc}':fontcolor=white:"
                f"fontsize={fs}:borderw=5:bordercolor=black:"
                f"shadowcolor=black@0.5:shadowx=0:shadowy=3:"
                f"x='(w-text_w)/2':y={top_y + i * line_h}:"
                f"enable='between(t,{s['start']},{s['end']})'")
    return parts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--audio")
    ap.add_argument("--subs")
    ap.add_argument("--sfx")
    ap.add_argument("--out", required=True)
    ap.add_argument("--ratio", default="9:16", choices=list(RATIOS))
    ap.add_argument("--sub-style", default="outline", choices=["outline", "box"],
                    help="outline=ASS 白字黑描边（推荐）; box=drawtext 降级方案")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--strict-safe", action="store_true",
                    help="安全区自检失败时直接报错退出（默认仅警告），用于 CI/批量流水线的自动拦截")
    a = ap.parse_args()

    W, H = RATIOS[a.ratio]
    wd = os.path.dirname(os.path.abspath(a.out)) or "."
    os.makedirs(wd, exist_ok=True)
    # 跨平台中文字体探测：把系统中文粗体本地化拷贝进工作目录
    # （供 libass fontsdir / drawtext 按文件名查找；Windows 盘符冒号会破坏 filter 语法，必须拷贝）
    global FONT_FILE, FONT_NAME
    src, detected_name = find_cjk_font()
    FONT_NAME = detected_name
    local_font = "vox_font.ttc" if (src and src.lower().endswith(".ttc")) else "vox_font.ttf"
    if src and not os.path.exists(os.path.join(wd, local_font)):
        shutil.copy(src, os.path.join(wd, local_font))
        print(f"[font] 已本地化中文字体：{detected_name} -> {local_font}")
    elif src:
        print(f"[font] 复用已本地化中文字体：{detected_name}")
    else:
        print("[font][warn] 未探测到系统中文字体，字幕可能缺字；请手动放一个中文字体到工作目录",
              file=sys.stderr)
    FONT_FILE = local_font
    video_abs = os.path.abspath(a.video)
    audio_abs = os.path.abspath(a.audio) if a.audio else None
    subs_abs = os.path.abspath(a.subs) if a.subs else None
    sfx_abs = os.path.abspath(a.sfx) if a.sfx else None
    os.chdir(wd)

    # 1) 画幅归一化：等比缩放到目标宽，上下用品牌色补条，画面偏上放
    #    偏上是为了把更多余量让给底部禁区（抖音互动栏在下面）
    #    top_offset 用 min(top_offset, H-ih) 钳制：当源已是 9:16（如 1080x1920 /
    #    720x1280 缩放后正好 1080x1920）时不再额外加偏移，避免 crop 把视频底部
    #    约 99px 直接裁掉（实测：旧逻辑对每个 9:16 源都丢底）。pad 直接产出精确
    #    H 高，故不再需要 crop。
    top_offset = int(H * 0.052)
    vf = [f"scale={W}:-2",
          f"pad={W}:{H}:0:min({top_offset},{H}-ih):color={PAD_COLOR}"]

    # 2) 字幕
    subs = json.load(open(subs_abs, encoding="utf-8")) if subs_abs else []
    if subs:
        if a.sub_style == "outline":
            fs, mv, ow, issues = build_ass(subs, W, H, a.ratio, "subs.ass")
            vf.append(f"subtitles=subs.ass:fontsdir=.")
            print(f"[subs] ASS 白字黑描边 | {len(subs)} 条 | 字号 {fs} | 描边 {ow}px | "
                  f"底边距 {mv}px（底部禁区 {int(H*SAFE[a.ratio][1])}px + 余量 {SAFE_GAP}px）")
            # 安全区几何自检默认即跑；--strict-safe 时拦截（自动拒绝踩禁区的成片）
            if issues and a.strict_safe:
                print(f"[safe-zone][error] 字幕越界，已拒绝渲染（去掉 --strict-safe 可强制出片）：",
                      file=sys.stderr)
                for it in issues:
                    print(f"  - {it}", file=sys.stderr)
                sys.exit(2)
        else:
            vf += box_filters(subs, W, H, a.ratio)
            print(f"[subs] drawtext 描边降级方案 | {len(subs)} 条")

    # 3) 安全区自检框（仅 --check）
    if a.check:
        t_, b_, s_ = SAFE[a.ratio]
        vf.append(f"drawbox=x={int(W*s_)}:y={int(H*t_)}:w={int(W*(1-2*s_))}:"
                  f"h={int(H*(1-t_-b_))}:color=red@0.5:t=3")

    cmd = [FF, "-y", "-i", video_abs]
    extra_inputs = []
    if audio_abs:
        extra_inputs.append(audio_abs)
    if sfx_abs:
        extra_inputs.append(sfx_abs)
    for e in extra_inputs:
        cmd += ["-i", e]
    cmd += ["-vf", ",".join(vf), "-c:v", "libx264", "-crf", "21",
            "-pix_fmt", "yuv420p", "-r", "24"]
    if not extra_inputs:
        cmd += [os.path.basename(a.out)]
    elif len(extra_inputs) == 1:
        # 只有配音 或 只有音效
        cmd += ["-c:a", "aac", "-b:a", "160k", "-map", "0:v",
                "-map", "1:a", "-shortest", os.path.basename(a.out)]
    else:
        # 配音 + 音效：音效先降 0.85 留余量，再与配音 amix（不归一化，保人声主导）
        # 末级挂 alimiter 防破音：人声(~0.7-0.9) + 音效(0.85*0.3≈0.255) 叠加峰值常
        # 超 1.0，amix normalize=0 不衰减，故用硬限幅把峰值压到 0.95 防削波破音。
        fc = (f"[2:a]volume=0.85[sfx];"
              f"[1:a][sfx]amix=inputs=2:duration=longest:normalize=0[mx];"
              f"[mx]alimiter=level_in=1:limit=0.95:level_out=1[aout]")
        cmd += ["-filter_complex", fc, "-map", "0:v", "-map", "[aout]",
                "-c:a", "aac", "-b:a", "160k", "-shortest", os.path.basename(a.out)]
    if sfx_abs:
        print(f"[sfx] 已叠加音效轨（音量 0.85×，低于人声）")

    r = subprocess.run(cmd, capture_output=True)
    if r.returncode != 0:
        err = r.stderr.decode("utf-8", "ignore")
        print(err[-2500:], file=sys.stderr)
        if a.sub_style == "outline":
            print("\n[hint] ASS 渲染失败可改用 --sub-style box 降级到 drawtext 描边方案",
                  file=sys.stderr)
        sys.exit(1)
    print(f"[ok] {a.out}  ->  {W}x{H} @{a.ratio}")


if __name__ == "__main__":
    main()
