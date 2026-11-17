# 第 1 章：WCAG 2.1 新增的 17 条成功准则（2018）

> **源文件（3 份）**｜`_standards/wcag20.html`（61 条，94,093 字符）／`_standards/wcag21.html`（78 条，153,775 字符）／`_standards/en_301549_v3.2.1.txt`（9.1–9.4 逐条转引 WCAG 2.1）
> **抓取日期**：**2026-11-17**
> **覆盖范围**：2.1 相对 2.0 的**全部新增条目**（正文清单 17 条，逐条引原文）+ 每条向实体产品的迁移
> **页码/定位口径**：**HTML 条目号 + 源文件行内定位**（WCAG 无印刷页；页码口径对 HTML 不适用，故用『条目号 + 源文件』双锚点）
>
> **读法说明**：按条目号 **1.3.4 → 4.1.3** 逐条展开，不跳条。每条含【原文】+【级别】+【为何新增】+【向实体产品迁移】。

---

## 1.1 总纲：2.1 到底加了什么，加在哪

### 1.1.1 先钉死一个数字：不是 15 条，是 17 条

本技能的所有条目数**都不是凭记忆写的**，是脚本比对三份本地原文的条目集合算出来的：

```bash
node _standards/sc_index.js wcag20.html _sc20.json
node _standards/sc_index.js wcag21.html _sc21.json
node _standards/sc_index.js wcag22.html _sc22.json
node _standards/diff_wcag.js
```

实测输出：

```
counts: 2.0=61  2.1=78  2.2=87
NEW in 2.1 (17): 1.3.4 1.3.5 1.3.6 1.4.10 1.4.11 1.4.12 1.4.13
                 2.1.4 2.2.6 2.3.3 2.5.1 2.5.2 2.5.3 2.5.4 2.5.5 2.5.6 4.1.3
NEW in 2.2 (9):  2.4.11 2.4.12 2.4.13 2.5.7 2.5.8 3.2.6 3.3.7 3.3.8 3.3.9
```

> **★★★ 判据：WCAG 2.1 新增 17 条，不是 15 条。**
> 流传最广的『2.1 新增 15 条』漏掉了 **1.3.6 Identify Purpose** 与 **2.3.3 Animation from Interactions**。
> 这两条都是 **AAA**，容易被漏；但它们同样是 2.1 新增条目，讨论『2.1 新增了几条』时必须计入。
> 本技能的 17 条与 `wcag21.html` 正文自述的清单**逐条一致**（见下引文）。

`wcag21.html` 自己的清单原文（这是最硬的内部证据）：

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「The following Success Criteria are new in WCAG 2.1:」

其后完整列出 17 条，含 `1.3.6 Identify Purpose (AAA)` 与 `2.3.3 Animation from Interactions (AAA)`。

### 1.1.2 新增条目的级别分布（脚本实测）

| 版本 | 条目总数 | A | AA | AAA | 无级别 |
|---|---|---|---|---|---|
| WCAG 2.0 | 61 | 25 | 13 | 23 | 0 |
| WCAG 2.1 | 78 | 30 | 20 | 28 | 0 |
| WCAG 2.2 | 87 | 31 | 24 | 31 | **1**（4.1.1，已废止，见 ch02） |

**2.1 新增的 17 条按级别拆开**：

| 级别 | 条数 | 条目号 |
|---|---|---|
| **A** | 5 | 2.1.4、2.5.1、2.5.2、2.5.3、2.5.4 |
| **AA** | 7 | 1.3.4、1.3.5、1.4.10、1.4.11、1.4.12、1.4.13、4.1.3 |
| **AAA** | 5 | 1.3.6、2.2.6、2.3.3、2.5.5、2.5.6 |

> **★★ 判据：2.1 的新增主力在『输入方式』（新增 2.5 整节 6 条）。**
> 2.0 的四条原则（可感知/可操作/可理解/健壮）里，『可操作』原有 4 个指南；
> 2.1 硬加了一个 **Guideline 2.5 Input Modalities**，专门管触摸、手势、动作感应。
> 这是移动终端普及直接推到标准里的结果。

### 1.1.3 编号规则：为什么新条目接在每节末尾

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「new success criteria in WCAG 2.1 have been appended to the end of the set of success criteria within their guideline.」

> **★ 判据：同一个指南里编号不再按级别排序，只按加入时间排序。**
> 实例：Guideline 1.4 里 1.4.9 是 **AAA**，紧接的 1.4.10 是 **AA**，1.4.12 又是 **AA**，而 1.4.6/1.4.7/1.4.8 都是 AAA。
> **所以『编号越大级别越高』是错的，反之也错 —— 每条必须单独看级别标记。**

---

## 1.2 逐条展开（17 条，按编号）

### 1.2.1 1.3.4 Orientation（AA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Content does not restrict its view and operation to a single display orientation, such as portrait or landscape, unless a specific display orientation is essential .」

**为何新增**：固定朝向假设（只做竖屏）会让装在支架/横屏上的设备不可用。

**向实体产品的迁移**：
> **★ 判据：产品若可旋转、可换装位，不能只支持一种朝向。**
> 例：扫码枪屏、POS 机、车载中控。检查法 —— 把样机转 90° 装，主任务（如收款、导航）能否完成。

### 1.2.2 1.3.5 Identify Input Purpose（AA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「The purpose of each input field collecting information about the user can be programmatically determined」

**为何新增**：让浏览器/辅助技术能自动填充（认知障碍与运动障碍用户受益最大）。

**向实体产品的迁移**：
> **★ 判据：凡是采集『关于用户本人』的字段，其语义要能被机器识别，不能只靠标签文字。**
> 实体产品上对应的是『字段语义可被外部读出』——例如自助机的表单字段要能被读屏读出『这是姓名/这是生日』，而不是只有印刷标签。

### 1.2.3 1.3.6 Identify Purpose（AAA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「the purpose of user interface components , icons, and regions can be programmatically determined .」

**为何新增**：与 1.3.5 同源，但覆盖面从『输入字段』扩到**组件、图标、区域**。这是 2.1 里最常被漏掉的两条之一。

**向实体产品的迁移**：
> **★ 判据：图标与区域也要有可读出的『用途』，不能只有形状。**
> 实体产品对应做法 —— 图标区留可触知的语义标识（盲文/凸起字/语音提示），使『这是什么按钮』不依赖看。

### 1.2.4 1.4.10 Reflow（AA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:」
> 「Vertical scrolling content at a width equivalent to 320 CSS pixels ;」
> 「Horizontal scrolling content at a height equivalent to 256 CSS pixels .」

**阈值**：**宽 320 CSS px / 高 256 CSS px**，等价于 1280 px 视口在 **400% 缩放**下的宽度。

> **原文 Note（wcag21.html，抓取 2026-11-17）**：
> 「320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom.」

**为何新增**：低视力用户放大 400% 后，页面不该要求左右来回滚。

**向实体产品的迁移**：
> **★ 判据：放大后只能单向滚动，不允许双向滚。**
> 实体产品对应 —— 大字号模式下，内容应**纵向连续**（单列），不出现『必须左右拖动才能看全』的表单。

### 1.2.5 1.4.11 Non-text Contrast（AA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s):」
> 「Visual information required to identify user interface components and states , except for inactive components」

**阈值**：**3:1**（针对界面组件的边界/状态、以及理解内容所必需的图形部分）。

**为何新增**：2.0 只管文字对比度（1.4.3 的 4.5:1），**不管控件边框和图标**，导致『按钮看不出边界』。

**向实体产品的迁移**：
> **★★★ 判据：实体产品的『可操作件轮廓』与『状态指示』按 3:1 校验，不按文字 4.5:1。**
> 应用：面板上的按键边界、指示灯亮/灭区分、充电口盖板与机身的区分。
> 这是本技能对工业设计最有直接约束力的一条 —— 因为它给了**除文字之外**的对比度门槛。

### 1.2.6 1.4.12 Text Spacing（AA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Line height (line spacing) to at least 1.5 times the font size;」
> 「Spacing following paragraphs to at least 2 times the font size;」
> 「Letter spacing (tracking) to at least 0.12 times the font size;」
> 「Word spacing to at least 0.16 times the font size.」

**阈值四件套**：行高 **≥1.5×**、段后 **≥2×**、字距 **≥0.12×**、词距 **≥0.16×**。

> **★★ 判据：这四组数是『不许丢内容』的下限测试值，不是推荐的排版值。**
> 意思是 —— 把行高调到 1.5 倍时，你的界面不能崩（不能裁字、不能溢出）。

**向实体产品的迁移**：
> 实体产品对应 —— **字距可调范围**（点阵屏、电子价签、HMI 面板）至少要覆盖这四组比例而不丢字。
> 印刷类（铭牌、说明书）则把这四组当**排版下限**。

### 1.2.7 1.4.13 Content on Hover or Focus（AA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Dismissible」
> 「A mechanism is available to dismiss the additional content without moving pointer hover or keyboard focus」
> 「Hoverable」
> 「Persistent」

**三项要求**：可关闭（Dismissible）、可移入（Hoverable）、保持（Persistent）。

**为何新增**：悬停才出现的提示，对不能精细控制指针的人是陷阱 —— 手一抖就消失。

**向实体产品的迁移**：
> **★ 判据：凡是『悬停/聚焦才出现』的信息，必须能主动关闭、能移过去、且不会自己消失。**
> 实体产品对应 —— 触摸屏上的长按提示、悬浮气泡。要能被固定住（点一下钉住），而不是必须一直按住。

### 1.2.8 2.1.4 Character Key Shortcuts（A）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「If a keyboard shortcut is implemented in content using only letter (including upper- and lower-case letters), punctuation, number, or symbol characters, then at least one of the following is true:」
> 「Turn off」「Remap」「Active only on focus」

**三个合规路径**：能关 / 能改键 / 仅在聚焦时生效。

**为何新增**：语音输入用户说出「a」时，单字符快捷键会误触发。

**向实体产品的迁移**：
> **★ 判据：单键快捷键（不带修饰键）必须可关或不常驻。**
> 实体产品对应 —— 设备上的单个物理快捷键（如『按 A 直接进入某模式』），语音控制用户会误触。需提供禁用或用组合键。

### 1.2.9 2.2.6 Timeouts（AAA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Users are warned of the duration of any user inactivity that could cause data loss, unless the data is preserved for more than 20 hours when the user does not take any actions.」

**阈值**：**20 小时**（数据保留超过 20 小时则免于警告）。

> **★★ 判据：超时警告的门槛是『会不会丢数据』，20 小时是免警告线。**
> 这是 2.1 里少数带具体时长数字的条目 —— 做自助机/终端时必须引用它，而不是凭感觉设 15 分钟。

**向实体产品的迁移**：
> 实体产品对应 —— 自助终端、缴费机、医疗设备操作界面的空闲退出策略：**要么保留 >20h，要么提前告知剩余时长**。

### 1.2.10 2.3.3 Animation from Interactions（AAA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Motion animation triggered by interaction can be disabled, unless the animation is essential to the functionality or the information being conveyed.」

**为何新增**：前庭功能障碍用户对**点击后触发的视差滚动与缩放过渡**会眩晕。这是另一条常被漏掉的 2.1 新增。

**向实体产品的迁移**：
> **★ 判据：交互触发的动效要能关，除非动效本身承载信息。**
> 实体产品对应 —— 车载 HMI、VR/AR 头显、大屏互动装置的转场动效，应提供『减弱动效』开关。

### 1.2.11 2.5.1 Pointer Gestures（A）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「All functionality that uses multipoint or path-based gestures for operation can be operated with a single pointer without a path-based gesture, unless a multipoint or path-based gesture is essential .」

**为何新增**：双指缩放、画路径解锁，对单手/义肢用户不可完成。

**向实体产品的迁移**：
> **★★ 判据：多点手势与划路径手势，必须有一个『单点、不用划』的替代。**
> 实体产品对应 —— 触摸屏的滑动调温、双指缩放，要配 +/- 按钮或旋钮。

### 1.2.12 2.5.2 Pointer Cancellation（A）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「No Down-Event」
> 「The down-event of the pointer is not used to execute any part of the function;」
> 「Abort or Undo」

**为何新增**：按下即触发（down-event）会误操作；应在『抬起』时完成并可撤销。

**向实体产品的迁移**：
> **★ 判据：危险动作在『按下瞬间』不得生效，要在『松开』时生效或可撤销。**
> 实体产品对应 —— 急停、付款确认、删除。手指一碰就执行是不可接受的。

### 1.2.13 2.5.3 Label in Name（A）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「For user interface components with labels that include text or images of text , the name contains the text that is presented visually.」

**为何新增**：语音控制用户说『点击提交』，若程序名是 "btn-ok"，则无法命中。

**向实体产品的迁移**：
> **★★ 判据：看得见的文字，必须包含在『程序知道了的名字』里。**
> 实体产品对应 —— 面板上印『启动』，那么语音/读屏能识别的名字里也必须含『启动』，不能是 "F1"。

### 1.2.14 2.5.4 Motion Actuation（A）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Functionality that can be operated by device motion or user motion can also be operated by user interface components and responding to the motion can be disabled to prevent accidental actuation」

**为何新增**：摇一摇、倾斜操作，对手抖或不能握持的用户既不可用也易误触。

**向实体产品的迁移**：
> **★ 判据：靠『晃动/倾斜/手势感应』触发的功能，必须另有按钮可达，且能关掉感应。**
> 实体产品对应 —— 摇一摇报修、倾倒报警、体感翻页。

### 1.2.15 2.5.5 Target Size（AAA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「The size of the target for pointer inputs is at least 44 by 44 CSS pixels except when:」

**阈值**：**44 × 44 CSS px**（2.1 版，级别 **AAA**）。

> **★★★ 注意版本关系（本技能反复要用的一条）：**
> **2.1 的 2.5.5 = 44×44，AAA；2.2 新增的 2.5.8 = 24×24，AA。**
> 2.2 同时把 2.5.5 改名为 **Target Size (Enhanced)** 以区别于 2.5.8。
> 所以『AA 要求 24』与『44 是 AAA』两句话都对，混着说就错。

**向实体产品的迁移**：
> 实体产品没有 CSS px，但**有等效的物理触点尺寸**。44×44 CSS px 对应到手持设备约 7–9 mm 边长（依 DPI）。
> 做实体按键/触摸区时，把 24 与 44 当成**两个档位**：AA 底线与 AAA 目标。

### 1.2.16 2.5.6 Concurrent Input Mechanisms（AAA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「Web content does not restrict use of input modalities available on a platform except where the restriction is essential , required to ensure the security of the content, or required to respect user settings.」

**为何新增**：不能因为检测到触摸就禁掉外接键盘。

**向实体产品的迁移**：
> **★ 判据：不要『检测到触摸就关掉键盘』——多种输入应可并存。**
> 实体产品对应 —— 触屏 + 物理键盘 + 语音三通道同时可用；切换时不必重启或重进模式。

### 1.2.17 4.1.3 Status Messages（AA）

> **原文（wcag21.html，抓取 2026-11-17）**：
> 「status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.」

**为何新增**：2.0 的 4.1.2 只管『有名字有角色』，但**动态出现的状态提示**（"已保存"）不给焦点也得念出来。

**向实体产品的迁移**：
> **★★ 判据：状态变化必须主动播报，不能要求用户先『移过去』才知道。**
> 实体产品对应 —— 充电完成、打印就绪、门已锁。要有声音/振动/清晰的视觉提示，且**不需要用户操作**就送达。

---

## 1.3 1.x 本章判据总表（共 17 条）

| # | 条目 | 级别 | 关键阈值/机制 | 判据（可执行） | 出处 |
|---|---|---|---|---|---|
| 1 | **1.3.4** Orientation | AA | 不限单一朝向 | 转 90° 主任务仍可完成 | wcag21.html |
| 2 | **1.3.5** Identify Input Purpose | AA | 字段语义可程序判定 | 采集『关于用户』的字段可被外部读出 | wcag21.html |
| 3 | **1.3.6** Identify Purpose | AAA | 组件/图标/区域用途可判定 | 图标区留非视觉语义 | wcag21.html |
| 4 | **1.4.10** Reflow | AA | **320×256 CSS px**（=1280px @400%） | 放大后只单向滚动 | wcag21.html |
| 5 | **1.4.11** Non-text Contrast | AA | **3:1** | 控件轮廓与状态按 3:1 校验 | wcag21.html |
| 6 | **1.4.12** Text Spacing | AA | 行高1.5×/段后2×/字距0.12×/词距0.16× | 调到这四组值不丢内容 | wcag21.html |
| 7 | **1.4.13** Content on Hover or Focus | AA | 可关闭/可移入/保持 | 悬停信息能钉住 | wcag21.html |
| 8 | **2.1.4** Character Key Shortcuts | A | 关/改键/仅聚焦 | 单键快捷键非常驻 | wcag21.html |
| 9 | **2.2.6** Timeouts | AAA | **20 小时** | 要么保留>20h，要么预告时长 | wcag21.html |
| 10 | **2.3.3** Animation from Interactions | AAA | 可关闭 | 交互动效有『减弱』开关 | wcag21.html |
| 11 | **2.5.1** Pointer Gestures | A | 单点可替代 | 多点/划路径手势配单点替代 | wcag21.html |
| 12 | **2.5.2** Pointer Cancellation | A | 抬升触发/可撤销 | 危险动作不在按下瞬间生效 | wcag21.html |
| 13 | **2.5.3** Label in Name | A | 可见文字∈名字 | 印『启动』则名字含『启动』 | wcag21.html |
| 14 | **2.5.4** Motion Actuation | A | 另有按钮 + 可关 | 感应触发功能有按钮替代 | wcag21.html |
| 15 | **2.5.5** Target Size | **AAA** | **44×44 CSS px** | 触摸区按 44 档 | wcag21.html |
| 16 | **2.5.6** Concurrent Input Mechanisms | AAA | 不限制输入通道 | 触屏+键盘+语音可并存 | wcag21.html |
| 17 | **4.1.3** Status Messages | AA | 无焦点可播报 | 状态变化主动送达 | wcag21.html |

> 全部 17 条的级别与阈值均可在 `wcag21.html` 中 grep 到；复核脚本：`node _standards/verify_sc_coverage.js`。

---

## 1.4 本章的空白

| 缺什么 | 本地原文情况 | 该去哪查 |
|---|---|---|
| 每条的 **Understanding 文档**（为什么这样定、测试步骤） | `wcag21.html` 只有 `Understanding 1.4.10` 这类**链接**，未含正文 | W3C Understanding WCAG 2.1（未抓，需联网） |
| 每条的 **失败技术（F-Techniques）与通过技术** | 同上，只有链接 | W3C Techniques for WCAG 2.1（未抓） |
| 2.1 对 **2.0 条目的修改**（非新增） | 本脚本只算了『新增/删除』集合差；**级别与文字的其他改动未逐条比对** | 需对 61 条共同条目做全文 diff，本次未做 |
| 1.3.6 / 2.3.3 的中文官方译名 | 本地只有英文原文，**W3C 官方中文授权译本未抓** | W3C 中文翻译页（未抓） |
| 实体产品的 **CSS px → mm 换算** | `wcag21.html` 只定义 CSS px 为「visual angle of about 0.0213 degrees」，**不含物理尺寸换算表** | 需按具体设备 DPI/视距自行推算；本技能不给统一换算表（会给错） |

> **明确区分**：上表前三行属『原文里有链接但正文未抓』；第四、五行属该内容本就不在 WCAG 原文里。

---

## 1.5 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 2.5.5 Target Size **44×44 / AAA** | **本书 ch02 §2.2.5** | **同一条目在 2.2 被改名 Enhanced，并新增 24×24 的 AA 条目** —— 必须对着读，否则记错级 |
| 1.4.11 Non-text Contrast **3:1** | **本书 ch03 §3.3**、`web-accessibility-cn` ch07 的对比度表 | 3:1 是『非文字』门槛，4.5:1 是『文字』门槛，两者不可互换 |
| 1.4.12 Text Spacing 四组比例 | `web-accessibility-cn` ch07（行距 1.5 倍、每行 40 中日韩字） | 中文那本给的是**行距**单一值，本章补上**字距/词距/段距**三组 |
| 2.1.4 / 2.5.x 全部输入相关条目 | **本书 ch04（EN 301 549 第 9 章）** | EN 301 549 把 2.5.1–2.5.4 逐条转引为强制性条款 9.2.5.x |
| 本章 17 条 | **本书 ch08 §8.2** | ch08 给三版对照总表与『旧技能讲哪条』的分工 |
| 4.1.3 Status Messages | `web-accessibility-cn` ch05 的 WAI-ARIA 段落 | 那本讲 ARIA 用法，本章给**动态状态**这一条具体要求 |
| 1.3.4 / 1.3.5 的『朝向与字段语义』 | `inclusive-accessibility-design` ch07（能力损失模拟器） | 模拟器测『能不能用』，本章给『标准要求是什么』 |
