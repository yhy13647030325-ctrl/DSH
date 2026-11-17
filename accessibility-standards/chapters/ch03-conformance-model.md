# 第 3 章：三级一致性模型，与『AAA 为什么不能当通用要求』

> **源文件（2 份）**｜`_standards/wcag21.html`（第 5 章 Conformance，全部 5.1–5.5）／`_standards/wcag22.html`（同名章节，用于确认 2.2 沿用同一模型）
> **抓取日期**：**2026-11-17**
> **覆盖范围**：一致性级别定义（5.2.1）、整页要求（5.2.2）、完整流程（5.2.3）、可访问性支持（5.2.4）、非干扰（5.2.5）、符合性声明（5.3）、部分符合（5.4/5.5）
> **定位口径**：**HTML 章节号 + 源文件行内定位**
>
> **读法说明**：按 WCAG 第 5 章原顺序 `5.1 → 5.5` 展开，不跳节。

---

## 3.1 总纲：一致性是『五条同时满足』，不是『逐条打勾』

### 3.1.1 五条符合性要求（缺一不可）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「In order for a web page to conform to WCAG 2.1, all of the following conformance requirements must be satisfied:」

后续五条为：**5.2.1 一致性级别 / 5.2.2 整页 / 5.2.3 完整流程 / 5.2.4 仅用可访问性支持的方式 / 5.2.5 非干扰**。

> **★★★ 判据：五条是「与」关系。**
> 常见误判：某个页面每条 A/AA 都过了，就宣布『符合 AA』。
> 但如果它只是**流程中的一步**而后续步骤没过（5.2.3），或页面里有不受支持的技术挡住了别的内容（5.2.5），**整页仍不成立**。

### 3.1.2 『符合』只有三个级别，且是累积的

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「For Level A conformance (the minimum level of conformance), the web page」
> 「satisfies all the Level A success criteria, or a conforming alternate version is provided.」
> 「For Level AA conformance, the web page satisfies all the Level A and Level AA success criteria, or a Level AA conforming alternate version is provided.」
> 「For Level AAA conformance, the web page satisfies all the Level A, Level AA and Level AAA success criteria, or a Level AAA conforming alternate version is provided.」

> **★★★ 判据：AA 不是『AA 那几条全过』，而是『A 的全过 + AA 的全过』。**
> AAA 同理要含 A + AA。所以**级别是包含关系**，不是互斥集合。
> 数量上：按脚本实测，2.2 的 A=31、AA=24、AAA=31（另有 1 条废止），
> 故『符合 2.2 AA』需满足 **31 + 24 = 55 条**（不含已废止的 4.1.1）。

### 3.1.3 每条只有『过 / 不过 / 不适用』，没有部分分

> **原文（en_301549_v3.2.1.txt，抓取 2026-11-17）**：
> 「A web page satisfies a WCAG success criterion when the success criterion does not evaluate to false when applied to the web page.」
> 「if the success criterion puts conditions on a specific feature and that specific feature does not occur in the web page, then the web page satisfies the success criterion.」

> **★★★ 判据：这条是最容易被误解的『不适用也算通过』。**
> EN 301 549 把 WCAG 的判定逻辑讲得比 WCAG 自己更直白：
> 条目的前提不成立（页面上根本没有这类内容）时，该条目**判定为满足**，不是『未测』。
> 例：页面没有预录音频 → 1.2.2 Captions (Prerecorded) 自动满足。

---

## 3.2 逐节展开（5.1 → 5.5）

### 3.2.1 5.1 规范性要求怎么读

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「The main content of WCAG 2.1 is normative and defines requirements that impact conformance claims.」
> 「Introductory material, appendices, sections marked as "non-normative", diagrams, examples, and notes are informative (non-normative).」

> **★★ 判据：NOTE 不是要求，Examples 也不是要求。**
> 前两章大量引用 NOTE（如 2.2.6 的隐私提示、2.5.8 的 line-height 解释）。
> 那些是**帮助理解的**，不构成符合性要求的组成部分 —— 引用时要标注这是 NOTE，不能当条款。

**关键词强度（RFC 2119）**：

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「The key words MAY , MUST , MUST NOT , NOT RECOMMENDED , RECOMMENDED , SHOULD , and SHOULD NOT are to be interpreted as described in [ RFC2119 ].」

### 3.2.2 5.2.2 整页：不许『只对一部分』声称符合

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Conformance (and conformance level) is for full web page(s) only, and cannot be achieved if part of a web page is excluded.」

**整页还包含『同一页的各个变体』**：

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「A full page includes each variation of the page that is automatically presented by the page for various screen sizes (e.g. variations in a responsive web page).」

> **★★★ 判据：响应式断点产生的每个变体都要各自合规。**
> 这条对实体产品迁移极其重要 —— **同一个界面的不同布局变体（横屏/竖屏、大字模式/常规）都是独立验收对象**，不能只测一个变体。

### 3.2.3 5.2.3 完整流程：流程里有一页不过，全流程不算

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「When a web page is one of a series of web pages presenting a process (i.e., a sequence of steps that need to be completed in order to accomplish an activity), all web pages in the process conform at the specified level or better.」
> 「Example An online store has a series of pages that are used to select and purchase products. All pages in the series from start to finish (checkout) conform in order for any page that is part of the process to conform.」

> **★★★ 判据：验收要按『任务流程』切，不按「页面」切。**
> 实体产品对应 —— 自助机的『选择→确认→支付→取凭条』是一条 process，
> 任何一步的界面不合规，整条流程都不能算合规。**验收清单要按流程串联，而不是按屏罗列。**

### 3.2.4 5.2.4 只用『可访问性支持』的方式

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Only accessibility-supported ways of using technologies are relied upon to satisfy the success criteria. Any information or functionality that is provided in a way that is not accessibility supported is also available in a way that is accessibility supported.」

> **★★ 判据：用了辅助技术支持不了的技术，就等于没实现。**
> 「accessibility supported」的门槛写在术语表里（辅助技术实测互通 + 有可获取的支持该技术的用户代理）。
> 实体产品对应 —— 某个自绘控件如果不向平台无障碍接口暴露信息，它就等于**不存在**，哪怕视觉上完美。

### 3.2.5 5.2.5 非干扰：四条『全线适用』的硬条目

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「the following success criteria apply to all content on the page, including content that is not otherwise relied upon to meet conformance, because failure to meet them could interfere with any use of the page:」
> 「1.4.2 - Audio Control ,」「2.1.2 - No Keyboard Trap ,」「2.3.1 - Three Flashes or Below Threshold , and」「2.2.2 - Pause, Stop, Hide .」

> **★★★ 判据：这 4 条是『连第三方内容都要满足』的。**
> 即使那段内容是广告、是用户上传、是你不依赖它来声称合规，只要它在页面上，
> 就必须过这 4 条 —— 因为它们失败会**妨碍用户使用页面其他部分**。
> EN 301 549 把这个逻辑照抄进了 9.6（见 ch04）。

### 3.2.6 5.3 符合性声明：可做可不做，但做了就有格式要求

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Conformance claims are not required . Authors can conform to WCAG 2.1 without making a claim.」

声明必含五项（日期 / 指南名称版本URI / 级别 / 页面范围描述 / 依赖的技术清单）。

> **★ 判据：不发声明也完全合规；一旦发声明，缺任何一项就是不合格的声明。**
> 实体产品做『无障碍声明』时照此五项写，不要自创格式。

### 3.2.7 5.4 / 5.5 部分符合：两种被明文允许的例外

**第一种：第三方内容**

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「If a page of this type is monitored and repaired (non-conforming content is removed or brought into conformance) within two business days, then a determination or claim of conformance can be made」

**第二种：语言导致的可访问性支持缺失**

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「A "statement of partial conformance due to language" may be made when the page does not conform, but would conform if accessibility support existed for (all of) the language(s) used on the page.」

> **★★ 判据：部分符合只能以『第三方内容』或『语言支持缺失』两种名义声明，且要按原文句式写。**
> 『两个工作日』是唯一的量化宽限，不是『大概几天』。

---

## 3.3 为什么 AAA 不能当通用要求

### 3.3.1 WCAG 自己写下的反对意见

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「It is not recommended that Level AAA conformance be required as a general policy for entire sites because it is not possible to satisfy all Level AAA success criteria for some content.」

EN 301 549 把这句原样转引了两次（9.0 与 9.5 的 NOTE）：

> **原文（en_301549_v3.2.1.txt，抓取 2026-11-17）**：
> 「The W3C states that "It is not recommended that Level AAA conformance be required as a general policy for entire sites because it is not possible to satisfy all Level AAA Success Criteria for some content"」

> **★★★★ 全书级判据：把 AAA 当准入门槛，是被 W3C 与 EN 301 549��次明文劝阻的做法。**
> 理由不是『太难』，而是**逻辑上不可能**：某些内容注定无法满足全部 AAA 条目。

### 3.3.2 为什么不可能 —— 用具体条目看

| AAA 条目 | 为什么某些内容注定做不到 |
|---|---|
| **1.4.6 Contrast (Enhanced) 7:1** | 品牌色、警示色（如纯红急停）受安全色规范约束，无法自由压到 7:1 |
| **1.2.6 Sign Language (Prerecorded)** | 需要专业手语译者与视频制作，**内容生产者无法自行满足**；且部分内容无手语版本可用 |
| **1.4.8 Visual Presentation** | 要求『行宽 ≤80 字符（CJK 40）』等，与某些强制版式（票据、标签）冲突 |
| **3.1.5 Reading Level** | 技术要求『不超过初中教育水平』——法律条文、医学说明**做不到** |
| **2.4.13 Focus Appearance** | 若焦点样式由用户代理决定且作者不能改，只能走例外 |

> **★★ 判据：AAA 是『按内容逐条商量的目标』，不是『项目级一刀切的门槛』。**
> 正确用法：**以 AA 为基线，把 AAA 里对本文内容可行的条目挑出来当加分项**（这正是 5.3.2 允许在声明里列出『超出所声称级别的已满足条目』的用途）。

### 3.3.3 『全部 A/AA 达标』在实践中的确切含义

把前面几条合起来，『符合 AA』= 同时满足：

1. **该版本下全部 A 条目**（2.2 为 31 条）
2. **该版本下全部 AA 条目**（2.2 为 24 条）
3. **整页范围内**，含所有自动呈现的布局变体
4. **流程内所有步骤**，而非单页
5. **仅依赖可访问性支持的用法**
6. **非干扰四条目**连第三方内容也过

> **★ 判据：验收报告要能回答『哪一版 / 哪一级 / 哪个范围 / 哪些变体』，缺一项就是不可复核的报告。**

---

## 3.4 3.x 本章判据总表（共 12 条）

| # | 判据 | 出处 |
|---|---|---|
| 1 | 符合性五条要求是「与」关系，缺一不成立 | wcag21.html §5.2 |
| 2 | AA = 全部 A + 全部 AA；AAA 再加 AAA（级别是包含关系） | wcag21.html §5.2.1 |
| 3 | 条目前提不成立时判定为满足，而非『未测』 | en_301549_v3.2.1.txt §9.0 |
| 4 | NOTE / Example / 附录均为非规范，不构成要求 | wcag21.html §5.1 |
| 5 | 整页合规包含响应式的每个布局变体 | wcag21.html §5.2.2 Note 3 |
| 6 | 流程内任一页不合规，则整条流程不合规 | wcag21.html §5.2.3 |
| 7 | 不受可访问性支持的技术用法，等于未实现 | wcag21.html §5.2.4 |
| 8 | 非干扰四条目（1.4.2/2.1.2/2.3.1/2.2.2）对全页含第三方内容生效 | wcag21.html §5.2.5 |
| 9 | 符合性声明可发可不发；发了就必含五项 | wcag21.html §5.3.1 |
| 10 | 部分符合只允许『第三方内容』与『语言支持』两种名义 | wcag21.html §5.4/5.5 |
| 11 | 第三方内容的宽限是『两个工作日内监控并修复』 | wcag21.html §5.4 |
| 12 | AAA 不得作为整站通用政策（W3C 与 EN 301 549 双重明文） | wcag21.html §5.2.1 Note 2；en_301549 §9.0/9.5 |

---

## 3.5 本章的空白

| 缺什么 | 本地原文情况 | 该去哪查 |
|---|---|---|
| **conforming alternate version（合规替代版本）**的完整定义与判据 | 术语表有定义，但本技能未逐字摘录其 7 条注释 | `wcag21.html` 第 6 章 Glossary，条目 `conforming alternate version` |
| **accessibility supported** 的四个判定分支 | 同上，术语表有完整定义，未摘录 | `wcag21.html` Glossary，条目 `accessibility supported` |
| 一致性要求在各**司法辖区**的法律效力 | 三份 WCAG 原文均只讲标准，不讲法律 | 各国法规原文（本项目 ch07 只写中国『存在』，同样不给条文） |
| **Statement of Partial Conformance** 的官方模板/示例句 | 原文给了句式框架，未给完整样例 | W3C Understanding Conformance（未抓） |
| **『两个工作日』的起算口径** | 原文只说 within two business days，未定义起算时点 | W3C Understanding Conformance（未抓） |
| 实体产品如何界定『整页』的对应物 | WCAG 只定义 web page，**没有实体产品的对应定义** | 本技能 ch07/ch08 的迁移判据（属本技能的推演，非原文） |

> **区分**：前两行是『原文里有、本次未摘』；后四行是『原文不含或口径缺失』。

---

## 3.6 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 『符合 AA = 31+24=55 条』 | **本书 ch01/ch02** | 两章给出 2.1 的 17 条与 2.2 的 9 条来源，本章给计数口径 |
| **4.1.1 在 2.2 废止** | **本书 ch02 §2.3**、**ch04 §4.4** | 本章的『哪一版』问题在 4.1.1 上体现得最清楚 |
| 非干扰四条目 | **本书 ch04 §4.5（EN 301 549 §9.6）** | EN 301 549 把同一条逻辑写成 9.6 的五项要求 |
| 『AAA 不得当通用政策』 | **本书 ch04 §4.3（9.5 与 Table 9.1）** | EN 301 549 用一整张表列 AAA 条目，但明确只作鼓励 |
| 流程/整页/变体 | `usability-testing` 的任务清单与场景设计 | 那本讲『怎么测』，本章给『测到什么粒度才算合规』 |
| 一致性声明五项 | `web-accessibility-cn` 的发布门禁 | 旧技能给门禁清单，本章给声明格式要求 |
| 本章 §3.3.2 的『为何 AAA 做不到』 | `inclusive-accessibility-design` 的用户金字塔 | 那本给人群分层，本章给『标准为何不在顶层设门槛』 |
