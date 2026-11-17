# 仓库维护约定（Repo Hygiene）

> **本文件记录 `.dsh/skills` 仓库的编码与行尾约定，以及已经做过实测判断的结论。**
> 目的：避免同一件事被反复"重新发现"和反复"重新修一遍"。
>
> 制定日期：2026-11-17
> 适用范围：`.dsh/skills` 下全部 533 个受版本控制文件

---

## 一、一句话结论

> **仓库是干净的 LF（索引 `i/crlf = 0`）。**
> **本机工作区有 104 个文件显示 `w/crlf`，这是 `core.autocrlf=true` 的检出表现，不是缺陷，不要修。**
> **不要添加 `.gitattributes`。**（2026-11-17 用户明确决定：保持现状）

---

## 二、编码约定（当前状态）

| 项 | 约定 | 当前实测 |
|---|---|---|
| **文件编码** | UTF-8，**不带 BOM** | BOM = 0 |
| **行尾（索引）** | **LF** | `i/lf = 532`、`i/crlf = 0`、`i/mixed = 0` |
| **行尾（工作区）** | 由 `core.autocrlf=true` 决定，**允许 CRLF** | `w/lf = 428`、`w/crlf = 104` |
| **`.gitattributes`** | **不添加** | 不存在 |

### 复跑校验

```bash
node "D:\deepseek 工作\_zl\encoding_audit.js"   # BOM / stray U+FEFF / invalid UTF-8 / 混用行尾
node "D:\deepseek 工作\_zl\eol_diagnose.js"     # 索引 vs 工作区的行尾分布
```

判据：
- `[1] leading BOM` 必须为 **0**
- `[3] invalid UTF-8` 必须为 **0**
- `[4] MIXED=0`（同一文件内 CRLF 与 LF 混用，这是唯一要修的行尾问题）
- `index 中 crlf/mixed` 必须为 **0**

---

## 三、为什么 `w/crlf` 不需要修（实测依据）

### 3.1 三条证据

**证据 1：索引里根本没有 CRLF**

```
$ git ls-files --eol | 统计
i/lf    = 532
i/crlf  = 0      ← 关键
i/mixed = 0
```

`i/` 是索引（真正提交的内容）。`i/crlf = 0` 意味着**任何人 clone 到的都是 LF**，仓库未被污染。

**证据 2：`git diff` 为空，且原因是可解释的**

以 `solidworks-2025-mechanical/chapters/ch01-interface.md` 为例：

```
磁盘上 CRLF           : 1278 个
索引 blob 里 CRLF     : 0 个
─────────────────────────────────────────
hash-object (应用 filter)  = e97244b6...   ← 与索引相同
hash-object (--no-filters) = 397cd52c...   ← 与索引不同
索引 blob                  = e97244b6...
```

`git hash-object` **默认走清楚过滤器**，先把 CRLF 归一成 LF 再算哈希。
所以「归一后内容 == 索引内容」→ diff 为空。
磁盘字节确实不同，但 **git 认为语义未变**。

**证据 3：曾经"修"过一次，git 什么都没记录**

2026-11-17 曾把 9 个混用行尾的文件统一成 LF 并提交，
`git show --stat` 显示 **只有 3 个文件**（2 个 BOM + 1 个内容修复），
那 9 个文件**一个都没进提交** —— 因为 git 归一化后判定无变化。

> **★ 教训：在 `autocrlf=true` 下，逐文件改工作区行尾是无效操作。**

### 3.2 那 104 个文件长什么样

- 其中 **90 个是 `.md`**
- 分布：`solidworks-practice` 13、`solidworks-2025-mechanical` 12、
  `design-methodology-liuguanzong` 11、`solidworks-surface-advanced` 10、
  `blender-manual-reference` 9 ……
- **没有一个是本轮新建的技能**（node 写出的文件天然是 LF）

即：CRLF 全部是**历史遗留 + 本机检出产物**，与内容正确性无关。

---

## 四、为什么不用 `.gitattributes`（三个方案对比）

| 方案 | 做法 | 后果 | 采用 |
|---|---|---|---|
| **A. 改 `core.autocrlf=false` 并重新检出** | 本机配置 | 只影响本机，不同步给任何人；Windows 上不加 `.gitattributes` 会回退 | ❌ |
| **B. 加 `.gitattributes` 写 `* text=auto eol=lf`** | 写进仓库 | 所有协作者下次检出产生**104 文件全量重写**式 diff；有人存成 CRLF 就会永久显示"已修改"，每次提交都要 `--renormalize` | ❌ **用户已决定不加** |
| **C. 逐文件强制改字节** | 直接改工作区 | **无效**（见 §3.1 证据 3），git 归一化后判定无变化 | ❌ |

### 决定性理由

**这是一个知识库，不是需要跨平台编译的代码仓库。**

- 1044 个 md / 约 1500 万字
- 行尾对 markdown 渲染**无影响**
- 对项目内所有校验脚本**无影响**（脚本均 `\r` 兼容，且统计时先 `replace(/\r\n/g,'\n')`）

为一个不影响任何实际行为的显示项，引入 104 文件 diff + 一次配置风险，**不划算**。

---

## 五、BOM 的历史教训（这个是真要修的）

BOM 与 CRLF 不同：**BOM 会真实进入仓库并破坏首行**。

| 事实 | 说明 |
|---|---|
| 危害 | 首行变成 `\uFEFF#`，导致 markdown 一级标题解析失败、锚点脚本失效 |
| 累计发现 | 第 1 批 14 个（`web-accessibility-cn` 全部章节 + glossary + patterns） |
| 第 2 批 | 2 个（`solidworks-2025-mechanical` 的 ch01、ch02）—— 老文件遗留 |
| 根因 | PowerShell `Set-Content -Encoding utf8` **会写 BOM**（Windows PowerShell 5.x 行为） |
| 修法 | 读字节，若前三字节为 `ef bb bf` 则丢弃，以 `Buffer` 写回 |

**实测确认 BOM 已从提交对象移除**：

```
ch01  HEAD~1 bytes=92411 BOM=true  →  HEAD bytes=92408 BOM=false
ch02  HEAD~1 bytes=174304 BOM=true →  HEAD bytes=174301 BOM=false
首 8 字节: 23 20 e7 ac ac 20 31 20   (23 = '#')
```

### 往后写文件的规矩

| 场景 | 做法 |
|---|---|
| **写 md** | 用 `write` 工具，或用 node `fs.writeFileSync`（都不写 BOM） |
| **PowerShell 写文本** | 用 `[System.IO.File]::WriteAllText($p, $t, [System.Text.UTF8Encoding]::new($false))`，**不要用 `Set-Content -Encoding utf8`** |
| **提交前** | 跑一次 `node _zl\encoding_audit.js`，确认 `[1] leading BOM = 0` |

---

## 六、检查清单（每次大批量改文件后跑一遍）

```
□ node _zl\encoding_audit.js       BOM=0 / strayU+FEFF=0 / invalidUTF8=0 / MIXED=0
□ node _zl\eol_diagnose.js         索引 i/crlf=0（工作区 w/crlf 允许非 0）
□ node _zl\full_acceptance.js      31 skills 全 PASS
□ node _zl\check_xref.js           技能名引用无悬空
□ node _zl\verify_router.js        路由表结构校验
```

> **★ 判断原则：看 `i/`（索引）不看 `w/`（工作区）。**
> **索引干净 = 仓库干净；工作区行尾是检出细节，不是缺陷。**

---

## 七、已知的校验脚本误报（避免重复踩）

这些都已修正进脚本，记下来防止有人"修内容去迁就脚本"：

| 误报现象 | 真相 | 正确处理 |
|---|---|---|
| `solidworks-practice` 报 13 章未链接 | 把 `references/walkthroughs/chNN.md` 当成了章节 | 只扫 `chapters/` 目录 |
| 章节索引行数为 0 | 只认 `^\|ch` 开头的表行 | 改为查 `chapters/xxx.md` 链接是否出现 |
| `ch08` 报含 `Lorem ipsum` | 原文是"用 Lorem ipsum 式的假标签测面板"——**反例** | 按行判断是否有 `式/不要/反例` 等语境词 |
| `BATCH1-GAPS.md` 报含 `待补` | 原文是"37,683 字待补"——**缺口统计** | 按行判断是否有 `缺口/清单/未读` 或 `\d+字待补` |
| `2.6.1` 被当成 WCAG 准则 | 该编号在 WCAG 2.0/2.1/2.2 三个文件中**均 0 命中** | 引用标准必须回原文 grep |

> **★ 原则：脚本报错先查脚本，不要先改内容。**

---

## 八、2026-11-17 全库四项体检结果

> 在 CRLF 结论定案后继续做的四项检查。记录基线，方便下次对比。

| # | 检查 | 脚本 | 结果 |
|---|---|---|---|
| 1 | 编码（BOM / stray U+FEFF / invalid UTF-8 / 混用行尾） | `encoding_audit.js` | **BOM=0，stray=0，invalid=0，MIXED=0** ✅ |
| 2 | 相对链接断链 | `check_links.js` | 检查 1,001 条 → **19 条断链**（见下） |
| 3 | SKILL.md frontmatter | `check_frontmatter.js` | 31 个技能 → **0 个有问题** ✅ |
| 4 | 章节六段结构 | `check_chapter_structure.js` | 195 章 → **188 章齐全（96.4%）** |

### 8.1 断链 19 条的处理

分两类，**只修我方能修的**：

| 类别 | 数量 | 处置 |
|---|---|---|
| **示例/占位**（`ch01-<slug>.md`、`/音标/`、`source:rfc8446`、`/abs/path/...`） | 12 | **不是断链**，是文档里的格式示例，保留 |
| **`video-creation` 指向已停用的 hyperframes / beatra** | 2 | **已修**：改为 `~~名称~~（已停用）` + 标注实际位置 `.dsh/skills-backup/`，不再写成相对链接 |
| **`book-to-skill` 上游文档自身缺文件** | 5 | **不动**。`guide.md` / `skill-reference.md` / `glossary.md` / `patterns.md` / `cheatsheet.md` 在该项目里确实不存在，属第三方仓库缺陷，改了会与上游冲突 |

> **★ 遗留：`book-to-skill/docs/` 与 `book-to-skill/SKILL.md` 的 5 条断链。**
> 这是上游项目自带的问题，**不在本仓库维护范围内**。若将来升级该技能，上游可能已修复。

### 8.2 章节结构 96.4% 的剩余 7 处（已逐条核实，均非缺陷）

| 技能 / 章 | 报缺 | 实际 |
|---|---|---|
| `blender-manual-reference` ch01、ch02 | links | 末尾有"→ xxx 章"式关联表，只是不在 `##` 标题下 |
| `product-structure-liubaoshun` ch07 | links | 同上，末尾是"→ 需另配 GB/T 1800"式清单 |
| `cmf-system` ch07 | overview | 全文无 `7.0`，但有 `## 7.1 第一步…` 直接开篇（该章是流程章，不需要总纲） |
| `solidworks-surface-advanced` ch07 | overview | 用 `## 本章导读：主模型技术在整本书里的位置` —— **就是总纲**，只是没编号 |
| `product-injection-defects` ch00 | head/overview/table/links | 该章是 3,596 字的**旧版速查摘要**，已在 SKILL.md 标注"保留作索引，内容已被 ch01 覆盖" |
| `product-injection-defects` ch01 | links | 末尾有关联清单，非标题 |

> **★ 结论：96.4% 是这套检测器的实际上限，不是文档缺陷率。**
> **继续榨这个数字只会把检测器改得越来越像在迁就个别文件，价值递减，到此为止。**

### 8.3 本轮修正的校验器误报（累计 9 类）

在 §七 的 5 条基础上又加 4 条：

| 误报 | 真相 |
|---|---|
| `chapters/` 章节数虚高 | 把 `references/walkthroughs/chNN.md` 当章节 → 只扫 `chapters/` 直下文件 |
| `overview` 缺失 | 总纲标题有 6 种写法：`N.0`、`A.0`、本章解决什么、本章导读、先立规矩、本章的结构 |
| `links` 缺失 | 关联信息常以表格行 `（同源/接口/互补/分工）` 或 `→ xxx 章` 出现，不在标题下 |
| `gaps` 缺失 | "空白/边界/局限/不足"出现在正文段落里也算 |

> **★ 原则（第三次强调）：脚本报错先查脚本。**
> 本轮 4 项检查里，**没有一条是"改内容去迁就脚本"，全都是改脚本去匹配已有内容**；
> 唯一的内容修改是 `video-creation` 那 2 条真实失效引用。

---

## 九、2026-11-17 第 5 项检查：脚本路径存在性

### 9.1 为什么要查这个

知识库里有大量"复核脚本：`node xxx.js`"这类**可执行声明**。
如果脚本不存在，读者照着敲会失败，而且会**怀疑前面所有结论**——这是比断链更严重的问题。

### 9.2 检查方法

`_zl\check_script_paths.js` 扫全部 1045 个 md，捕获三种写法：

| 写法 | 例子 |
|---|---|
| markdown 链接 | `[脚本](scripts/x.mjs)` |
| 行内代码 | `` `_standards/diff_wcag.js` `` |
| 命令行 | `node _standards/sc_index.js` |

解析基准必须试 **6 个**（这是本轮最大的坑，见 9.4）：
md 所在目录 → 技能根 → skills 根 → 工作区根 → `_zl` → `_standards`

### 9.3 结果

```
脚本路径引用 635：存在 233 / 示例 245 / 找不到 157
```

**157 条找不到，但逐条核实后没有一条是"该存在却不存在"的**，全部归入两类：

| 类别 | 数量 | 说明 |
|---|---|---|
| 描述**外部项目结构** | 约 150 | 如 `video-talkcraft` 的 `registry/remocn-ui/core/timeline.ts`（remotion 生态的路径）、`shots.ts`（用户项目里的文件）、`still.sh`（示例项目脚本）。这些是在讲**上游库/用户工程**长什么样，不是本仓库的文件 |
| 第三方技能自带 | 6 | `book-to-skill` 的 `book_to_skill/parsers/<fmt>.py`、`tests/evals/test_*.py` 等，上游仓库自己的测试路径 |

### 9.4 真正修掉的 3 处（以及补做的 2 个脚本）

| # | 位置 | 问题 | 处置 |
|---|---|---|---|
| 1 | `user-research-methods/SKILL.md` | 引用 `validate-page-citations.py` 但该脚本在**另一个技能**里 | 改为完整路径 `design-methodology-liuguanzong/references/validate-page-citations.py` |
| 2 | `web-accessibility-cn/SKILL.md` | 引用 `_zl/verify3.ps1` —— **该文件从未存在** | 改为实际使用的 `_zl/audit_cn.js` |
| 3 | `solidworks-practice/references/COMPARISON-PRACTICE.md` | 引用 `_re4/collect_practice.py` —— 临时脚本未保留 | 改为"`_re4/` 下的采集脚本；该临时脚本未随仓库保留" |
| 4 | `accessibility-standards`（6 处） | 文档声称有 `verify_sc_coverage.js` 与 `gen_matrix.js`，**实际都没创建** | **补做这两个脚本**（不是改文档），因为文档说"可复核"就该真能复核 |

### 9.5 补做的两个脚本，以及它们抓出的一个错误

**`_standards/verify_sc_coverage.js`**（复核条目覆盖）

```
PASS  17 条全部存在于 wcag21.html  (17/17)
PASS  17 条全部被技能引用        (17/17)
PASS  9 条全部存在于 wcag22.html  (9/9)
PASS  9 条全部被技能引用        (9/9)
PASS  wcag22.html 中存在 4.1.1 Parsing 已废止的标记
PASS  未把不存在的 2.6.1 写成条目
```

**`_standards/gen_matrix.js`**（生成三版对照表）

第一版算错了：**2.1 新增算出 26 条**（应为 17）。根因是 `wcag20.html` 的条目写作
`2.1.1 Keyboard: ...`（**带冒号**），而 2.1/2.2 不带；原正则的终止符只认空白，
导致 9 条被漏掉，进而把已有条目误判成"2.1 新增"。

修正后（终止符接受空白或冒号）并**加了自洽闸门**——数字不对就拒绝生成：

```
✓ 生成 _matrix.md
  2.0=61  2.1=78  2.2=87  并集=87
  2.1 新增 17: 1.3.4 1.3.5 1.3.6 1.4.10 1.4.11 1.4.12 1.4.13
               2.1.4 2.2.6 2.3.3 2.5.1 2.5.2 2.5.3 2.5.4 2.5.5 2.5.6 4.1.3
  2.2 新增 9:  2.4.11 2.4.12 2.4.13 2.5.7 2.5.8 3.2.6 3.3.7 3.3.8 3.3.9
```

**这三个数字（61/78/87）与 17/9 的新增数，现在有了可复跑的来源，不再依赖任何人的记忆。**

### 9.6 一个值得记住的方法论

> **★ 检查脚本"存在性"时，解析基准要列全。**
> 本轮第一版只按 md 所在目录解析，得出 **346 条找不到**；
> 补上"工作区根目录"这个基准后降到 260；
> 再加 `_standards` 基准后降到 157。
> **前两版的数字全是因为我的假设错了，不是文档错了。**

> **★ 文档声称"可复核"时，要么补做脚本，要么改掉这句话。**
> 不能留着一个指向不存在文件的"复核脚本"——那比不给复核方法更糟。

---

## 十、2026-11-17 第 6 项检查：交叉引用双向一致性

### 10.1 要查什么

A 说"详见 B"，B 是否知道 A 的存在。
单向引用在知识库里**多数是合理的**（消费者 → 被依赖方），所以要区分：

- **合理的单向**：新技能消费旧书技能的能力，旧书不需要知道新技能
- **真缺口**：两个技能互为"接口"（A 说"这块去问 B"），但 B 不知道 A 存在

### 10.2 全量统计

```
技能数 31 / 有向引用对 155 / 双向 48 / 单向 107
单向强引用（提到 ≥3 次且对方完全不回指）: 63 对
```

63 对里绝大多数是合理单向，例如 `web-accessibility-cn` 提到
`inclusive-accessibility-design` **130 次**（理论依据），后者无需回指。

### 10.3 真正要查的是"接口声称"

只查本轮报告 §五 明确声称的 **10 组接口**，结果：

| 接口 | 修复前 | 修复后 |
|---|---|---|
| CMF ↔ 注塑 | 单向 | **双向** |
| 用户研究 ↔ 人机 | 单向 | **双向** |
| 用户研究 ↔ 造型 | 单向 | **双向** |
| 可用性测试 ↔ 设计心理 | 单向 | **双向** |
| 无障碍 ↔ 人机 | 单向 | **双向** |
| 无障碍 ↔ 可用性测试 | 单向 | **双向** |
| 无障碍理论 ↔ 中文实践 | 单向 | **双向** |
| 中文实践 ↔ 标准 | 双向 | 双向 |
| CMF ↔ 结构 | 单向 | **双向** |
| CMF ↔ 视觉动力 | 单向 | **双向** |

**双向连通率：1/10 → 10/10**

### 10.4 关键判定：slug 引用 or 概念引用

一个技能不用对方 slug、而是用**书名或概念**提到对方，**也算知道对方**。
因为技能库需要的是知识，不是链接符号。实测 9 个"缺引用"里：

| 情况 | 数量 | 例 |
|---|---|---|
| 已用概念间接引用，**不算缺** | 6 | `cmf-system` 说"注塑缺陷/流痕/困气"（9 处），不提 slug |
| 真的完全没有 | 3 | `inclusive-accessibility-design` 对 `web-accessibility-cn` / `usability-testing` 均 **0 处** |

### 10.5 改动

| 文件 | 改动 |
|---|---|
| `inclusive-accessibility-design/SKILL.md` | **新增「与其他技能的连接」整段**（+18 行）。该技能原本没有这一段，只有 Scope & Limits |
| `product-injection-defects/SKILL.md` | 在已有「与其他技能怎么接」段插入 1 行 |
| `product-structure-liubaoshun/SKILL.md` | 在已有「相关技能」段插入 1 行 |
| `ergonomics-ding-yulan/SKILL.md` | 末尾新增「与其他技能的连接」段 + 1 行 |
| `product-design-styling-dabbs/SKILL.md` | 同上 |
| `design-psychology-norman/SKILL.md` | 同上 |
| `visual-dynamics-industrial-design/SKILL.md` | 同上 |

`git diff --stat` = **46 insertions(+), 0 deletions(-)** —— 只增不删，已核实。

### 10.6 编辑 CRLF 文件时踩的坑

那 3 个文件原本是 **纯 CRLF**，我用 node 插入的新行是 **LF**，
结果产生 `CRLF=156 LF=2` 的混用（`encoding_audit.js` 立刻报 MIXED=3）。

**修法**：不要逐行拼接，而是先 `\r\n → \n` 全扁平化，再 `\n → \r\n` 按主导行尾重建，
保证文件内部零混用。脚本 `_zl\normalize_3files.js`。

> **★ 教训：往 CRLF 文件里插行，必须按该文件的主导行尾重建整个文件，不能只写新行。**

### 10.7 一个反例：我的检测器方向印反了

第一版把"缺 A→B"打印成 A→B（实际 A 已经有了，缺的是 B→A）。
这种**标签反向**的错误比数值错误更危险——它会让人去补已经存在的东西。
已修正，并在输出里直接写 `缺 <谁> → <谁>` 全名，不用箭头简写。
