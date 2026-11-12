#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验技能文档的"原书页码引用"。

解决的问题
----------
多本技能是从纸质书/PDF 蒸馏的，正文里大量写 `（p123）` 标记原文出处。
这类引用有三个常见缺陷，肉眼很难发现：

  1. **页码越界** —— 引用了书里不存在的页（如全书到 p135，却写 p137）
  2. **格式不一致** —— 同一技能内混用 `p12` 与 `p012`
  3. **未实读引用** —— 页码来自二手转述，且没有实读清单支撑

第 3 项需要一份"实读清单"（manifest）。本脚本支持可选 manifest：
未提供时只查 1、2 项。

用法
----
    # 只查越界与格式（不需要 manifest）
    python validate-page-citations.py --skill product-structure-liubaoshun

    # 用 manifest 查"未实读引用"
    python validate-page-citations.py --skill product-structure-liubaoshun \\
        --manifest page-manifest.json

    # 全部技能
    python validate-page-citations.py --all

    # 生成 manifest 模板（把已实读的页填进去）
    python validate-page-citations.py --skill XXX --init-manifest

    # 也扫描 CHANGELOG 等元文档（默认跳过，见教训 2）
    python validate-page-citations.py --skill XXX --include-meta

manifest 格式（JSON）
---------------------
单一页码体系：
    {
      "book": "《产品结构设计》刘宝顺",
      "page_range": [9, 136],          // 书内正文页码范围
      "read": [9, 10, 12, ...],        // 已实读的页（逐页核对过的）
      "note": "p136 是参考文献页"
    }

多页码体系并存（有些书/技能同时用"书内页"和"PDF 页"）：
    {
      "book": "《…》",
      "page_type": "PDF 页与书内页混用",
      "ranges": [
        {"type": "书内页", "range": [2, 202]},
        {"type": "PDF 页",  "range": [28, 228]}
      ],
      "read": [],
      "note": "页码落在任一体系内即算合规"
    }

退出码：0 = 通过，1 = 有 ERROR。


================================================================================
两个真实踩过的坑（2026-11-12 修，写在这里避免再犯）
================================================================================

【教训 1】统计页码范围时，必须同时匹配"两位"和"三位"写法
------------------------------------------------------------------
现象
    第一次为 solidworks-2025-mechanical 建 manifest 时，
    用 `p(\\d{3})` 统计引用到的页码，得到范围 [145, 921]。
    跑 --all 时报了 **180 个 ERROR**，全部是假的：
        [ERROR] 页码越界 p11 —— ch01-interface.md:3 `p11–69`
    但 `p11–69` 明明是合法的章节范围。

根因
    该技能里存在 **`p11`（两位）** 这样的写法。
    用三位正则 `p(\\d{3})` 匹配不到它，
    于是"引用到的最小页"被算成 145（而不是真实的 11），
    manifest 的 page_range 下限过高 → 所有 <145 的引用全被判越界。

正确做法
    统计范围时用 **`p(\\d{2,3})`**（见下方 RE_ANY），两种写法都要吃进去。
    本脚本的 RE_RANGE / collect_citations 已经这样处理。

教训提炼
    **"格式不统一"会连带破坏"范围统计"** ——
    这两件事不是独立的：只要允许两种写法共存，
    任何只认一种写法的统计代码都会漏数据。
    → 所以格式统一（警告项）不只是美观问题，它是**数据正确性的前提**。


【教训 2】CHANGELOG 等"元文档"必须排除在页码扫描之外
------------------------------------------------------------------
现象
    在 CHANGELOG 里记录了各技能的页码范围（如 `p13–p207`），
    再跑 --all 时，design-methodology-liuguanzong 报了 **784 个 ERROR**：
        [ERROR] 页码越界 p138 —— references\\CHANGELOG.md:1282

根因
    CHANGELOG 是**元文档**：它的内容是关于"所有技能"的，
    里面会引用**别的技能**的页码范围。
    扫描它，就会把他人的页码当成"本技能的引用"，从而误判越界。

正确做法
    默认跳过 META_FILES 里列出的元文档（见下方常量）。
    如果确实要检查某个元文档自身，用 `--include-meta` 显式开启。

教训提炼
    **"描述内容的文档"与"被描述的内容"必须分层**。
    日志/索引/总览这类文件天然跨技能，
    把它们纳入单技能的机械扫描，必然产生假阳性。
    → 新写扫描类工具时，先问一句：**这个文件是在"讲事情"还是在"记录事情"？**

================================================================================
这两个坑的共同特征：**都是工具误报，不是文档有错**。
误报比漏报更消耗信任——一次假 ERROR 就会让人开始怀疑所有 ERROR。
所以宁可多花一行代码排除，也不要让工具报出它自己没把握的东西。
================================================================================
"""
import argparse
import json
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# 本脚本位于 <skills>/<某技能>/references/ 时，向上 2 级为 skills 根
_HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SKILLS_ROOT = os.path.normpath(os.path.join(_HERE, "..", ".."))

# 页码写法：p123 / （p123） / (p12) / p123-124 / p123-45
#
# ⚠ 教训 1（2026-11-12）：统计**页码范围**时必须用 RE_ANY（\d{2,3}），
#    不能用 RE_P3（\d{3}）。因为只要存在 `p11` 这类两位写法，
#    三位正则就会漏掉它，导致 range 下限偏高 → 大量假越界。
#    这两个正则的用途不同，别混用：
#      RE_P3 / RE_P2 —— 用于"格式一致性"检查（要区分写法）
#      RE_ANY        —— 用于"范围统计"（两种都要吃）
RE_P3 = re.compile(r"p(\d{3})")
RE_P2 = re.compile(r"[（(]p(\d{1,2})[）)]")
RE_RANGE = re.compile(r"p(\d{2,3})\s*[–\-~]\s*p?(\d{2,3})")
# 范围统计专用：两位/三位通吃（见教训 1）
RE_ANY = re.compile(r"p(\d{2,3})(?!\d)")

# ⚠ 教训 2（2026-11-12）：这些是"元文档"——它们的内容是**关于所有技能**的，
#    里面会引用**别的技能**的页码范围（例如 CHANGELOG 里写 "solidworks-surface-advanced p13-p207"）。
#    把它们纳入单技能扫描，就会把他人的页码判成本技能越界 → 实测产生 784 个假 ERROR。
#
#    判断标准：这个文件是在"讲内容"还是在"记录内容"？
#    "记录内容"的（日志/索引/总览/规范）一律排除。
#    确需检查时用 --include-meta 显式开启。
#
#    新增元文档时，记得往这个集合里加。
META_FILES = {"changelog.md", "before-after.md", "skill-catalog.md",
              "skill-index.md", "standard.md"}


def find_skills_root(explicit=None):
    if explicit:
        return os.path.abspath(explicit)
    if os.path.isdir(DEFAULT_SKILLS_ROOT):
        return DEFAULT_SKILLS_ROOT
    # 兜底：向上找含多个技能目录的父级
    cur = _HERE
    for _ in range(5):
        cur = os.path.dirname(cur)
        if os.path.isdir(cur) and any(
            os.path.isdir(os.path.join(cur, d)) for d in os.listdir(cur)
        ):
            return cur
    return DEFAULT_SKILLS_ROOT


def iter_md(skill_dir, include_meta=False):
    for dp, _, fs in os.walk(skill_dir):
        for f in sorted(fs):
            if not f.endswith(".md"):
                continue
            if not include_meta and os.path.basename(f).lower() in META_FILES:
                continue
            yield os.path.join(dp, f)


def collect_citations(skill_dir, include_meta=False):
    """返回 {页码: [(相对文件, 行号, 原始片段)]}，以及格式统计。"""
    cites = {}
    fmt = {"p3": 0, "p2": 0}
    for path in iter_md(skill_dir, include_meta):
        rel = os.path.relpath(path, skill_dir)
        try:
            text = open(path, encoding="utf-8").read()
        except Exception:
            continue
        lines = text.split("\n")
        # 行号索引
        line_of = []
        for i, ln in enumerate(lines, 1):
            line_of.extend([i] * (len(ln) + 1))

        consumed = set()

        # 先处理区间（p100-p105），避免把两端重复计
        for m in RE_RANGE.finditer(text):
            a, b = int(m.group(1)), int(m.group(2))
            lo, hi = min(a, b), max(a, b)
            consumed.add((m.start(), m.end()))
            snippet = m.group(0)
            ln = line_of[m.start()] if m.start() < len(line_of) else 0
            for pg in (lo, hi):
                cites.setdefault(pg, []).append((rel, ln, snippet))
                fmt["p3"] += 1
            for pg in range(lo + 1, hi):
                cites.setdefault(pg, []).append((rel, ln, snippet + "（区间内）"))

        for pat, key in ((RE_P3, "p3"), (RE_P2, "p2")):
            for m in pat.finditer(text):
                if any(s <= m.start() < e for s, e in consumed):
                    continue
                pg = int(m.group(1))
                ln = line_of[m.start()] if m.start() < len(line_of) else 0
                cites.setdefault(pg, []).append((rel, ln, m.group(0)))
                fmt[key] += 1
    return cites, fmt


def check(skill_dir, manifest=None, include_meta=False):
    errs, warns, oks = [], [], []
    cites, fmt = collect_citations(skill_dir, include_meta)
    if not cites:
        return errs, [f"该技能没有页码引用（可能不用 pXXX 标注）"], oks, fmt, cites

    all_pages = sorted(cites)

    # --- 检查 1：越界 ---
    if manifest:
        # 支持两种 manifest 形态：
        #   (a) 单一体系：{"page_range": [lo, hi]}
        #   (b) 多体系并存：{"ranges": [{"type":"书内页","range":[2,202]}, ...]}
        # 多体系时，只要页码落在**任一**体系内即算合规。
        spans = []
        for r in manifest.get("ranges", []) or []:
            rg = r.get("range")
            if rg and len(rg) == 2:
                spans.append((rg[0], rg[1], r.get("type", "")))
        if not spans:
            pr = manifest.get("page_range")
            if pr and len(pr) == 2:
                spans.append((pr[0], pr[1], ""))

        if spans:
            out = [p for p in all_pages
                   if not any(lo <= p <= hi for lo, hi, _ in spans)]
            label = " / ".join(f"{t or '页码'} p{lo}-p{hi}" for lo, hi, t in spans)
            if out:
                for p in out:
                    where = cites[p][0]
                    errs.append(
                        f"页码越界 p{p}（允许范围 {label}）"
                        f" —— {where[0]}:{where[1]} `{where[2]}`"
                    )
            else:
                oks.append(f"页码范围合规（{label}，共 {len(all_pages)} 个不同页）")

    # --- 检查 2：格式一致性（p3 与 p2 混用）---
    if fmt["p3"] and fmt["p2"]:
        p2_pages = sorted({int(m) for p in all_pages for _, _, s in cites[p]
                           for m in re.findall(r"[（(]p(\d{1,2})[）)]", s)})
        warns.append(
            f"页码格式混用：三位 `pNNN` {fmt['p3']} 处 vs 两位 `pNN` {fmt['p2']} 处"
            f"（两位的页：{p2_pages[:12]}{'...' if len(p2_pages) > 12 else ''}）"
            f" → 建议统一为三位 `pNNN`"
        )
    elif fmt["p2"]:
        warns.append(f"全部使用两位格式 `pNN`（{fmt['p2']} 处），建议改为三位 `pNNN`")
    else:
        oks.append(f"页码格式统一（三位 `pNNN`，{fmt['p3']} 处）")

    # --- 检查 3：未实读引用 ---
    if manifest and manifest.get("read"):
        read = set(manifest["read"])
        unread = [p for p in all_pages if p not in read]
        if unread:
            for p in unread[:20]:
                where = cites[p][0]
                errs.append(
                    f"引用未实读页 p{p} —— {where[0]}:{where[1]} `{where[2]}`"
                )
            if len(unread) > 20:
                errs.append(f"……另有 {len(unread) - 20} 个未实读页")
        else:
            oks.append(f"所有引用页均已实读（{len(all_pages)} 个）")

        # 覆盖率提示
        if manifest.get("page_range"):
            lo, hi = manifest["page_range"]
            total = hi - lo + 1
            covered = len([p for p in all_pages if lo <= p <= hi])
            oks.append(
                f"页码覆盖：{covered}/{total} 页被正文引用"
                f"（实读 {len([p for p in read if lo <= p <= hi])}/{total}）"
            )
    return errs, warns, oks, fmt, cites


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", help="技能目录名（在 skills 根下）")
    ap.add_argument("--all", action="store_true", help="检查所有含页码引用的技能")
    ap.add_argument("--skills-root", help="skills 根目录")
    ap.add_argument("--manifest", help="实读清单 JSON 路径")
    ap.add_argument("--include-meta", action="store_true",
                    help="也扫描 CHANGELOG 等元文档（默认跳过，避免误判他技能页码）")
    ap.add_argument("--init-manifest", action="store_true",
                    help="生成 manifest 模板（列出当前引用的所有页）")
    args = ap.parse_args()

    root = find_skills_root(args.skills_root)

    targets = []
    if args.all:
        for d in sorted(os.listdir(root)):
            p = os.path.join(root, d)
            if not os.path.isdir(p):
                continue
            c, _ = collect_citations(p, args.include_meta)
            if c:
                targets.append(d)
    elif args.skill:
        targets = [args.skill]
    else:
        ap.error("需要 --skill 或 --all")

    grand_err = 0
    for name in targets:
        skill_dir = os.path.join(root, name)
        if not os.path.isdir(skill_dir):
            print(f"[ERROR] 找不到技能目录：{skill_dir}")
            grand_err += 1
            continue

        # manifest
        manifest = None
        mf_path = args.manifest
        if not mf_path:
            cand = os.path.join(skill_dir, "references", "page-manifest.json")
            if os.path.exists(cand):
                mf_path = cand
        if mf_path and os.path.exists(mf_path):
            try:
                manifest = json.load(open(mf_path, encoding="utf-8"))
            except Exception as e:
                print(f"[WARN] manifest 读取失败：{e}")

        print("=" * 70)
        print(f"技能：{name}")
        if manifest:
            print(f"书目：{manifest.get('book', '(未注明)')}")
        else:
            print("书目：(无 manifest，跳过越界与实读检查)")

        if args.init_manifest:
            cites, _ = collect_citations(skill_dir)
            pages = sorted(cites)
            tpl = {
                "book": "（填写书名）",
                "page_range": [min(pages), max(pages)] if pages else [1, 1],
                "read": pages,
                "note": "read 应只填真正逐页核对过的页；page_range 是书内正文范围",
            }
            out = os.path.join(skill_dir, "references", "page-manifest.json")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            json.dump(tpl, open(out, "w", encoding="utf-8"),
                      ensure_ascii=False, indent=2)
            print(f"已生成模板：{out}")
            print(f"（其中 read 当前填的是'已被引用的页'{len(pages)} 个，请按实际核对情况删减）")
            continue

        errs, warns, oks, fmt, cites = check(skill_dir, manifest, args.include_meta)
        for x in oks:
            print(f"  [OK]    {x}")
        for x in warns:
            print(f"  [WARN]  {x}")
        for x in errs:
            print(f"  [ERROR] {x}")
        grand_err += len(errs)
        print()

    print("=" * 70)
    if grand_err:
        print(f"结果：{grand_err} 个 ERROR")
        return 1
    print("结果：无 ERROR")
    return 0


if __name__ == "__main__":
    sys.exit(main())
