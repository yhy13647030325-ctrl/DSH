#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""VoxLite 音效铺设：把转场 / 揭示音效按时间轴混成一条 sfx_track.wav。

输入：
  - subs.json（可选）：自动派生音效事件——
      转场间隔(相邻句间隔 > 0.7s) 放 whoosh；含 **高亮** 的句放 pop；结尾放 ding
  - sfx.json（可选，手动覆盖 / 追加）：[{"t":1.2,"type":"pop","gain":0.3}, ...]
输出：
  - sfx_track.wav：与视频等长的音效轨（其余处静音），供 finalize.py --sfx 叠加

音效素材由 sfx_lib.ensure_assets() 首次运行时自动合成到 assets/sfx/，无需手动准备。

用法：
  python sfx_mix.py --subs subs.json --out sfx_track.wav [--sfx sfx.json] \
      [--lib ../assets/sfx] [--duration 18.0] [--gain 0.3]
"""
import argparse
import json
import os
import struct
import sys
import wave

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sfx_lib


def read_wav_mono(path):
    with wave.open(path, "rb") as w:
        ch = w.getnchannels()
        sr = w.getframerate()
        n = w.getnframes()
        width = w.getsampwidth()
        raw = w.readframes(n)
    if width == 2:
        vals = struct.unpack("<" + "h" * (n * ch), raw)
    else:
        vals = struct.unpack("<" + "b" * (n * ch), raw)
        vals = [v << 8 for v in vals]
    if ch == 1:
        return [v / 32768.0 for v in vals], sr
    return [(vals[i] + vals[i + 1]) / 2 / 32768.0 for i in range(0, len(vals), 2)], sr


def derive_events(subs):
    ev = []
    prev_end = 0.0
    for s in subs:
        st = float(s.get("start", 0))
        en = float(s.get("end", st))
        txt = s.get("text", "")
        if st - prev_end > 0.7:                       # 间隔大 = 镜头/转场切换
            ev.append({"t": st, "type": "whoosh", "gain": 0.3})
        if "**" in txt:                               # 高亮词弹入
            ev.append({"t": st, "type": "pop", "gain": 0.25})
        prev_end = max(prev_end, en)
    if subs:
        last_end = max(float(s.get("end", 0)) for s in subs)
        ev.append({"t": last_end + 0.2, "type": "ding", "gain": 0.3})
    return ev


def write_wav(path, buf, sr=sfx_lib.SR):
    frames = bytearray()
    for x in buf:
        v = max(-1.0, min(1.0, x))
        iv = int(v * 32767)
        frames += struct.pack("<hh", iv, iv)
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(bytes(frames))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subs")
    ap.add_argument("--sfx")
    ap.add_argument("--out", required=True)
    ap.add_argument("--lib")
    ap.add_argument("--duration", type=float, default=None)
    ap.add_argument("--gain", type=float, default=0.3)
    a = ap.parse_args()

    lib = a.lib or sfx_lib.default_lib_dir()
    created = sfx_lib.ensure_assets(lib)
    if created:
        print(f"[sfx] 自动合成缺失音效: {created}")

    events = []
    if a.subs and os.path.exists(a.subs):
        subs = json.load(open(a.subs, encoding="utf-8"))
        events += derive_events(subs)
    if a.sfx and os.path.exists(a.sfx):
        events += json.load(open(a.sfx, encoding="utf-8"))

    if not events:
        print("[sfx] 无音效事件，输出静音轨（finalize 可安全叠加）", file=sys.stderr)
        write_wav(a.out, [0.0] * int(0.1 * sfx_lib.SR))
        return

    dur = a.duration or (max(e["t"] for e in events) + 1.0)
    n = int(dur * sfx_lib.SR)
    buf = [0.0] * n

    for e in events:
        t = float(e["t"])
        typ = e.get("type", "pop")
        g = float(e.get("gain", a.gain))
        fp = os.path.join(lib, f"{typ}.wav")
        if not os.path.exists(fp):
            print(f"[warn] 缺音效 {typ}，跳过", file=sys.stderr)
            continue
        samples, sr = read_wav_mono(fp)
        if sr != sfx_lib.SR:                         # 简易线性重采样
            ratio = sfx_lib.SR / sr
            res = []
            for i in range(int(len(samples) * ratio)):
                idx = i / ratio
                i0 = int(idx)
                i1 = min(i0 + 1, len(samples) - 1)
                frac = idx - i0
                res.append(samples[i0] * (1 - frac) + samples[i1] * frac)
            samples = res
        off = int(t * sfx_lib.SR)
        for j, s in enumerate(samples):
            if off + j >= n:
                break
            buf[off + j] += s * g

    peak = max((abs(x) for x in buf), default=0.0)
    if peak > 0.95:                                  # 软限幅防削波
        scale = 0.95 / peak
        buf = [x * scale for x in buf]

    write_wav(a.out, buf)
    print(f"[sfx] 已生成 {a.out} | {len(events)} 个事件 | {dur:.1f}s | lib={lib}")


if __name__ == "__main__":
    main()
