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
