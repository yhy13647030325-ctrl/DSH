#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验 skill-index.md 的内部一致性。

检查两项（按 8.2 变更义务的需求）：
  1. 数字一致性 —— 标题声明的技能数 vs 速览表实际行数 vs skills/ 目录数
  2. 编号唯一性 —— "### X 类：" 的字母前缀是否重复

★ 数字写法兼容（2026-11-12 改造）
--------------------------------
本脚本原先只认**中文数字**（"十四个技能"），
一旦有人写成"## 二、14 个技能速览"，就会：
  - 抓不到标题声明 → 数字一致性检查**静默失效**（漏报，比误报更危险）
  - --fix-numbers 也改不动（正则不匹配）

现统一用 NUM_PAT，**两种写法全吃**：
    "十四个技能" / "14 个技能" / "14个技能"  → 均能解析为 14

这与 validate-page-citations.py 的 RE_ANY(\\d{2,3}) 是同一条原则：
    **格式共存时，解析/统计代码必须全格式覆盖。**
只认一种写法的代码不会报错，它只会**悄悄算错**。

--fix-numbers 另有一处保守设计：**保持原写法**
    原文是中文 → 改完仍是中文（"二个技能"）
    原文是阿拉伯 → 改完仍是阿拉伯（"2 个技能"）
避免"修数字"顺带把格式也改了，从而掩盖格式不一致问题。

★ 三项补充改造（2026-11-12 第二次，修掉两个"静默失效"）
===================================================================

【改造 1】中文数字不再有上限
    原先 CN_NUM 是硬编码字典，最大到"二十"。
    超过 20 时 cn2int 返回 None → 调用方 `if n:` 判假 → **整项检查静默跳过**。
    实测："## 一、二十一个技能" 抓得到字符但解析为 None，
          最终 decl_nums 为空，检查 1 完全不执行，退出码仍是 0。

    现改为**算法解析**（见 cn2int）：按"十/百/千"分段累加，
    支持到 9999，实测 "一百零五" → 105 正确。

【改造 2】章节序号前缀不再精确匹配
    原先要求 "一、"/"1、"/"1. " 形式，实测以下写法**全部抓不到**：
        "## 1. 14 个技能速览"        ← 1. 后是空格
        "## （一）14 个技能速览"      ← 全角括号
        "## 第1章 14 个技能速览"      ← 章节词
        "## 1.5 节 14 个技能速览"
    根因：标题里可能有两个数字（序号 + 声明数），惰性匹配会锁定错的那个。

    现改为：前缀贪婪吞掉任意内容，**锁定紧邻"个技能"的那个数字**。
    实测 8 种写法全部命中。

【改造 3】新增自检，把"静默"变"可见"  ← 最重要
    上述两类问题的共同特征是：**不报错，直接跳过**。
    这比误报更危险——误报会引起注意，静默让人误以为"检查通过了"。

    现增加两道自检：
      (a) 抓到"N 个技能"但 cn2int 返回 None → WARN（解析缺口）
      (b) 标题含"个技能"但 RE_DECL 未命中 → WARN（列出文件行号）

    实测：标题写"若干 个技能"时，会明确提示
        [WARN] 以下标题含「个技能」但未能解析出数字，数字一致性检查对它们无效：
                 L3: ## 一、若干 个技能是什么关系

★ 三条改造的共同原则：
    **宁可 WARN，不可静默。**
    一个检查工具最坏的状态不是"报错太多"，而是"看起来在跑，其实没查"。

用法：
    python validate-skill-index.py                # 检查，有问题则退出码 1
    python validate-skill-index.py --fix-numbers  # 自动修正标题里的数字（谨慎）

设计说明：
- 只读不写（除非显式 --fix-numbers）
- 输出带 [ERROR] / [WARN] / [OK] 前缀，便于 grep
- 退出码：0 = 全部通过，1 = 有 ERROR
"""
import argparse
import os
import re
import sys

# 本脚本位于 <skills>/design-methodology-liuguanzong/references/
#   dirname            -> .../design-methodology-liuguanzong/references
#   ../..              -> <skills>
#   ../../..           -> .dsh
# 故：本技能根 = ../..；skills 根 = ../..
_here = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.normpath(os.path.join(_here, "..", ".."))

# Windows 控制台常为 GBK，强制 UTF-8 输出以免中文乱码
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

CN_DIGIT = {"零": 0, "〇": 0, "一": 1, "二": 2, "两": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
CN_UNIT = {"十": 10, "百": 100, "千": 1000}
# 大单位（分节）：万=10^4, 亿=10^8
# 中文数字按"节"分段：一万三千 = 1*10000 + 3000
CN_SECTION = {"万": 10 ** 4, "亿": 10 ** 8}
# 反向表（用于 --fix-numbers 回写中文，覆盖 1..99 足够）
CN_NUM = {
    1: "一", 2: "二", 3: "三", 4: "四", 5: "五", 6: "六", 7: "七",
    8: "八", 9: "九", 10: "十", 11: "十一", 12: "十二", 13: "十三",
    14: "十四", 15: "十五", 16: "十六", 17: "十七", 18: "十八",
    19: "十九", 20: "二十", 21: "二十一", 22: "二十二", 30: "三十",
    40: "四十", 50: "五十", 60: "六十", 70: "七十", 80: "八十",
    90: "九十", 100: "一百",
}
CN_NUM_REV = {v: k for k, v in CN_NUM.items()}

# ---------------------------------------------------------------------------
# ⚠ 教训（2026-11-12，来自 validate-page-citations.py 的同名问题）
#
# 凡是"数字"在不同地方可能写成**中文（十四个）**或**阿拉伯（14个）**两种形式，
# 只用一种正则去抓，就会漏掉另一种 → 误报或漏报。
#
# 本脚本原先只认中文数字（`[一二三四五六七八九十]+`），
# 一旦有人写成"## 二、14 个技能速览"，就会：
#   - 抓不到标题声明 → 数字一致性检查形同虚设（漏报）
#   - --fix-numbers 也改不动（因为正则不匹配）
#
# 现在统一用 NUM_PAT 一个模式，两种写法全吃。
# 这与页码脚本的 RE_ANY(\d{2,3}) 是同一个原则：
#   **格式共存时，统计/解析代码必须全格式覆盖。**
# ---------------------------------------------------------------------------

# 数字：中文（一…二十）或阿拉伯（1…99）
_RE_CN = r"[一二三四五六七八九十百千万亿零〇两]+"
_RE_AR = r"\d{1,4}"
NUM_PAT = rf"(?:{_RE_CN}|{_RE_AR})"

# ★ 2026-11-12 改造：章节序号前缀不再"精确匹配"，改为"尽量剥离"。
#
# 原先用 NUM_PAT + [、.．] 强制要求 "一、"/"1、"/"1. " 形式，
# 实测以下常见写法**全部抓不到数字**（decl=[]）：
#     "## 1. 14 个技能速览"       ← 1. 后是空格，不是 、
#     "## （一）14 个技能速览"     ← 全角括号
#     "## 第1章 14 个技能速览"     ← 章节词
# 抓不到 → 数字一致性检查静默跳过。
#
# 现改为：可选前缀 = 行首到数字之间的"任意非数字噪声"（含括号/顿号/章节词）。
# 只要能定位到 "N 个技能"，就允许 N 前面有各种装饰。
# 关键：标题里可能**有两个数字**（序号 + 声明数），如 "## 1. 14 个技能速览"、
# "## 第1章 14 个技能速览"。必须锁定**紧邻"个技能"的那个数字**，而不是第一个。
#
# 做法：前缀允许吞掉"除换行外任意字符（含数字）"，用贪婪匹配，
#       然后捕获**最后出现的**那个数字。
RE_HEADING_PREFIX = r"^#+\s*(?:.*?)"          # 贪婪吞掉，交给下面捕获最关键数字
RE_DECL = rf"{RE_HEADING_PREFIX}({NUM_PAT})\s*个技能"


def cn2int(s):
    """数字转整数，支持中文（含万/亿）与阿拉伯（任意位数）。

    返回 None 表示**无法解析**（调用方应视为"未声明"）。

    ★ 演进记录（2026-11-12，三次）
      1) 最初硬编码字典，最大"二十" → 超限返回 None → 调用方跳过 → **静默失效**
      2) 改算法解析（十/百/千）→ 支持到 9999
      3) 本轮补"万/亿"分节
         —— 修一个**更隐蔽**的 bug：
            "一万三千" 原先被正则截成 "三千" → 解析 3000（数字看似合理！）
            **不返回 None，自检也兜不住**，属"静默算错"。

    算法（标准做法，逐位扫描，按"节"归并）：
        ① 数字 → last
        ② 小单位（十/百/千）→ 把 pending 乘单位并入 section
        ③ 大单位（万/亿）→ 把 (total+section) 乘节单位并入 total，section 清零
        ④ 末尾把 section 并回 total

    验证：
        十四         = 10 + 4                    = 14
        一百零五     = 100 + 5                   = 105
        九千九百九十九 = 9000+900+90+9            = 9999
        一万三千     = 10000 + 3000              = 13000
        一亿二千万   = 10^8 + 2000*10^4          = 120000000

    ★ 裸量词规则（2026-11-12，第四次）
      "十" 单独出现 = 10（**标准写法**，"十个"是规范表达，允许省略"一"）
      "百/千/万/亿" 单独出现 = **None**（非规范数词，应写"一百/一千/一万/一亿"）

      为什么不能把它们也当成 100/1000/10000/10^8：
        - 规范中文数词中，除"十"外都必须带前导数字
        - 若强行当成数值，就又回到"静默算出一个看似合理的值"的老问题
        - 返回 None 能触发自检 WARN，把笔误**变成可见提示**
      "十"是唯一例外，不能类推——这是中文数词的固有规则，不是设计选择。
    """
    if s is None:
        return None
    s = str(s).strip()
    if not s:
        return None

    if s.isdigit():
        return int(s)

    if not all(c in CN_DIGIT or c in CN_UNIT or c in CN_SECTION for c in s):
        return None

    total = 0        # 已完成的大节累计（万/亿 之上）
    section = 0      # 当前节内累计（十/百/千 层）
    pending = 0      # 等待乘单位的数字
    seen = False
    # ★ 单位合法性校验（2026-11-12 第六次）：
    #   "十十"/"二十十"/"十百"/"一千一千" 这类写法不是中文数词，
    #   但简单累加会算出貌似合理的值（十十→20、十百→110）。
    #   规范要求：节内单位必须**严格降序**且**不重复**（千 > 百 > 十）。
    #   大单位（万/亿）必须**升序**（亿 > 万）。
    last_small_unit = 10 ** 9     # 上一个节内单位的数值（从大到小）
    last_big_unit = 0             # 上一个大单位的数值（从小到大）

    for ch in s:
        if ch in CN_DIGIT:
            d = CN_DIGIT[ch]
            if d == 0:
                # "零"只作占位，不参与累加
                continue
            pending = d
            seen = True
        elif ch in CN_UNIT:
            unit = CN_UNIT[ch]
            if pending == 0:
                # ★ 裸量词判定（2026-11-12）：
                #   "十" 单独出现是**标准写法**（十个=10），允许省略"一"；
                #   但"百/千"单独出现不是规范数词（应写"一百"/"一千"）。
                #   遇到裸的 百/千 → 视为无法解析，返回 None。
                #   这样会触发自检 WARN，而不是静默当成 100/1000。
                if unit != 10 and section == 0 and total == 0:
                    return None
                pending = 1          # "十四" 的 "十" 前省略"一"
            # 节内单位必须严格降序且不重复（千 > 百 > 十）
            if unit >= last_small_unit:
                return None
            last_small_unit = unit
            section += pending * unit
            pending = 0
            seen = True
        else:  # 万 / 亿
            mult = CN_SECTION[ch]
            if pending == 0 and section == 0:
                # ★ 裸 "万/亿"（前面没有任何数字、也没有已累计的值）→ 非规范数词
                #   规范写法是"一万"/"一亿"。返回 None 以触发自检。
                #   注意：total != 0 时（如"一万亿"的"亿"）是合法的。
                if total == 0:
                    return None
                pending = 1
            section += pending
            pending = 0

            # 大单位校验（2026-11-12 第七次修正）
            #   拒：重复同一单位（"万万"、"亿亿"）
            #   允：亿 → 万（亿级内可含万级，如"一亿二千万"）
            if mult == last_big_unit:
                return None
            last_big_unit = mult

            if mult == 10 ** 8:
                # 亿：把此前累计的全部（含万级）升格为"亿"
                total = (total + section) * mult
                section = 0
                # 亿之后允许重新出现 千/百/十（如"一亿二千万"）
                last_small_unit = 10 ** 9
            else:
                # 万：小节升格后并入 total（不乘已有 total）
                total += section * mult
                section = 0
            # 进入新节，节内单位从小重新开始
            last_small_unit = 10 ** 9
            seen = True

    result = total + section + pending

    if not seen:
        return None
    # 单个"万"/"亿"被吃掉后 pending 会被补 1，但那是合法写法（一万）
    # 真正要拒的是"空数字"（已由 not seen 覆盖）
    return result if result > 0 else None


def int2cn(n):
    """整数转中文数字（用于 --fix-numbers **保持原写法**）。

    覆盖 1..9999（万位亦可）。与 cn2int 互为逆运算，已完成 1..9999 全量往返验证。

    ★ 2026-11-12 第五次改造
      原实现只查 CN_NUM 字典（仅 1..100 的部分值），
      99 / 105 / 200 / 1000 等**退回阿拉伯写法**——
      于是 --fix-numbers 在"保持中文写法"时会冒出 `105 个技能`，
      **破坏了"保持原写法"这个承诺**。
      现改为算法生成。

    ★ 第六次改造（同日）
      首版实现里 `_under_100` / `_under_1000` 互相调用但有一处漏定义，
      1..105 正常、110 起崩溃。教训：
      **递归分段的实现必须跑全量往返测试，不能只抽查前几个**。
      现改为单函数 + 分段判断，不再嵌套辅助函数。

    规则（与 cn2int 对称）：
        1..9       → 一..九
        10..19     → 十 / 十一..十九          （"十"前省"一"）
        20..99     → 二十 / 二十一..九十九
        100..999   → 一百 / 一百零五 / 一百二十 （零位补"零"）
        1000..9999 → 一千 / 一千零五 / 一千二百
        10000+     → 一万 / 一万三千
    """
    if not isinstance(n, int) or n <= 0:
        return str(n)

    D = "零一二三四五六七八九"

    # ---------- 0..999 的基础表达 ----------
    def _seg(x):
        """1..999"""
        if x < 10:
            return D[x]
        if x < 20:
            return "十" + (D[x % 10] if x % 10 else "")
        if x < 100:
            t, r = divmod(x, 10)
            return D[t] + "十" + (D[r] if r else "")
        h, r = divmod(x, 100)
        body = D[h] + "百"
        if r == 0:
            return body
        if r < 10:
            return body + "零" + D[r]
        # ★ 110 → "一百一十"（规范），不是"一百十"
        #   十位为 1 时要显式写"一十"，否则孤立的"十"会被读成 10 而非 110
        if r < 20:
            return body + "一十" + (D[r % 10] if r % 10 else "")
        return body + _seg(r)

    # ---------- 1..9999 ----------
    def _big(x):
        """1..9999"""
        if x < 1000:
            return _seg(x)
        th, r = divmod(x, 1000)
        body = D[th] + "千"
        if r == 0:
            return body
        if r < 100:
            # 1005 → 一千零五；1050 → 一千零五十；1010 → 一千零一十
            if r < 10:
                return body + "零" + D[r]
            if r < 20:
                # 1010 不能写"一千零十"（"十"孤立会被读成 10）
                return body + "零一十" + (D[r % 10] if r % 10 else "")
            return body + "零" + _seg(r)
        return body + _seg(r)

    if n < 10000:
        return _big(n)

    w, r = divmod(n, 10000)
    head = _big(w) + "万"
    if r == 0:
        return head
    if r < 1000:
        # 10005 → 一万零五；10500 → 一万零五百；10010 → 一万零一十
        if r < 10:
            return head + "零" + D[r]
        if r < 20:
            return head + "零一十" + (D[r % 10] if r % 10 else "")
        return head + "零" + _seg(r)
    return head + _big(r)


# 明确不属于「设计类」的技能：即使被提及，也不要求在速览表中出现
# （索引里会提到 Blender 作为第 4 层视觉呈现，但它不进设计速览表时属正常；
#   若你要把它纳入速览表，从本集合移除即可）
NON_DESIGN_SKILLS = {
    "video-creation", "video-shotcraft", "video-talkcraft", "voxlite",
    "anything2explainer", "remotion", "archify", "book-to-skill",
    "ori-ai-product-design", "civil-code-china",
    "skills-backup", "_shared",
}


def find_index_file(root):
    """定位 skill-index.md。

    root 是 skills 根目录；skill-index.md 位于
    <root>/design-methodology-liuguanzong/references/skill-index.md。
    若在根目录直接找到，也接受（便于迁移）。
    """
    cands = [
        os.path.join(root, "design-methodology-liuguanzong", "references", "skill-index.md"),
        os.path.join(root, "references", "skill-index.md"),
        os.path.join(root, "skill-index.md"),
    ]
    for p in cands:
        if os.path.exists(p):
            return p
    # 兜底：全盘搜（限 3 层深）
    for dp, dns, fns in os.walk(root):
        if dp.count(os.sep) - root.count(os.sep) > 3:
            dns[:] = []
            continue
        if "skill-index.md" in fns:
            return os.path.join(dp, "skill-index.md")
    return None


def list_skill_dirs(root):
    """列出 skills/ 下所有技能目录名。"""
    if not os.path.isdir(root):
        return []
    return sorted(d for d in os.listdir(root)
                  if os.path.isdir(os.path.join(root, d)))


def md_chars(skill_path):
    """统计一个技能目录下所有 .md 的字符数。"""
    total = 0
    for dp, _, fs in os.walk(skill_path):
        for f in fs:
            if f.endswith(".md"):
                try:
                    total += len(open(os.path.join(dp, f), encoding="utf-8").read())
                except Exception:
                    pass
    return total


# ---------- 检查 1：数字一致性 ----------

def strip_code_blocks(text):
    """把 ``` 围栏代码块与行内代码内容清空，避免其中的"示例标题"被当成真标题。

    ★ 2026-11-12 补：规范文档里会举例说明各种标题写法，例如
          ``` 
          ## 二十一、21 个技能速览   ✓
          ```
      未剥离时，脚本把这个**示例**当成真标题，报出假 ERROR：
          [ERROR] 标题声明「21个技能」但速览表实际 14 行
      与"教训 2（元文档排除）"是同一类问题：**示例内容不等于真实内容**。
    """
    out = []
    in_fence = False
    for line in text.split("\n"):
        st = line.lstrip()
        if st.startswith("```") or st.startswith("~~~"):
            in_fence = not in_fence
            out.append("")          # 围栏行本身也清掉
            continue
        if in_fence:
            out.append("")          # 代码块内容清掉
        else:
            out.append(line)
    return "\n".join(out)


def check_numbers(text, index_path, skills_root):
    errs, warns, oks = [], [], []

    # 剥离代码块后再解析（见 strip_code_blocks 说明）
    text = strip_code_blocks(text)

    # 1a. 标题里声明的技能数（去重：两处标题可能都写同一个数字）
    # 支持「十四个技能」与「14 个技能」两种写法（见文件头教训）
    decl = re.findall(RE_DECL, text, re.M)
    decl_nums = []
    seen_decl = set()
    unparsed = []
    for d in decl:
        n = cn2int(d)
        if n is None:
            # ★ 自检（2026-11-12）：抓到了"N 个技能"却解析不出数字。
            #   以前这种情况会被 `if n:` 静默跳过，导致整项检查失效。
            #   现在显式记录，稍后报 WARN。
            unparsed.append(d)
            continue
        if n not in seen_decl:
            seen_decl.add(n)
            decl_nums.append((d, n))

    # 再扫一遍"疑似声明"：出现"个技能"但 RE_DECL 没抓到数字的行
    # （例如"共十三个技能"这种复述句不该报，只报**标题行**里的）
    suspicious = []
    for ln, line in enumerate(text.split("\n"), 1):
        if "个技能" not in line:
            continue
        if not line.lstrip().startswith("#"):
            continue                      # 只查标题行
        if re.search(RE_DECL, line):
            continue                      # 已成功解析
        suspicious.append((ln, line.strip()[:70]))

    if unparsed:
        # 区分两类原因，给出可操作的提示
        bare = [x for x in unparsed if x in ("百", "千", "万", "亿")]
        other = [x for x in unparsed if x not in ("百", "千", "万", "亿")]
        msgs = []
        if bare:
            msgs.append(
                "发现**裸量词** %s —— 这不是规范数词，"
                "应写成「一百」「一千」「一万」「一亿」（「十」除外，它可单独使用）"
                % "、".join(repr(x) for x in bare))
        if other:
            msgs.append("无法解析：%s" % "、".join(repr(x) for x in other))
        warns.append(
            "标题里的数字无法解析 → 数字一致性检查对它无效。\n"
            + "\n".join("            " + m for m in msgs))
    if suspicious:
        warns.append(
            "以下标题含「个技能」但未能解析出数字，数字一致性检查对它们无效：\n"
            + "\n".join("            L%d: %s" % (ln, t) for ln, t in suspicious))

    # 1b. 速览表的实际技能行
    sec = re.search(r"^##[^\n]*技能速览[^\n]*$", text, re.M)
    table_names = []
    if sec:
        start = sec.end()
        nxt = re.search(r"^##\s", text[start:], re.M)
        body = text[start:start + nxt.start()] if nxt else text[start:]
        table_names = re.findall(r"^\|\s*`([a-zA-Z0-9\-_]+)`", body, re.M)

    # 1c. skills/ 实际目录数（排除非技能目录）
    actual_dirs = [d for d in list_skill_dirs(skills_root)
                   if not d.startswith(".") and d != "_shared"]

    if not sec:
        errs.append("找不到「技能速览」章节，无法校验数字")
    else:
        n_table = len(table_names)
        for cn, n in decl_nums:
            if n != n_table:
                errs.append(
                    "标题声明「%s个技能」但速览表实际 %d 行" % (cn, n_table))
            else:
                oks.append("标题声明 %d 个 = 速览表 %d 行" % (n, n_table))

            # 与 skills/ 目录数比（注意：速览表只列设计类，不等于全部）
            if n != len(actual_dirs):
                warns.append(
                    "标题声明 %d 个，但 skills/ 下有 %d 个目录"
                    "（速览表只列设计类，差额可能是预装技能，属正常）"
                    % (n, len(actual_dirs)))

        # 1c-bis. 速览表是否遗漏了「全文其他地方提到的设计技能」
        #   做法：取全文反引号里的技能名，减去表内已列，再排除明确的非设计技能
        mentioned = set(re.findall(r"`([a-zA-Z0-9\-_]{8,})`", text))
        missing = sorted(mentioned - set(table_names) - NON_DESIGN_SKILLS)
        # 只报告确实是技能目录的
        missing = [m for m in missing if os.path.isdir(os.path.join(skills_root, m))]
        if missing:
            errs.append(
                "速览表遗漏了这些技能（全文已提及但表中无行）：%s"
                % "、".join("`%s`" % m for m in missing))

        # 1d. 速览表字数 vs 实测
        if sec:
            start = sec.end()
            nxt = re.search(r"^##\s", text[start:], re.M)
            body = text[start:start + nxt.start()] if nxt else text[start:]
            for line in body.split("\n"):
                m = re.match(r"^\|\s*`([a-zA-Z0-9\-_]+)`.*?\|\s*([\d.]+)\s*万字", line)
                if not m:
                    continue
                name, claimed = m.group(1), float(m.group(2))
                sp = os.path.join(skills_root, name)
                if not os.path.isdir(sp):
                    errs.append("速览表列了 `%s`，但 skills/ 下没有该目录" % name)
                    continue
                actual = md_chars(sp) / 10000.0
                if abs(actual - claimed) >= 0.3:
                    warns.append(
                        "字数偏差 `%s`：表内 %.1f 万，实测 %.1f 万"
                        % (name, claimed, actual))

    return errs, warns, oks


# ---------- 检查 2：编号唯一性 ----------

def check_class_ids(text):
    errs, warns, oks = [], [], []
    heads = [(m.group(1), m.group(2).strip())
             for m in re.finditer(r"^###\s*([A-Z])\s*类[：:]\s*(.+)$", text, re.M)]
    if not heads:
        warns.append("没找到「X 类：」形式的类别标题")
        return errs, warns, oks

    seen = {}
    for letter, title in heads:
        if letter in seen:
            errs.append(
                "类别编号重复：`%s 类` 出现两次 —— 「%s」与「%s」"
                % (letter, seen[letter], title))
        else:
            seen[letter] = title
            oks.append("%s 类：%s" % (letter, title))

    # 顺序连续性提示（A,B,C,D,E 应连续）
    letters = [h[0] for h in heads]
    expected = [chr(ord("A") + i) for i in range(len(letters))]
    if letters != expected:
        warns.append("类别字母不连续：实际 %s，期望 %s"
                     % ("".join(letters), "".join(expected)))

    return errs, warns, oks


# ---------- 主流程 ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-root", default=SKILLS_DIR,
                    help="skills 根目录（默认自动推断）")
    ap.add_argument("--fix-numbers", action="store_true",
                    help="自动把标题里的数字改成速览表行数")
    args = ap.parse_args()

    skills_root = os.path.abspath(args.skills_root)
    idx = find_index_file(skills_root)
    if not idx:
        print("[ERROR] 找不到 skill-index.md，查找起点：%s" % skills_root)
        return 1

    text = open(idx, encoding="utf-8").read()
    print("检查文件：%s" % idx)
    print("字符数：%d" % len(text))
    print()

    all_err = []

    print("=" * 62)
    print("检查 1：数字一致性")
    print("=" * 62)
    e1, w1, o1 = check_numbers(text, idx, skills_root)
    for x in o1:
        print("  [OK]    %s" % x)
    for x in w1:
        print("  [WARN]  %s" % x)
    for x in e1:
        print("  [ERROR] %s" % x)
    all_err += e1
    print()

    print("=" * 62)
    print("检查 2：编号唯一性")
    print("=" * 62)
    e2, w2, o2 = check_class_ids(text)
    for x in o2:
        print("  [OK]    %s" % x)
    for x in w2:
        print("  [WARN]  %s" % x)
    for x in e2:
        print("  [ERROR] %s" % x)
    all_err += e2
    print()

    print("=" * 62)
    if all_err:
        print("结果：%d 个 ERROR，%d 个 WARN" % (len(all_err), len(w1) + len(w2)))
        if args.fix_numbers:
            print("\n--fix-numbers：尝试修正标题数字……")
            sec = re.search(r"^##[^\n]*技能速览[^\n]*$", text, re.M)
            if sec:
                start = sec.end()
                nxt = re.search(r"^##\s", text[start:], re.M)
                body = text[start:start + nxt.start()] if nxt else text[start:]
                n = len(re.findall(r"^\|\s*`([a-zA-Z0-9\-_]+)`", body, re.M))
                # ★ 保持原写法：原文是中文就写中文，是阿拉伯就写阿拉伯。
                #   避免"修数字"顺带把格式也改了（那样会掩盖格式不一致问题）。
                # ★ 用命名组，避免 RE_HEADING_PREFIX 内部的捕获组导致编号错位
                #   （2026-11-12 实测 bug：原先按 1/2/3 取组，实际前缀占了 group(1)，
                #     运行时报 IndexError: no such group）
                def _keep_style(m):
                    old_num = m.group("num")
                    # 只替换数字本身，前后文原样保留
                    start, end = m.span("num")
                    whole = m.group(0)
                    offset = start - m.start()
                    new_num = str(n) if old_num.isdigit() else int2cn(n)
                    return whole[:offset] + new_num + whole[offset + len(old_num):]

                fixed = re.sub(
                    rf"{RE_HEADING_PREFIX}(?P<num>{NUM_PAT})(\s*个技能)",
                    _keep_style, text, flags=re.M)
                if fixed != text:
                    open(idx, "w", encoding="utf-8").write(fixed)
                    print("已把标题数字改为 %d（保持原写法）" % n)
                else:
                    print("未能修正（无匹配）")
        return 1
    else:
        print("结果：全部通过（%d 个 WARN）" % (len(w1) + len(w2)))
        return 0


if __name__ == "__main__":
    sys.exit(main())
