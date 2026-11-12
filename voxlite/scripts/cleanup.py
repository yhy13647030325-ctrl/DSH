#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""VoxLite 成片交付后清理「单个任务文件夹」里的临时中间文件。

按 §0 任务目录隔离约定，每个任务各占一个独立文件夹（如
voxlite-<主题>-<YYMMDD-HHMM>/）。本脚本只清理 --dir 这个「单个任务文件夹」
内的临时产物（关键帧图、分镜视频、配音分段、字幕轴、拼接静音片、Python
缓存），保留成片与可复用源。脚本非递归、只删直接子项，因此绝不会跨文件夹
误删其他任务的文件。若 --dir 内含有看起来像其他任务文件夹的子目录
（voxlite-*），会直接拒绝执行，提醒你指向具体任务目录。

用法：
  python cleanup.py --dir <本任务文件夹> [--dry-run]
--dry-run  只打印将要删除的文件，不真删（推荐先跑一次确认）
"""
import argparse
import os
import shutil

# 要删除的临时/中间产物（glob，仅匹配 --dir 直接子项，不上溯）
DEL_FILE_PATTERNS = [
    "*.png", "*.jpg", "*.jpeg",          # ImageGen 关键帧原图
    "shot*.mp4", "clip*.mp4",            # VideoGen 分镜视频
    "silent.mp4", "concat.mp4", "raw.mp4", "*_silent.mp4",  # 拼接静音/中间片
    "_seg*.mp3", "_*.mp3", "narration.mp3",  # 配音分段与中间音频
    "subs.json", "*.ass",                # 字幕中间轴 / finalize 临时 ASS（已烧入成片）
    "sfx_track.wav", "sfx.json",         # 音效中间轨 / 手动音效清单
]
DEL_DIR_PATTERNS = ["__pycache__"]

# 永不删除（交付物与可复用源）
KEEP = {"final.mp4", "subs_final.json"}
KEEP_SUFFIX = (".md", ".ttc", ".ttf", ".otf", ".json")  # 但 subs.json 已列入删除
# 说明：script.json 是旁白源、*.md 是记录、字体复用——均保留。
# subs.json 虽以 .json 结尾但属中间轴，已在 DEL_FILE_PATTERNS 显式删除。


def collect(target_dir):
    import glob
    to_del = []
    for pat in DEL_FILE_PATTERNS:
        for p in glob.glob(os.path.join(target_dir, pat)):
            if os.path.isfile(p):
                to_del.append(p)
    for pat in DEL_DIR_PATTERNS:
        for p in glob.glob(os.path.join(target_dir, pat)):
            if os.path.isdir(p):
                to_del.append(p)
    # 二次保护：绝不动非 --dir 内、或属于保留集的文件
    final = []
    for p in to_del:
        name = os.path.basename(p)
        if name in KEEP or name.endswith((".md", ".ttc", ".ttf", ".otf")):
            continue
        if name == "script.json":        # 旁白源，保留
            continue
        final.append(p)
    return list(dict.fromkeys(final))    # 去重（同一文件可能命中多个 glob）


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=".", help="成片所在工作目录（默认当前目录）")
    ap.add_argument("--dry-run", action="store_true", help="只打印，不真删")
    a = ap.parse_args()

    target = os.path.abspath(a.dir)
    if not os.path.isdir(target):
        print(f"[skip] 目录不存在: {target}")
        return

    # 防误删：若 --dir 内含其他任务文件夹（voxlite-* 子目录），说明很可能
    # 指错了上级目录，拒绝执行，避免清错范围。
    import glob
    sibling_tasks = [d for d in glob.glob(os.path.join(target, "voxlite-*"))
                     if os.path.isdir(d)]
    if sibling_tasks:
        print(f"[abort] {target} 内发现其他任务文件夹：")
        for d in sibling_tasks:
            print("  -", os.path.relpath(d, target))
        print("[abort] cleanup.py 只清理「单个任务文件夹」。请把 --dir 指向具体的任务目录，")
        print("         例如 voxlite-boba-sugar-260806-0430/，而不是它的上级目录。")
        return

    files = collect(target)
    if not files:
        print(f"[ok] {target} 无临时文件可清理")
        return

    print(f"{'[dry-run] ' if a.dry_run else ''}将清理 {len(files)} 个文件/目录 @ {target}:")
    for p in files:
        print("  -", os.path.relpath(p, target))

    if a.dry_run:
        return

    for p in files:
        try:
            if os.path.isdir(p):
                shutil.rmtree(p)
            else:
                os.remove(p)
        except OSError as e:
            print(f"  [warn] 删除失败 {p}: {e}")
    print(f"[done] 已清理 {target}")


if __name__ == "__main__":
    main()
