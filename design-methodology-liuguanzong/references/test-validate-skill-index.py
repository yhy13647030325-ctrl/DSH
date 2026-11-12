#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate-skill-index.py 的回归测试（数字解析与回写）。

为什么需要这份测试
------------------
`cn2int` / `int2cn` 是本项目最容易"静默出错"的代码：

  - 静默失效：超限返回 None → 调用方 `if n:` 跳整项检查
  - 静默算错："一万三千" 被截成 "三千" → 3000（数字看似合理，自检兜不住）
  - 边界崩溃：辅助函数漏定义 → 1..105 正常、110 起 NameError

这些错误**都不是逻辑想错，而是没在边界上验证**。
实测教训：第一次只测到 105，正好跳过了 110 那个坑。

所以本测试的两个硬要求：
  1. **全量往返**（1..99999）：int2cn → cn2int 必须还原原值
  2. **边界显式列举**：10/100/1000/10000 附近逐个点名

用法
----
    python test-validate-skill-index.py          # 跑全部，输出汇总
    python test-validate-skill-index.py -v       # 显示每个用例
    python test-validate-skill-index.py --quick  # 跳过 10 万级全量往返（约 3 秒）

退出码：0 = 全通过，1 = 有失败。

设计说明
--------
- 不依赖 pytest（环境里没有），纯标准库
- 被测模块用 importlib 按路径加载，无需安装
- 每个断言失败都打印 **输入 / 期望 / 实际**，便于直接定位
"""
import argparse
import importlib.util
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

_HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(_HERE, "validate-skill-index.py")


def load_target():
    """按路径加载被测模块。"""
    if not os.path.exists(TARGET):
        print(f"[FATAL] 找不到被测脚本：{TARGET}")
        sys.exit(1)
    spec = importlib.util.spec_from_file_location("vsi", TARGET)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# 用例表
# ---------------------------------------------------------------------------

# ① cn2int：中文/阿拉伯 → 整数
CN2INT_CASES = [
    # 基础
    ("一", 1), ("二", 2), ("九", 9),
    ("十", 10), ("十一", 11), ("十四", 14), ("十九", 19),
    ("二十", 20), ("二十一", 21), ("三十", 30), ("九十九", 99),
    # 百位
    ("一百", 100), ("一百零一", 101), ("一百零五", 105),
    ("一百一十", 110), ("一百二十", 120), ("二百", 200),
    ("五百", 500), ("九百九十九", 999),
    # 千位
    ("一千", 1000), ("一千零五", 1005), ("一千零一十", 1010),
    ("一千零五十", 1050), ("一千一百", 1100),
    ("一千二百三十四", 1234), ("九千九百九十九", 9999),
    # 万位
    ("一万", 10000), ("一万零五", 10005), ("一万三千", 13000),
    ("三万二", 30002), ("五万", 50000), ("十万", 100000),
    ("十四万", 140000), ("一百二十万", 1200000),
    # 亿位
    ("一亿", 100000000), ("一亿二千万", 120000000),
    # 阿拉伯
    ("14", 14), ("105", 105), ("10000", 10000), ("99999", 99999),
]

# ② cn2int：裸量词 → None（"十" 除外，它是标准写法）
BARE_CASES = [
    ("十", 10),      # 唯一允许裸用的量词
    ("百", None), ("千", None), ("万", None), ("亿", None),
]

# ③ cn2int：无法解析的输入 → None
#
# ★ 这一组是"简单累加会算出貌似合理值"的非法写法（2026-11-12 发现）：
#     "十十" 曾算出 20、"十百" 曾算出 110、"一千一千" 曾算出 2000
#   中文数词要求：节内单位严格降序且不重复（千>百>十），大单位不得重复。
#   这些用例是**测试写出来后才发现的缺陷**，务必保留。
INVALID_CASES = [
    "", "   ", None, "abc",
    "零",              # 单独零
    "十十",            # 单位重复（曾=20）
    "百百",            # 单位重复
    "万万",            # 大单位重复
    "十百",            # 单位升序（曾=110）
    "二十十",          # 单位重复（曾=30）
    "一千一千",        # 单位重复（曾=2000）
]

# ④ int2cn：整数 → 中文（规范写法）
INT2CN_CASES = [
    (1, "一"), (9, "九"), (10, "十"), (11, "十一"), (14, "十四"),
    (19, "十九"), (20, "二十"), (21, "二十一"), (99, "九十九"),
    (100, "一百"), (101, "一百零一"), (105, "一百零五"),
    (110, "一百一十"),      # 不是"一百十"
    (120, "一百二十"), (200, "二百"), (999, "九百九十九"),
    (1000, "一千"), (1005, "一千零五"),
    (1010, "一千零一十"),   # 不是"一千零十"
    (1050, "一千零五十"), (1100, "一千一百"),
    (1234, "一千二百三十四"), (9999, "九千九百九十九"),
    (10000, "一万"), (10005, "一万零五"), (13000, "一万三千"),
]

# ⑤ 端到端：标题数字声明解析
DECL_CASES = [
    ("## 一、14 个技能速览", "14"),
    ("## 1、14 个技能速览", "14"),
    ("## 1. 14 个技能速览", "14"),
    ("## （一）14 个技能速览", "14"),
    ("## 第1章 14 个技能速览", "14"),
    ("## 1.5 节 14 个技能速览", "14"),
    ("## 二、十四个技能是什么关系", "十四"),
    ("## 二十一、21 个技能速览", "21"),
    ("## 一、一万三千个技能", "一万三千"),
]


class Runner:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.pass_ = 0
        self.fail = 0
        self.failures = []

    def check(self, label, got, exp):
        ok = (got == exp)
        if ok:
            self.pass_ += 1
            if self.verbose:
                print(f"    ✓ {label}")
        else:
            self.fail += 1
            msg = f"    ✗ {label}\n        期望 {exp!r}\n        实际 {got!r}"
            print(msg)
            self.failures.append((label, exp, got))

    def section(self, title):
        print(f"\n{'=' * 66}\n{title}\n{'=' * 66}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", action="store_true", help="显示每个用例")
    ap.add_argument("--quick", action="store_true",
                    help="跳过 1..99999 全量往返（约省 3 秒）")
    args = ap.parse_args()

    m = load_target()
    r = Runner(args.verbose)

    # ---- ① 中文/阿拉伯 → 整数 ----
    r.section("① cn2int：中文/阿拉伯 → 整数")
    for txt, exp in CN2INT_CASES:
        r.check(f"cn2int({txt!r})", m.cn2int(txt), exp)
    print(f"  {len(CN2INT_CASES)} 个用例")

    # ---- ② 裸量词 ----
    r.section("② cn2int：裸量词（只有「十」允许裸用）")
    for txt, exp in BARE_CASES:
        r.check(f"cn2int({txt!r})", m.cn2int(txt), exp)
    print(f"  {len(BARE_CASES)} 个用例")

    # ---- ③ 非法输入 ----
    r.section("③ cn2int：无法解析 → None")
    for x in INVALID_CASES:
        r.check(f"cn2int({x!r})", m.cn2int(x), None)
    print(f"  {len(INVALID_CASES)} 个用例")

    # ---- ④ 整数 → 中文 ----
    r.section("④ int2cn：整数 → 中文（规范写法）")
    for n, exp in INT2CN_CASES:
        r.check(f"int2cn({n})", m.int2cn(n), exp)
    print(f"  {len(INT2CN_CASES)} 个用例")

    # ---- ⑤ 标题声明解析 ----
    r.section("⑤ 端到端：标题里的「N 个技能」解析")
    import re
    for line, exp in DECL_CASES:
        got = re.findall(m.RE_DECL, line, re.M)
        r.check(f"RE_DECL({line!r})",
                got[0] if got else None, exp)
    print(f"  {len(DECL_CASES)} 个用例")

    # ---- ⑥ 全量往返（核心）----
    if args.quick:
        r.section("⑥ 往返测试（已跳过，--quick）")
        print("  ⚠ 未执行最关键的验证。正式提交前请跑完整版。")
    else:
        r.section("⑥ 往返测试：int2cn → cn2int 必须还原原值")
        bad = []
        for n in range(1, 100000):
            cn = m.int2cn(n)
            back = m.cn2int(cn)
            if back != n:
                bad.append((n, cn, back))
        r.check("1..99999 全量往返", len(bad), 0)
        for n, cn, back in bad[:10]:
            print(f"        失败样本：{n} → {cn!r} → {back}")

    # ---- 汇总 ----
    total = r.pass_ + r.fail
    print(f"\n{'=' * 66}")
    if r.fail:
        print(f"结果：{r.fail} 失败 / {total} 用例")
        print("\n失败清单：")
        for label, exp, got in r.failures:
            print(f"  - {label}: 期望 {exp!r}，实际 {got!r}")
        return 1
    print(f"结果：全部通过（{total} 个断言）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
