---
name: inclusive-accessibility-design
description: 《Inclusive Design: Design for the Whole Population》与《Design for Inclusivity》结构化技能知识库。当用户需要无障碍设计、包容性设计、可及性评估、老龄化设计、残障用户设计、通用设计相关指导时使用，包括：设计排除（design exclusion）与排除率估算、"需求 > 能力"失配判据、能力谱（capability spectrum，原书称 capability loss as a continuum）与七条能力轴（locomotion/reach/dexterity/vision/hearing/communication/intellectual）、三轴立方体（感官·认知·机动）与包容性设计立方体 IDC、用户金字塔（user pyramid）与十级严重度、WINIT 五层人口与六种包容度比值、"最差+0.4×次差+0.3×第三差"加权、多轴耦合与多重计数消除、知识回路（Knowledge Loop）与 7-Level 设计法、四步排除评估法与 30 分钟七轴评估表、能力损失模拟器与标定边界、极端用户/边界用户/关键用户（critical users）与共情法、用户研究与焦点小组权限问题、通用设计七原则、BS 7000-6 管理标准、OXO Good Grips 等商业案例、老年女性作为首要目标人群、可达性尺寸与力（视距 1m／照度 3×）等。
---

# 包容性设计 / 无障碍设计

**源书①**：Clarkson, Coleman, Keates, Lebbon《Inclusive Design: Design for the Whole Population》，Springer 2003（611 页，理论主线）
**源书②**：Coleman, Clarkson, Dong, Cassim《Design for Inclusivity》，Gower 2007（267 页，方法与应用补充）
**页码口径**：**PDF 索引**（文本文件内 `===== PAGE N =====` 的 N）。两本书均为此口径，全书引文只引这两个文件。
**Chapters**: 9 ｜ **判据/论点**: 190 条 ｜ **引文段**: 529 段（已逐段回源核验）｜ **Generated**: 2026-11-17

---

## ⚠ 时效边界（先读这一条）

> **本技能的内容止于 2007 年。**
> 两本源书分别成书于 2003 与 2007 年，因此**不包含**下列 2010 年后的标准与规范，任何情况下**不要从记忆补写**：
> - **WCAG 2.1 / 2.2**、WAI-ARIA
> - **EN 17161**（Design for All 标准）、**EN 301 549**（ICT 可及性）
> - **ISO 21542**（建成环境无障碍）、**ISO 9241-171 / -210** 的现行版本
> - 中国《无障碍环境建设法》与 GB 系列现行条文
>
> 另需注意：原计划的第三本源书经核验**不是包容性设计著作**（其版权页实为 `Handbook of Research on Applying Universal Design for Learning Across Disciplines`，是 UDL 教育书，且文本层不可读），**已弃用，本技能不含任何 2021 年版内容**。
> 需要上述标准时，请查标准原文；本技能不替代。
> **2010 年后标准的具体条文（WCAG 2.1/2.2 新增条目、EN 301 549 v3.2.1 第 4/5/8/9 章、三级一致性模型、中国法规现行状态）→ 查技能 `accessibility-standards`。**

---

## 用法

- **不带参数** — 加载下方核心框架速查
- **给一个主题** — 例如"怎么估算排除率""用户金字塔怎么画""极端用户怎么用"，我会定位并读取相关章节
- **给章号** — 例如 `ch04`，我直接加载该章
- **浏览** — 问"有哪些章节"即可看到完整索引

核心框架未覆盖的主题，我会先读对应章节文件再回答。

---

## 核心框架速查（14 条）

### 1. 全书前提：残疾在环境里，不在身体里
> 「**disability arises not within the individual, due to impaired capability, but is a result of environments, products and services that fail to take into account the needs and capabilities of all potential users.**」（Clarkson p18）
**推论**：既然排除是设计造成的，排除就可被**度量**（ch04）、**定位**（ch03）、**评估**（ch06）和**反向设计掉**（ch05）。

### 2. 唯一不等式：`Demand > Capability → Exclusion`
> 「**If Demand > Users' Capability then Exclusion**」（Coleman p187）
左侧（产品需求）与右侧（用户能力）可**独立描述**，因此可分别评估、分别修改。这是全部量化方法的骨架。

### 3. 两类排除：需求性 vs 设计性（不可混淆）
> 工作定义：「**An inclusively designed product should only exclude the end-users who the product requirements exclude.**」（Clarkson p111）
**判别方法**：换个设计决定，这个人还能不能用？——能，则属**设计性排除**（不可辩护）；不能，则属**需求性排除**（需提交管理层决定）。
**需求性排除不是设计团队的免责理由**：原文要求 `A managerial decision is therefore required between marketability of the product and the level of population exclusion`。

### 4. 能力谱：七条轴 → 合并成三条 → 对齐同一把尺
七轴（各自严重度 0–13）：**Locomotion / Reaching and Stretching / Dexterity / Vision / Hearing / Communication / Intellectual functioning**（Clarkson p377）
三类：**Motion**（前三条）｜**Sensory**（视、听）｜**Cognition**（沟通、智力）（Clarkson p439）
> 关键性质：「**equal scores broadly relate to equivalent levels of capability**」（Clarkson p435）——**没有这条对齐，七个数就不能合并**。
**描述用户时必须写行为，不写病因**：`it is not very helpful for the designer to know that certain users have 'arthritis of the knee joint' ... Instead it is more useful to know how long the user can stand or walk`（Clarkson p468）。

### 5. 三轴 = 三段交互，不是三个感官
来源是 Card/Moran/Newell 的人类信息处理模型：**感知 → 认知 → 机动**（Clarkson p115–p116）。原文用 `Applying equal weight` 建立方体——**等权重是几何建模假设，不是重要性判断**；要排序必须回到七轴分别看人数。

### 6. 用户金字塔：十级严重度 × 人口百分比
分档：**1–2 轻微 / 3–6 中度 / 7–10 重度**；底数 **8,582,200 人 = 英国成年人口 20%**。
实际分布：轻微 **34%**、中度 **45%**、重度 **21%**（Clarkson p375、p439）。
> **判据**：只做"重度专用版"会漏掉最大的中度层；**塔身才是可量化回报所在**。
> **user pyramid 是瑞典 Ergonomi Design Gruppen（Benktzon & Juhlins）的专有方法名**（Clarkson p107、p605），与 i~design 那张十级人口图是两个东西，引用时须区分。

### 7. 严重度合并算式（全书唯一算式）
```
Overall severity = worst + 0.4 × (second worst) + 0.3 × (third worst)
```
（Clarkson p375、p436）
三条设计判断：① **最差的那一项决定命运**（权重 1）；② 第二、第三差仍有实质加成；③ 第四名以后权重 0。
> **优化顺序：拉起最差那一项，而不是平均改善。**

### 8. WINIT 五层人口 + 六种包容度比值
| 字母 | 名称 | 谁能改这一层 |
|---|---|---|
| **W** | Whole population（全体） | 不可改 |
| **I** | Ideal population（理想上限，剔除法定的/安全的/不可弥补的） | 换品类或辖区 |
| **N** | Negotiable maximum（需求规格所纳入的） | **需求制定者** |
| **I** | Included population（实际能用的） | **设计团队** |
| **T** | Target population（原定目标，`an arbitrary definition`） | 公司管理层 |
> **最重要比值：Included ÷ Negotiable maximum，`this ratio should approach unity`**（Clarkson p114）——这是唯一有收敛目标、也是设计团队唯一可正当免责的边界。
> **Target 是任意定义，不能用来论证包容性**："目标用户 25–40 岁"是选择，不是事实。

### 9. 排除率：默认 P5–P95 设计 = 主动排除 460 万人
> 「**the remaining 1 0% of users may be excluded, which in the UK corresponds to 4 600 000 adults**」（Clarkson p442）
多尺寸产品**每个尺寸各排除一次 10%**。**任何写"按 P5–P95 设计"的地方，旁边必须写出被排除人数。**

### 10. 四步排除评估法（30 分钟可完成一份）
1. **定语境**：写出环境假设 + 完整动作序列
2. **评能力需求**：七轴打分 + **同时报"被排除者"与"处于劣势但未排除者"** 两个数
3. **评身体属性**：尺寸/力（间隙 ≥ 目标人群 P95 指厚这类判据）
4. **消除多重计数**：跨数据集合并"难以做到甚至不可能"（`difficult, if not impossible`），只用同一数据集内去重
**七轴人数不可相加**——相加会严重高估。
**量表无对应描述时用"主观类比"**：找一个已标定的相似动作做锚点（原文实例：**按按钮 ≈ 挤海绵 = dexterity 8.0**）。

### 11. 多轴耦合：单轴改进会失效
- **单一受损者之和（约 412 万）远小于去重后总数（约 813 万）**，即**过半受损者是跨轴受损**（Clarkson p379–p380）
- 机动 × 感官耦合率 **50%**
- 壶 E 与壶 F 的差距 = **1,880,000 人**，全部落在视觉×灵巧的耦合区（Clarkson p444）
> **判据**：若排除集中在两轴耦合区，**必须同时降两轴**；只降一轴，"只会让贴着该轴的气泡被纳入，耦合区的不会"。
> **优先级由"每降一档需求能换回多少人"（边际收益）决定，不由当前哪轴人数多决定。**

### 12. 知识回路 + 7-Level（流程落地）
**Knowledge Loop**（Clarkson p451）：认识用户 → 捕获并表征 → 验证表征 → 验证产品 → 使用信息 → 回收。**可从任意点进入**（中途接项目也能用）。
**关键约束**：`Only once those summary representations are available can the product be truly validated` ——**做完测试没做成可复用表征，等于下一轮重做**。
**7-Level = 2 + 3 + 2**：
| Stage | Level | 验什么 |
|---|---|---|
| 1 问题定义 | **L1** 用户期望 → **L2** 功能规格 | 动机 + 功能 |
| 2 系统定义 | **L3** 感知 → **L4** 认知 → **L5** 机动 | 三轴各一层 |
| 3 系统验证 | **L6** 实用可接受性 → **L7** 社会可接受性 | **L6 正式用户试验 `essential`，不可省**；L7 必须回扣 L1 |
> **可迭代但不可逆序**；每层是 **aim（目标）** 不是 **step（步骤）**。
> **L4 依赖 L3**：用户说"不知道现在什么状态"是 L3 病，不是 L4 病。

### 13. 极端用户 → 反推主流（共情是动机问题，不是知识问题）
> 「**It is not sufficient just to know about 'inclusive design' ... designers also need to be motivated**」（Clarkson p537）
> 「**emotionally engaging with people makes their inclusion unarguable**」（Clarkson p537）
**共情是一条谱**，不是一档标准：**三年沉浸（Patricia Moore）→ 数周观察 → 两小时用户论坛**。两小时已是有效剂量。
**选分布两端的人**（IDEO 方法卡 `Extreme users`），不选典型/平均。判断价值不问"是不是目标用户"，问**"他在哪件事上比常人更懂"**。
**三类用户分工**：**极端用户**（概念期，逼出创造性提问、示范应对策略）｜**边界用户 boundary**（正卡在能不能用的边缘，最能定位排除点）｜**健全用户**（基线）。
> **招募标准用能力分数，不用年龄或诊断。**边界用户的定义就是"能力分数接近产品需求分数"的人。

### 14. 三个稳定的红旗与三条禁令
**红旗（全书反复出现）**：
- **双手操作**（`Tasks which require the use of two hands`）——因为另一只手要维持平衡
- **推送+旋拧的复合动作**（`Double actions such as push and twist`）
- **社会可接受性**（`people do not necessarily want to be seen with a phone that looks as though it has been made easier to use`）
**禁令（原文原话）**：
- `Blue-violet-green combinations should be avoided`（老年晶状体滤蓝紫）
- `Natural frequencies ... in preference to percentages`（用 `1 in 1,000`，不用 `0.1%`）
- `Designs which impose a high demand on memory should be avoided`（序列操作必须逐步提示）

---

## Chapter Index

| # | 主题 | 内容要点 |
|---|---|---|
| [ch01](chapters/ch01-cong-bianyuan-dao-zhuliu.md) | 从边缘到主流：问题意识、历史与设计原则（**Clarkson p17–p42 全 26 页 ＋ Coleman p32–p52 的 12 页**） | **约 3.2 万**：disabled by design、期望阶梯（barrier-free→universal access→universal design）、"最低即最高"警告、平均人的构成、特殊需求三重失败回路、design for a broader average、Transgenerational 三选项、通用设计**七原则全文+24 条指南**、**"三原则"核查（全书唯一命中是 Simply 项目三条）**、**12 条概念-论点** |
| [ch02](chapters/ch02-nengli-pu-yu-yonghu-jinzita.md) | 能力谱与用户金字塔：把"人"拆成可测的三条轴（**Clarkson p371–p382、p435–p442 ＋ Coleman p207–p208 ＋ Clarkson p47–p63，共 34 页**） | **约 4.9 万**：七轴含点数与分数区间、**听觉轴 8 级完整量表**、四点行为量表、视距 8→50→100cm、照度 2×/3×/10×/100×、蓝紫绿禁令、两点辨别退化、认知靶点三项、老年女性为首要目标人群、单损 vs 组合损人口表、**worst+0.4+0.3 算式**、**22 条概念-论点**、capability spectrum 术语核查 |
| [ch03](chapters/ch03-sheji-paichu-yu-winit.md) | 设计排除与 WINIT 人口模型、包容性设计立方体（**Clarkson p104–p118 全 15 页 ＋ Coleman p186–p199 的 14 页**） | **约 4.3 万**：Demand>Capability、排除四层谱、**56% 电商任务成功率**、通路任务不可打折、工作定义、**WINIT 五层 + 六比值**、三种设计策略与"用户觉察主导立方体"、**按病因分组会切碎人群（震颤案例）**、bad fit、通用设计"没有实施描述"、**19 条概念-论点** |
| [ch04](chapters/ch04-paichulv-lianghua-sibufa.md) | 排除率的量化：四步评估法与实测数字（**Clarkson p433–p447 全 15 页 ＋ Coleman p201–p216 的 16 页**） | **约 6.2 万**：两条桥（能力/尺寸）、数据源与 6 倍口径差、**四步法**、**Acoustiguide 30 分钟评估表全文**、主观类比（挤海绵=8.0）、**壶 D/E/F 逐格排除表**、**理想下界演算（200 万人能用杯喝水却用不了壶）**、DTV 四档方案与市场规模、**P5–P95 排除 460 万**、气泡图与耦合、**21 条概念-论点** |
| [ch05](chapters/ch05-zhishi-huilu-yu-7level.md) | 知识回路与 7-Level 设计法（**Clarkson p448–p463 全 16 页**） | **约 4.3 万**：Knowledge Loop 五环与四类表征、信息准时制、responsive designer 判据、**reactive 是默认路径**、**7-Level 逐层表（2+3+2）**、L3/L5 对称检查表、只有 L6 无替代、L7 回扣 L1、**IDC 两个未证实假设（已被 50% 耦合反证）**、业界阻力是成本认知、**19 条概念-论点** |
| [ch06](chapters/ch06-pinggu-fangfa-ku.md) | 评估方法库：六种方法、生命周期与流程表（**Clarkson p464–p484 全 21 页 ＋ Coleman p202–p216 的 15 页**） | **约 5.8 万**：单一方法本身不包容、interesting user 取代 representative user、**生命周期排除高发段在安装与维护**、六种方法各自局限、**Table 27.2 阶段×方法表**、快慢分层、**五步手机审计（双独立团队）**、家政用品六条发现、**26 条概念-论点** |
| [ch07](chapters/ch07-mon-ni-gongju-biaoding.md) | 能力损失模拟器：做法、标定与边界（**Coleman p218–p231 全 14 页 ＋ p209–p211 的 3 页**） | **约 4.2 万**：disorder/impairment/capability/disability 四层链、五件零成本模拟器、整装式三缺陷、**洗碗机推理（体感强度≠问题严重度）**、**模拟器是量具**、五类模块化组件、三阶段对照实验、**"动作变成需要预谋的事"**、**水壶烫手：模拟器物理遮蔽问题**、三个结构性盲区、认知靠双任务、**18 条概念-论点** |
| [ch08](chapters/ch08-gongqing-yu-jiduan-yonghu.md) | 共情与极端用户：从"为别人设计"到"被人改变"（**Clarkson p486–p500、p539–p548 ＋ p527–p538，共 37 页**） | **约 4.6 万**：动机是独立变量、共情是一条谱、Moore 三年实验真正发现（规范只基于子集）、五步流程与六类用户、**极端用户四案例**、四条流程原则、**体验原型三案例（椅子/水球钉子/周末呼机）**、critical users 与"同代人"、**用户拒绝完美特殊化（"I don't want a spacey park"）**、**25 条概念-论点** |
| [ch09](chapters/ch09-yonghu-yanjiu-fangfa.md) | 设计师导向的用户研究方法（**Coleman p152–p184 全 33 页 ＋ Clarkson p413–p431 章题**） | **约 5.5 万**：三分类（问/看/参与）、**参与阶梯七级**、好工具五条性格（含"不能太描述性"）、**能力需求访谈六问**、**删掉那一步 > 优化那一步**、persona 2–7 个与"第一张不是残障者"、informance 与"we not they"、十项常见缺陷、**样本量 ≥12/≥50、招募 25 人=5 天/4 周、单场 1.5–2 小时、成本 £3,000–4,500**、**28 条概念-论点** |

> **章节索引表行数 = 9，与 `chapters/` 实际文件数一致。**

---

## Topic Index

- **capability loss as a continuum（能力连续统）** → ch02
- **capability spectrum 术语核查（原书不叫这个）** → ch02
- **customer / user 区分** → ch08（六类用户）、ch01（Simply）
- **Demand > Capability** → ch03
- **design for a broader average** → ch01
- **design exclusion（设计排除）** → ch03、ch04
- **disorder / impairment / capability / disability 四层** → ch07
- **exclusion audit（排除审计）** → ch04、ch06
- **extreme users（极端用户）** → ch08、ch04（boundary users）
- **HADRIAN —— 本书 0 命中** → ch03 §3.8
- **IDC（包容性设计立方体）** → ch03、ch05
- **ITK —— 本书 0 命中（"A Design Toolkit"只是节名）** → ch03 §3.8
- **Knowledge Loop（知识回路）** → ch05
- **OXO Good Grips** → ch10 商业论证引用于 ch01/ch03
- **P5–P95 排除 460 万** → ch04、ch02
- **patricia moore 三年实验** → ch08
- **responsive designer** → ch05
- **transgenerational design 三选项** → ch01
- **universal design 七原则** → ch01
- **user pyramid（用户金字塔）** → ch02、ch03
- **WINIT 五层人口** → ch03
- **7-Level 设计法** → ch05
- **boundary users（边界用户）** → ch04、ch06
- **critical users（关键用户）** → ch08
- **informance（信息化表演）** → ch09
- **persona** → ch09
- **task analysis / HTA / PTR** → ch09
- **三轴（感官·认知·机动）** → ch02、ch03
- **七条能力轴** → ch02
- **中年女性 / 老年女性为首要目标人群** → ch02
- **双手操作红旗** → ch02、ch09
- **多轴耦合与多重计数** → ch02、ch04
- **最差三项加权算式** → ch02、ch04
- **视距 / 照度 / 色彩禁令** → ch02
- **老年女性力量 2/3** → ch02
- **前 5 后 5 百分位** → ch04、ch02
- **模拟器标定** → ch07
- **水壶三兄弟（含理想下界演算）** → ch04
- **数字电视四档方案** → ch04
- **共情是一条谱** → ch08
- **体验原型** → ch08
- **焦点小组 vs 用户论坛** → ch08、ch09
- **参与阶梯七级** → ch09
- **十项常见缺陷** → ch09、ch06
- **样本量 ≥12 / ≥50** → ch09
- **测试时长 1.5–2 小时** → ch09
- **招募偏倚四源** → ch09
- **BS 7000-6** → ch01、ch03
- **DDA / ADA / Section 508** → ch01、ch03
- **最低即最高** → ch01

---

## Supporting Files

- [cheatsheet.md](cheatsheet.md) — 一页速查（三轴 + 排除率 + 关键判据 + 否决项）
- [glossary.md](glossary.md) — 术语表（中英对照，含术语核查标注）
- [patterns.md](patterns.md) — 10 个可复用配方（P1–P10）

---

## Scope & Limits

**覆盖范围**：Clarkson（2003）与 Coleman（2007）两本源书，共 9 章、190 条判据/论点、529 段引文。
**抽样声明（不假设读过更多）**：
- Clarkson 611 页中，**逐页读**了 34 章的正文页（约 200 页，占全书三分之一强），涵盖 ch1、ch5、ch10、ch21、ch25、ch26、ch27、ch28、ch29、ch30、ch31、ch36 及导论；**未逐页读**的章节包括 ch7（Living longer）、ch8（legal，Coleman 版已覆盖）、ch11–ch20（各国实践与商业案例）、ch22–ch24、ch32–ch35。
- Coleman 267 页中，**逐页读**了 ch1–ch4、ch9–ch13 的关键页（约 150 页）；**未逐页读**的包括 ch5–ch8（实践者访谈与教育案例）、ch14–ch15。
- **Clarkson ch24（Observation for innovation, p413–p431）只读了章题与转述**，未逐页读。

**已知空白**（详见各章⑤）：
- **HADRIAN 与 ITK 在两书中均为 0 命中**，本技能不含（见 ch03 §3.8）
- 排除率的**置信区间与抽样误差**全书未给
- **认知轴的逐级行为量表**缺失（只给了听觉轴的 H1–H8 模板）
- 模拟器**标定含主观性**，原书自认无法精确标定
- 专家评估者**如何训练**，原书自认未解决
- 英国 national key 制度等**具体法规条文**未展开
- **无中国人群数据**，全部数字为 GB（Great Britain）16+ 人口
- **2007 年之后的标准与技术一概不含**（见顶部"时效边界"）

**引用纪律**：
1. 全部页码为 **PDF 索引**（`===== PAGE N =====` 的 N），可用文本文件逐一复核
2. 引文**逐字**照录，含原文本层的 OCR 断字（如 `speciﬁ cation`、`able- bodied`、`sub- groups`）、项目符号错位（如 `Forum • :`）与错拼（如 `illcreasingly`），**一律不改字**；确需说明的写在引文外的括注里
3. 跨页引文按页**分两段**引用，不合并
4. 图注凡 OCR 读不出的，写"**未完整读出，不做补猜**"
5. 本技能**不引 `ergonomics-ding-yulan` 的页码**（该书为"书内印刷页"，与本技能不同源）；指路时只写章名
