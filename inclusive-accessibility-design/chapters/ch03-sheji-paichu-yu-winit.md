# 第 3 章：设计排除与包容性设计立方体——WINIT 人口模型与"包容度"

> **原书 PDF 页序 p104–p118（15 页，Clarkson 第 5 章）＋ p186–p199（14 页，Coleman 第 11 章）｜本版逐页读完全部 29 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）
>
> **读法说明**：按 Clarkson ch5 的 `Design exclusion and inclusive design → Existing approaches to inclusive design → The need to address exclusion → A working definition of inclusive design → Defining the target populations → Defining measures of inclusive merit → The inclusive design cube → The IDC and exclusion → Summary` 逐节展开，不跳节；Coleman ch11 作为同一理论的 2007 年简化版并行引用（它多了"排除 vs 困难/挫败"的谱与应用案例）。
> 每节含【原文摘录】+【判据提炼】。

---

## 3.0 总纲：从"包容"转向"排除"

这一章是全书方法论的中枢，做的是一次**视角反转**：

> **原文（Clarkson p105）**：
> 「**While inclusive design and universal design are commonly accepted as good design aims, this chapter discusses the merits of focusing on design exclusion. The concept of design exclusion is particularly powerful because identifying why and how end-users cannot use a product enables us to counter such exclusion.**」

> **★★★★ 判据：问"谁能用"不给方向；问"谁不能用、为什么"直接给出改进点。**
> 这是全章唯一的核心论证，原书重复了四次（p105、p108、p116、p28）。它的逻辑是：
> ① "多少人能用"是一个**标量**，标量不指向任何具体特征；
> ② "多少人不能用 + 因为哪条需求"是一个**向量**，向量直接指出要改哪个特征；
> ③ 因此排除视角才能驱动改进，包容视角只能驱动汇报。

**本章的四个产出物：**

| 产出 | 内容 | 页码 |
|---|---|---|
| **① 工作定义** | 「只应排除被产品需求本身排除的人」 | p111 |
| **② WINIT 人口模型** | Whole / Ideal / Negotiable max / Included / Target 五层人口 | p112–p114 |
| **③ 包容度（inclusive merit）** | 五种人口之比，作为量化指标 | p114–p115 |
| **④ 包容性设计立方体（IDC）** | 感官 × 认知 × 机动 三轴体积图 | p115–p116 |

---

## 3.1 设计排除是什么：需求 > 能力

### 3.1.1 最简形式

> **原文（Coleman p186）**：
> 「**Design exclusion arises when the demands of using a particular product, within a given environment, exceed the capabilities of the user. At worst this leads to**」

> **原文（Coleman p187）**：
> 「**the user being unable to use the product; at best the product may be difﬁ cult or frustrating to use. Put simply:** … **If Demand > Users' Capability then Exclusion**」

（该句跨 p186–p187；此处按页分两段引用，不改字。）

> **★★★★ 判据：`Demand > Capability → Exclusion` 是全书唯一的不等式，其余都是它的展开。**
> 注意左右两侧都是**可独立描述的**：
> - **Capability** = `derived from their cognitive, sensory and physical characteristics, which include a mix of simple physical measures (for example anthropometrics and strength), functional measures (for example the ability to climb stairs or to read newsprint) and experiential measures (for example prior use of computers)`（Coleman p187）
> - **Demand** = `derived from its physical and behavioural characteristics, which may be described by its interface features (for example screen, text, buttons, and so on) and design variables/attributes (for example colour, dimensions, shape, force, interaction sequence, and so on)`（Coleman p187）

> **★★★ 判据：右侧（能力）三分——物理测量、功能测量、经验测量。第三条最常被漏。**
> "经验测量"（prior use of computers，即先前使用经验）意味着**能力不是纯粹的生理量，它包含学习史**。
> **产品含义：** 一个"从没用过触摸屏的老人"在触屏产品上的能力，低于其生理年龄所对应的能力。这是"新奇性本身构成需求"的正式依据 —— 也解释了为什么原书反复要求 `Care should be taken when introducing novel symbols, acronyms etc.`（Clarkson p62）。

### 3.1.2 "排除"是一条谱，不是二值

> **原文（Coleman p187）**：
> 「**The model also accommodates the view that design exclusion describes a spectrum of user / product interaction challenges, from total or partial exclusion, to difﬁ culty or frustration for those users who are not excluded. It also allows for the fact that demands and capabilities may change with time,**」

| 层级 | 表现 | 商业后果 |
|---|---|---|
| **完全排除** | 用不了 | 丢失该用户 |
| **部分排除** | 某些功能用不了 | 价值打折、退换货 |
| **困难** | 能用但费劲 | 满意度低、差评 |
| **挫败** | 能用但情绪受损 | 品牌损伤 |

> **★★★★ 判据："没被排除"不等于"没问题"—— 困难与挫败是可量化的商业损失，不是软性抱怨。**
> 原书给了两组外部数据支撑这一点（Clarkson p186 / p530）：
> - `two out of three Americans report having lost interest in a technology product because it seemed 'too complex to set up or operate'`（Philips, 2004）
> - `On average, the user success rate was 56%. E-commerce sites lose almost half of their potential sales because users cannot use the site.`（Nielsen, 2002，496 次任务尝试，20 个站点）

> **★★★★ 判据：56% 的任务成功率意味着"排除"绝不只是少数群体问题。**
> 这个数字来自**普通电商用户**，不是残障用户。它把设计排除从"公益议题"改写为"转化率议题" —— 这是本章最能说服商业方的一组数据。

### 3.1.3 频率与时长：为什么"难得一次的排除"也是致命的

> **原文（Coleman p188）**：
> 「**Exclusion may also be a function of the frequency or duration of the activity or task. An infrequent, difﬁ cult task is less likely to lead to the same levels of frustration as a frequent, difﬁ cult task. For example, the infrequent, yet difﬁ cult, replacement of a battery will not frustrate as much as the regular and difﬁ cult activation of the on / off switch.**」

> **原文（Coleman p188）**：
> 「**However, an infrequent (or short) task that excludes the user may lead to exclusion for the whole product. For example, a user who is unable (in the absence of help) to 'programme' a new cooker may not be able to access features that are temporarily disabled – in particular where use of the oven is typically governed by a 'child safety' interlock. Herein lies the key difference between exclusion, where a single infrequent excluding task can compromise use of the whole product, and difﬁ culty / frustration.**」

> **★★★★ 判据：区分"排除"与"困难"的唯一标准是：这个任务是否是通路（gate）。**
> 困难可以按"频率 × 时长"打折；**排除不能打折**，因为一个低频的排除性任务会锁死整个产品（安全联锁、首次设置、配对、激活）。
> **可执行的评审问题（本章最有用的单条）：** 列出全部任务，标出哪几个是**关键通路任务**（不做就无法使用其余功能）；对这几个任务，一律按最高标准评估，不允许"反正很少用"。

---

## 3.2 工作定义：只排除"需求本身排除的人"

这是全书最锋利的一句话，也是判断"设计失职"的准绳。

> **原文（Clarkson p111）**：
> 「**An inclusively designed product should only exclude the end- users who the product requirements exclude.**」

> **原文（Clarkson p111）**：
> 「**The corollary of this is, of course, that the design fails to be inclusive if people are excluded from using the product even though they possess the functional capabilities to meet the demands of the idealised design based on the requirements. This implies that the designers have introduced new capability demands on the users that are not essential attributes of the product, but resultant from the designer's decisions.**」

> **★★★★ 判据：排除分两类 —— 需求性排除（可辩护）与设计性排除（不可辩护）。**
> 判据的判别方法是**"假如换个设计决定，这个人还能不能用？"**
> - 水壶必须装 1.7 L 水才够泡几杯咖啡 → 重量下限是**需求**给的 → 抬不动的人属需求性排除；
> - 但"壶盖需要双手拧开"不是需求，是**设计决定** → 抬得动却拧不开的人属设计性排除。

> **原文（Clarkson p111）**：
> 「**Taking the example of the kettle, how much water should it hold? A smaller capacity decreases weight and increases inclusivity, but the marketability probably decreases. A managerial decision is therefore required between marketability of the product and the level of population exclusion, and consequent potential market size.**」

> **★★★ 判据：需求性排除不能由设计师单方面决定，必须上抬到管理决策层。**
> 原文用 `managerial decision` 和 `strategic level of the design management` 两个词明确了这个层级。
> **实操含义：** 产品评审时若发现"某个排除来自需求本身"，正确动作不是"尽力补偿"，而是**把"容量 ↔ 排除率 ↔ 市场规模"三者的取舍提交给能改需求的人**。

> **原文（Clarkson p111）**：
> 「**In summary, one possible measure of inclusive merit of a product depends on two criteria: the merit of the requirements that define it; and its merit when judged against those requirements.**」

> **★★★ 判据：包容度有两个自变量 —— 需求本身好不好，以及产品是否达成了需求。**
> 只看第二个会漏掉"需求本身就把人排除了"的情况。这是本章最容易犯的评估错误。

---

## 3.3 WINIT 人口模型：五种"人口"的精确定义

这是本章的方法论主干。原书用 W-I-N-I-T 五个字母定义五层人口。

### 3.3.1 五层定义（逐字）

> **原文（Clarkson p112）**：
> 「**The most logical place to begin is defining the terminology for the global/ geographical population being considered, i.e. the absolute maximum number of people who could use the product. This is referred to as the whole population and it includes all people of all ages and capabilities.**」

> **原文（Clarkson p112）**：
> 「**Another group that may be excluded are those who, even under the most optimistic assessment, would be incapable of using the product for its intended purpose. This assessment should be completely solution-neutral.**」

> **原文（Clarkson p112）**：
> 「**The resulting population following the removal of those who are prevented by law, safety considerations and irremediable lack of capability from using the product, shall be referred to as the ideal population. This is the maximum population by which a product could possibly be used under ideal conditions.**」

> **原文（Clarkson p112）**：
> 「**The people who could actually use the product, based on its physical properties, are referred to as the included population.**」

> **原文（Clarkson p113）**：
> 「**This is referred to as the negotiable maximum population. 'Negotiable' implies that this population is not fixed and can change as the requirements change. It is the 'maximum' because by definition the inclusivity of the product cannot exceed that of the requirements specification.**」

> **原文（Clarkson p114）**：
> 「**To summarise the defined WINIT populations: Whole population - everyone** … **Ideal population - the maximum achievable** … **Negotiable max population- everyone included by the specification** … **Included population - those who can actually use the product** … **Target population - those who were intended to use the product**」

### 3.3.2 五层人口速查表

| 字母 | 名称 | 中文 | 定义（原文关键词） | 谁能改这一层 |
|---|---|---|---|---|
| **W** | **Whole population** | 全体人口 | `all people of all ages and capabilities` | 不可改（地理既定） |
| **I** | **Ideal population** | 理想人口 | `the maximum population by which a product could possibly be used under ideal conditions` | 只能靠**改变产品定位**（换法规辖区、换品类） |
| **N** | **Negotiable maximum** | 可协商上限 | `everyone included by the specification` | **需求规格**的制定者 |
| **I** | **Included population** | 已纳入人口 | `those who can actually use the product` | **设计团队** |
| **T** | **Target population** | 目标人口 | `those who were intended to use the product` | **公司管理层**（销售目标） |

**"理想人口"的剔除规则（三条，且必须 solution-neutral）：**

> **原文（Clarkson p112）**：
> 「**An example would be if the requirement was 'to produce a product for making hot drinks'. The exclusions under this requirement would be: motor capability- unable to lift/manipulate any cup-size container of hot liquid; cognitive capability - unable to understand how to handle any cup- size container of hot liquid safely; sensory capability - unable to distinguish correct cup-size container from other objects.**」

| 剔除理由 | 判定标准 | 例子 |
|---|---|---|
| **法律** | 法规禁止 | 英国 17 岁以下不得驾车 |
| **安全** | 无法安全操作 | 无法安全处理任何杯装热液 |
| **不可弥补的能力缺失** | 换任何设计都不行 | 无法分辨"正确的杯"与其他物体 |

> **★★★★ 判据：理想人口的剔除必须"solution-neutral（与方案无关）"—— 换个设计也救不回来，才算剔除。**
> 这条规则是防止把设计失败伪装成"本来就不可能"的唯一防线。
> **审核问法：** "这属于 ideal 的剔除，还是属于 included 的失败？" —— 如果答案是"只要改设计就能救"，那它属于后者，是设计责任。

### 3.3.3 Target population 为什么被刻意排除在定义之外

> **原文（Clarkson p113）**：
> 「**At no point in the above definitions is the 'target' population referred to, because there are so many options to which it can be mapped. For example, the whole population is the utopian target solution, the ideal population is the best that can be achieved and the negotiable maximum may be what a product designer is happy to reach.**」

> **原文（Clarkson p114）**：
> 「**One possible 'target' population that may be of interest is the intended (sales) target population. We can add this to the above WINIT categorisation, but with caution because it is an arbitrary definition, dependent upon the choices of the company management.**」

> **★★★★ 判据：Target 被单独标为"任意定义"，因为它由管理层选择，不含任何客观内容。**
> 原书用 `arbitrary definition` 这个词。这一点极其重要：**"目标用户"不是设计输入，是商业决定**，因此不能用它来论证包容性。
> **反面用法（常见错误）：** "我们的目标用户是 25–40 岁，所以不需要考虑老人。" —— 这句话在 WINIT 模型里是把 T 当成了 I，逻辑上不成立。

---

## 3.4 包容度（inclusive merit）：五种比值

> **原文（Clarkson p114）**：
> 「**Having defined the different types of populations being considered, it is possible to enumerate the ratios between them. These can be used as measures of the inclusive merit of the product.**」

> **原文（Clarkson p114）**：
> 「**The ratio between the whole and ideal populations gives an indication of the level of exclusion associated with the concept task, irrespective of the solutions developed. Changing the positioning of the product being considered, so that it is subject to different health and safety regulations or different legislation, is the only option for changing this ratio.**」

> **原文（Clarkson p114）**：
> 「**The ratio between the negotiated maximum and ideal populations reflects the level of exclusion that has been generated by the refinement of the product requirements.**」

> **原文（Clarkson p114）**：
> 「**The ratio between the included and negotiable maximum populations indicates the level of exclusion generated by the particular configuration of the product at that point in time. As the design progresses and the requirements are refined more explicitly, this ratio should approach unity.**」

> **原文（Clarkson p115）**：
> 「**The ratio between the included and ideal populations is probably the most important as it provides a direct comparison of how good the product is at the moment compared to its theoretical maximum.**」

> **原文（Clarkson p115）**：
> 「**Finally, the ratio between the included and intended populations shows how successfully the product reaches the intended sales target population, while the ratio between the negotiable maximum and intended populations shows the success of the product requirements in meeting that same target population.**」

### 3.4.1 五个比值速查表

| # | 比值 | 衡量什么 | 谁负责改进 | 原书评价 |
|---|---|---|---|---|
| 1 | **W ÷ I** | 品类/法规层面的固有排除 | 定位决策者 | 只能靠换辖区或换品类改变 |
| 2 | **N ÷ I** | **需求规格**造成的排除 | 需求制定者 | 反映需求精化带来的损失 |
| 3 | **Included ÷ N** | **产品配置**造成的排除 | 设计团队 | 设计推进时**应趋近 1** |
| 4 | **Included ÷ I** | **当前产品 vs 理论最优** | 设计团队 | **`probably the most important`** |
| 5 | **Included ÷ T** | 是否达成销售目标 | 商业方 | 与第 6 条配合看需求是否定对 |
| 6 | **N ÷ T** | 需求是否对准目标市场 | 商业方 | — |

> **★★★★ 判据：第 3 号比值（Included ÷ N）是唯一有明确收敛目标的指标 —— 必须趋近 1。**
> 原文：`this ratio should approach unity`。这意味着**设计阶段的全部工作，就是把"已纳入"推到"可协商上限"**。
> 而"可协商上限"之外的损失不归设计团队负责 —— 这是设计团队唯一可以正当免责的边界。

> **★★★ 判据：第 4 号比值"最重要"，因为它是唯一能跨产品比较的指标。**
> 原书用 `provides a direct comparison of how good the product is at the moment compared to its theoretical maximum`。
> **实操：** 做竞品对标时用第 4 号（各自对比各自的理论上限），做自身迭代时用第 3 号（看是否趋近 1）。

---

## 3.5 包容性设计立方体（IDC）

### 3.5.1 三种设计策略（立方体的三条边）

> **原文（Clarkson p108）**：
> 「**user-aware design- pushing the boundaries of'mainstream' products to include as many people as possible;** … **customisable/modular design- design to minimise the difficulties of adaptation to particular users;** … **special purpose design - design for specific users with very particular needs.**」

| 策略 | 原文定义 | 覆盖哪一层 | 成本/规模特性 |
|---|---|---|---|
| **User-aware design** | 把主流产品的边界推到尽可能多的人 | **塔基 + 塔身** | 单位成本低、量大 |
| **Customisable / modular** | 最小化适配特定用户的难度 | 塔身 | 中 |
| **Special purpose design** | 为有非常特殊需求的特定用户设计 | 塔尖 | 单位成本高、量小 |

> **原文（Clarkson p108）**：
> 「**It was recognised that the principles of user-aware design generate products that are widely accessible to the population and hence offer good population coverage. Consequently, this approach dominates the cube.**」

> **原文（Clarkson p108）**：
> 「**In between the two approaches is an intermediary design approach with flexible boundaries. Customisable/ modular design takes a base unit designed using the user-aware design principles, but with a changeable interface that is either adaptable or can be swapped for one of a series of modular designs.**」

> **★★★★ 判据：可用性顺序是 用户觉察 → 可定制 → 专用，而不是反过来。**
> 原文用 `dominates the cube` 明确 user-aware 是主体。
> **为什么重要：** 绝大多数团队的实际顺序是从"给残障用户做个专用版"开始的 —— 这正是第 1 章"特殊需求三重失败"的商业形态。正确顺序是先扩主流产品的边界，覆盖不了的部分才做可定制，最后才是专用。

### 3.5.2 三轴的来历与体积含义

> **原文（Clarkson p115）**：
> 「**A more attractive proposition would be to replace the arbitrary shape with one that represented features of the population that would be of use to a designer. Such methods of dividing the population could be along lines of gender or age, for example, but although such partitioning of the population is useful for marketing purposes, it is not necessarily helpful for designers. An alternatiye partitioning is suggested by studying the nature of human-product interaction.**」

> **★★★ 判据：按性别/年龄切分"对营销有用，对设计者没用"；按交互三阶段切分才有用。**
> 原书直接否定了人口学切分作为设计工具的价值。这一条为第 2 章"为什么不用年龄做设计输入"提供了第二处独立论证。

> **原文（Clarkson p116）**：
> 「**The resultant inclusive design cube is a very potent visualisation tool and communicates the needs of different sections of the population.**」

> **原文（Clarkson p116）**：
> 「**Each axis on the cube represents user capability and the enclosed volumes reflect population coverage.**」

**图注还原：**

- **图 5.1（Clarkson p108）**「The inclusive design cube：Mapping design approaches to the whole population using the inclusive design cube」——图上标注三种策略名：`Special purpose design`、`Customisable/modular design`、`User-aware design`。
- **图 5.3（Clarkson p116）**「The inclusive design cube：Mapping capabilities to the whole population」——三轴分别标注 `Sensory capability`、`cognitive capability`（第三轴在 OCR 文本中未完整读出，按上下文与 p449 图 26.4 应为 motor capability；**图不清处不猜，此处只录读出部分**）。
- **图 5.4（Clarkson p116）**「Design exclusion：The inclusive design cube showing product inclusion and exclusion」——图上标注 `excluded` / `included` 两个区域。
- **图 26.4（Clarkson p459）**「The inclusive design cube for use with the seven-level approach」——轴标签改为 `User perception` / `cognition`（第三轴同上未完整读出）。

> **★★★ 判据（图以文为准）：立方体是"人口覆盖体积"图，不是"产品性能"图。**
> `the enclosed volumes reflect population coverage` —— 体积大小就是被覆盖的人数比例。
> **这解释了立方体的核心用途：** 改动产品 → 体积变化 → 一眼看出"多纳入的是哪群人、多少人"。

### 3.5.3 IDC 的诊断价值

> **原文（Clarkson p116）**：
> 「**Presenting design exclusion by employing visual representations, such as the !inclusive design cube, allows the succinct communication of the levels of exclusion to the designers and design commissioners thereby enabling rapid review of the success of the current state of the design.**」

> **原文（Clarkson p116）**：
> 「**For example, if a product excludes a significant proportion of the population because of the perceptual demands, this implies that users either cannot hear or see the output from the product.**」

> **★★★★ 判据：「排除集中在哪一轴」直接指向「改哪个界面要素」。**
> 感官轴排除 → 改输出（视觉/听觉呈现）；
> 认知轴排除 → 改结构（心智模型、步骤、语言）；
> 机动轴排除 → 改形态（力、行程、握持、双手要求）。
> 立方体的价值不在"图形好看"，而在**把"改哪里"这一步从猜测变成读图**。

> **原文（Coleman p198）**：
> 「**The inclusive design cube (Figure 11.15) was proposed to assist in the visualisation of the scale of exclusion and the resultant design task (Keates and Clarkson, 2003). The axes represent sensory, cognitive and motion capabilities. Hence, the cube conveys a sense of the overall level of exclusion and some indication as to its source.**」

> **原文（Coleman p198）**：
> 「**The cube also helps to illustrate the fact that for every product family there is an ideal population who may be able to use a well-designed product. This is likely to be smaller that the whole population. The included population, who are actually able to use the product, may also be signiﬁ cantly smaller than the ideal population.**」

> **★★★ 判据：立方体同时呈现三层嵌套 —— 全体 ⊃ 理想 ⊃ 已纳入。**
> 三层之间的两个间隙，正好对应第 3.4 节的第 1 号和第 4 号比值。
> **汇报用语：** "外层间隙是品类固有的（不可改），内层间隙是我们的责任（可改，当前 X 人）。"

---

## 3.6 三种"看起来像包容设计"但其实不是的做法

原书用一整节否定了五种既有方法。这一节对产品团队最有价值，因为它列出了常被误当作答案的做法。

> **原文（Clarkson p106）**：
> 「**Initially it was recognised that the disabled and elderly were the principal groups excluded from using most products. The solution appeared obvious - if such users could not use the products, then developing special products designed specially for them would solve the problem. Thus concepts such as 'design for disability' appeared.**」

> **原文（Clarkson p106）**：
> 「**While many good products were developed, they were outnumbered by those that were either expensive, inappropriate, or simply did not offer the necessary utility.**」

> **原文（Clarkson p107）**：
> 「**The situation became so bad that many rehabilitation robotics products, for example, failed to even sell more than 1 0 units (Mahoney, 199 7).**」

> **原文（Clarkson p107）**：
> 「**In parallel with the lack of attention paid to usability issues, the social acceptability of the products was often overlooked as well. Many products were developed with no thought of whether someone would actually want to use, or be seen using, them.**」

> **★★★★ 判据：`failed to even sell more than 1 0 units` —— 这是"为残疾人设计"路线最刺眼的一次失败量化。**
> 失败原因被拆成两条独立缺失：**可用性**被忽略 + **社会可接受性**被忽略。
> 第二条（`be seen using`）是纯产品设计判断，与功能无关。它对应第 1 章 Simply 手机的 `people do not necessarily want to be seen with a phone that looks as though it has been made easier to use`。

### 3.6.1 五种既有方法及其短处

> **原文（Clarkson p107）**：
> 「**A number of new design approaches were developed to overcome the shortcomings of the earlier methods. However, these newer approaches have their own shortcomings, for example often being targeted only at specific population groups or impairment types. For example, transgenerational design (Pirkl, 1993) focuses on design for older adults, while rehabilitation design focuses on specific impairment types (Hewer et al., 1995).**」

> **原文（Clarkson p107）**：
> 「**In addition, the prescribed methods of application of the existing approaches are often vague. For example, universal design is more of an ethos than a rigorous, systematic design approach. There are very few structured descriptions of the implementation of universal design in more detail than broad design objectives (Bowe, 2000).**」

| # | 方法 | 短处（原文） |
|---|---|---|
| 1 | **Design for disability** | 昂贵、不合适、缺乏必要效用；开发周期长成本高；把时间花在技术上而非可用性上 |
| 2 | **Transgenerational design**（Pirkl 1993） | `focuses on design for older adults` —— 只覆盖一类人群 |
| 3 | **Rehabilitation design** | `focuses on specific impairment types` —— 只覆盖一类损伤 |
| 4 | **Universal design**（Bowe 2000） | `more of an ethos than a rigorous, systematic design approach` —— **是理念不是方法** |
| 5 | **User Pyramid Approach**（Benktzon 1993） | 按原文并列，未单独批评短处 |

> **★★★★ 判据：通用设计最致命的问题不是理念错，而是"没有实施描述"。**
> 原文用 `more of an ethos than a rigorous, systematic design approach` 和 `very few structured descriptions of the implementation`。
> **这条判据解释了整本书为什么写成现在这个样子**：它不提供原则清单（那已经有了），它提供**可算的过程**（WINIT + 比值 + 排除率 + 7-Level）。
> **与 `design-psychology-norman` 的对照：** 诺曼给的是"设计原则"，本书给的是"设计的度量与流程"。原则不缺，缺的是从原则到人数的换算。

### 3.6.2 关键的技术论断：为什么"扩大用户定义"不够

> **原文（Clarkson p109）**：
> 「**Many of the existing approaches to inclusive design and design for all are focused on making products and services more accessible by extending the initial concept of the end-user to include a wider range of users. While this is an excellent starting point, the success of the resultant design is highly dependent upon the choice of the end-users at the outset. If the end-user selection is very specific, then the needs of those users should be well catered for. However, the overall ability of the final product to meet the needs of different end-user groups may be compromised, if the design is tailored too closely to the specified end- user group.**」

原书给了一个非常精确的反例：

> **原文（Clarkson p109）**：
> 「**For example, consider the design of a computer input device that filters out tremor. Tremor can arise from a number of medical conditions, as a result of the ageing process, or from external environmental factors such as movements from being on a train. Tailoring the input filters to assist users with just one condition such as ataxic cerebral palsy, may inadvertently limit their usefulness for end- users with Parkinson's Disease, say Therefore, it is best to consider the needs of all users with similar conditions during the design process.**」

> **★★★★ 判据：按"病因"分组做适配，会把同一能力门槛下的人切碎。**
> 震颤（tremor）可由多种病因产生 —— 脑瘫、帕金森、老化、甚至坐在火车上。若按"脑瘫"调滤波器，帕金森用户反而可能被排除。
> **这是"按能力分组"优于"按病因分组"的最强技术论证**，比伦理层面的论证更难反驳。

> **原文（Clarkson p109）**：
> 「**The underlying principle of design exclusion is that by identifying the capability demands placed upon the user by the features of the product, it is possible to establish the end-users who cannot use the product irrespective of the cause of their functional impairment. Consequently. by re-designing the product to lessen the capability demand, users from a wide range of end-user groups can potentially be included and no-one is excluded unnecessarily by considering one cause to the detriment of others.**」

> **原文（Clarkson p109）**：
> 「**The concept of addressing exclusion is supported by Alexander's notion of'bad fit' ( 1964):** … **When we speak of bad fit we refer to a single identifiable property of an ensemble, which is immediate in experience, and describable. Where an instance of misfit occurs in an ensemble, we are able to point specifically at what fails and describe it.**」

> **★★★ 判据：`irrespective of the cause` 是本节的关键词 —— 排除可以脱离病因被独立识别。**
> 加上 Alexander 的"bad fit"概念（失配是**可直接指认并描述**的单一属性），这两条合起来证明了：**排除是可定位的产品属性，不是用户属性。**

---

## 3.7 本章概念-论点表（共 19 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | **排除视角优于纳入视角** | 「identifying why and how end-users cannot use a product enables us to counter such exclusion」 | 全书四次重复 | 纳入是标量（不指向特征），排除是向量（指向特征）。汇报用纳入，改进必须用排除 | Clarkson p105 |
| 2 | **Demand > Capability** | 「If Demand > Users' Capability then Exclusion」 | — | 全书唯一不等式。两侧可独立描述，因此可分别评估、分别改 | Coleman p186 |
| 3 | **能力三分含"经验"** | 「experiential measures (for example prior use of computers)」 | 老年人首次用触屏 | 能力含学习史，不只是生理量。新奇性本身构成需求门槛 | Coleman p187 |
| 4 | **排除是一条谱** | 「from total or partial exclusion, to difﬁ culty or frustration」 | — | "没被排除"≠"没问题"。困难与挫败有可量化商业代价 | Coleman p187 |
| 5 | **56% 任务成功率** | 「the user success rate was 56%」 | Nielsen 2002，496 次尝试 / 20 站 | 把设计排除从公益议题改写为转化率议题。这是最有说服力的商业证据 | Clarkson p530 |
| 6 | **通路任务不能打折** | 「An infrequent (or short) task that excludes the user may lead to exclusion for the whole product」 | 灶具儿童安全联锁 | 区分"排除"与"困难"的唯一标准：该任务是否是通路。通路任务一律按最高标准 | Coleman p188 |
| 7 | **工作定义** | 「should only exclude the end- users who the product requirements exclude」 | 水壶容量 | 排除分需求性（可辩护）与设计性（不可辩护）。判据：换设计能否救回 | Clarkson p111 |
| 8 | **需求性排除是管理决策** | 「A managerial decision is therefore required between marketability of the product and the level of population exclusion」 | 水壶容量取舍 | 设计团队无权以"需求如此"免责；必须把容量↔排除率↔市场提交给能改需求的人 | Clarkson p111 |
| 9 | **包容度有两个自变量** | 「the merit of the requirements that define it; and its merit when judged against those requirements」 | — | 只评估"达成度"会漏掉"需求本身就把人排除"。这是最常见的评估错误 | Clarkson p111 |
| 10 | **WINIT 五层** | Whole / Ideal / Negotiable max / Included / Target | — | 五层各有责任人。混淆层级会导致"用商业目标论证包容性"的逻辑错误 | Clarkson p112–p114 |
| 11 | **Solution-neutral 剔除** | 「This assessment should be completely solution-neutral」 | 热饮产品三轴剔除 | 防伪："本来就不可能"必须先证明"换任何设计都救不回" | Clarkson p112 |
| 12 | **Target 是任意定义** | 「it is an arbitrary definition, dependent upon the choices of the company management」 | — | "目标用户是 25–40 岁"不能用来论证包容性，因为它是选择而非事实 | Clarkson p114 |
| 13 | **Included ÷ Negotiable → 1** | 「this ratio should approach unity」 | — | 唯一有收敛目标的指标；也是设计团队唯一可正当免责的边界 | Clarkson p114 |
| 14 | **可用性顺序 觉察→定制→专用** | 「this approach dominates the cube」 | — | 与行业惯常顺序相反。先扩主流边界，覆盖不了才定制，最后才专用 | Clarkson p108 |
| 15 | **按病因分组会切碎人群** | 「may inadvertently limit their usefulness for end-users with Parkinson's Disease」 | 震颤输入设备（脑瘫 vs 帕金森） | 同一门槛多种病因；按病因适配会互相排斥。这是"按能力分组"的最硬技术论证 | Clarkson p109 |
| 16 | **Bad fit 可指认** | 「we are able to point specifically at what fails and describe it」 | Alexander 1964 | 失配是产品的单一可描述属性，不是用户的属性。这为"排除可定位"提供了哲学依据 | Clarkson p109 |
| 17 | **通用设计没有实施描述** | 「more of an ethos than a rigorous, systematic design approach」 | Bowe 2000 | 解释了本书为何写成"可算的过程"而非"原则清单" | Clarkson p107 |
| 18 | **专用路线卖出不到 10 台** | 「failed to even sell more than 1 0 units」 | 康复机器人 | 特殊需求路线最刺眼的失败量化。与第 1 章三重失败回路互为证据 | Clarkson p107 |
| 19 | **"被看见使用"是独立判断** | 「no thought of whether someone would actually want to use, or be seen using, them」 | — | 社会可接受性与功能可及是两个独立失效点。仅改功能不能救 | Clarkson p107 |

---

## 3.8 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **章节页说明**：本章引用的 p105–p118 为 Clarkson ch5 正文；p119 为空白页 `103`；p120 起为 ch6 | **已逐页核对**：`p105` 起为正文，`p117` 为 Summary 与 Further reading，`p118` 为参考文献续，`p119` 仅页码 | — |
| **ITK / Inclusive Design Toolkit 名义下的完整方法** | **只提及，未展开**。Clarkson 全书 `ITK` 关键字 **0 命中**；`Toolkit` 仅在导论提及 "A Design Toolkit" 作为**节名**（p9、p13），不是产品名。Coleman 中的 `Inclusive Design Toolkit` 是 **BT 公司的网站**（`www.inclusivedesigntoolkit.com`，Coleman p18、p22），非本方法名 | 该网站已随时代变更；本技能不含其内容。**不要把它当作书里的方法名引用** |
| **HADRIAN 工具** | **0 命中**。Clarkson 与 Coleman 全文检索 `HADRIAN` 均为 0 | HADRIAN 是 Loughborough 的后续成果，**不在本书范围**。本技能不覆盖 |
| **排除率的具体数字** | 本章只给模型与比值定义，**不给具体百分比**（除 p439 的 6% 举例） | 见 ch04 §4.5（水壶/电视机/助听器等实测数字） |
| **IDC 的数值坐标系与可量化体积** | **未给出**。原文只有定性描述与示意图，无坐标刻度值 | 原书在 p461 承认：`The authors are currently developing a tool to allow designers to interrogate a database and to automatically produce IDCs based on capability requirements` —— **当时尚未完成** |
| 立方体三轴是否应等权 | **未解决**（同 ch02 第 4 条判据） | 无后续论证 |
| 认知轴的界面要素清单 | **未展开**。原文只说"改结构"，未给认知轴的"界面变量"清单（对比感官/机动有 colour、dimensions、force 等） | 需结合 `design-psychology-norman` 的七阶段与四类限制因素补齐 |
| 中国/东亚的 WINIT 人口基数 | **无**。全部数字为 GB | 中国残联数据、《中国残疾人事业统计年鉴》 |
| 2010 年后的标准对接（EN 17161 / ISO 9241-171） | **不在源书范围**（成书 2003/2007） | 标准原文 |

---

## 3.9 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 七轴 + 三类别 | **ch02 §2.1** | 立方体三轴的直接来源（本章 p115 引用 Card/Moran/Newell） |
| 金字塔十级 | **ch02 §2.4** | IDC 与金字塔是"能力图"与"人口图"两种呈现（p116 明说继承 Benktzon） |
| WINIT + 五比值 | **ch04 §4.2** | 排除率的分子分母定义直接取自 WINIT |
| 工作定义（只排除需求排除的人） | **ch04 §4.4** | 四步评估法 Step 2/3 的判定标准 |
| 需求性排除是管理决策 | **ch10 §10.6** | BS 7000-6 把"需求设定"放在组织级管理而非项目级 |
| 通路任务不可打折 | **ch06 §6.4** | 排除审计（exclusion audit）的任务分解必须标出通路 |
| 按能力分组 vs 按病因分组 | **ch07 §7.3** | 模拟工具刻意"模拟能力损失而非模拟损伤"的同一逻辑 |
| 通用设计没有实施描述 | **ch05 §5.1** | 7-Level 方法正是补上"实施描述"的那一步 |
| 56% 成功率 / 66% 失去兴趣 | **ch08 §8.1** | 共情方法要处理的"语境性失能"的量化背景 |
| 「被看见使用」是社会可接受性 | **ch08 §8.4** | Simply 手机三原则中 Suitable Aesthetic 的由来 |

### 3.9.1 跨技能挂钩（本机已有技能）

| 本技能内容 | 挂钩技能 | 关系与用法 |
|---|---|---|
| **`Demand > Capability` 与"需求性/设计性排除"二分** | **`ergonomics-ding-yulan`** | 丁玉兰的"产品尺寸设计三类（I/II/III 型）"本质上就是在处理"需求给定的边界"：I 型（如门高）取上限保安全，II 型（如可调范围）取下限，III 型取 P5–P95。**本技能补的是丁玉兰没有的一步：把"取 P5–P95"这个决定明确标为"设计性排除"，并要求给出人数与免责理由。** |
| **WINIT 五层人口 + 五比值** | **`ergonomics-ding-yulan`** | 丁玉兰的"满足度"只有一维（尺寸落在区间内的人口比例）。本技能把单一满足度扩展成六比值，区分"需求给的"与"设计造成的"。<br>**合用判据：丁玉兰算满足度 → 本技能判断这个满足度损失属于哪一层、归谁负责。** |
| **通路任务（gate task）概念** | **`product-structure-liubaoshun`** | 刘宝顺的结构件里，卡扣、螺纹、密封、锁止往往就是"通路"：打不开就整机不可用。本技能给"通路任务按最高标准"的规则，刘宝顺给"如何做成单手可开、且不失锁止力"的机构方案。<br>**合用判据：先用本技能标出通路任务，再用刘宝顺的结构原理逐个改造。** |
| **"按病因分组会切碎人群"（震颤案例）** | **`design-psychology-norman`** | 诺曼的"预设用途/限制因素"是按**动作与形态**组织的，与病因无关 —— 与本技能"按能力需求分组"同构。二者都反对按人群标签设计。 |
| **56% 成功率与"语境性失能"** | **`design-psychology-norman`** | 诺曼的"行动七阶段"给出了"为什么会在某一步失败"的定位框架；本技能给出"这一步失败有多少人、损失多少"。<br>**合用：诺曼定位（哪一阶段）＋ 本技能量化（多少人）。** |
| **IDC 的"改哪里"三段对应** | **`design-psychology-norman`** | 感官→改输出，认知→改结构，机动→改形态。认知段的具体改法应直接调用诺曼的"概念模型/匹配/反馈/限制因素"四件套；本技能只负责诊断出"问题在认知轴"。 |
