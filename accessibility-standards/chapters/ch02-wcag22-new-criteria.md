# 第 2 章：WCAG 2.2 新增的 9 条 + 4.1.1 Parsing 废止（2023）

> **源文件（2 份）**｜`_standards/wcag22.html`（87 条，165,465 字符）／`_standards/wcag21.html`（78 条，用于对照『2.2 相对 2.1 改了什么』）
> **抓取日期**：**2026-11-17**
> **覆盖范围**：2.2 相对 2.1 的**全部 9 条新增**（逐条引原文）+ **1 条废止**（4.1.1 Parsing）+ 2 处**改名**
> **定位口径**：**HTML 条目号 + 源文件行内定位**
>
> **读法说明**：先讲废止（§2.1，因为它改变的是**存量条目**），再逐条讲 9 条新增（§2.2），最后讲改名与实务影响（§2.3–2.4）。

---

## 2.1 总纲：2.2 不是『又加了 9 条』，是『加 9 条、废 1 条、改名 2 条』

### 2.1.1 三件事一次说清

脚本实测（`node _standards/diff_wcag.js`）：

```
NEW in 2.2 (9):  2.4.11 2.4.12 2.4.13 2.5.7 2.5.8 3.2.6 3.3.7 3.3.8 3.3.9
GONE in 2.2 (0): none

- level changes 2.1 to 2.2 -
  4.1.1 Parsing (Obsolete and removed): A -> (none)

- title changes 2.1 to 2.2 -
  2.5.5: "Target Size" -> "Target Size (Enhanced)"
  4.1.1: "Parsing" -> "Parsing (Obsolete and removed)"
```

> **★★★ 判据：2.2 的条目总数是 87，但『有效条目』是 86。**
> 87 = 78（2.1）+ 9（2.2 新增）；其中 4.1.1 已废止**但仍占编号**，
> 所以『符合 WCAG 2.2 AA』要满足的是 A/AA 条目里**不含 4.1.1** 的那一份。
> 任何说『2.2 有 87 条要求』的表述都不准确 —— 是 87 个编号，86 条有效要求。

### 2.1.2 2.2 的定位：它替 2.1 收口了『焦点可见性』与『认证』

2.2 的 9 条新增集中在三个新痛点：

| 主题 | 条目 | 为什么 2.2 才加 |
|---|---|---|
| **焦点不被遮挡** | 2.4.11、2.4.12、2.4.13 | 粘性页头/弹窗普及后，2.4.7『焦点可见』被实际遮住 |
| **触摸与拖拽** | 2.5.7、2.5.8 | 2.5.5 是 AAA（44px），AA 层一直没有尺寸门槛 |
| **表单与认证** | 3.2.6、3.3.7、3.3.8、3.3.9 | 重复填表、验证码把认知障碍用户挡在门外 |

> **★★ 判据：2.2 的新增全部是『已经发生的问题』，不是前瞻性条款。**
> 所以它们对**存量产品**的改造压力比 2.1 更大 —— 2.1 补的是新场景（触摸），2.2 补的是老场景里的老漏洞。

### 2.1.3 级别分布

| 级别 | 条数 | 条目号 |
|---|---|---|
| **A** | 2 | 3.2.6、3.3.7 |
| **AA** | 4 | 2.4.11、2.5.7、2.5.8、3.3.8 |
| **AAA** | 3 | 2.4.12、2.4.13、3.3.9 |

> **★ 判据：AA 层新增 4 条，这是做产品最相关的一档。**
> 其中 **2.5.8 Target Size (Minimum) = 24×24 CSS px** 是 2.2 对实体产品约束最硬的一条（见 §2.2.5）。

---

## 2.2 逐条展开（9 条新增）

### 2.2.1 2.4.11 Focus Not Obscured (Minimum)（AA）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「When a user interface component receives keyboard focus, the component is not entirely hidden due to author-created content.」

**为何新增**：粘性页脚、Cookie 横幅、聊天浮窗会把刚获得焦点的控件整个盖住。

> **原文 Note（wcag22.html，抓取 2026-11-17）**：
> 「Where content in a configurable interface can be repositioned by the user, then only the initial positions of user-movable content are considered for testing and conformance of this success criterion.」

**向实体产品的迁移**：
> **★★ 判据：焦点所在的位置，不能被自家浮层整个盖住（盖住一部分可以，全盖不行）。**
> 实体产品对应 —— 弹窗/浮层弹出时，用户当前正在操作的那个控件不能被完全遮挡。验收：逐个控件走一遍 Tab，看有没有『焦点在下面、屏幕上看不见』的时刻。

### 2.2.2 2.4.12 Focus Not Obscured (Enhanced)（AAA）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「When a user interface component receives keyboard focus, no part of the component is hidden by author-created content.」

> **★★ 判据：AA 允许『部分遮挡』，AAA 要求『一点都不许遮』。**
> 这是同一个问题设了两档 —— AA 是『别看丢』，AAA 是『别遮住』。做产品时先守 AA 的『不全遮』。

### 2.2.3 2.4.13 Focus Appearance（AAA）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「an area of the focus indicator meets all the following:」
> 「is at least as large as the area of a 2 CSS pixel thick perimeter of the unfocused component or sub-component, and」
> 「has a contrast ratio of at least 3:1 between the same pixels in the focused and unfocused states.」

**阈值**：焦点指示器面积 **≥ 2 CSS px 厚的周界面积**；对比度 **≥ 3:1**（同一批像素，聚焦前后）。

> **★★★ 判据：焦点框不是『有个框就行』，有两条可测的下限（2px 周长 + 3:1）。**
> 注意 3:1 这个数与 1.4.11 的 3:1 是**两个不同用途**的同一门槛：一个管控件可见性，一个管焦点状态。

**向实体产品的迁移**：
> 实体产品对应 —— 遥控器/键盘在屏幕上移动的高亮框。要有足够粗、且和未选中态有 3:1 差异。

### 2.2.4 2.5.7 Dragging Movements（AA）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging, unless dragging is essential or the functionality is determined by the user agent and not modified by the author.」

**为何新增**：滑块、拖拽排序、拖动进度条，对手抖或义肢用户不可完成。

**向实体产品的迁移**：
> **★★ 判据：凡是「拖」才能完成的，必须能『点/按』完成。**
> 实体产品对应 —— 触摸屏上的滑条调音量，要配 +/- 键；拖拽排序要配『上移/下移』按钮。

### 2.2.5 2.5.8 Target Size (Minimum)（AA）★ 本章最硬的一条

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「The size of the target for pointer inputs is at least 24 by 24 CSS pixels , except when:」
> 「Spacing」
> 「Undersized targets (those less than 24 by 24 CSS pixels) are positioned so that if a 24 CSS pixel diameter circle is centered on the bounding box of each, the circles do not intersect another target or the circle for another undersized target;」

**阈值**：**24 × 24 CSS px**，级别 **AA**。

> **★★★ 判据：24×24（AA）与 44×44（AAA）是两档，不是两个版本的前后替代。**
> - **2.5.8 / 24×24 / AA** —— 2.2 新增，AA 底线
> - **2.5.5 / 44×44 / AAA** —— 2.1 就有，2.2 起改名为 **Target Size (Enhanced)**
>
> 两档**同时有效**。所谓『2.2 把 44 降到 24』是错的 —— 是**在 AAA 之下补了一个 AA 门槛**。

**spacing 替代路径**：小于 24px 的控件，只要以 24px 直径圆互不相交也算过。这条给了小图标的合法出路。

**向实体产品的迁移**：
> **★★★ 这是本技能对工业设计最可操作的一条数值判据。**
> 实体按钮/触摸区：**AA 档按 24 CSS px 等效尺寸，AAA 档按 44**。
> 更实用的是**spacing 规则**：小按键可以小，但**相邻两个小按键的『24px 圆』不许相交** —— 这条比『必须做大』更容易落地。

### 2.2.6 3.2.6 Consistent Help（A）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「If a web page contains any of the following help mechanisms , and those mechanisms are repeated on multiple web pages within a set of web pages , they occur in the same order relative to other page content, unless a change is initiated by the user:」
> 「Human contact details;」「Human contact mechanism;」「Self-help option;」「A fully automated contact mechanism.」

**为何新增**：帮助入口位置飘忽，认知障碍用户每页都要重找。

**向实体产品的迁移**：
> **★★ 判据：帮助/客服入口在多页/多屏之间必须保持『相对顺序』一致。**
> 注意原文的口径是 **same order relative to other page content**（相对于其他内容的顺序），不是『绝对坐标一致』。
> 实体产品对应 —— 多级菜单里『帮助』永远排在同一相对位置；不要一级菜单在第 5 项、二级菜单跑到第 2 项。

### 2.2.7 3.3.7 Redundant Entry（A）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「Information previously entered by or provided to the user that is required to be entered again in the same process is either:」「auto-populated, or」「available for the user to select.」
> 「Except when:」「re-entering the information is essential ,」「the information is required to ensure the security of the content, or」「previously entered information is no longer valid.」

**为何新增**：同一流程里重复填同一信息，是认知与记忆负担的直接来源。

**向实体产品的迁移**：
> **★ 判据：同一流程内，此前填过的信息不许要求再填一遍（除非安全/失效）。**
> 实体产品对应 —— 自助机分步办理时，第二步不该再问第一步已经给过的信息。

### 2.2.8 3.3.8 Accessible Authentication (Minimum)（AA）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「A cognitive function test (such as remembering a password or solving a puzzle) is not required for any step in an authentication process unless that step provides at least one of the following:」
> 「Alternative」「Mechanism」「Object Recognition」「Personal Content」

**四项豁免路径**：另有不做认知测试的认证方式 / 有辅助机制 / 是识别物体 / 是识别用户自己提供的非文字内容。

> **原文 Note（wcag22.html，抓取 2026-11-17）**：
> 「Examples of mechanisms that satisfy this criterion include:」
> 「support for password entry by password managers to reduce memory need, and」
> 「copy and paste to reduce the cognitive burden of re-typing.」

> **★★★ 判据：不许『禁止粘贴密码』——这直接违反 3.3.8。**
> 这是 2.2 里最容易被产品经理违反的一条：出于安全考虑关掉密码框的粘贴，正好挡死了密码管理器。
> **允许粘贴 = 合规动作**，不是安全漏洞。

**向实体产品的迁移**：
> 实体产品对应 —— 设备登录、APP 配网时的认证步骤。不要强制『记住一串数字』或『解一道题』，应允许扫码、生物识别、或由密码管理器代填。

### 2.2.9 3.3.9 Accessible Authentication (Enhanced)（AAA）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「A cognitive function test (such as remembering a password or solving a puzzle) is not required for any step in an authentication process unless that step provides at least one of the following:」
> 「Alternative」「Mechanism」

> **★ 判据：AAA 去掉了 AA 的两个豁免（物体识别、个人内容）。**
> AA 允许『让你识别图片里的物体』，AAA 不允许 —— 这就是两档的实际差别。

---

## 2.3 4.1.1 Parsing 的废止及其影响

### 2.3.1 废止的事实

`wcag22.html` 中该条目已改名为：

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「Success Criterion 4.1.1 Parsing (Obsolete and removed)」

并且**不再带 Level 标记**（2.1 中为 Level A）。这正是脚本把它记为 `A -> (none)` 的原因。

### 2.3.2 废止的理由（原注逐字）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「This criterion was originally adopted to address problems that assistive technology had directly parsing HTML . Assistive technology no longer has any need to directly parse HTML . Consequently, these problems either no longer exist or are addressed by other criteria. This criterion no longer has utility and is removed.」

> **★★★ 判据：废止的理由是『问题消失了』，不是『要求降低了』。**
> 三条理由读清楚：① 辅助技术不再直接解析 HTML；② 当年那些问题要么不存在了，要么被别的条目覆盖。
> 所以**不要**把它理解成『现在可以写不合法的 HTML 了』。

### 2.3.3 废止的实务影响（原文自己给出的那条）

> **原文（wcag22.html，抓取 2026-11-17）**：
> 「WCAG 2.2 has removed one success criterion, 4.1.1 Parsing . Authors that are required by policy to conform with WCAG 2.0 or 2.1 will be able to update content to WCAG 2.2, but may need to continue to test and report 4.1.1.」

> **★★★★ 全书级判据：废止 ≠ 你不用测了。**
> 如果你所在项目/客户/法规**引用的是 WCAG 2.0 或 2.1**，你仍然要测 4.1.1 并报告结果。
> 只有当你瞄准的是 **WCAG 2.2** 时，4.1.1 才退出范围。
> **这是本技能最重要的一条『版本相对性』提醒** —— 同一个条目合不合规，取决于你声称符合哪一版。

### 2.3.4 与 EN 301 549 的冲突点（重要）

`en_301549_v3.2.1.txt` 第 9.4.1.1 条仍然逐字转引 2.1 的 Parsing：

> **原文（en_301549_v3.2.1.txt，抓取 2026-11-17）**：
> 「Where ICT is a web page, it shall satisfy WCAG 2.1 Success Criterion 4.1.1 Parsing.」

> **★★★ 判据：EN 301 549 v3.2.1 仍要求 4.1.1。**
> 因为它锁定的是 **WCAG 2.1**，而 4.1.1 在 2.1 里是有效的 Level A。
> 所以做欧洲采购项目时：**WCAG 2.2 说废止，EN 301 549 说要测 —— 以采购合同引用的版本为准。**

---

## 2.4 2.x 本章判据总表（共 9 条新增 + 1 条废止）

| # | 条目 | 级别 | 关键阈值/机制 | 判据（可执行） | 出处 |
|---|---|---|---|---|---|
| 1 | **2.4.11** Focus Not Obscured (Minimum) | AA | 不得**整个**遮住 | Tab 走查：焦点控件是否被浮层全盖 | wcag22.html |
| 2 | **2.4.12** Focus Not Obscured (Enhanced) | AAA | 不得**部分**遮住 | 同上，标准更严 | wcag22.html |
| 3 | **2.4.13** Focus Appearance | AAA | **2 CSS px 周界** + **3:1** | 焦点框测量：厚度与对比度双达标 | wcag22.html |
| 4 | **2.5.7** Dragging Movements | AA | 单点可替代拖拽 | 每个拖拽操作都有点击替代 | wcag22.html |
| 5 | **2.5.8** Target Size (Minimum) | **AA** | **24×24 CSS px** | 触摸区 ≥24，或 24px 圆不相交 | wcag22.html |
| 6 | **3.2.6** Consistent Help | A | 相对顺序一致 | 帮助入口在多屏间顺序不变 | wcag22.html |
| 7 | **3.3.7** Redundant Entry | A | 自动填充或可选 | 同流程不重复问同一信息 | wcag22.html |
| 8 | **3.3.8** Accessible Authentication (Minimum) | AA | 四豁免 | **允许粘贴密码**；不强制记忆/答题 | wcag22.html |
| 9 | **3.3.9** Accessible Authentication (Enhanced) | AAA | 仅两豁免 | 不可用『识别图片物体』通关 | wcag22.html |
| — | **4.1.1** Parsing | **已废止** | 2.2 起移出 | 若引用 2.0/2.1 仍须测 | wcag22.html |

> 复核脚本：`node _standards/verify_sc_coverage.js`（9/9 命中 + 4.1.1 废止判定）。

---

## 2.5 本章的空白

| 缺什么 | 本地原文情况 | 该去哪查 |
|---|---|---|
| 9 条的 **Understanding 文档**与**测试步骤** | `wcag22.html` 只有 `Understanding ...` **链接** | W3C Understanding WCAG 2.2（未抓） |
| 9 条的**失败技术（F-Techniques）** | 同上，只有链接 | W3C Techniques（未抓） |
| 2.2 相对 2.1 的**其他文字修订** | 本脚本只比对『条目集合 + 级别 + 标题』三项；**条目正文措辞的改动未逐条 diff** | 需对 78 条共同条目做全文 diff，本次未做 |
| 4.1.1 废止的**生效日期/决议记录** | `wcag22.html` 不含 W3C 工作组决议（只给结论与理由） | W3C AGWG 决议记录与 changelog（未抓） |
| **WCAG 3.0** 与 2.2 的关系 | 三份 HTML 均无 3.0 内容 | W3C WCAG 3.0 草案（未抓，属另一文档） |
| 9 条的**官方中文译名** | 只有英文原文 | W3C 中文授权译本（未抓） |

> **区分**：前四行是『原文有链接、正文未抓』；第五行是『不在本文档范围内』；第六行是『译本未抓』。

---

## 2.6 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| **2.5.8 = 24×24 AA** | **本书 ch01 §1.2.15（2.5.5 = 44×44 AAA）** | **同族两条、两个级别；本章 §2.2.5 已并列对照** |
| **4.1.1 废止** | **本书 ch04 §4.4（EN 301 549 9.4.1.1）** | EN 301 549 仍要求它；采购以合同版本为准 |
| **2.4.13 的 3:1** | **本书 ch01 §1.2.5（1.4.11 的 3:1）** | 同一个数，用在两处：控件可见性 vs 焦点状态 |
| **3.3.8 密码粘贴** | `web-accessibility-cn` ch05『不越俎代庖』 | 旧技能讲原则，本章给**可测的合规/违规界线** |
| **2.5.7 / 2.5.8 触摸** | `inclusive-accessibility-design` 的 dexterity 能力轴 | 那本给『手部能力怎么建模』，本章给『尺寸要多少』 |
| 本章 9 条 | **本书 ch08 §8.2** | ch08 汇总三版对照与旧技能分工 |
| 4.1.1 废止的『版本相对性』 | **本书 ch03 §3.4** | 一致性模型里『声明符合哪一版』决定测什么 |
