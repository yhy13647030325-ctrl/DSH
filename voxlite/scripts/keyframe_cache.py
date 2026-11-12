#!/usr/bin/env python3
"""VoxLite 关键帧缓存：相同 (风格 + 场景描述) 的关键帧只生成一次，跨任务/多次运行复用，省 ImageGen 积分。

为什么：ImageGen 按张计费（单张约 5–15 分），是积分大头。很多主题（奶茶含糖、咖啡致癌、
油价涨跌…）会被反复制作，或同一视频里多个拍描绘同一场景。缓存命中即可跳过 ImageGen（0 积分）。

用法：
  # 生成前查询：命中则打印缓存图绝对路径并 exit 0；未命中 exit 1
  python keyframe_cache.py --check "标准 Vox 4.0|一杯中杯珍珠奶茶约700ml"

  # 一键复用：命中则把缓存图拷到 --out（本任务文件夹关键帧）并打印路径、exit 0；
  #          未命中则 exit 1，调用方再去跑 ImageGen，生成后用 --store 落缓存。
  python keyframe_cache.py --resolve "标准 Vox 4.0|一杯中杯珍珠奶茶约700ml" --out keyframe.png

  # 生成后落缓存：把刚生成的 keyframe.png 存入缓存，打印缓存路径
  python keyframe_cache.py --store "标准 Vox 4.0|一杯中杯珍珠奶茶约700ml" --file keyframe.png

  # 清空缓存（换风格标准 / 嫌缓存图质量参差时）
  python keyframe_cache.py --clear

缓存目录：~/.cache/voxlite_keyframes/（Windows 为 %USERPROFILE%\\.cache\\voxlite_keyframes）
键：sha256(style + '|' + 归一化场景描述) 前 16 位 → <hash>.png
注意：缓存是「同风格同场景」的近似复用，复用前务必肉眼确认缓存图与本次需求一致；
      若画面主体/构图有差异，应重新生成并覆盖缓存。
"""
import argparse
import hashlib
import os
import shutil
import sys

DEFAULT_CACHE = os.path.join(os.path.expanduser("~"), ".cache", "voxlite_keyframes")


def norm(s: str) -> str:
    """归一化场景描述：去首尾空白、转小写、合并多余空格，让近似描述命中同一缓存"""
    return " ".join(s.strip().lower().split())


def key_of(style: str, scene: str) -> str:
    return hashlib.sha256(f"{norm(style)}|{norm(scene)}".encode("utf-8")).hexdigest()[:16]


def cache_path(style: str, scene: str, root: str) -> str:
    return os.path.join(root, f"{key_of(style, scene)}.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", help="查询缓存：传入 'style|scene'，命中打印路径 exit 0")
    ap.add_argument("--resolve", help="一键复用：传入 'style|scene'，命中则拷到 --out 并 exit 0，未命中 exit 1")
    ap.add_argument("--store", help="落缓存：传入 'style|scene'")
    ap.add_argument("--file", help="--store 对应的关键帧图片路径")
    ap.add_argument("--clear", action="store_true", help="清空整个缓存目录")
    ap.add_argument("--root", default=DEFAULT_CACHE, help="缓存根目录（默认 ~/.cache/voxlite_keyframes）")
    a = ap.parse_args()

    if a.clear:
        if os.path.isdir(a.root):
            shutil.rmtree(a.root)
        print(f"[cleared] {a.root}")
        return

    os.makedirs(a.root, exist_ok=True)

    if a.check:
        style, _, scene = a.check.partition("|")
        p = cache_path(style, scene, a.root)
        if os.path.isfile(p) and os.path.getsize(p) > 1000:
            print(p)
            sys.exit(0)
        sys.exit(1)

    if a.resolve:
        style, _, scene = a.resolve.partition("|")
        p = cache_path(style, scene, a.root)
        if os.path.isfile(p) and os.path.getsize(p) > 1000:
            if a.out:
                shutil.copy2(p, a.out)
                print(a.out)
            else:
                print(p)
            sys.exit(0)
        sys.exit(1)

    if a.store:
        style, _, scene = a.store.partition("|")
        if not a.file or not os.path.isfile(a.file):
            print("[error] --store 需要有效的 --file", file=sys.stderr)
            sys.exit(2)
        p = cache_path(style, scene, a.root)
        shutil.copy2(a.file, p)
        print(p)
        return


if __name__ == "__main__":
    main()
