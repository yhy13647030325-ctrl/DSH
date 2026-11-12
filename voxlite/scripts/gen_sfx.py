#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""VoxLite 音效素材生成器（一次性 / 手动重生成用）。

正常流程无需手动调用——sfx_mix.py 会在首次运行时通过 sfx_lib.ensure_assets()
自动合成 assets/sfx/ 下的音效。此脚本仅供手动补全 / 重建素材。

用法：
  python gen_sfx.py [--lib ../assets/sfx]
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sfx_lib


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lib")
    a = ap.parse_args()
    lib = a.lib or sfx_lib.default_lib_dir()
    created = sfx_lib.ensure_assets(lib)
    if created:
        print(f"[ok] 已生成音效: {created} -> {lib}")
    else:
        print(f"[ok] 音效素材已齐全: {lib}")


if __name__ == "__main__":
    main()
