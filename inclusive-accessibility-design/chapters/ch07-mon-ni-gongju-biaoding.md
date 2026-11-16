# 第 7 章：模拟工具——能力损失模拟器的做法、标定与边界

> **原书 PDF 页序 p218–p231（14 页，Coleman 第 13 章）＋ p209–p211（3 页，Coleman 第 12 章）｜本版逐页读完全部 17 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）
>
> **读法说明**：按 Coleman ch13 的 `Simulation: Background（含义辨析） → Simple simulators → Sophisticated simulators → Limitations of the simulation tools → A Calibrated Simulation Toolkit → Description of the toolkit（视觉/听觉/行走/伸手/灵巧） → Testing the toolkit → Overview of results → Simulation as a Supplementary Assessment Tool → Simulating the 'Right' Capability Losses → Summary` 逐节展开，不跳节。
> 每节含【原文摘录】+【判据提炼】。

---

## 7.0 总纲：模拟是"量具"，不是"体验玩具"

> **原文（Coleman p219）**：
> 「**Simulation, as discussed here, involves a person (usually able-bodied) wearing physical restrainers to feel the effects of different types of capability loss.**」

> **原文（Coleman p219）**：
> 「**Ultimately, the aim is to show how everyday products often 'disregard' (and hence disable) a large number of users, due to a lack of consideration of their capacities.**」

**本章的四个产出：**

| 产出 | 内容 | 页码 |
|---|---|---|
| **① 概念澄清** | 模拟的是"能力损失"，不是"损伤"；disorder / impairment / disability 三层区分 | p219 |
| **② 工具清单** | 五类模拟器：视觉（9 副眼镜）、听觉、行走、伸手、灵巧 | p223–p226 |
| **③ 标定问题** | 为什么"感觉更强烈"≠"问题更严重"；为什么无法精确标定 | p222 |
| **④ 使用纪律** | 只作补充手段，不可替代自省与用户试验 | p221、p228、p229 |

> **★★★★ 判据（本章核心）：模拟器的正确定位是"标尺（scale/ruler）"，其可信度完全取决于**标定**。**
> 未标定的模拟器给出的是"设计者自己的体感强度"，而**体感强度与受影响人数无关** —— 这是本章最容易犯、后果最严重的错误（详见 §7.4）。

---

## 7.1 概念澄清：模拟的是能力，不是损伤

这是全书概念最严谨的一节。原书把三个常被混用的词拆开：

> **原文（Coleman p219）**：
> 「**At this stage, it is important to clarify why this chapter talks about simulating functional capability loss and not simulating impairments. Within the context of inclusive design, a disorder is a medical condition such as osteoarthritis, which can affect several different joints in the body (for instance, hands, knees and hips). This disorder may cause an impairment that describes how particular body parts are affected due to the effects of the condition, such as osteoarthritis causing bone cartilage to become pitted, rough and brittle resulting in pain and stiffness of the joints. These symptoms of impairment may affect a person's functional capabilities, for instance limiting the hand's or arm's freedom of movement and/ or strength.**」

**三层链（原书定义）：**

| 层 | 术语 | 定义 | 例子 |
|---|---|---|---|
| **①** | **Disorder**（疾患） | 医学状况本身 | 骨关节炎（osteoarthritis） |
| **②** | **Impairment**（损伤） | 身体部位受该状况影响的方式 | 软骨变得坑洼、粗糙、脆弱 → 疼痛与僵硬 |
| **③** | **Functional capability loss**（功能能力损失） | 损伤导致的能力受限 | 手/臂活动范围与力量受限 |

> **原文（Coleman p219）**：
> 「**Disability, which is caused by products and surroundings, occurs when the capabilities required to use a product or service surpass those of the user.**」

| **④** | **Disability**（失能） | **由产品与环境造成**：产品所需能力超过用户能力 | 拧不动那个太紧的旋钮 |

> **★★★★ 判据：`Disability, which is caused by products and surroundings` —— 失能的责任被明确划到产品与环境一侧。**
> 这是第 1 章 `disabled by design` 的术语级重述，也是本章选择"模拟能力损失而非模拟损伤"的根本理由：
> **因为可设计的是能力需求，不是疾患。**

> **原文（Coleman p219）**：
> 「**Simulation involves reducing the wearers' sensory and motor functional capabilities. The aim is to alter the wearers' experience of their environment by imposing sensory and/or motor capability losses upon them.**」

> **★★★ 判据：模拟的操作定义是"降低穿戴者的感官与运动功能能力"—— 即在第③层动手术，不碰第①②层。**
> 这一条决定了模拟器的合法边界：**它只能模拟"能力受限"，不能模拟"疼痛""疲劳的持续性""社会污名"**（后文 §7.5 会逐条说明为什么）。

---

## 7.2 简易模拟器：几乎零成本的那一档

> **原文（Coleman p219）**：
> 「**One of the ﬁ rst capability loss simulations took place in the early 1980s and involved a group of architects wearing spectacles that reduced their visual capabilities, while carrying out several tasks in everyday environments.**」

> **原文（Coleman p219–p220）**：
> 「**The students tried to simulate, for instance, the effects of arthritic ﬁ ngers by afﬁ xing buttons with tape on the knuckles of each ﬁ nger. Visual capability loss was simulated by wearing blindfolds and fogged spectacles. Also, some experiments have been carried out involving students dressed** … **up with ice hockey equipment, to simulate motor losses, such as difﬁ culties reaching for and manipulating objects.**」

> **原文（Coleman p220）**：
> 「**Other interesting exercises include, for instance, breathing through a straw while climbing stairs to simulate fatigue related problems. Some people also suggest putting dried beans inside the shoes to simulate the effects of gout and, ultimately, affecting the ability to walk and keep balance.**」

| 要模拟什么 | 简易做法（原文） | 成本 |
|---|---|---|
| 手指关节炎 | **在每个指关节上用胶带粘纽扣** | 极低 |
| 视觉能力损失 | 眼罩、起雾的眼镜 | 极低 |
| 运动能力损失（伸手/操作） | 穿冰球护具 | 低 |
| 疲劳 | **爬楼梯时用吸管呼吸** | 极低 |
| 痛风 → 行走与平衡 | **鞋里放干豆** | 极低 |

> **原文（Coleman p220）**：
> 「**Despite being low- ﬁ delity tools, these and other simulation approaches are an economical and effective way of raising awareness about the effects of capability loss variation, which a large number of people may exhibit.**」

> **★★★★ 判据：五个几乎零成本的模拟器，已足以完成"意识唤醒"这一步 —— 不必等买套件。**
> 这一条对预算受限的团队极重要：**先做胶带 + 眼罩 + 吸管，就足够让团队第一次真正意识到问题。**

> **★★★ 判据（关键区分）：简易模拟器的用途是 `raising awareness`（唤醒意识），不是"评估"。**
> 原书用词很精确：`an economical and effective way of raising awareness`。
> **用错用途的后果：** 把胶带纽扣模拟当作评估依据，会得出"这个问题不严重"这类错误结论（因为玩家只体验了几分钟，而真实用户是几十年）。

---

## 7.3 复杂模拟器：整套装与它们被指出的缺陷

> **原文（Coleman p220）**：
> 「**More complex simulation apparatus include the Third-Age Suit, developed by Ford Motor Co. and Loughborough University in the UK; and the Age Explorer, developed by Meyer-Hentshel, a consulting ﬁ rm in Germany**」

> **原文（Coleman p220）**：
> 「**Both suits are made of coveralls with components (for instance, elbow and knee braces) sewn on, which attempt to simulate average levels of physical capability loss that older adults (over 60 years) may exhibit. These suits restrict movement in hinge points of the body, such as hands, elbows, knees and neck. Additionally, earmuffs and yellow spectacles try to simulate hearing and visual capability losses, respectively.**」

> **原文（Coleman p220）**：
> 「**The Third-Age Suit has helped Ford's designers to understand and anticipate the special driving requirements of their older customers. This contributed to the commercial success of the Ford Focus, which has been described as easy to use, especially in terms of getting in and out of the car and of operating the driving controls.**」

**Third-Age Suit 的三处硬伤（原书原文指出的）：**

> **原文（Coleman p220）**：
> 「**Despite the usefulness and popularity of these simulation tools, recent studies recognised the limitations of the Third-Age Suit when taking into account the combination of multiple impairments as well as the simulation of different levels of physical capability loss. Consequently, those studies pointed out the need to develop practical simulators, which provided designers with meaningful data, simulated different levels of capability loss and did not restrict design creativity.**」

| # | 缺陷 | 后果 |
|---|---|---|
| **①** | 只模拟**单一平均水平的损伤** | 不能模拟不同严重度 |
| **②** | 难以模拟**多重损伤的组合** | 而多重损伤才是多数（ch02 §2.3.1） |
| **③** | 整件连体衣，**穿上就全套** | 只想测手臂却也得穿全身 → 抑制设计创造力 |

> **★★★★ 判据：整装式模拟器的三重缺陷是"单水平、单损伤、不可分模块"—— 三者合起来使它只能做演示，不能做评估。**
> 第三条（`did not restrict design creativity`）最容易被忽视：**穿全身套会让人处于"我什么都做不了"的状态，从而得出"什么都不改算了"的消极结论。**

---

## 7.4 标定问题：本章最重要的一节

### 7.4.1 案例：洗碗机

这是全书最精彩的一段推理，它精确地暴露了"凭体感排序"的荒谬：

> **原文（Coleman p222）**：
> 「**For instance, while wearing visual and dexterity restrainers to assess the ease of use of a dishwasher, a designer may feel more physically affected by the capability limitations imposed by the visual simulator. This may lead the designer to consider that the visual attributes of the dishwasher (the labelling, colour of different features, and so on) may be a more urgent problem to address, than for example the shape of the door handle, or the ease of turning of different buttons. However, if in the wider population there happen to be more people exhibiting dexterity rather than visual limitations, such an assessment decision may prove inadequate.**」

> **★★★★ 判据：`designers may feel more physically affected` ≠ `the problem is more urgent`。体感强度与受影响人数之间没有必然关系。**
> 洗碗机案例的完整逻辑链：
> ① 视觉模拟器让人**主观上更难受**；
> ② 于是设计者判定"视觉问题是首要问题"；
> ③ 但若人群中灵巧受损者更多，**真正的首要问题应该是灵巧**；
> ④ 因此这个判断是错的 —— **错在把"我难受的程度"当成了"问题的严重程度"。**

> **原文（Coleman p222）**：
> 「**Hence the importance of knowing about the number of people behind each level of calibration of the toolkit. Without this information, and solely based on their own physical perception, designers may overlook such problems.**」

> **★★★★ 判据：优先级只能由"人数的乘积"决定，绝不能由"体感强度"决定。**
> 这是对 ch04 排除率存在理由的最生动论证：**如果没有人口数据，模拟器会系统性地把团队引向错误的首要目标。**

### 7.4.2 为什么无法（当时）精确标定

> **原文（Coleman p222）**：
> 「**In order to achieve this quantiﬁ able calibration, however, it would be necessary to have access to statistical demographic data on how peoples' capabilities vary across the wider population. Such a complete source of information does not presently exist. In fact, data sources comprising information about people with impairments and disabilities vary widely. Also, they are more likely to focus on single capabilities rather than all the necessary human characteristics that should be considered when assessing user-device interaction. Therefore, until a new and thorough population survey on the relevant human characteristics is carried out, it is not feasible to accurately and realistically calibrate a wearable simulation toolkit.**」

> **原文（Coleman p223）**：
> 「**Nevertheless, as an exploratory study, the toolkit presented here was calibrated against an existing population survey of disability carried out in Great Britain** … **Therefore, a series of assumptions had to be made while designing the calibration of the toolkit, inevitably involving some degree of subjectivity.**」

> **★★★★ 判据：原书明确承认标定"不可避免地带有某种程度的主观性"（`some degree of subjectivity`）—— 这是使用时必须知道的。**
> 三个原因：
> ① 没有一份完整的人口能力分布数据；
> ② 现有数据源大多是**单轴**的，而真实交互是多轴的；
> ③ 只能对着"残障水平描述"标定，而描述本身不含能力细节。
> **使用纪律：任何基于模拟器得出的定量结论，都必须标注"标定含主观成分"。**

---

## 7.5 工具包的五类组件（可复制的做法）

> **原文（Coleman p223）**：
> 「**The toolkit presented here is made of modular components, each one addressing the simulation of physical capability loss in different parts of the body. The advantage of using modular components is that the assessors need only put on the parts of the toolkit that will enable them to affect speciﬁ c capabilities. Previous simulation tools (such as the Third Age Suit or the Age Explorer) were generally made of coveralls with restrainers sewn on, making it necessary to put on the whole suit even if the objective was only to simulate, for instance, arm movement limitations.**」

> **★★★ 判据：模块化（而非整装）是这一版工具包的核心改进 —— 只戴需要的那部分。**
> 这直接回应了 §7.3 的缺陷③（抑制创造力）：**只戴一只手套时，设计者还能思考；穿全身套时只能体验绝望。**

> **原文（Coleman p223）**：
> 「**The simulation toolkit presented here is basically divided into the number of capabilities that it tries to impair: vision, hearing, locomotion, reaching and stretching, and dexterity.**」

| # | 能力 | 组件做法（原文 p224–p226） | 关键参数 |
|---|---|---|---|
| **1** | **视觉** | **9 副眼镜**，逐级增加镜片模糊度 | 9 个等级 |
| **2** | **听觉** | 耳罩 + 耳塞（**市面采购**） | 降低可辨声级 |
| **3** | **行走** | 带金属结构的膝部支架（阻碍走路、上台阶、下蹲）+ 插竖向塑料条的大腰带（限制前屈与侧屈） | 塑料条数可调 |
| **4** | **伸手/伸展** | 肘部支架（后侧插塑料条限制前臂屈）+ 与腰带相连的可调肩带 | **可设定双臂具体活动角度** |
| **5** | **灵巧** | 手指背面松口袋 + 逐根插入塑料条 + 腕带 | **塑料条数决定闭合难度** |

> **原文（Coleman p224）**：
> 「**The visual simulators comprise nine pairs of spectacles that try to reproduce decreasing levels of visual acuity (the ability to perceive details presented with good colour contrast) through increasing the blurriness on the lenses** … **The spectacles also affect the ability to perceive objects with poor colour contrast.**」

> **原文（Coleman p225）**：
> 「**Adjustability of the shoulder movement enables the wearer to set the range of motion of both arms to speciﬁ c angles**」

> **★★★★ 判据：这套工具包的可贵之处在于"每类能力都有连续等级可调"—— 这才是"能力连续统"的物化。**
> 逐条对应：
> - 视觉：9 级模糊度
> - 行走：塑料条数
> - 伸手：**可设定到具体角度**
> - 灵巧：塑料条数
> **这与第 5 章"capability loss as a continuum"（p221）是同一件事的工具版**：不是"能/不能"两档，而是可调档位。

---

## 7.6 实测结果：模拟器到底有没有用

### 7.6.1 实验设计（三阶段对比）

> **原文（Coleman p226）**：
> 「**The studies involved observation of several groups of older adult users (exhibiting varying levels and different types of capability loss) and able-bodied young design practitioners. All groups were involved in the assessment of a number of everyday devices (electric kettles, domestic central heating control units, and digital television receivers).**」

> **原文（Coleman p226）**：
> 「**The older adult participants acted as potential end-users and the designers as assessors. Whereas the former group used each device once only, the designers performed self-observation evaluations ﬁ rst, followed by simulation assessment (while wearing the toolkit).**」

**三阶段对照（原文的试验设计）：**

| 阶段 | 谁 | 做什么 |
|---|---|---|
| **①** | 老年用户（真实能力损失） | 每个设备只用一次 → 记录问题 |
| **②** | 设计者 | 先做**自省评估**（self-observation） |
| **③** | 设计者 | 再做**模拟评估**（戴工具包） |

> **★★★ 判据：这是一个"以真实用户为金标准"的对照实验 —— 不是问设计者"觉得有用吗"，而是比对"发现的问题是否一致"。**
> 这种实验设计值得照抄：**用真实用户的问题集，去校验替代手段的召回率。**

### 7.6.2 结果：模拟器总是发现更多问题

> **原文（Coleman p226）**：
> 「**Apart from minor exceptions, the simulation toolkit (Figure 13.6) enabled the designers to always identify more problems than those found during their self-observation assessments. The problems designers identiﬁ ed while wearing the simulators were also generally consistent with those that the users had previously encountered.**」

> **原文（Coleman p226）**：
> 「**The physical restrainers prompted the designers to revisit problems identiﬁ ed**」

> **原文（Coleman p227）**：
> 「**during self-observation, being particularly useful at helping designers to uncover several new ones.**」

（该句跨 p226–p227；此处按页分两段引用，不改字。）

> **★★★★ 判据：模拟器相对自省的两个作用 —— ① 让设计者重新审视自己已发现的问题（提高确信度）；② 发现新问题（提高召回）。**
> 注意原文说的是 `always identify more problems`（除少数例外），且 `generally consistent with those that the users had previously encountered`（与真实用户一致）。
> **「发现更多且与真实用户一致」正是有效的替代手段应具备的两个性质。**

### 7.6.3 设计者的原话（最有价值的部分）

> **原文（Coleman p227）**：
> 「**This was clearly verbalised, for instance, by one of the designers wearing the simulators while trying to bend down to plug a cable to the main socket: 'this is very difﬁ cult… how am I supposed to go down? This is exhausting, every single movement becomes a big act when you think about whether you really have to get up and down or not, whereas normally I would not think about it'.**」

> **原文（Coleman p227）**：
> 「**Designers had not anticipated how common, everyday actions could become exceedingly difﬁ cult to perform when their capabilities were severely reduced.**」

> **★★★★ 判据：`every single movement becomes a big act when you think about whether you really have to get up and down` —— 这句话揭示了模拟器最有价值的发现：**不是"某个动作变难"，而是"动作变成了需要预谋的事"**。**
> 这个洞察用任何问卷都问不出来，只能靠亲身体验。**它是"减少不必要的动作次数"这一设计原则的体验来源。**

> **原文（Coleman p227）**：
> 「**For instance, one designer described the effort required to undo a set of small cable ties, which were holding together some electrical cables of a digital set up box receiver, saying: 'if I had one disabled [hand] or eyesight it would be much easier, but since I have simultaneous disabilities, this makes it even harder to [do] it'.**」

> **原文（Coleman p227）**：
> 「**Another designer talks about the difﬁ culties in using a remote control: ' … is like hard to read and [you] can't actually press the right button'; or as another designer also commented 'very difﬁ cult to press buttons… [the] remote is very small, so I cannot hold it with one hand properly'.**」

> **★★★★ 判据：`if I had one disabled [hand] or eyesight it would be much easier, but since I have simultaneous disabilities, this makes it even harder` —— 多重损伤不是相加，是相乘。**
> 这是第 2 章"耦合"数据的第一人称版本，也是本章最强的实证：**模拟多重损伤时，难度显著超出各单损伤之和。**

### 7.6.4 最有效的组件竟然是最便宜的那个

> **原文（Coleman p227）**：
> 「**The visual simulators were probably the most effective component of the whole toolkit. This is very interesting because these simulators were also the easiest and cheapest to construct, which suggests that even simple simulators can be quite useful.**」

> **★★★★ 判据：最有效的是视觉模拟器，而它也是最容易、最便宜的 —— 说明"贵"与"有用"无关。**
> 这直接回应了第 6 章的工具门槛（`straightforward, fast and economic`）：**最该先做的那一件，往往是最便宜的那一件。**

---

## 7.7 使用纪律：三条不可越过的边界

### 7.7.1 边界一：只能作补充，不能作替代

> **原文（Coleman p221）**：
> 「**Consequently, simulation is suggested here as a supplementary assessment tool and not a replacement for the experience and beneﬁ ts of working with real users. Resorting to simulation as the only assessment technique to be implemented throughout a typical design process is likely to be insufﬁ cient at milestone stages when involving real users is of most importance.**」

> **原文（Coleman p228）**：
> 「**However, it is important to bear in mind that this is a supplementary technique to designers' self-observation and not a replacement for the way they work. Using simulation as the only method of assessing a device's ease of use could induce designers to focus only on the physical capability loss being simulated.**」

> **★★★★ 判据：模拟器不能替代三样东西 —— 真实用户、自省、以及"未被模拟的那些问题"。**
> 原文列出三个替代对象：real users（真实用户）、self-observation（自省）、以及"未模拟的其他交互方面"。
> **判据形式：模拟是"加法"（在已有方法上叠加），不是"减法"（砍掉别的方法）。**

### 7.7.2 边界二：会遮蔽问题（水壶烫手案例，全书最精彩的实证）

> **原文（Coleman p228）**：
> 「**For instance, when assessing the ease of use of three electrical kettles, some of the designers pointed out during self-observation that the surface of two of the kettles got dangerously hot after boiling. They also said that the hot steam would come towards the handle when pouring water from the ﬁ rst kettle. These same problems were not mentioned again by these same designers during simulation assessments. It is possible that the gloves simulating dexterity limitations (which were an earlier version of the latest simulators) unintentionally protected their hands against the high temperatures. These restrainers have since been redesigned to avoid situations like these.**」

> **★★★★★ 判据（本章最重要的一条）：模拟器会**物理性地遮蔽**问题 —— 灵巧模拟手套同时隔热，导致设计者再也感受不到"水壶外壳烫手"。**
> 这个案例的可怕之处在于：
> ① 问题**曾经被发现**（自省阶段两人都提到）；
> ② 戴上手套后**消失了**；
> ③ 原因是**手套挡住了热**，而不是问题被解决了；
> ④ 如果只用模拟法，这个安全事故隐患会被完全漏掉。
> **可迁移教训：任何"代理手段"都可能与其所测对象发生物理/认知上的干扰。** 判断方法：**比较两种方法的结果差异，差异处就是干扰点。**

### 7.7.3 边界三：模拟的是能力，不是"持续承受"与"社会处境"

> **原文（Coleman p221）**：
> 「**It is important to be aware that any simulation, in spite of being a useful way of experiencing temporarily the symptoms of impairment, does not enable designers to fully understand the consequences of being constantly impaired. People who exhibit real capability losses may have lived with that problem for a long time and may have developed alternative strategies for interacting with their surroundings, which designers would probably not predict even if using very accurate simulators.**」

> **原文（Coleman p229）**：
> 「**Another important aspect of the toolkit that ought to be considered is the fact that any restriction placed upon the wearers' capabilities is applied externally. The toolkit components consist of physical wearables that are placed over different parts of the body to reduce the wearer's capabilities. However, most real capability losses are likely to be caused by different and usually complex internal dysfunctions, such as swelling of the joints, muscle breakdown, or clouding of the eye lenses. Hence the toolkit's limitation in simulating rather than replicating particular behaviours.**」

> **原文（Coleman p229）**：
> 「**An equally critical issue is the fact that the simulators were not designed to cause any pain or suffering, but instead to reduce the designers' motor and sensorial capabilities. Real users may, for instance, experience varying levels of pain while using their hands (for example caused by rheumatoid arthritis of the hand), which may result in capability losses not being simulated by the toolkit. However, causing exceeding levels of discomfort or even inﬂ icting pain upon designers was considered unethical, and thus efforts were made to avoid such occurrences.**」

> **★★★★ 判据：模拟器的三个结构性盲区 —— ① 短暂 vs 长期（无法模拟"一直如此"的后果）；② 外置 vs 内生（绑上去 ≠ 从身体里发生）；③ 无痛 vs 有痛（模拟不施加疼痛）。**
> 第三条尤其重要且诚实：**不是因为疼痛不重要，而是因为"施加疼痛"在伦理上不可接受**（`considered unethical`）。
> **这条给了一个可辩护的边界说明：模拟器的不完整是有意为之的伦理选择，不是偷懒。**

> **原文（Coleman p229）**：
> 「**Yet in terms of capability loss simulation, externally stiffening a joint to limit range of movement is probably one of the few things that can be 'ethically' simulated, since it can be achieved without causing any pain.**」

> **★★★ 判据：能"伦理地模拟"的，恰好只是"限制活动范围"这类能力约束。**
> 反过来推：**凡涉及疼痛、疲劳持续性、认知退化、社会污名的，都不在模拟能力范围内。**

### 7.7.4 认知模拟为什么做不了

> **原文（Coleman p221）**：
> 「**Another limitation of this type of tool is the difﬁ culty in simulating cognitive capability losses. It has been suggested (but not recommended) that cognitive loss could be induced temporarily by consuming alcohol and other drugs or by undergoing sleep deprivation. However, safety is an obvious issue and it would be more appropriate, for instance, to ask people to perform several tasks at the same time, such as doing some mathematical count backwards while using the device being assessed.**」

> **原文（Coleman p221）**：
> 「**Due to the complexity of incorporating the simulation of cognitive capability loss into existing toolkits, these have been hitherto focusing on mimicking the effects of sensory and motor capability losses.**」

> **★★★★ 判据：认知模拟的唯一可行替代是"双任务负荷"（一边倒着数数一边用产品），而不是酒精/睡眠剥夺。**
> 原书对后者的措辞是 `suggested (but not recommended)`，理由是安全（`safety is an obvious issue`）。
> **可执行做法：** 需要测认知负荷时，让受试者在操作产品同时做倒数心算 —— 这是安全、可重复、可撤回的负荷施加方式。

---

## 7.8 "模拟了错误的东西"：损伤与失能的混淆

> **原文（Coleman p228）**：
> 「**Despite the efforts involved in calibrating the existing capability loss simulators, these were not accurately calibrated against the real impairments that the users exhibited. Instead, the simulators were calibrated against the descriptions of the users' level of disabilities, presented in the population scales mentioned previously.**」

> **原文（Coleman p228）**：
> 「**However, impairment and disability are two distinct concepts. In fact, different impairments can give rise to the same disability. For instance, two entirely different impairments such as: a swelling and stiffness of the joints (typically generalised as 'arthritis'); and a breakdown of the muscled ﬁ bres leading to weak and wasted muscles**」

> **原文（Coleman p229）**：
> 「**(muscular dystrophy), could both result in the same disability of not being able to turn knobs on a microwave, if these were too stiff to rotate.**」

> **★★★★ 判据：关节炎与肌营养不良 —— 两种完全不同的损伤，导致**同一个失能**（拧不动那个僵硬的旋钮）。**
> 这个逻辑反过来证明了两件事：
> ① **模拟能力（而不是损伤）是对的** —— 因为要设计的就是"旋钮扭矩"这个可及性参数；
> ② **按病因分组是错的**（回到 ch03 的震颤案例）—— 因为同一病因可能产生多种失能，同一失能可来自多种病因。
> **这条是本章对 ch03 §3.6.2 的正面印证。**

> **原文（Coleman p230）**：
> 「**The major shortcomings of the toolkit developed have also been acknowledged and identiﬁ ed. They were mainly related to the lack of a complete and consistent data source on impairments and capability loss.**」

---

## 7.9 一个被低估的用途：与客户沟通

> **原文（Coleman p230）**：
> 「**Preliminary interviews with these companies showed that the toolkit was particularly useful to identify a series of accessibility problems not predicted by the designers. In addition, feedback from these practitioners also suggested that the simulators can play an important role in facilitating the communication of ideas between the designers and their clients. This is particularly the case in raising the client's awareness regarding the levels of avoidable exclusion of 'non-mainstream' users (such as older and disabled people), caused by particular product features.**」

> **★★★★ 判据：模拟器最有价值的商业用途可能是"让客户亲身体验"—— 这比任何报告都更能争取预算。**
> 理由：第 6 章指出评估预算取决于客户是否理解（`if the client is not conversant ... it is unlikely ... financial resources`）。**模拟器是让客户"变得 conversant"最快的工具。**

> **原文（Coleman p230）**：
> 「**In everyday design practice it is expected that the simulators would have a greater impact (and thus be more useful) for design practitioners who are not particularly familiar with the issues pertinent to inclusive design.**」

> **★★★ 判据：模拟器对"不熟悉包容性议题"的设计者作用最大 —— 对已内化的人，边际收益小。**
> 这意味着它的定位是**入门工具**，而不是专家工具。

---

## 7.10 本章概念-论点表（共 15 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | **四层术语链** | disorder → impairment → capability loss → **disability（由产品与环境造成）** | 骨关节炎→软骨脆弱→手部活动受限→拧不动旋钮 | 只有第③层可设计、可模拟；第④层是设计的责任 | Coleman p219 |
| 2 | **模拟只动第③层** | 「reducing the wearers' sensory and motor functional capabilities」 | — | 合法边界：只模拟能力受限，不碰疼痛、疲劳持续性、污名 | Coleman p219 |
| 3 | **简易模拟器五件套** | 指关节粘纽扣 / 眼罩起雾眼镜 / 冰球护具 / 吸管爬楼 / 鞋里放豆 | — | 几乎零成本即可完成"意识唤醒"，不必等买套件 | Coleman p219–p220 |
| 4 | **简易模拟器只用于唤醒** | 「an economical and effective way of raising awareness」 | — | 用途是 awareness 不是 assessment；当评估用会得出"不严重"的错误结论 | Coleman p220 |
| 5 | **整装式三缺陷** | 「the combination of multiple impairments as well as the simulation of different levels ... did not restrict design creativity」 | Third-Age Suit / Age Explorer | 单水平 + 单损伤 + 不可分模块 → 只能演示不能评估 | Coleman p220 |
| 6 | **模块化是核心改进** | 「the assessors need only put on the parts of the toolkit that will enable them to affect speciﬁc capabilities」 | — | 只戴手套时还能思考，穿全身套只能体验绝望 | Coleman p223 |
| 7 | **洗碗机推理** | 「designers may feel more physically affected ... However, if in the wider population there happen to be more people exhibiting dexterity ... such an assessment decision may prove inadequate」 | 洗碗机 | **体感强度 ≠ 问题严重度。** 优先级只能由体感 × 人数决定，或干脆只看人数 | Coleman p222 |
| 8 | **标定必然含主观性** | 「a series of assumptions had to be made ... inevitably involving some degree of subjectivity」 | — | 无完整人口能力数据 + 数据多为单轴 + 只有残障描述可对标 | Coleman p223 |
| 9 | **以真实用户为金标准** | 三阶段对照：真实用户一次 / 设计者自省 / 设计者戴模拟器 | 水壶、供暖控制、数字电视接收器 | 有效替代手段的两个性质：发现更多 + 与真实用户一致 | Coleman p226 |
| 10 | **动作变成"需要预谋的事"** | 「every single movement becomes a big act when you think about whether you really have to get up and down」 | 弯腰插电源 | 问卷问不出的洞察：不是动作变难，是动作变贵。这是"减少动作次数"原则的体验来源 | Coleman p227 |
| 11 | **多重损伤相乘不 相加** | 「if I had one disabled [hand] or eyesight it would be much easier, but since I have simultaneous disabilities, this makes it even harder」 | 拆线扎带 | 第 2 章耦合数据的第一人称版 | Coleman p227 |
| 12 | **最有效的组件最便宜** | 「The visual simulators were probably the most effective ... also the easiest and cheapest to construct」 | 9 副眼镜 | 回应第 6 章工具门槛：最该先做的那件往往最便宜 | Coleman p227 |
| 13 | **模拟器会遮蔽问题** | 「These same problems were not mentioned again ... the gloves ... unintentionally protected their hands against the high temperatures」 | 水壶外壳烫手 | **代理手段可能与所测对象发生物理干扰。** 比对两种方法的差异即可定位干扰点 | Coleman p228 |
| 14 | **三个结构性盲区** | 短暂vs长期 / 外置vs内生 / 无痛vs有痛（`considered unethical`） | — | 不完整是有意的伦理选择，不是偷懒。能伦理模拟的只剩"限制活动范围" | Coleman p221、p229 |
| 15 | **认知只能靠双任务** | 「ask people to perform several tasks at the same time, such as doing some mathematical count backwards」 | 酒精/睡眠剥夺被明确不推荐 | 安全、可重复、可撤回的认知负荷施加方式 | Coleman p221 |
| 16 | **同一失能多种病因** | 「arthritis ... and muscular dystrophy, could both result in the same disability of not being able to turn knobs on a microwave」 | — | 反过来证明"模拟能力而非损伤"是对的，且按病因分组是错的 | Coleman p228–p229 |
| 17 | **与客户沟通的最佳工具** | 「raising the client's awareness regarding the levels of avoidable exclusion」 | — | 让客户变 conversant 最快的方式，直接决定评估预算能否拿到 | Coleman p230 |
| 18 | **入门工具而非专家工具** | 「would have a greater impact ... for design practitioners who are not particularly familiar」 | — | 对已内化者边际收益小；定位要摆正 | Coleman p230 |

---

## 7.11 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **精确标定的数值表** | **不存在**。原书明确：`it is not feasible to accurately and realistically calibrate a wearable simulation toolkit`（p222）；实际标定 `inevitably involving some degree of subjectivity`（p223） | 无。这是原书自认未解决的问题 |
| **每级模拟器对应的人数** | **未给出**。这是标定的目标，但数据源缺失 | 需新的人口能力调查 |
| **认知模拟的完整方案** | **只有双任务一招**，且是"更合适"而非"已验证" | 无 |
| **疼痛的正当代替方案** | **无**。因为施加疼痛不伦理 | 无。只能靠用户访谈 |
| **"持续承受"的模拟方法** | **无**。原书明说无法模拟 `being constantly impaired` | 无 |
| **模拟器的定量效度（与用户问题的重合率）** | **只有定性**（`generally consistent`），无具体百分比 | 需复现该实验 |
| **Third-Age Suit / Age Explorer 的标定细节** | **只提及**，未给参数 | 原厂资料 |
| **模拟器对"社会可接受性"的作用** | **完全未涉及**。它只模拟物理能力，不模拟"被看见使用"的尴尬 | 需共情方法（ch08） |
| **中国人群的标定** | **无** | 无 |
| **2010 年后的模拟技术**（VR/AR 模拟） | **不在源书范围**（成书 2007） | 现行文献 |

---

## 7.12 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 能力连续统的物化 | **ch02 §2.5** | 同一概念的工具版（原文 p221 就引用了该表述） |
| 多重损伤相乘 | **ch02 §2.3.1、§2.3.2** | 本章给第一人称证据 |
| 按病因分组是错的 | **ch03 §3.6.2** | 本章用"同一失能多种病因"正面印证 |
| 优先级由人数决定 | **ch04 §4.4、§4.6** | 本章给"体感不可靠"的反证 |
| 模拟作为八法之一 | **ch06 §6.6** | 本章是那一节的完整展开 |
| Level 3/5 可用标定模型 | **ch05 §5.3.3、§5.3.4** | 本章给"标定"的具体含义与不确定度 |
| 与客户沟通争取预算 | **ch06 §6.8.2** | 本章给"如何让客户变 conversant" |
| 社会可接受性无法模拟 | **ch08 §8.4、ch03 §3.6** | 需另一套方法 |
| 真实用户不可替代 | **ch09 全章** | 用户研究方法的完整体系 |

### 7.12.1 跨技能挂钩（本机已有技能）

| 本技能内容 | 挂钩技能 | 关系与用法 |
|---|---|---|
| **"限制活动范围"的模拟（膝/肘/肩支架）** | **`ergonomics-ding-yulan`** | 丁玉兰有各关节活动角度（ROM）标准值；本技能给"把 ROM 限制到某个具体角度"的模拟做法。<br>**合用判据：设定模拟档位时，直接取丁玉兰的关节活动度百分位值，而不是凭感觉绑紧。** |
| **9 级视觉模糊度** | **`ergonomics-ding-yulan`** | 丁玉兰的视度/照明标准给出基准；本技能给"按等级模糊"的施加方式。<br>**合用：用丁玉兰定基准视锐度，用本技能做分级剥夺。** |
| **"动作变成需要预谋的事"（p227）** | **`design-psychology-norman`** | 诺曼的"行动七阶段"解释了为什么每个动作都要额外的认知步骤（确定目标→意图→行动内容）。**当能力下降，七阶段中每一段都变贵。** 本技能给体验证据，诺曼给机制。<br>**合用判据：设计时数"完成一件事需要几个七阶段循环"，循环越多越贵。** |
| **认知负荷用双任务施加（p221）** | **`design-psychology-norman`** | 诺曼的"知识在头脑中 vs 外界"与"记忆负荷"直接对应双任务失效机制；本技能给一个安全的施加方法。<br>**合用：用诺曼判断哪些步骤依赖记忆（可用外界知识替代），用双任务法验证。** |
| **模拟器会遮蔽问题（水壶烫手，p228）** | **`product-structure-liubaoshun`** | 这个案例本质是**结构与热设计**问题（外壳隔热）。刘宝顺的壳体结构与安全结构（警示/转换/有限损坏/冗余）正是解法。<br>**合用判据：模拟评估若漏掉"烫/夹/划"这类物理危害，必须补一轮结构安全检查。** |
| **关节炎导致"拧不动旋钮"（p229）** | **`product-structure-liubaoshun`** | 旋钮扭矩是结构 + 机构参数（阻尼、棘轮、摩擦）。本技能给"这是一个跨病因的共同失能"，刘宝顺给"如何降低操作扭矩"的结构方案。<br>**合用：把"拧不动"当需求指标，用结构设计降扭矩。** |
| **简易模拟器的"唤醒意识"用途（p220）** | **`design-methodology-liuguanzong`** | 柳冠中强调"设计者要跳出自我经验"，本技能给了一个具体的、可操作的跳出方式（限制自己的身体）。<br>**合用：作为"外部因素分析"的体验化补充。** |
| **与客户沟通（p230）** | **`design-methodology-liuguanzong`** | 柳冠中的"设计评价"环节需要各方共识；本技能给"让决策者亲身体验"这一最快达成共识的手段。 |
