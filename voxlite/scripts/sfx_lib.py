#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""VoxLite 免版权音效合成库（纯 stdlib，离线零依赖）。

合成短视频常用音效：whoosh / swoosh / pop / click / ding / impact / chime。
首次调用 ensure_assets() 时，若 assets/sfx/ 下缺文件则原地合成，保证技能自举、
无需任何外部音频资源或 API。所有音效均为程序生成，无版权风险。
"""
import math
import os
import random
import struct
import wave

SR = 44100

# 各音效默认时长（秒）
TYPES = {
    "whoosh": 0.55,   # 转场：镜头扫过 / 切换
    "swoosh": 0.85,   # 转场：更长的甩动
    "pop":    0.12,   # 元素弹出 / 数字弹入
    "click":  0.05,   # 轻点 / UI 点击
    "ding":   0.55,   # 揭示 / 收尾提示
    "impact": 0.40,   # 重击 / 强调落地
    "chime":  0.80,   # 结尾铃音
}


def _noise(n, seed=0):
    rnd = random.Random(seed)
    return [rnd.uniform(-1.0, 1.0) for _ in range(n)]


def _write_wav(path, samples, sr=SR):
    """samples: list[float] in [-1,1]，单声道入，输出 16bit 立体声 wav。"""
    frames = bytearray()
    for s in samples:
        v = max(-1.0, min(1.0, s))
        iv = int(v * 32767)
        frames += struct.pack("<hh", iv, iv)
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(bytes(frames))


def _synth_whoosh(dur, sweep=(0.02, 0.20)):
    """一阶低通 + 截止上扫 + 渐起渐落包络，模拟“咻”的转场气声。"""
    n = int(dur * SR)
    x = _noise(n, seed=7)
    prev = 0.0
    y = [0.0] * n
    a0, a1 = sweep
    for i in range(n):
        t = i / n
        a = a0 + (a1 - a0) * t
        prev = prev + a * (x[i] - prev)
        y[i] = prev
    out = [0.0] * n
    for i in range(n):
        t = i / n
        env = math.sin(math.pi * t)          # 0 -> 1 -> 0 平滑起落
        out[i] = y[i] * env * 1.3
    return out


def _synth_swoosh(dur):
    return _synth_whoosh(dur, sweep=(0.015, 0.30))


def _synth_pop(dur):
    n = int(dur * SR)
    f = 880.0
    return [math.sin(2 * math.pi * f * (i / SR)) * math.exp(-30 * (i / SR))
            for i in range(n)]


def _synth_click(dur):
    n = int(dur * SR)
    x = _noise(n, seed=3)
    return [x[i] * math.exp(-180 * (i / SR)) for i in range(n)]


def _synth_ding(dur):
    n = int(dur * SR)
    out = []
    for i in range(n):
        t = i / SR
        out.append((math.sin(2 * math.pi * 1318 * t) +
                    0.5 * math.sin(2 * math.pi * 1976 * t)) * math.exp(-5 * t))
    return out


def _synth_impact(dur):
    n = int(dur * SR)
    x = _noise(n, seed=11)
    out = []
    for i in range(n):
        t = i / SR
        body = (math.sin(2 * math.pi * 90 * t) * math.exp(-11 * t) +
                0.4 * math.sin(2 * math.pi * 170 * t) * math.exp(-16 * t))
        noise = x[i] * math.exp(-40 * t) * 0.5
        out.append(body + noise)
    return out


def _synth_chime(dur):
    n = int(dur * SR)
    out = []
    for i in range(n):
        t = i / SR
        out.append(math.sin(2 * math.pi * 880 * t) * math.exp(-3 * t) +
                    0.6 * math.sin(2 * math.pi * 1320 * t) * math.exp(-4 * t))
    return out


_SYNTH = {
    "whoosh": lambda: _synth_whoosh(TYPES["whoosh"]),
    "swoosh": lambda: _synth_swoosh(TYPES["swoosh"]),
    "pop":    lambda: _synth_pop(TYPES["pop"]),
    "click":  lambda: _synth_click(TYPES["click"]),
    "ding":   lambda: _synth_ding(TYPES["ding"]),
    "impact": lambda: _synth_impact(TYPES["impact"]),
    "chime":  lambda: _synth_chime(TYPES["chime"]),
}


def synth(type_name):
    if type_name not in _SYNTH:
        raise KeyError(f"unknown sfx type: {type_name}")
    return _SYNTH[type_name]()


def default_lib_dir():
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "assets", "sfx")


def ensure_assets(lib_dir=None):
    """确保 assets/sfx/ 下 7 个音效齐全；缺失则原地合成。返回本次新生成的类型列表。"""
    lib_dir = lib_dir or default_lib_dir()
    os.makedirs(lib_dir, exist_ok=True)
    created = []
    for t in TYPES:
        p = os.path.join(lib_dir, f"{t}.wav")
        if not os.path.exists(p):
            _write_wav(p, synth(t))
            created.append(t)
    return created
