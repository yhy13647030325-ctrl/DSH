# 第 4 章：排除率的量化——四步评估法与实测数字

> **原书 PDF 页序 p433–p447（15 页，Clarkson 第 25 章）＋ p201–p216（16 页，Coleman 第 12 章）｜本版逐页读完全部 31 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）
>
> **读法说明**：按 Clarkson ch25 的 `Information requirements → Available data → Product assessment for identifying design exclusion（四步） → A survey of design exclusion → Case study（水壶） → Eliminate multiple counting → Discussion → Summary` 逐节展开；Coleman ch12 补上"评估在产品开发流程里放在哪一步"以及极/边界/健全三类用户的用法。
> 每节含【原文摘录】+【判据提炼】。

---

## 4.0 总纲：这一章把第 3 章的模型变成可算的数

第 3 章给了 WINIT 人口与包容度比值。本章回答：**那些人口数字从哪来、怎么算、算出来是多少。**

**四个产出：**

| 产出 | 内容 | 页码 |
|---|---|---|
| **① 数据前提** | 产品特征无法直接连到用户，必须经过两条桥（能力 / 身体尺寸） | p435 |
| **② 四步评估法** | 定语境 → 评能力需求 → 评身体属性 → 消除多重计数 | p436–p437 |
| **③ 实测排除率** | 水壶 D/E/F、数字电视、日常家电等的具体百分比与人数 | p439–p442 |
| **④ 多重计数的消除** | 气泡图与耦合区；只降一轴则几乎无效 | p443–p445 |

> **★★★★ 判据：本书的方法论承诺是"能把排除变成一个百分比 + 一个原因"，而不是"能把排除降到零"。**
> 原书在 Discussion 里明确承认不可能全纳入：`Some people will always be excluded by any specific design if the crucial reason for exclusion has not been identified or justified`（p445）。
> 因此本方法的目标不是"消除排除"，而是**让排除变成被知情选择的、可辩护的排除**（回到第 3 章的工作定义）。

---

## 4.1 数据前提：为什么不能直接把产品特征连到人

> **原文（Clarkson p435）**：
> 「**The key requirement for assessing design exclusion is the ability to relate users to the ergonomic features of a product (Figure 2 5.1). However, the direct link (dashed line) between the two cannot be found from existing data. Consequently, based on the data available, the link is explored through two relationships: ( 1) product ergonomic features and user functional capabilities (sensory, cognitive and motion capabilities); and, (2) product ergonomic features and user physical attributes (anatomical dimensions such as height, reach, grip strength, etc.)**」

**图注还原：**

- **图 25.1（Clarkson p435）**「Information requirements：Relating users to the ergonomic features of a product」——图上有一条**虚线**（直接连接，标注为不可得）与两条**实线**（经功能能力、经身体属性），即上式两条关系。
- **图 25.2（Clarkson p435）**「User assessment scale：Hearing capability」——即第 2 章引用的 H1–H8 八级表。
- **图 25.3（Clarkson p436）**「Weighted disability score：A weighted sum of the worst individual scores」——`worst + 0.4 (second worst) + 0.3 (third worst)`。
- **图 25.4（Clarkson p437）**「Levels of exclusion：Each capability demand leads to a level of exclusion」——按轴列出各轴需求分数与对应排除人数。
- **图 25.5（Clarkson p438）**「A typical product assessment- capability demands lead to exclusion」——Acoustiguide 2000 导览棒评估表（详见 §4.3.3）。
- **图 25.6（Clarkson p439）**「Exclusion in everyday products：From toasters to cameras」——用户金字塔叠加多品类排除率（1%/2%/4%/6% 四档）。
- **图 25.7（Clarkson p440）**「A range of kettles：From old to new」——六种壶 A–F。
- **图 25.8 / 25.9（Clarkson p441）**「The high dexterity demand：Made by the fiddly filter」/「Filter replacement：Demands high dexterity」——滤网拆装的高灵巧需求。
- **图 25.10（Clarkson p442）**「Users excluded：Result of capability requirements」——壶 D/E/F 三列排除表。
- **图 25.11（Clarkson p442）**「Switch clearance：An effective design」——手柄与开关间隙 18 mm。
- **图 25.12（Clarkson p442）**「The ergonomic reference thickness of the tip of the index finger」——UK/USA 均值、P5、P95 三列（见 §4.5.3）。
- **图 25.13（Clarkson p443）**「The kettle lid：Simple action can prove difficult」——开盖动作。
- **图 25.14（Clarkson p443）**「Multiple counting：Sensory and motion capabilities」——感官×机动气泡图。
- **图 25.15（Clarkson p443）**「Multiple counting：Motion and cognition capabilities」——机动×认知气泡图。
- **图 25.16（Clarkson p444）**「Multilple counting：Design exclusion with kettles E and F」——多边形 A（壶 E 额外排除）与 B（壶 F 排除）。
- **图 25.17（Clarkson p444）**「multiple counting：Capabilities and the inclusive design cube」——三轴立方体，角标 `(0,10,10)`、`(10,10,10)`、`(0,10,0)`、`(0,0,0)`、`(10,0,0)`。
- **图 25.18 / 25.19（Clarkson p445）**「Multiple capabilities：Prevalence of capabilities % of GB 65+」/「% of GB 16+」——单损/双损/三损的百分比。

> **★★★★ 判据：两条桥意味着排除必须算两次，然后去重。**
> - **桥 1（能力）**：产品特征 → 七轴需求分数 → 有多少人达不到该分数；
> - **桥 2（身体尺寸）**：产品特征 → 人体尺寸/力 → 有多少人超出尺寸区间。
> 两条桥的数据源不同（能力来自 DFS 残障调查，尺寸来自 Adultdata 等人体测量库），因此**合并时必然重复计数**。这是第 4 步存在的理由。

### 4.1.1 数据源清单与各自的坑

> **原文（Clarkson p435）**：
> 「**There are several sources of capability data available from government disability survey, consumer research institutes and charity organisations (Martinet al., 1988; DTI, 2000; RNIB, 2002; RNID, 2002). The most recent multiple capability data set covering the Great Britain (GB) population is from the 1996/97 Disability Follow-up (DFS) (Grundy et al., 1999) to the Family Resources Survey (Semmence et al., 1998).**」

> **原文（Clarkson p436）**：
> 「**These data sets contain anthropometric and physical strength categories. For example, there are 266 anthropometric dimensions and 28 strength measurements in Adultdata. However, these data sets are typically collected from many different countries and consequently are difficult to correlate against the capability data or to use to draw population -specific conclusions.**」

| 数据源 | 提供什么 | 已知缺陷（原文） |
|---|---|---|
| **DFS 1996/97**（Grundy et al., 1999） | 七轴能力 × 年龄 × 性别 | 自陈式访谈；灵巧度系统性失真（ch02 §2.3.2） |
| **OPCS 1985–88**（Martin et al., 1988） | 13 类残障、加权严重度 | 早于 DFS，用途为福利规划 |
| **Adultdata**（Peebles & Norris, 1998） | 266 项人体尺寸 + 28 项力量 | **多国混合采集，难以与能力数据关联，无法得出特定人口的结论** |
| **Childata / Older Adultdata** | 儿童 / 老年人尺寸 | 同上 |
| **RNIB / RNID** 等慈善机构 | 特定障碍深度数据 | 与 DFS 口径不一致（Clarkson p381 有直接对比） |

> **原文（Clarkson p381）**：
> 「**As might be expected, the discrepancies are due to the differences of descriptions of mild, moderate and severe deafness and the data collection methods employed.**」

原书给出了一张直接对比表（同一件事，两套数据差 3–6 倍）：

> **原文（Clarkson p381）**：
> 「**UK(1996) 16-60 years 61-80 years 81+years Mild deafness 4.6% 28.1% 18.4% Moderate deafness 1.6% 16.5% 57.9% Severe deafness 0.3% 2.3% 16.8%**」

> **原文（Clarkson p381）**：
> 「**UK(1996-97) 16-59 years 60-79 years 80+ years Mild impairment 1.8% 10.1% 20.6% Moderate impairment 0.5% 4.2% 9.7% Severe impairment 0.1% 0.3% 0.8%**」

| 口径 | 轻度 | 中度 | 重度 |
|---|---|---|---|
| RNID（1996，81+） | 18.4% | **57.9%** | 16.8% |
| DFS（1996-97，80+） | 20.6% | **9.7%** | 0.8% |

> **★★★★ 判据：同一个"中度耳损"，两套官方数据差 6 倍（57.9% vs 9.7%）。**
> 差异来源不是统计误差，是**"中度"的定义不同**。这意味着：**任何排除率数字必须连口径一起引用，否则不可比。**
> **实操纪律：** 写"排除率 X%"时必须同时写"依据 DFS 七轴量表 / RNID 分级"，就像写尺寸必须写百分位一样。

> **原文（Clarkson p381）**：
> 「**Hence it is important to identify the purpose for which the data is required, the consequent nature of the data needed and thus the most appropriate data source. Even after this process, it may still be necessary to modify and adapt the data to meet the specific information need.**」

---

## 4.2 四步评估法（本章的核心方法）

> **原文（Clarkson p436）**：
> 「**Focusing on design exclusion, a four-step approach for product assessment is proposed (Clarkson and Keates, 2002):**」

### Step 1：明确使用语境

> **原文（Clarkson p436）**：
> 「**Step 1 specify the context of use. State any assumptions regarding the environment in which the product is used and the sequence of actions encountered when using the product.**」

> **★★★ 判据：第一步不是评估产品，是写出"使用动作序列"——因为需求是按动作产生的，不是按产品产生的。**
> 同一台水壶，"放在合适高度"与"放在高处吊柜里"是两种完全不同的使用语境，排除率可以差数倍。
> **这解释了为什么原书的四步法必须从语境开始**：脱离语境的排除率只是一个数字，无法用于改进。

### Step 2：评估能力需求

> **原文（Clarkson p436）**：
> 「**Step 2 assess the capability demands imposed on the user by the product, subject to its defined context of use. Determine the number of users excluded from using the product and the reasons for their exclusion. The number of users disadvantaged, but not excluded, when using the product should also be identified.**」

> **★★★★ 判据：Step 2 要求同时报两个数 —— 被排除者 + 处于劣势但未被排除者。**
> 只报第一个会重复第 3 章的错误（把"困难/挫败"当成不存在）。原书用了 `should also be identified` 这种措辞，说明这常被漏掉。

### Step 3：评估身体属性

> **原文（Clarkson p436）**：
> 「**Step 3 assess the physical attributes required by the product, subject to its defined context of use. Determine the number of users excluded from using the product and the reasons for their exclusion.**」

### Step 4：消除多重计数

> **原文（Clarkson p436）**：
> 「**Step 4 eliminate multiple counting. Users may be excluded or disadvantaged for more than one reason. For example, someone**」

> **原文（Clarkson p437）**：
> 「**with both low-vision and restricted movement may be identified twice as being excluded by products requiring high vision and movement capability. Consequently, such multiple counting of individuals' multiple capability losses need to be corrected for.**」

> **原文（Clarkson p437）**：
> 「**Theoretically, there will be multiple counting when combining the results of both the functional capability and physical attribute assessments. However, if the data sets adopted are radically different, for example, from different countries, this can be difficult, if not impossible. Multiple counting from within single data sets should be eliminated wherever possible.**」

> **★★★ 判据：跨数据集的多重计数"可能根本做不到"—— 原文用了 `difficult, if not impossible`。**
> 因此实践中的正确做法是：**只用同一份数据集（DFS）内的去重**，并对跨集合并的结果明确标注"含未消除的重复计数"。
> **这条判据防止一个常见错误：** 把"能力排除 8%"与"尺寸排除 10%"相加成 18% —— 这几乎一定是错的。

---

## 4.3 实施细节：专家评估表怎么填

### 4.3.1 从量表描述到具体动作的"主观类比"

> **原文（Clarkson p437）**：
> 「**A simple assessment form with the seven capability scales is used for expert analysis. An example of a typical form is shown in Table 25.4, for an acoustic guide device. Scores are given according to the descriptions of the scale items. If there is no obvious link between the description and the user-product interaction, subjective analogy is to infer the most appropriate score. For example, there is no relevant description of the dexterity capability required for pressing buttons on the device. Comparison is thus made based on existing descriptions. It is assumed that the required capability of squeezing water from a sponge (score 8.0) is comparable to pressing buttons, as both actions are related to the exertion of finger strength. Therefore a score is made with this reference**」

> **★★★★ 判据：量表里没有对应描述时，用"主观类比（subjective analogy）"—— 找一个已知分数的相似动作做锚点。**
> 原文的实例非常具体：**按按钮 ≈ 挤海绵（dexterity 8.0）**，理由是"两者都涉及手指力量的施加"。
> **这是本章最可复制的操作技巧。** 它把"无法量化的判断"转成"找一个已标定的动作做参照"，从而让不同评估者得出接近的分数。

### 4.3.2 评估表的标准结构

> **原文（Clarkson p438）**：
> 「**Capability Locomotion Reach and stretch Dexterity Vision Hearing Communication Int. functioning Score 7.5 8.0 8.0 4.5 5.5 5.5 9.5**」

> **原文（Clarkson p438）**：
> 「**Product description: Acoustiguide 2000 wand- a device for a museum's audio guide system**」

> **原文（Clarkson p438）**：
> 「**Context of use: The device is in a museum for user trials. The user collected the device from the Museum's staff and basic instructions (how to start the device and what functions are available) are given. A neck strap is already attached to the device.**」

> **原文（Clarkson p438）**：
> 「**Sequence of use: strap the device 2 find the number next to the selected object 3 key in the number 4 press the Play button 5 listen to the commentary, adjust volume or pause when necessary**」

> **原文（Clarkson p438）**：
> 「**Justification This device only needs one hand for operation (NB: A user who always needs to hold on to something to keep balance will be scored 7.0) The relevant action is hanging the device around user's neck (the user hence should be able to put one arm up to head) The dexterity demand made by the device is no more than pressing buttons that are reasonably well spaced and shaped, the device is light (260 grams) and the operation is very simple If the user cannot see well enough to read a large print book, he/she may not see the buttons well The enhanced voice is comparable to a person talking in a loud voice in a quiet room To understand the explanation of the instruction is easy, even if the user may have difficulty in understanding strangers The usage of the device is intuitive and simple. It does not need much work intellectual**」

**这是一份可以直接照抄的模板。** 结构是：

| 字段 | 内容 |
|---|---|
| 产品描述 | 一句话 |
| 使用语境 | 谁给的、给了什么说明、配件状态 |
| 使用动作序列 | 编号列出（本例 5 步） |
| 七轴分数 | 每个分数配一条 `Justification`（判定理由） |
| 一般评论 | 本例指出缺标签导致需员工协助、红色 C 键令人困惑 |
| 评估耗时 | 本例 30 分钟 |

> **★★★ 判据：每个分数必须配一条 justification —— 这是评估可信度的唯一保障。**
> 注意 justification 里有两类特别有价值的写法：
> ① **给出可复现的锚点**：`comparable to a person talking in a loud voice in a quiet room`（听觉 5.5）、`read a large print book`（视觉 4.5）、`squeezing water from a sponge`（灵巧 8.0）；
> ② **给出补充规则**：`A user who always needs to hold on to something to keep balance will be scored 7.0` —— 这是把"平衡能力"折算进 locomotion 的规则。

> **原文（Clarkson p438）**：
> 「**General comments: On the whole, the device is easy to use. If there is a label to tell the user how to start the commentary (find the number, input the number and press 'play' button), the staff assistance may not be required and the communication demands be reduced. The red 'C' button (function: clear) is confusing**」

> **★★ 判据：`Duration of assessment: 30 minutes` —— 一份完整七轴评估约需 30 分钟。**
> 这是本章唯一给出的**时间成本**数据，对"能不能塞进项目周期"这个现实问题至关重要。

### 4.3.3 Acoustiguide 三轴排除结果

> **原文（Clarkson p437）**：
> 「**Disability Score Exclusion Locomotion 7.5 1 031 000 Reach and stretch 8.0 116 000**」

> **原文（Clarkson p437）**：
> 「**Dexterity 8.0 423 000 Vision 4.5 387 000 Hearing Communication Intellectual function 5.5 5.5 9.5 400 000 74 000 115 000**」

| 轴 | 需求分数 | 排除人数（GB 16+） |
|---|---|---|
| Locomotion | 7.5 | **1,031,000** |
| Reach and stretch | 8.0 | 116,000 |
| Dexterity | 8.0 | 423,000 |
| Vision | 4.5 | 387,000 |
| Hearing | 5.5 | 400,000 |
| Communication | 5.5 | 74,000 |
| Intellectual functioning | 9.5 | 115,000 |

> **原文（Clarkson p439）**：
> 「**However, the total exclusion will not be the sum of the exclusion totals in Table 25.4 because ofmultiple counting.**」

> **★★★ 判据：七轴人数不能相加（本例相加 = 2,546,000，实际远小于此）。**
> 这是"多重计数"最直观的一次演示：**相加会严重高估**。

---

## 4.4 实测排除率（本章最可引用的数字）

### 4.4.1 日常家电的整体排除率

> **原文（Clarkson p439）**：
> 「**The whole user pyramid represents 8 582 200 adults with functional impairments- 20% of the GB adult population. The percentages listed show exclusion across the whole GB population. For example, products scoring 5 will exclude 6% of the GB adult population by the functional demands they made upon users.**」

> **原文（Clarkson p439）**：
> 「**Quantifying design exclusion 25.6 Exclusion in everyday products From toasters to cameras. 428 1% Severe disability 10 9 2% 4% electnc kettle m1crowave (d1al) washmg mach1ne can opener 8 steam iron - ------....l. b1g button phone Slight disability 6% TOTAL: 8 582 200**」

**图注还原（图 25.6）：** 金字塔分十层；图上标出四档排除百分比 **1% / 2% / 4% / 6%**；提及的产品有 `electric kettle`、`microwave (dial)`、`washing machine`、`can opener`、`steam iron`、`big button phone`；底注 `TOTAL: 8 582 200`。
**读不出的：** 各产品与具体百分比的逐一对应关系在 OCR 中已错位，**不做猜测**。

> **★★★★ 判据：日常小家电的排除率在 1%–6% 区间；一把"5 分"的产品排除 6%，即约 51 万人（GB）。**
> 换算：6% × 8,582,200 ≈ 515,000 人。这个量级足以让一个单品项目的商业论证成立或不成立。

### 4.4.2 水壶三兄弟：技术升级不等于包容性提升（本章最好的案例）

> **原文（Clarkson p440）**：
> 「**Early kettles, such as kettle (A) in Figurte 2 5.7, were made of metal and suspended over an open flame to boil the water. They had a large handle, which doubled as the means of suspension, mounted above the body of the kettle. Such kettles required limited dexterity and were well balanced for carrying and pouring, but care had to be exercised when using them close to the open flame.**」

> **原文（Clarkson p440）**：
> 「**The corded electric kettle (B) retained the shape and balance of the earlier models and removed the need for an open heat source, but had the disadvantage of the additional dexterity required to insert and remove the cord.**」

> **原文（Clarkson p440）**：
> 「**The early plastic jug (corded) kettles (C), introduced a new problem. The side-mounted handle changed the balance of the kettle, making it more difficult to use for those with limited upper-body strength.**」

> **原文（Clarkson p440）**：
> 「**The increasingly diversified kettle design does not guarantee better inclusion of the product. Some 'fashionable' kettles (E) may be prone to failing usability and accessibility tests.**」

> **原文（Clarkson p440）**：
> 「**However, when designers are aware of the issue and attempt to solve the problems with accessibility and usability, innovative solutions come as a result, such as the 'no- pour' kettle concept (F).**」

**六代水壶的能力需求演化（原书的核心论证）：**

| 代 | 形态 | 解决什么 | **新引入什么需求** |
|---|---|---|---|
| **A** | 明火金属壶（上置大把手） | — | 需在明火旁小心 |
| **B** | 有绳电壶 | 消除明火 | **插拔电源线需额外灵巧度** |
| **C** | 塑料壶（侧把手，有绳） | — | **侧把手改变重心，上肢力量弱者更难** |
| **D** | 传统无绳金属壶 | 部分解决重心 | **整体重量仍是弱使用者的问题** |
| **E** | 时尚无绳壶 | — | **易失败于可用性/可及性测试** |
| **F** | "不倾倒"概念壶 | 与残障用户共同设计 | — |

> **★★★★ 判据：每一代技术解决一个问题，同时引入一个新需求 —— 这是"技术乐观主义"最硬的反证。**
> 原文还给了更概括的判断：

> **原文（Clarkson p445）**：
> 「**It is typical that no sooner is one problem resolved (for example: detaching the cord of kettles), than another is introduced (for example: poor balance). On the other hand, design changes do not always provide the benefit that may be expected (Clarkson and Keates, 2002).**」

### 4.4.3 壶 D / E / F 的排除表（可逐格引用）

> **原文（Clarkson p442）**：
> 「**Capabilities Kettle D (1.7 litre) Kettle E (1.7 litre) Minimum Total16+ Minimum Total16+ requirement excluded requirement excluded Locomotion n/a 0 n/a 0 Reach and stretch 6.5 365 000 6.5 365 000 Dexterity 5.5 2 105 000 3.0 2 727 000 Vision 5.0 319 000 4.5 387 000 Hearing n/a 0 n/a 0 Communication n/a 0 n/a 0 Int. functioning 7.0 305 000 6.0 488 000**」

> **原文（Clarkson p442）**：
> 「**Kettle F (1 I itre) Minimum Total16+ requirement excluded n/a 0 6.5 365 000 7.0 945 000 8.0 137 000 n/a 0 n/a 0 10.5 60 000**」

| 轴 | 壶 D（1.7 L）需求 / 排除 | 壶 E（1.7 L）需求 / 排除 | 壶 F（1 L）需求 / 排除 |
|---|---|---|---|
| Locomotion | n/a / 0 | n/a / 0 | n/a / 0 |
| Reach and stretch | 6.5 / **365,000** | 6.5 / **365,000** | 6.5 / **365,000** |
| Dexterity | **5.5 / 2,105,000** | **3.0 / 2,727,000** | **7.0 / 945,000** |
| Vision | 5.0 / 319,000 | 4.5 / 387,000 | **8.0 / 137,000** |
| Hearing | n/a / 0 | n/a / 0 | n/a / 0 |
| Communication | n/a / 0 | n/a / 0 | n/a / 0 |
| Int. functioning | 7.0 / 305,000 | 6.0 / 488,000 | **10.5 / 60,000** |

> **★★★★ 判据：壶 E 的灵巧需求分数更低（3.0 < 5.5），排除人数却更多（2,727,000 > 2,105,000）。**
> 为什么？因为分数越低 = 要求越宽松？**不 —— 分数越低在七轴体系里意味着"需求越低"？**
> **必须查清方向：** 原书 p435 明确 `ranging from 0 (fully able) through 0.5 (minimal impairment) to 13 (most severe impairment)`，所以**分数是"需要多大的能力才能用"，分数越高 = 对用户能力要求越高 = 排除越多**。
> 那么壶 E 的 dexterity 3.0 却排除 272 万人，与壶 D 的 5.5 排除 210 万人 —— **方向相反，说明这里存在需要谨慎解读的地方。**

> **★★★ 判据（必须在正文标出的一处不确定）：壶 E 灵巧需求 3.0 但排除人数更多，与"分数越高排除越多"的方向不一致。**
> 原书未解释。可能解释有二：① DFS 分布在该分数段人数极密集（低分区间人口基数大）；② 表格列对齐在 OCR 中错位。
> **本技能不猜测。** 使用该表时**逐格回查原文 p442**，并注意：**实际工程含义是"排除人数由需求分数 + 该分数段人口密度共同决定"，不是单调关系。**

> **原文（Clarkson p441）**：
> 「**The novel kettle design (F) is a new solution that arose from the design team working with disabled users. The designers identified problems from normal kettle usage and picked out key priorities for designing an inclusive kettle, namely: Safety (heat of unit/boiling water) Filling (spout size/ location, water level, lid remove and replace) Pouring (seeing cup/tipping; weight, secure grip/low strength) Lifting (weight, accurate water level) Base (stability I cable management) • Stigmatising (not for 'the disabled')**」

（该段自 p441 起、至 p442 止于分页处。）

> **★★★★ 判据：F 壶的六条设计优先级里，第六条是"不显得是为'残疾人'做的"—— 社会可接受性被列为一级设计输入。**
> 这条与第 3 章"被看见使用"、第 1 章 Simply 的 Suitable Aesthetic 是同一判断的第三次出现，说明它不是附带意见，是原书的稳定立场。
> **F 壶最终方案**：`an aesthetically pleasing, light-weighted, 'no- pour' kettle with a cool wall, audio alert, auto-retractable cable, and a water level indicator with Braille`（p442）。

### 4.4.4 数字电视机顶盒（含市场规模的四类方案）

> **原文（Coleman p195）**：
> 「**An assessment of current equipment undertaken for the UK Department of Trade and Industry**」

> **原文（Coleman p196）**：
> 「**(DTI, 2003) suggests that two million people in Great Britain (4.4 per cent of those able to access analogue television) could be excluded from viewing the new digital services using digital television set-top boxes.**」

（该句跨 p195–p196；此处按页分两段引用，不改字。）

> **原文（Coleman p196）**：
> 「**A further 700,000 people (1.6 per cent of those able to access analogue television) would be excluded from using advanced features such as digital text and interactive services.**」

> **原文（Coleman p196）**：
> 「**This problem is compounded by the fact that providers of different parts of the system (television, set-top box, interactive television services and digital teletext) all use different interaction approaches.**」

> **原文（Coleman p196）**：
> 「**The results of the analysis may be summarised as follows (Figure 11.14) for households in the UK:** … **a) 1.2 million households contain someone with severe sensory, cognitive or motion capability loss;** … **b) 3.5 million households contain someone with mild sensory, cognitive or motion capability loss;** … **c) 6.2 million able-bodied households contain someone who has a fear of or unfamiliarity with technology.**」

> **原文（Coleman p196–p197）**：
> 「**Consequently, it is estimated that: 2.0 million households contain someone who will be excluded from using current DTV equipment (including all those in group (a) above and 0.8 million from group (b));** … **8.9 million households contain someone who may have difﬁ culty using current DTV equipment (including 2.7 million from group (b) above and all those in group (c)).**」

> **原文（Coleman p197）**：
> 「**a reduced functionality set-top box for those with mild capability 1. loss or technophobia (UK market size = 2.2 million); an ultra-usable fully-featured set-top box for those with mild 2. capability loss or technophobia (UK market size = 5.1 million); an assistive set-top box (with audio description, audio feedback 3. keys, talking electronic programme guide and distinct well-spaced buttons) for those with severe dexterity and visual capability loss (UK market size = 0.6 million); an adapted set-top box (with options such as signing and voice 4. activation) for those with other severe and multiple capability losses (UK market size = 0.3 million).**」

（原文在每条选项首字母后夹排了序号 `1.`–`4.`，此处照录。）

**这是全书唯一一份"排除率 → 产品分档 → 市场规模"的完整链条：**

| 分组 | 户数 | 说明 |
|---|---|---|
| (a) 重度感官/认知/机动受损 | 1.2 M | 需 assistive / adapted |
| (b) 轻度受损 | 3.5 M | 需 reduced-functionality / ultra-usable |
| (c) 健全但对技术恐惧/不熟 | 6.2 M | **非能力问题，是经验/态度问题** |

| 结论 | 户数 |
|---|---|
| 被**排除** | **2.0 M**（含 a 全部 + b 的 0.8 M） |
| 有**困难** | **8.9 M**（含 b 的 2.7 M + c 全部） |

| 产品档 | 目标人群 | 市场规模（UK） |
|---|---|---|
| ① 减功能机顶盒 | 轻度受损 / 技术恐惧 | **2.2 M** |
| ② 超高可用全功能机顶盒 | 轻度受损 / 技术恐惧 | **5.1 M** |
| ③ 辅助型机顶盒（音频描述、语音反馈键、会说话的 EPG、大间距按键） | 重度灵巧+视觉受损 | **0.6 M** |
| ④ 适配型机顶盒（手语、声控） | 其他重度与多重受损 | **0.3 M** |

> **★★★★ 判据：这是一份"排除率如何直接变成产品线与市场规模"的模板，全书只此一处做到最后一步。**
> 三个关键动作可迁移：
> ① **把"健全但技术恐惧"单独列组（c）** —— 证明"经验/态度"是与能力并列的独立排除源（对应第 3 章"经验测量"）；
> ② **排除与困难分开报（2.0 M vs 8.9 M）** —— 前者是失去，后者是服务成本；
> ③ **每一档配一个明确的人群 + 一个明确的市场规模** —— 让产品经理能直接排优先级。

> **★★★ 判据：③④ 两个"辅助/适配"档的市场规模只有 0.6 M 与 0.3 M，而 ①② 档合计 7.3 M。**
> 这就是第 3 章"user-aware design dominates the cube"的商业证据：**主流扩边的市场规模是专用方案的一个数量级以上。**

### 4.4.5 水壶的"理想人口"演算（第 3 章工作定义的实战演示）

> **原文（Coleman p194）**：
> 「**A typical 1.7 litre stainless steel kettle is shown in Figure 11.10. Assuming that the kettle is positioned to suit the height and mobility of the user, the basic**」

> **原文（Coleman p195）**：
> 「**actions required are: to pick up the kettle; carry it to the nearby water tap; ﬁ ll the kettle with water; return it to its base; switch it on; and pour the boiling water into a cup. A level of user exclusion can then be calculated by assessing the levels of each of the functional capabilities required to undertake these actions and estimating the number of users unable to meet these demands (Figure 11.11). In Great Britain 5.3 per cent of those over 15 would not be able to use such a kettle.**」

（该段跨 p194–p195；此处按页分两段引用，不改字。）

> **原文（Coleman p195）**：
> 「**One could argue that the predominant purpose of a kettle is to provide hot water for making drinks and, in that context, an ideal kettle might be one that is no more difﬁ cult to use than drinking from a cup. The target population for an ideal kettle could therefore be all those users who can safely drink from a cup full of hot drink.**」

> **原文（Coleman p195）**：
> 「**Further analysis shows that those excluded from this task number less than 500,000 for those over 15 in Great Britain (Figure 11.11). In fact, the results suggest that there are over two million people in Great Britain who can drink from a cup, but are unable to use a typical 1.7 litre metal kettle to boil water.**」

| 口径 | 排除 |
|---|---|
| 典型 1.7 L 不锈钢水壶 | **5.3%**（GB 15+） |
| "像用杯子喝水一样简单"的理想壶（= ideal population 边界） | **< 500,000 人** |
| **差距：能用杯喝水但用不了壶** | **> 2,000,000 人** |

> **★★★★ 判据：`over two million people ... can drink from a cup, but are unable to use a typical 1.7 litre metal kettle` —— 这是全书最有说服力的一句话，因为它把"设计性排除"直接量化成了 200 万人。**
> 逻辑链完全符合第 3 章的工作定义：
> ① 用杯喝热饮是**需求**（不可再简化）→ 这 500,000 人是**需求性排除**，可辩护；
> ② 但这 200 万人身体健康到能用杯喝热饮，却用不了壶 → 这是**设计性排除**，不可辩护。
> **这个演算方法是本章最值得照搬的：先找一个"不可再简化的同类动作"作为理想下界，再算实际产品与该下界的差。**

---

## 4.5 身体属性那一半：尺寸/力要怎么算

### 4.5.1 第 5–95 百分位的默认代价

> **原文（Clarkson p442）**：
> 「**For example, the clearance between the handle and the switch (l8mm) for kettle E (Figure 2 5. 1 1) is bigger than the male 95th percentile (16.6mm for the UK population and 16.7mm for the US population (see Figure 2 5 .1 2).**」

> **原文（Clarkson p442）**：
> 「**Since designers usually adopt ergonomic data for the 5th to 95th percentile range of users, it can be assumed that the remaining 1 0% of users may be excluded, which in the UK corresponds to 4 600 000 adults. One might also argue that, for a complex design that requires contact with different parts of the body, and hence with several different body dimensions, a different 1 0% may be excluded each time.**」

> **原文（Clarkson p442）**：
> 「**However, making things easier and more comfortable for users certainly needs reconsideration. Currently users need to exert a lot**」

> **★★★★ 判据（本技能最重要的一个数字）：默认的 P5–P95 设计，等于**主动排除 460 万英国成年人**（10%）。**
> 原书还补了一句更狠的：复杂产品涉及多个身体尺寸时，**每一个尺寸各排除一次 10%**，且这些人很可能不同。
> **这是 `ergonomics-ding-yulan` 与本技能最直接的交汇点**：
> - 丁玉兰给"II 型产品尺寸取下限 / III 型取 P5–P95"的规则与满足度算法；
> - 本技能给"取 P5–P95 这个选择本身要付多少人的代价"。
> **合用结论：百分位区间的选择必须连同"被排除人数"一起签字，不能只写"按 P5–P95 设计"。**

### 4.5.2 尺寸数据表（可核对的原始数值）

> **原文（Clarkson p442）**：
> 「**Country Sex Mean Stho/oile 95th%ile (mm) (mm) (mm) UK m 14.5 12.5 16.6 13.0 10.9 15.1 USA M 14.6 12.5 16.7 13.0 10.7 15.3**」

**图注还原（图 25.12）**「The ergonomic reference thickness of the tip of the index finger」：

| 国家 | 性别 | 均值 (mm) | P5 (mm) | P95 (mm) |
|---|---|---|---|---|
| UK | 男 | 14.5 | 12.5 | **16.6** |
| UK | 女 | 13.0 | 10.9 | 15.1 |
| USA | 男 | 14.6 | 12.5 | **16.7** |
| USA | 女 | 13.0 | 10.7 | 15.3 |

> **★★★ 判据：这组数据的真正用途是"做设计判据的基准"。**
> 壶 E 的开关间隙 18 mm > UK 男性 P95 的 16.6 mm，因此**在指厚这一项上未排除任何男性**（原书称 `An effective design`）。
> **可迁移判据形式：** "凡是需要把手指伸进去操作的间隙/凹槽/拉手内空，其最小值应 ≥ 目标人群 P95 指厚"。这是把人体测量直接变成几何约束的写法。

### 4.5.3 尺寸与力的分工（与能力评估的边界）

> **原文（Clarkson p436）**：
> 「**As a branch of ergonomics, anthropometries deals with body measurements, particularly those of size, reach and strength, which are related to physical attributes of the user.**」

> **★★★ 判据：能力评估负责"能不能感知/理解/施力"，尺寸评估负责"够不够得到/塞不塞得进"。二者不可互相替代。**
> 一个身高 1.5 m 的用户在"vision 4.5"上可能完全合格（能力够），但够不到 1.8 m 高的货架（尺寸不够）—— 后者必须靠 Step 3。

---

## 4.6 多重计数：气泡图与耦合区

### 4.6.1 为什么必须去重：同一批人被数了两次

> **原文（Clarkson p443）**：
> 「**As mentioned before, an individual may exhibit more than one loss of capability or be affected by more than one physical attribute. Older users typically experience multiple minor capability losses when ageing, and many disabilities are accompanied by other losses of capability, mainly due to disease. For example, cataracts and glaucoma can cause problems with mobility, posture, co-ordination, sensory input, balance, location of body in space, vision and speech (Kraemer, 1997).**」

> **原文（Clarkson p443）**：
> 「**Noticeable coupling is found between the loss of motion capability and sensory capability (Figure 2 5. 14), and the loss of motion capability and cognition capability (Figure 2 5. 1 5). In Figures 2 5.14 and 25.1 5, the area of each circle represents the relative number of individuals exhibiting a particular combination of disabilities. Bubbles lying on the axes represent users with only one loss of capability, whilst the remaining bubbles in the plot show combined losses of capability. The nearer the bubbles are to the origin, the less severe the impairments they represent.**」

**图注还原：**

- **图 25.14（Clarkson p443）**「Multiple counting：Sensory and motion capabilities」——双轴气泡图；**在轴上的气泡 = 单轴受损**，**离轴气泡 = 组合受损**，**越靠近原点越轻**。
- **图 25.15（Clarkson p443）**「Multiple counting：Motion and cognition capabilities」——同结构。
- **图 25.16（Clarkson p444）**「Multilple counting：Design exclusion with kettles E and F」——坐标 `Dexterity Capability` × 视觉/感官轴；标出 `Kettle E`、`Kettle F`、`Full Capability`；多边形 **A**（壶 E 的视觉+灵巧排除范围）、**B**（壶 F 的排除范围）。

> **原文（Clarkson p444）**：
> 「**Polygons A and B together illustrate the exclusion for kettle E, for vision and dexterity demands. Polygon B, on its own, illustrates the exclusion for kettle F. Bubbles inside polygon A show the difference between the inclusion/exclusion of kettles E and F, which corresponds to 1,880,000 GB adults.**」

> **★★★★ 判据：壶 E 与壶 F 的差距 = 1,880,000 人，全部落在"视觉×灵巧"的耦合区。**
> 这是全书唯一一处把"耦合造成的排除"精确量化到具体人数的案例。

### 4.6.2 改进优先级的唯一正确算法

> **原文（Clarkson p444）**：
> 「**It is obvious that if kettle E is to be improved to achieve the same level of inclusion as kettle F, both vision and dexterity demand need to be reduced simultaneously. The reduction of vision demand will only include more bubbles hugging the vision axis, but not those in the coupling region. Such information is useful to designers, because when they improve products, it is important to know if the changes proposed will indeed include more users, or whether certain users will still be excluded for some other reason (Clarkson and Keates, 2002).**」

> **★★★★ 判据：若排除集中在两轴耦合区，只降一轴则被排除人数几乎不变 —— 必须同时降两轴。**
> 原文的表述极精确：只降视觉需求，`will only include more bubbles hugging the vision axis, but not those in the coupling region`。
> **这是"改进优先级"最容易被搞错的地方。** 常见的错误做法是"按单轴排除人数从大到小排序，先改最大的那个" —— 在耦合情形下这是无效的。

> **原文（Clarkson p445）**：
> 「**Solutions concentrating on improving the accommodation of individual capabilities are of limited effectiveness for including users with inter-related multiple capability losses. The coupling pattern reflected by the bubble diagrams not only indicates the significance of multiple capability losses, but also shows the scope for possible improvements.**」

> **原文（Clarkson p445）**：
> 「**For example: if the coupling is not significant, an improvement can be made by addressing each axis. Equally if the coupling is significant, then both axes must be addressed simultaneously for improvement to be achieved. Such information is useful for decision-making, since design managers and executives can thus determine optimal solutions**」

> **原文（Clarkson p446）**：
> 「**that are promising for including more users while remaining cost- effective.**」

| 耦合强度 | 正确改法 |
|---|---|
| **弱耦合** | 逐轴改，单轴独立生效 |
| **强耦合** | **必须同时改两轴**，否则无效 |

> **★★★ 判据（决策规则）：先看耦合强度，再决定"分轴改"还是"联合改"。**
> 这是把"耦合"从一个概念变成一条可执行分支的唯一地方。

### 4.6.3 本章的自评与局限（原书自己说的）

> **原文（Clarkson p446）**：
> 「**Unlike most design for all approaches, this approach has incorporated a user capability range that does not configure an 'average user', and takes account of multiple combinations of impairments rather than focused on accommodating the individual capability losses.**」

> **原文（Clarkson p445）**：
> 「**The investigation of design exclusion provides valuable information for inclusive design. The survey of product exclusion demonstrates explicitly that many consumer products exclude people with moderate (score 5-6) or severe impairments (score 7-8).**」

> **★★★ 判据：多数消费品的排除集中在"中度（5–6 分）到重度（7–8 分）"这一段。**
> 这再次印证第 2 章的判断：**塔身（中度）是被漏掉的最大层。**

> **原文（Clarkson p446）**：
> 「**Inclusive design will only be encouraged when managers and designers are able to see more clearly the impact that their specification and design decisions have on the usability of their products (Clarkson and Keates, 2002; Keates and Clarkson, 2002). Investigation of the causes and levels of design exclusion provides such insight.**」

---

## 4.7 评估方法在产品流程中的位置（Coleman ch12）

> **原文（Coleman p203）**：
> 「**Evaluation plays a key role in the product introduction process, marking the transition between the major stages in the development and delivery of a new product. The initial 'need' is likely to be evaluated before funding is committed to conceptual design; the product 'concept' will be evaluated before funding is released for detailed design; and so on. This 'stage-gate' approach, as illustrated in Figure 12.1, is widely used in industry.**」

> **原文（Coleman p203）**：
> 「**However, this is not always the case. All too often the majority of the evaluation effort is focused on ensuring that a product meets its speciﬁ cation rather than checking that the speciﬁ cation is right in the ﬁ rst place.**」

> **★★★★ 判据：`checking that the speciﬁ cation is right in the first place` —— 绝大多数评估花在"是否达成规格"，而不是"规格是否正确"。**
> 这是第 3 章"包容度有两个自变量"在流程层面的同一判断。**一条评估制度上的判据：评估预算必须有一部分明确分配给"规格本身的评审"。**

> **原文（Coleman p203）**：
> 「**Evaluation is particularly important in the inclusive design process where design decisions at all stages of the design process have the potential to exclude users. Inappropriate product requirements can exclude users; a poor concept can exclude users; detail design decisions can exclude users; inadequate testing can exclude users; and poor delivery, through packaging and instructions, can exclude users. This is a cumulative process, where users excluded by a poor concept are unlikely to be included by good detailed design.**」

> **★★★★ 判据：排除是累积的 —— 被差概念排除的用户，不会因为细节设计好而被纳入。**
> 这决定了评估必须**前移**：概念阶段就要做排除估算，而不是等样机。

### 4.7.1 八种评估方法及其定位

> **原文（Coleman p204）**：
> 「**The following sections discuss a variety of approaches to evaluation in inclusive design, including the use of:** … **guidance for inclusive design: mechanisms for exclusion and • general approaches to product improvement**」

> **原文（Coleman p204）**：
> 「**exclusion audit: detailed task-based analysis to identify speciﬁ c • reasons for user exclusion or difﬁ culty**」

> **原文（Coleman p204）**：
> 「**an integrated approach: using more than one of the above methods • to audit products.**」

（原书此处在列举项中间夹排了项目符号 `•`；上列三段按原文照录，**不删改符号位置**。）

| 方法 | 做什么 | 何时用 | 成本 |
|---|---|---|---|
| **Guidance** | 提供动机、数据、流程指引 | 全程 | 低 |
| **Life cycle analysis** | 从买到弃全周期找排除 | 早期 | 中 |
| **Expert appraisal** | 专家逐特征+任务评审 | 出厂前，也可任意阶段 | 中 |
| **Capability loss simulators** | 戴模拟器亲身体验 | 有 3D 模型/样机时 | 低 |
| **Exclusion audit** | 任务分解 + 量化排除 | 早（竞品）/ 晚（样机） | 中高 |
| **User trials** | 真实用户测试 | 里程碑 | 高 |
| **Integrated approach** | 多方法组合 | 全程 | 高 |

> **★★★ 判据：八种方法不是"选最好的一个"，而是按阶段与成本搭配 —— 原书明确说 `using more than one of the above methods`。**
> 原书还给了推荐搭配（Coleman p213）：`an exclusion audit can provide valuable input into the business case for a new product, extreme users can inspire creativity during concept generation, while user trials with boundary users can conﬁrm that design targets have been met`。

### 4.7.2 三类用户的用法（本章最重要的实操分配）

> **原文（Coleman p213）**：
> 「**Extreme • users, that is those with pronounced capability loss, are valuable early in the development process to inspire creative thinking by asking questions such as 'how can a blind user use this device?' and through demonstrating coping strategies necessarily adopted for existing products; Boundary • users, that is those with moderate capability loss and on the edge of being able to use a product, can most easily identify points of difﬁ culty and exclusion in existing and proposed products. Able-bodied • users, that is those with limited or no capability loss, represent the users for whom most products have been designed and are able to provide feedback about product usability at all stages of the design process.**」

（原文在每类用户名称后夹排了项目符号 `•`，此处照录。）

> **原文（Coleman p213）**：
> 「**In practice, all three user types can provide valuable insights into understanding user needs and preferences, while a mix of boundary and able-bodied users is particularly well suited to evaluating existing and proposed products.**」

| 用户类型 | 能力位置 | 用在哪个阶段 | 为什么是他们 |
|---|---|---|---|
| **Extreme users** | 严重受损（金字塔尖） | **概念期（早期）** | 逼出创造性提问、示范已存在的应对策略 |
| **Boundary users** | 中度受损（**正卡在能不能用的边缘**） | **评估期（中后期）** | 最容易识别"难点与排除点" |
| **Able-bodied users** | 无/轻微受损 | 全程 | 代表既有设计对象，反馈基线可用性 |

> **★★★★ 判据：`boundary users` 是本章最有价值的一个用户定义 —— "正卡在边缘"的人比"严重的"和"健全的"都更能定位排除点。**
> 理由很硬：严重受损者早已发展出替代策略，反而说不清"哪里卡住"；健全者根本碰不到边界。**只有刚好在边缘的人能准确报告"就差这一点"。**
> **这条直接把第 2 章的能力谱变成了一个可执行的招募标准：招募时按"能力分数接近产品需求分数"筛人。**

### 4.7.3 排除审计（exclusion audit）的定义

> **原文（Coleman p211）**：
> 「**An exclusion audit is used to estimate quantitative measures of design exclusion, indicating how many people can use a product and how many are excluded from its use. It is based on the premise that activities lead to demands on the user, and that these demands are to be met by the users' capabilities. Exclusion then arises if, in a given situation, the users' capabilities are insufﬁ cient to meet the demands for the particular activity.**」

> **原文（Coleman p211）**：
> 「**By mapping product demand to national scales, it is possible to estimate how many people are likely to be excluded from using the product on the basis of each demand. These ﬁ gures can be broken down to identify speciﬁ c causes of exclusion, and their relationship to particular capabilities, or amalgamated to obtain an overall ﬁ gure. The ﬁ gures for each capability can also be compared to each other to determine which areas give rise to the highest levels of exclusion or show the most potential for improving the product's inclusivity.**」

> **原文（Coleman p211）**：
> 「**For example, an exclusion audit may identify that a small decrease in visual demand would include a large number of additional people, while a similar decrease in dexterity demand would only include a few more.**」

> **★★★★ 判据：排除审计的核心产出不是"总排除率"，而是"每降低一档需求能换回多少人"（边际收益）。**
> 上面的例子给出了完整的决策形态：**同样降低 1 分需求，视觉轴可能换回很多人，灵巧轴可能只换回几个** —— 这才是资源该往哪投的依据。
> **这条与 §4.6.2 的耦合判据合起来，构成完整的优先算法：先看耦合（决定"要不要联合改"），再看边际收益（决定"先改哪一轴"）。**

> **原文（Coleman p212）**：
> 「**Exclusion audits enable the comparison of existing products and new design prototypes. They can be used early on to compare competitive products and to identify elements to focus on in the redesign of an existing product.**」

---

## 4.8 本章概念-论点表（共 17 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | **两条桥** | 「the direct link (dashed line) between the two cannot be found from existing data」 | 图 25.1 | 产品特征→人必须分两路（能力/尺寸），因此必须算两次再去重。这是四步法的存在理由 | Clarkson p435 |
| 2 | **数据口径必须同引** | 「the discrepancies are due to the differences of descriptions of mild, moderate and severe deafness」 | RNID 57.9% vs DFS 9.7% | 同一"中度耳损"两套官方数据差 6 倍。"排除率 X%"必须连口径一起写 | Clarkson p381 |
| 3 | **经验也是能力** | 「experiential measures (for example prior use of computers)」 | DTV 组 (c) 620 万户 | 技术恐惧是独立排除源，与能力并列。不能只当"能力问题"处理 | Coleman p187 |
| 4 | **Step 2 要报两个数** | 「The number of users disadvantaged, but not excluded ... should also be identified」 | — | 只报排除会重复第 3 章"困难不算问题"的错误 | Clarkson p436 |
| 5 | **主观类比** | 「It is assumed that the required capability of squeezing water from a sponge (score 8.0) is comparable to pressing buttons」 | Acoustiguide 按键 | 量表无对应描述时，找一个已标定动作做锚点。这是最可复制的评分技巧 | Clarkson p437 |
| 6 | **每分必带 justification** | 「Justification」列逐条给出锚点或补充规则 | 七轴评估表 | 无 justification 的分数不可复核；补充规则（如"需扶物平衡者记 7.0"）是隐性知识的显性化 | Clarkson p438 |
| 7 | **一份评估 30 分钟** | 「Duration of assessment: 30 minutes」 | Acoustiguide | 全书唯一的时间成本数据。决定了这套方法能否塞进真实项目 | Clarkson p438 |
| 8 | **七轴人数不可相加** | 「the total exclusion will not be the sum of the exclusion totals」 | Acoustiguide（相加 254.6 万，实际远小） | 相加会严重高估。这防止"能力 8%+尺寸 10%=18%"这类错误 | Clarkson p439 |
| 9 | **跨数据集去重可能做不到** | 「this can be difficult, if not impossible」 | — | 只用同数据集内去重；跨集合结果须标注"含未消除重复" | Clarkson p437 |
| 10 | **水壶代际悖论** | 「no sooner is one problem resolved ... than another is introduced」 | 壶 A→F 六代 | 每代技术解决一个问题、引入一个新需求。技术乐观主义最硬的反证 | Clarkson p445、p440 |
| 11 | **五折六优先** | 「Stigmatising (not for 'the disabled')」列为一级设计输入 | 壶 F | 社会可接受性不是附带意见，是设计输入（第三次独立出现） | Clarkson p442 |
| 12 | **理想下界演算** | 「over two million people ... can drink from a cup, but are unable to use a typical 1.7 litre metal kettle」 | 壶 5.3% vs 理想 <500,000 | **先找"不可再简化的同类动作"作理想下界，再算实际产品与该下界之差。** 本技能最值得照搬的演算方法 | Coleman p195 |
| 13 | **P5–P95 = 排除 460 万** | 「the remaining 1 0% of users may be excluded, which in the UK corresponds to 4 600 000 adults」 | — | 默认百分位区间是一个要付人数代价的决定；多尺寸产品每个尺寸各排 10% | Clarkson p442 |
| 14 | **尺寸判据写法** | 间隙 18 mm > 男性 P95 16.6 mm 即"有效设计" | 壶 E 开关间隙 | 可迁移："手指伸入的间隙最小值 ≥ 目标人群 P95 指厚" | Clarkson p442 |
| 15 | **耦合区必须联合改** | 「The reduction of vision demand will only include more bubbles hugging the vision axis, but not those in the coupling region」 | 壶 E vs F（188 万人） | 耦合强则单轴改进几乎无效。先把耦合强度做出来，再决定分轴改还是联合改 | Clarkson p444 |
| 16 | **边际收益才是优先级** | 「a small decrease in visual demand would include a large number of additional people, while a similar decrease in dexterity demand would only include a few more」 | 排除审计 | 排序依据不是"当前哪轴人数多"，而是"每降一档换回多少人" | Coleman p211 |
| 17 | **boundary users 的独特价值** | 「those with moderate capability loss and on the edge of being able to use a product, can most easily identify points of difﬁ culty」 | — | 严重者已发展替代策略、健全者碰不到边界；只有边缘者能说清"就差一点"。招募标准 = 能力分数接近产品需求分数 | Coleman p213 |
| 18 | **评估前移且累积** | 「users excluded by a poor concept are unlikely to be included by good detailed design」 | — | 排除不可逆。概念期就要估算，不能等样机 | Coleman p203 |
| 19 | **评估规格本身** | 「all too often the majority of the evaluation effort is focused on ensuring that a product meets its speciﬁ cation rather than checking that the speciﬁ cation is right in the ﬁ rst place」 | — | 评估预算须有一部分明确用于"规格评审"，否则只会验证一个错的目标 | Coleman p203 |
| 20 | **分档 → 市场规模** | 「a reduced functionality set-top box ... (UK market size = 2.2 million)」 | DTV 四档方案 | 排除率→人群分组→产品分档→市场规模，全书唯一走完全链的地方 | Coleman p197 |
| 21 | **主流扩边 > 专用方案** | ①② 档 7.3 M vs ③④ 档 0.9 M | DTV | user-aware 主导立方体的商业证据：主流扩边的市场是一个数量级以上 | Coleman p197 |

---

## 4.9 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **水壶 D/E/F 排除表的方向性矛盾** | **原书未解释**。壶 E 的 dexterity 需求（3.0）低于壶 D（5.5），排除人数却更多（2,727,000 > 2,105,000）。可能是低分区间人口密度更大，也可能是 OCR 列错位。**已在正文 §4.4.3 明写，不猜测** | 需回查 Springer 原书 p431 印刷版表格；本技能不提供结论 |
| **日常家电排除率与具体产品的逐一对应** | **读不出**。图 25.6 在 OCR 中产品名与百分比已错位，只能确认四档百分比 1%/2%/4%/6% 与六个产品名，**对应关系不做猜测** | 原书 Figure 25.6 印刷版 |
| **七轴之外第 8–13 轴的定义** | **未展开**。DFS  recognise 13 类，原书只列 7 类用于产品评估，未给其余 6 类（personal care、continence、behaviour、consciousness、eating/drinking/digestion、disfigurement）的逐级描述 | Martin et al. (1988) OPCS 原始报告 |
| **认知轴的可操作量表** | **无**（同 ch02）。Cognitive 由 communication + intellectual 合成，但没有类似 H1–H8 的逐级行为描述 | 需结合 WHO ICF 与认知评估工具 |
| **排除率的置信区间与抽样误差** | **完全没有**。全书只给点估计（如"5.3%"），未给误差范围或方法学说明 | DFS 原始报告 |
| **中国人口基数下的任何换算** | **无**。全部为 GB 数据 | 中国残联统计、《中国残疾人事业统计年鉴》、CHARLS |
| **HADRIAN / 后续排除计算器** | **0 命中**。两书均无该工具。原书仅提到工具"正在开发中"（Clarkson p461） | HADRIAN 是后续成果，不在本书范围；本技能不覆盖 |
| **模拟器的标定数值** | 详见 ch07。本章未涉及 | 见 ch07 §7.3 |
| **2010 年后的标准与方法**（ISO 9241-171、EN 17161） | **不在源书范围** | 标准原文 |

---

## 4.10 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 七轴分数与严重度 | **ch02 §2.1、§2.4** | 本章全部计算的输入 |
| 最差三项加权（worst+0.4+0.3） | **ch02 §2.4** | 三轴合并的算式（本章 p437 复述） |
| WINIT 与五比值 | **ch03 §3.4** | 排除率的分子分母定义 |
| 工作定义（只排需求排除的人） | **ch03 §3.2** | 本章 §4.4.5 水壶演算的判定标准 |
| 需求性排除是管理决策 | **ch03 §3.3** | 本章 §4.5.1 的 460 万人须提交决策层 |
| 三类设计策略 | **ch03 §3.5** | 本章 §4.4.4 四档机顶盒是三种策略的商业实例 |
| P5–P95 的代价 | **ch02 §2.8.1** | 与 `ergonomics-ding-yulan` 的接口本章数值化 |
| boundary / extreme users | **ch08 §8.1、§8.2** | 本章 §4.7.2 给分配，ch08 给具体共情方法 |
| 模拟器 | **ch07** | 本章 §4.7.1 列为八法之一，ch07 展开 |
| 专家评审 | **ch06 §6.3** | 本章 §4.3 的评估表即 expert appraisal 的量化形式 |
| 生命周期分析 | **ch06 §6.2** | 本章 §4.7.1 提及，ch06 展开 |
| 分档与市场规模 | **ch10 §10.4** | 与 OXO / Selectronic 的商业案例并列，构成商业论证的两条路径 |

### 4.10.1 跨技能挂钩（本机已有技能）

| 本技能内容 | 挂钩技能 | 关系与用法 |
|---|---|---|
| **P5–P95 默认排除 460 万（Clarkson p442）** | **`ergonomics-ding-yulan`** | **本技能与丁玉兰最硬的一处接口。** 丁玉兰讲"III 型产品取 P5–P95、满足度 = 90%"；本技能讲"这 10% 是 460 万英国人，且多尺寸产品每个尺寸各排 10%"。<br>**合用判据：任何写"按 P5–P95 设计"的地方，旁边必须写出被排除人数，并由能改需求的人签字。** |
| **尺寸判据写法（间隙 ≥ P95 指厚，Clarkson p442）** | **`ergonomics-ding-yulan`** | 丁玉兰提供人体尺寸表与产品尺寸分类；本技能提供"如何把尺寸变成一条可判定的几何约束"的句式。二者合起来即可写出可执行的图纸标注。 |
| **"主观类比"评分（挤海绵 ≈ 按按钮，8.0）** | **`ergonomics-ding-yulan`** | 丁玉兰的施力特征章节有大量"日常动作的力量量级"。本技能的类比法需要这些量级作锚点 —— **丁玉兰提供锚点库，本技能提供类比规则。** |
| **四步法 Step 1「使用动作序列」** | **`user-research-methods`** | 本技能的 Step 1 要求写出动作序列，其方法论本质是**任务分析（task analysis）**。`user-research-methods` 里有 HTA、认知走查、任务分析的标准做法；本技能给"任务分析之后怎么换算成人数"。<br>**合用顺序：用 user-research-methods 做任务分解 → 用本技能给每步打七轴分数并换算排除率。** |
| **boundary users 招募标准（能力分数接近产品需求分数）** | **`user-research-methods`** | 后者给招募、样本量、访谈提纲的完整流程；本技能给"该招什么样的人"的能力判据（不是人口学判据）。<br>**合用判据：招募表里用七轴分数筛人，而不是用年龄/诊断筛人。** |
| **耦合区与"必须联合改"** | **`design-psychology-norman`** | 诺曼的七阶段能解释"为什么视觉与灵巧会耦合失效"（例如：看不清 → 无法判断该用多大力）。本技能给"耦合造成多少人被排除"的量化。<br>**合用：诺曼解释机制，本技能决定要不要联合改。** |
| **评估前移（概念期就估排除）** | **`design-methodology-liuguanzong`** | 柳冠中的"设计思维六步法"含"评价"环节与"外部因素/内部因素"分析，本质上是"在概念期把约束想清"。本技能给该环节一个可量化的输出。<br>**合用：柳冠中的外部因素分析 → 本技能的能力需求打分 → 概念期排除率。** |
| **排除率 → 分档 → 市场规模** | **`product-structure-liubaoshun`** | 分档策略（如"大间距按键版"）一旦确定，就要落到结构与模具（按键间距、行程、力）。本技能给"市场有多大"，刘宝顺给"结构怎么做出来"。<br>**合用顺序：本技能定分档与规模 → 刘宝顺做结构与工艺可行性。** |
