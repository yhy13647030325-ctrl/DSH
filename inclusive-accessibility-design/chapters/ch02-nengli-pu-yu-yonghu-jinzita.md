# 第 2 章：能力谱与用户金字塔——把"人"拆成可测的三条轴

> **原书 PDF 页序 p371–p382（12 页，Clarkson 第 21 章）＋ p435、p439、p442（3 页，Clarkson 第 25 章）＋ p207–p208（2 页，Coleman 第 12 章）＋ p47–p63（17 页，Clarkson 第 1 章 Huppert）｜本版逐页读完全部 34 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）
>
> **读法说明**：先按 Clarkson ch21 的 `A model of disability → The disability surveys → The prevalence of capability losses → Multiple capability losses → Other sources of data` 逐节展开能力轴的原始数据来源；再用 ch25 的三类别合并（Mot/Sen/Cog）与 Coleman ch12 的四点量表把轴做成可用工具；最后用 Huppert ch1 的生理老化数据给每一条轴填上"随年龄怎么变"。
> 每节含【原文摘录】+【判据提炼】。
> **时效边界**：本技能源书成书于 2003 与 2007 年，**不含 2010 年后标准**（WCAG 2.1/2.2、EN 17161、EN 301 549 等）。详见 §2.7。

---

## 2.0 总纲：这一章解决什么

第 1 章说"残疾在环境里，不在身体里"。但要动手，必须先回答：**那么身体这一端要怎么描述？**

本章给出全书唯一的答案，分三层：

| 层 | 内容 | 原书位置 |
|---|---|---|
| **① 七条功能能力**（7 capabilities） | locomotion、reach & stretch、dexterity、vision、hearing、communication、intellectual functioning | Clarkson p377、p435 |
| **② 三大类**（3 categories） | **Motion** = ① locomotion + reach + dexterity；**Sensory** = vision + hearing；**Cognition** = communication + intellectual | Clarkson p439、Coleman p192 |
| **③ 十级严重度 + 用户金字塔** | 每轴 0（全能力）至 13（最重）；严重度 1–10 分级；八百万人的金字塔 | Clarkson p375、p439 |

> **★★★★ 判据：本书描述"人"的单位不是"残疾类别"，也不是"年龄"，而是"七条能力各自的严重度分数"。**
> 这条选择带来三个直接后果：
> ① 同一句需求可以同时覆盖关节炎、骨折、抱小孩、拎重物 —— 因为它们落在同一格；
> ② 严重度是**连续量**，所以"边界人群"可以被精确指定（ch08 的 boundary users）；
> ③ 分数可以**映射回人口数**，于是"排除"可以直接换算成人和市场份额（ch04）。

**为什么不是"年龄"？** 原书给了一句很硬的判断：

> **原文（Clarkson p49）**：
> 「**The differences between individuals of the same age (e.g. 30-year olds) are far greater than the differences between age groups (e.g. the average 30-year old compared with the average 60-year old).**」

> **★★★ 判据：同龄人之间的差异 > 年龄组均值之间的差异。**
> 因此任何以"年龄段"为设计输入的方法（"面向 60 岁以上"）在统计上都是低效的：它同时高估了这个群体的同质性、低估了组内分散度。
> **本条是与 `ergonomics-ding-yulan` 接口最紧的一句**：百分位本身也不按年龄分组，按的是**尺寸分布**；两本书在这一点上完全一致。

---

## 2.1 能力谱：七条轴各自怎么描述用户

### 2.1.1 七条轴的原始定义（含点数与分数区间）

> **原文（Clarkson p377）**：
> 「**The disability severity scales adopted by the above surveys were adapted for research purposes, and seven capabilities closely related to product evaluation were selected. They are: Locomotion (13 points, with severity scores of 0.5-11.5); Reaching and Stretching ( 10 points, with severity scores of 1.0-9.5); Dexterity (11 points, with severity scales of0.5-10.5); Seeing (9 points, with severity scores of0.5-12.0); Hearing (8 points, with severity scores of 0.5-11.0); Communication (5 points, with severity scores 0.5-12.0), and Intellectual functioning ( 11 points, with severity scores of 1.0-13.0).**」

| # | 能力轴 | 中文 | 题项数 | 严重度分数区间 | 归属大类 | 典型产品评估含义 |
|---|---|---|---|---|---|---|
| 1 | **Locomotion** | 行走/移动 | 13 | 0.5–11.5 | **Motion** | 站立、上下楼、走到产品前 |
| 2 | **Reaching and Stretching** | 伸手/伸展 | 10 | 1.0–9.5 | **Motion** | 够到货架、举手过头 |
| 3 | **Dexterity** | 灵巧度 | 11 | 0.5–10.5 | **Motion** | 抓握、旋拧、按压 |
| 4 | **Seeing** | 视觉 | 9 | 0.5–12.0 | **Sensory** | 读标签、辨色、看显示屏 |
| 5 | **Hearing** | 听觉 | 8 | 0.5–11.0 | **Sensory** | 听提示音、听懂语音 |
| 6 | **Communication** | 沟通 | 5 | 0.5–12.0 | **Cognition** | 理解说明、表达需求 |
| 7 | **Intellectual functioning** | 智力功能 | 11 | 1.0–13.0 | **Cognition** | 理解菜单结构、记住步骤 |

**关键性质：**

> **原文（Clarkson p435）**：
> 「**Each of these scales, ranging from 0 (fully able) through 0.5 (minimal impairment) to 13 (most severe impairment), has been aligned to ensure that equal scores broadly relate to equivalent levels of capability (Martin et al., 1 9 8 8).**」

> **★★★★ 判据：七条轴被"对齐"过 —— 相同分数在不同轴上大致代表同等的能力水平。**
> 这是全部量化方法的技术前提。**没有这条对齐，就不可能把七个数合并成一个严重度**，也不可能画"等能力曲线"。
> **实操含义：** 你可以放心地说"这个产品的视觉需求是 4.5、灵巧需求是 8.0"，然后比较哪个更严格 —— 因为 4.5 与 8.0 在同一把尺上。

### 2.1.2 三条轴的合并规则

> **原文（Clarkson p439）**：
> 「**The seven capabilities can be compiled to three broad categories: Motion (derived from locomotion, reach and stretch, and dexterity)** … **Sensory (derived from vision and hearing)** … **Cognition (derived from communication and intellectual function)**」

> **原文（Coleman p192）**：
> 「**For the purposes of product assessment, seven of the 13 capabilities identiﬁ ed by the surveys are of particular relevance. These may be grouped into three overall capability categories:** … **motion − locomotion, reaching and stretching, and dexterity** … **sensory − seeing and hearing** … **cognitive − communication and intellectual functioning.**」

> **★★★ 判据：三轴不是三个"感官"，是三段交互。**
> 三轴的来源是 Card、Moran & Newell (1983) 的人类信息处理模型，原书写得很明确：

> **原文（Clarkson p115）**：
> 「**The division of human-product interaction into three distinct stages - perception, cognition and motor functions (Card, Moran and Newell, 1983)- suggests a method for dividing the population according to the ability to perform those functions. Applying equal weight**」

> **原文（Clarkson p116）**：
> 「**to the capability to perform each of these actions implies a cubic representation of the population.**」

（该句跨 p115–p116；此处按页分两段引用，不改字。）

> **★★★ 判据：「等权重」是三轴立方体的建模假设，不是事实判断。**
> 原文用了 `Applying equal weight`。这意味着立方体把感知、认知、机动视为同等重要 —— 这在几何上是必需的（否则画不出等边长立方体），在现实中是**可质疑的**。
> **用法：** 立方体适合做**结构可视化**（谁在哪一格），不适合做**加权重要性排序**。要排序，必须回到七条原始轴分别看人数（ch04）。

**三轴与"设计者常见误区"的对应关系：**

| 轴 | 设计者最容易忽略什么 | 原书对应用语 |
|---|---|---|
| **Sensory** | 输出是否被感知（不是"有没有输出"） | `if a product excludes a significant proportion of the population because of the perceptual demands, this implies that users either cannot hear or see the output`（Clarkson p116） |
| **Cognition** | 心智模型是否匹配，而不是"够不够聪明" | Level 4 = `structure the interaction to match the user's expectations`（Clarkson p457，见 ch05） |
| **Motion** | 力、行程、双手操作 | `Tasks which require the use of two hands`（Clarkson p126，十项常见失败之一） |

---

## 2.2 三条轴各自的"用户怎么描述"（用原书的量表定义示范）

原书只用**听觉轴**给了完整的量表定义表，但这一张表足以让你照着为另外六轴建表。

> **原文（Clarkson p435）**：
> 「**Hearing Severity score H1 Cannot hear sounds at all 11 .0 H2 Cannot follow a TV programme with the volume turned up 8.5 H3 Has difficulty hearing someone talking in a loud voice in a quiet room 6.0 H4 Cannot hear a doorbell, alarm clock or telephone bell 5.5 HS Cannot use the telephone 4.0 H6 Cannot follow a TV programme at a volume others find acceptable 2.0 H7 Difficulty hearing someone talking in a normal voice in a quiet room 1.5 H8 Difficulty following a conversation against background noise 0.5**」

### 2.2.1 听觉轴量表（8 级，逐级可判）

| 级 | 行为描述（原文） | 分数 | 产品含义 |
|---|---|---|---|
| H1 | Cannot hear sounds at all | 11.0 | 任何声音输出无效 |
| H2 | Cannot follow a TV programme with the volume turned up | 8.5 | 大音量语音仍不可用 |
| H3 | Has difficulty hearing someone talking in a loud voice in a quiet room | 6.0 | 需近距离大声 |
| H4 | Cannot hear a doorbell, alarm clock or telephone bell | 5.5 | **提示音全部失效** |
| H5 | Cannot use the telephone | 4.0 | 语音交互失效 |
| H6 | Cannot follow a TV programme at a volume others find acceptable | 2.0 | 需超常音量 |
| H7 | Difficulty hearing someone talking in a normal voice in a quiet room | 1.5 | 安静环境正常音量困难 |
| H8 | Difficulty following a conversation against background noise | 0.5 | **仅在噪声下困难** |

> **★★★★ 判据：这张表是"能力量表"的模板 —— 它的每一格都是行为，不是病因。**
> 注意它完全不提"耳聋""老年性耳聋""听神经瘤"。它只写"能不能听见门铃"。
> **为什么这很重要（原书在另一处说得最直白）：**

> **原文（Clarkson p468）**：
> 「**it is not very helpful for the designer to know that certain users have 'arthritis of the knee joint', unless they have the appropriate medical expertise to interpret that diagnosis. Instead it is more useful to know how long the user can stand or walk or how many steps the user can climb.**」

> **★★★ 判据：把"诊断"翻译成"行为门槛"，是能力谱最核心的一次转译。**
> 诊断（arthritis of the knee joint）→ 设计者无法使用；
> 行为（how many steps the user can climb）→ 可以直接变成"楼梯级高/级数"参数。
> **与 `ergonomics-ding-yulan` 的接口就在这里**：丁玉兰提供的是**尺寸与力的行为门槛**（第 5 百分位身高、握力、推拉力），本技能提供**把它扩展到感官与认知的模板**，并把门槛换算成人数。

### 2.2.2 四点行为量表（比七级更好用的快速版）

> **原文（Coleman p207–p208）**：
> 「**It can be helpful to understand the prevalence of different capability levels within the target population since this provides insights into potential product performance targets. This is most easily done using a four-point scale:** … **Full ability – has adequate use of the capability for everyday activities;** … **Moderate ability – experiences some difﬁ culties with the capability in several everyday situations;** … **Partial ability – has signiﬁ cant problems with the capability in most everyday situations;** … **Minimal ability – cannot use that capability for practical everyday purposes.**」

| 级 | 名称 | 判据（原文关键词） | 设计动作 |
|---|---|---|---|
| **4** | **Full ability** | `adequate use … for everyday activities` | 无需特殊考虑 |
| **3** | **Moderate ability** | `some difﬁ culties … in several everyday situations` | **主力目标**：改进细节即可纳入 |
| **2** | **Partial ability** | `signiﬁ cant problems … in most everyday situations` | 需要替代通道（冗余模态、可调参数） |
| **1** | **Minimal ability** | `cannot use that capability for practical everyday purposes` | 需要专门方案（立方体的 special purpose 端） |

> **★★★★ 判据：四点量表是"设计评审"最快的抓手 —— 每一级都对应一种设计动作，而不是一种人。**
> 表里第三列不是描述用户，是**触发什么设计响应**。这一列才是产品团队真正要用的。
> **与七级量表的分工：** 七级（0–13 分）用于**量化与人数换算**（ch04）；四级用于**评审与沟通**（说给非专业者听）。

### 2.2.3 感官轴：随年龄具体怎么变（Huppert 的硬数据）

这一节是全书数值密度最高的部分，也是与 `ergonomics-ding-yulan` 的显示/照明设计衔接最直接的部分。

**视觉：**

> **原文（Clarkson p53）**：
> 「**Age-related physiological changes lead to a decline in our ability to see detail, to focus on near objects, to discriminate differences between levels of contrast, adapt to changes in brightness, and manage in extremely bright light, as well as to mild impairments in colour vision and depth perception.**」

> **原文（Clarkson p53）**：
> 「**This results in a change in the optimal viewing distance, which begins to lengthen from 8 em at around age l 0, to SO em at age SO, to l OOcm at age 60 (Grandjean, 1986).**」

| 年龄 | 最佳视距 | 设计含义 |
|---|---|---|
| ~10 岁 | **8 cm** | — |
| ~50 岁 | **50 cm** | 台面阅读尚可 |
| ~60 岁 | **100 cm** | **手持标签、面板刻度必须按 1 m 阅读距离设计** |

> **原文（Clarkson p54）**：
> 「**even when they have had ample time to adapt to the dark, 60 year olds require ten times as much light (I unit on the log scale) as 2 0 year olds to detect that there is a light present, while 80 year olds require I 00 times as much light (2 units on the log scale) as 20 year olds to detect that a light is present.**」

> **原文（Clarkson p54）**：
> 「**However, under normal conditions of illumination, twice as much light is required at age 40 as at age 2 0, and three times as much light at age 60.**」

| 条件 | 40 岁 | 60 岁 | 80 岁 |
|---|---|---|---|
| 正常照明下看清细节 | **2×**（相对 20 岁） | **3×** | — |
| 暗适应后探测到光源 | — | **10×** | **100×** |

**色彩：**

> **原文（Clarkson p53）**：
> 「**The discolouration of the lens also reduces colour vision, the effect being particularly to filter out blues and violets.**」

> **原文（Clarkson p54）**：
> 「**Surfaces should be non-reflective, and brightness and colour contrast high. Blue-violet-green combinations should be avoided.**」

> **★★★★ 判据：蓝—紫—绿配色对老年用户是三重失效（晶状体滤蓝紫 + 对比度不足 + 常见色觉异常）。**
> 这不是美学偏好，是光学后果。**直接可执行的禁令：状态指示不要只靠蓝/紫/绿区分。**

**听觉：**

> **原文（Clarkson p55）**：
> 「**The first nerve cells to die are those that respond to high frequency signals. This process starts around puberty. By about age 50, there is generally sufficient hearing loss to cause impairment in reasonably demanding listening situations such as detecting faint sounds or in the presence of background noise.**」

> **原文（Clarkson p56）**：
> 「**Lower frequency sounds should be used to convey important messages.**」

**触觉：**

> **原文（Clarkson p56–p57）**：
> 「**The skin of our hands becomes less sensitive to pressure, and there is a reduction in 2-point discrimination; that is, two points touching the skin need to be further apart for an older person to recognise that there are two sources of pressure rather than one. This leads to a reduced ability to differentiate between shapes and textures by touch. After age SO, our ability to perceive vibrations is also diminished, particularly if the vibrations are high frequency.**」

> **★★★★ 判据：50 岁后"两点辨别"退化 —— 触觉编码必须按"间距"而不是"凸起数"来设计。**
> 这条对按键凸点、盲文点距、触摸屏振动反馈都直接成立。**判据形式：触觉可辨元素之间的最小间距，须按目标人群的两点辨别阈来定，而不是按"摸得出来"直觉来定。**

### 2.2.4 认知轴：哪些能力下降、哪些不下降

这是全书对"认知"最细致的一段，也是避免"把老人当认知障碍"的关键。

> **原文（Clarkson p57）**：
> 「**Mental abilities which are based on bodies of information acquired over long periods of time (e. g. vocabulary, work-related expertise, hobbies and interests) tend to remain stable with advancing age, whereas abilities which require the rapid assimilation and analysis of new information tend to decline quite sharply.**」

| 认知子能力 | 随年龄走向 | 设计含义 |
|---|---|---|
| 词汇、专业知识、兴趣 | **稳定甚至上升** | 不要简化术语为"儿童语言"；专业用户仍是专家 |
| 处理速度 | **明显下降** | 禁止极短呈现、快速轮播 |
| 双任务（dual task） | **最明显下降** | 禁止"边做 A 边做 B" |
| 数字能力 | **下降最多**（纵向研究） | 用自然频次替代百分比 |
| 回忆（recall） | 比再认（recognition）难得多 | 用可见选项代替记忆输入 |
| 前瞻记忆（记得去做） | **明显下降** | 必须提供提醒与步骤引导 |
| 执行功能 | 下降，但与教育与经验强相关 | 复杂决策鼓励咨询他人 |

> **原文（Clarkson p59）**：
> 「**For example, there is a marked ageing effect in dual task situations such as speaking while driving, reading and listening to the radio, following signs and listening to announcements at train stations or airport terminals.**」

> **原文（Clarkson p60）**：
> 「**people understand natural frequencies far more readily than they understand percentages or proportions (Gigerenzer and Goldstein, 1996) e.g. they understand the concept that a particular event occurs 3 times in I 00 far better than that it occurs 3% of the time.**」

> **原文（Clarkson p62）**：
> 「**Numerical information should be presented as simply as possible and natural frequencies should be used in preference to percentages (e.g. 1 in 1,000 is more readily understood at all ages than 0.1 %).**」

> **原文（Clarkson p61）**：
> 「**The other type of memory which shows marked age-related impairment is prospective memory i.e. remembering to carry out an action (Huppert, Johnson and Nickson, 2001). In the absence of a reminder, older people are far more likely than younger people to forget to perform an action, such as posting a letter, keeping an appointment or taking medication.**」

> **原文（Clarkson p62）**：
> 「**Designs which impose a high demand on memory should be avoided, such as activities involving a sequence of operations which need to be memorised (e.g. programming a washing machine or video recorder). The memory load can be eliminated by cueing each step in the sequence.**」

> **★★★★ 判据：认知负荷的靶点不是"理解力"，是"处理速度 + 双任务 + 前瞻记忆"三项。**
> 这三项恰好是绝大多数产品"默认不难、实际最难"的地方：快速轮播的界面、多点同时操作、需要记住步骤的程序设定。
> **可执行改写：** ① 一切序列操作逐步提示（消前瞻记忆负荷）；② 一切数值用自然频次（`1 in 1,000` 而非 `0.1%`）；③ 一切信息禁止极短呈现与多源竞争。

### 2.2.5 机动轴：力、灵活性、平衡、耐力

> **原文（Clarkson p50）**：
> 「**Muscle strength (e.g. hand grip, quadriceps strength) is at its peak around age 25 on average, and begins to decline quite sharply from around age 50. Hand strength is needed for lifting and as an adjunct to leg strength when rising from a low chair, getting onto a bus or out of the bath.**」

> **原文（Clarkson p50）**：
> 「**Figure 1. 2 shows a steep decline in hand grip strength for men and women from age 45-54, and for those aged 7 5+ it is less than half of the value for young adults.**」

| 能力 | 峰值 | 明显下降起点 | 75+ 相对值 |
|---|---|---|---|
| 握力（hand grip） | ~25 岁 | **45–54 岁** | **< 年轻人的一半** |
| 肌肉功率（power） | — | 比力量**下降更快** | — |

> **原文（Clarkson p51）**：
> 「**In general, physical strength is related to body size, so women are physically weaker than men at all ages. Women's physical capabilities are about two-thirds those of men (see Bassey, 1997).**」

> **原文（Clarkson p51）**：
> 「**Older women should therefore be a priority target group for inclusive design.**」

> **原文（Clarkson p51）**：
> 「**The combined effect is that the average height of someone aged 65- 74 is 5cms less than the average heigt of someone aged 16-24, and this height difference is almost double for those aged 7 5+ (Health Survey for England, 2000).**」

> **★★★ 判据：老年女性是包容性设计的**首要目标人群**（原书原话 `priority target group`），理由是三条叠加：力量约为男性 2/3 + 身高再降 5–10cm + 人数上占多数。**
> 这条判据在实操上等价于：**设计基准人不是"平均成年男性"，而是"较矮的老年女性"。**
> 这与 `ergonomics-ding-yulan` 的百分位选择直接冲突又直接互补：丁玉兰教你怎么在 5–95 百分位之间取舍，本书提示你**选哪个百分位本身就是一个人群判断**。

> **原文（Clarkson p52）**：
> 「**People with arthritis find it difficult to get a firm grip or make fine, precise finger movements. Double actions such as push and twist are particularly difficult for people with poor dexterity.**」

> **原文（Clarkson p52）**：
> 「**Where possible and appropriate, heights of products should be adjustable, and tasks should be achievable using one hand rather than two to allow for strength variation between the hands and to allow for balance support while undertaking the task.**」

> **★★★★ 判据：双手操作是机动轴的头号硬门槛 —— 因为另一只手必须留着维持平衡。**
> 这一条把"双手操作"从"方便与否"提升为"是否可及"。原书的十项常见失败里赫然在列：`Tasks which require the use of two hands`（Clarkson p126）。
> **可执行改写：** 任何需要"一手扶、一手拧"的结构（瓶盖、旋钮、卡扣、旋锁）都应重新评估；**"push and twist" 双重动作要单独标注为高风险**。

> **原文（Clarkson p52）**：
> 「**Designs which largely avoid physical demands (e.g. rely on voice-activation) are valuable for those with severe physical impairment, but may be a disservice to the average older person.**」

> **★★★ 判据：把体力需求全部消除，对一般老人可能是"帮倒忙"。**
> 理由：`Designs which impose physical demands which are well within the capability of most older people can play a part in maintaining their physical activity, which in turn reduces physical decline.`（p52）
> **这条判据与第 1 章 Fisk 的"design to counter decline"是同一判断的两种说法**，也是三轴模型唯一一处明确的"能力轴之间有权衡"的地方。

---

## 2.3 多个能力同时受损：本章最重要的一条数据

只按单轴设计是错的。原书用两张表把这件事钉死。

### 2.3.1 单损 vs 组合损（英国 16+ 人口）

> **原文（Clarkson p379）**：
> 「**Loss of capability type Numbers of GB Percentage of GB 16+ population 16+ population Mobility loss only 2 915 000 6.2% Sensory loss only 771 000 1.6% Cognition loss only 431 000 0.9% Combination loss of motion and sensory 1 819 000 3.9% Combination loss of sensory and cognitive 213 000 0.5% Combination loss of cognitive and motion 801 000 1.7% Loss of motion, sensory and cognitive 1 175 000 2.5%**」

| 类型 | 人数（GB 16+） | 占比 |
|---|---|---|
| 仅机动受损 | 2,915,000 | 6.2% |
| 仅感官受损 | 771,000 | 1.6% |
| 仅认知受损 | 431,000 | 0.9% |
| **机动 + 感官** | **1,819,000** | **3.9%** |
| **感官 + 认知** | 213,000 | 0.5% |
| **认知 + 机动** | 801,000 | 1.7% |
| **三轴全部受损** | **1,175,000** | **2.5%** |

> **原文（Clarkson p380）**：
> 「**Loss of capability type Some motion loss Some sensory loss Some cognitive loss Some motion, sensory or cognitive loss Numbers of GB 16+ population 6 710 000 3 979 000 2 622 000 8 126 000 Percentage of GB 16+ population 14.3% 8.5% 5.6% 17.3%**」

| 汇总口径 | 人数 | 占比 |
|---|---|---|
| 有任何机动受损 | 6,710,000 | 14.3% |
| 有任何感官受损 | 3,979,000 | 8.5% |
| 有任何认知受损 | 2,622,000 | 5.6% |
| **有任何一轴受损（去重后）** | **8,126,000** | **17.3%** |

> **★★★★ 判据：单损人数之和（2,915,000 + 771,000 + 431,000 = 4,117,000）远小于去重后的总数（8,126,000）。**
> 也就是说，**超过一半的受损者是"多条轴同时受损"**。这一条数据单独就否定了"按单一障碍做设计"的做法。

> **原文（Clarkson p380）**：
> 「**It is evident that there is a high level of coupling (50%) between motion capability and sensory capability.**」

> **原文（Clarkson p380）**：
> 「**The implication of the distribution of multiple capability losses for design is that focusing on accommodating individual capability losses may not necessarily include everyone with that loss.**」

> **原文（Clarkson p444）**：
> 「**It is obvious that if kettle E is to be improved to achieve the same level of inclusion as kettle F, both vision and dexterity demand need to be reduced simultaneously. The reduction of vision demand will only include more bubbles hugging the vision axis, but not those in the coupling region.**」

> **★★★★ 判据：「耦合区」是不可回避的设计事实 —— 单轴改进会在耦合区失效。**
> 原书给了量化实例（Clarkson p444）：壶 E 与壶 F 的差异对应 **1,880,000 名英国成年人**，而这批人全部落在视觉—灵巧的耦合区里。
> **可执行结论：** 若评审显示某产品的主要排除来自两条轴，必须**同时**降低两条轴的需求；只降一条，被排除人数几乎不变。这是"多轴改进优先级"的唯一正确算法。

### 2.3.2 年龄与性别分布（用来说明"为什么不能按年龄设计"）

> **原文（Clarkson p376）**：
> 「**Multiple impairments were more commonly found among older adults than among younger disabled people. Communication, behavioural and intellectual function impairments were more common among those aged under 60 than among older adults.**」

> **★★ 判据：认知/沟通类受损在 60 岁以下更常见，机动/感官类在 60 岁以上更常见。**
> 这直接反驳"包容性设计 = 适老化设计"的简化理解：**年轻障碍者的主战场在认知与沟通，不在机动。** 这也是 ch08 "critical users 偏年轻"的理论根据。

**一个必须记住的方法论警告：**

> **原文（Clarkson p376）**：
> 「**Dexterity, however, degrades gradually over time, and there are no obvious measures of one's own dexterity performance. It is difficult to assess whether it is a little harder to pick something than it used to be, or if glass jar lids seems a bit tighter than it was a few years ago.**」

> **原文（Clarkson p376）**：
> 「**The above example illustrates the importance of addressing the process by which population capability data is collected. Only by knowing that the DFS was gathered by interview and self-reporting was it possible to understand and interpret the dexterity impairment data.**」

> **★★★ 判据：自陈式能力数据在"灵巧度"上系统性失真 —— 因为人无法自测自己的灵巧度下降。**
> 后果：用自陈数据估算灵巧排除率会**低估**。机动轴中的 locomotion（有明确终点，如"上完楼梯"）与视/听（有对照物）失真小，灵巧度失真最大。
> **实操含义：** 灵巧度需求必须靠**实测**（原型试握）或**专家判定**，不能靠问卷。

---

## 2.4 用户金字塔：把十级严重度叠成一张图

### 2.4.1 金字塔的构成

> **原文（Clarkson p439）**：
> 「**User capability losses are divided into ten levels, with the lowest band 1, representing the mildest impairment and the top level, 1 0, being the most severe. Different shading is applied to differentiate mild impairment (score 1-2); moderate impairment (score 3-6); and severe impairment (score 7-1 0). The whole user pyramid represents 8 582 200 adults with functional impairments- 20% of the GB adult population.**」

| 层 | 严重度分数 | 名称 | 金字塔位置 | 设计响应 |
|---|---|---|---|---|
| 顶 | **7–10** | Severe impairment | 塔尖 | Special purpose design |
| 中 | **3–6** | Moderate impairment | 塔身 | Customisable / modular |
| 底 | **1–2** | Mild impairment | 塔基 | User-aware design |

**金字塔的底数（关键人口锚点）：**

> **原文（Clarkson p375）**：
> 「**The results showed that an estimated 8 582 200 adults in Great Britain- 20% of the adult population- had a disability according to the definition used. 34% of these disabled people had severity scores of 1 or 2, indicating quite mild disability, 45% had severity scores in the range of 3-6 (moderate disability) and 21% had scores of 7 or more (severe disability).**」

| 严重度 | 占受损人口 | 人数（推算，8,582,200 基数） |
|---|---|---|
| 1–2（轻微） | 34% | ≈ 2,918,000 |
| 3–6（中度） | 45% | ≈ 3,862,000 |
| 7+（重度） | 21% | ≈ 1,802,000 |

> **★★★★ 判据：金字塔的塔尖（重度）只有约 180 万人，塔基+塔身（轻中度）约 678 万人 —— 但产品往往只按塔尖做"特殊版"。**
> 这就是第 1 章"特殊需求三重失败"的人口学证据：**真正的大市场在塔身（中度），而塔身恰恰是最容易被"专用品"策略漏掉的一层。**
> **可执行判据：任何"包容性版本"若只覆盖塔尖，商业论证必然站不住；塔身才是可量化回报所在。**

### 2.4.2 金字塔与容斥：为什么不能简单相加

上一节已给出耦合数据。金字塔是**十级单一严重度**（由七轴加权合并而来），所以它天然解决了多重计数：

> **原文（Clarkson p374）**：
> 「**In essence, the severity of disability in thirteen specified areas of disability is first established, and then the three highest of these thirteen separate scores are combined to give an overall score, from which people are allocated to one of ten overall severity categories.**」

> **原文（Clarkson p375）**：
> 「**Capability loss Lowest worst+ 0.4 (second worst)+ 0.3 (third worst)**」

> **原文（Clarkson p436）**：
> 「**The severity of overall disability can be calculated as a weighted sum using an equation: worst + 0.4 (second worst) + 0.3 (third worst)**」

**加权公式（全书最重要的一个算式）：**

```
Overall severity = worst + 0.4 × (second worst) + 0.3 × (third worst)
```

> **★★★★ 判据：整体严重度只取"最差三项"，权重 1 / 0.4 / 0.3，其余忽略。**
> 这个公式内含三条设计判断：
> ① **最差的那一条决定命运**（权重 1，远超其余）→ 产品的最严门槛定生死；
> ② 第二、第三差仍有实质加成（0.4、0.3）→ 不能只优化一项；
> ③ 第四名以后权重 0 → 超过三项的额外损伤不影响整体判定。
> **产品含义：** 优化顺序应当是"把最差那一项拉起来"，而不是"把所有项平均改善"。这也是 ch04 排除率计算背后的合并逻辑。

> **★★★ 判据：金字塔是"人"的图形，立方体是"能力"的图形。二者不是同一个工具。**
> 金字塔（Benktzon 1993）: 一维严重度 → 十层人口 → 适合**汇报与定位**；
> 立方体（Keates 2000）: 三轴能力 → 体积覆盖 → 适合**诊断与改进**。
> 原书自己说明了继承关系：

> **原文（Clarkson p116）**：
> 「**Building on the concept of the user pyramid (Benktzon, 1993) with its banding of users by impairment level, the authors have developed a model that relates capability level, population profile and design approaches in a simple graphical format. The resultant model, the inclusive design cube (IDC) (Keates et al., 2 0 0 0), is shown in Figure 5. 3. Each axis on the cube represents user capability and the enclosed volumes reflect population coverage.**」

---

## 2.5 关于"capability spectrum"这个术语的核查（诚实说明）

任务要求覆盖 **capability spectrum**（能力谱）。本节记录检索结果。

**检索方法**：全文检索 `capability spectrum`、`ability spectrum`、`spectrum of capability`。

| 检索项 | Clarkson（611 页） | Coleman（267 页） | Fovet（573 页） |
|---|---|---|---|
| `capability spectrum` | **0 命中** | **0 命中** | **0 命中**（文本层损坏，见 §2.7） |
| `ability spectrum` | **0 命中** | **0 命中** | — |
| `spectrum of capability` | **0 命中** | **0 命中** | — |

**实际存在的相关表述：**

| 原书用语 | 出处 | 含义 |
|---|---|---|
| **`a spectrum of user / product interaction challenges, from total or partial exclusion, to difﬁ culty or frustration`** | Coleman p187 | **不是**指能力谱，指**排除程度的谱**（从完全排除到轻度挫败） |
| `the extreme end of the user spectrum` | Coleman p112 | 指用户分布的极端端，不是能力轴 |
| `the extreme end of the usability needs spectrum` | Clarkson p544 | 同上 |
| `our design populations are far more diverse than we ever realised` | Clarkson p531 | 多样性陈述 |
| **`capability variation is split between the minimally able and the able-bodied`**（作为**要反驳的误解**） | Coleman p221 | 原书明确反对"二分" |
| `since people's capabilities can range from low through medium to high levels` | Coleman p221 | **连续谱的实质表述** |

> **★★★★ 判据（关于术语）："capability spectrum / 能力谱"在本三部书中不是原书术语，而是对原书"能力连续统"思想的通行叫法。**
> 原书自己的表述是 **`capability loss as a continuum`**（Coleman p221：`the incorporation of the concept of capability loss as a continuum`）与 **`continuum version of disability`**（Clarkson p373：`the continuum version of disability, whereby the severity of capability loss ranges from very slight (category 1) to very severe (category 1 0)`）。
> **引用纪律：写"能力谱（原书称 capability loss as a continuum）"，不写"原书的 capability spectrum"。**

**原书对"连续统"最完整的一段陈述：**

> **原文（Coleman p221）**：
> 「**One of the main aspects that differentiate the simulation toolkit presented here from other existing solutions is the incorporation of the concept of capability loss as a continuum. The toolkit aims at counteracting the common misconception that capability variation is split between the minimally able and the able- bodied. In fact, since people's capabilities can range from low through medium to high levels, the toolkit is designed so as to enable a graduated simulation of different levels and combinations of physical capability losses.**」

> **原文（Clarkson p381）**：
> 「**Treating disability as a continuum raises awareness among designers, and society as a whole, that everyone has the material to be excluded from using a product at some point if the product has not been designed with sufficient consideration of the end-users.**」

> **★★★★ 判据：连续统的真正用途不是"分等级"，是"证明每个人都在这条线上"。**
> 原书用这句把"我们 / 他们"彻底拆掉：`everyone has the material to be excluded`。
> 这也是 ch08 共情方法与 ch09 极端用户法的合法性基础 —— 如果每个人都在谱上，那么"为极端端设计"就不是慈善，而是**为自己未来设计**。

### 2.5.1 "用户金字塔（user pyramid）"的术语核查（结论：真实存在）

与 capability spectrum 不同，`user pyramid` 是原书真实术语：

| 检索项 | Clarkson | Coleman |
|---|---|---|
| `user pyramid` | **命中 4 处**（p107、p116、p177、p439） | **命中**（p604 术语表） |
| `User Pyramid` | 命中（p605 关键词索引） | 命中（p604） |
| `pyramid of needs` | 命中（p33） | — |

> **原文（Clarkson p107）**：
> 「**Design approaches can also be culture-related. For instance, universal design (Bowe, 2000) dominates US, Japanese and Australian approaches to inclusive design, whereas Europe has generally tended to develop other methods, such as the User Pyramid Approach (Benktzon, 1993).**」

> **原文（Clarkson p605）**：
> 「**Some larger design companies (e.g. IDEO) have in-house user-research specialists, while otl1ers develop ilieir own particular approaches, e.g. Ergonomi De ign Gruppen's User Pyramid.**」

> **★★★ 判据：`User Pyramid` 是瑞典 Ergonomi Design Gruppen（Benktzon & Juhlins）的**专有方法名**，不是通用图式。**
> 在本书语境里，"用户金字塔"有**两个**近亲但不同的东西：
> ① **Benktzon 的 User Pyramid Approach / pyramid of needs**（能力分层 + 设计边界扩展）；
> ② **i~design 团队的 user pyramid 图**（十级严重度 × 人口百分比 × 产品排除率叠加）。
> **引用时须区分**：谈方法时指 ①，谈排除率图时指 ②。

---

## 2.6 本章概念-论点表（共 14 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | **七条能力轴** | 「seven capabilities closely related to product evaluation were selected」 | GB 残障调查 | 描述人的单位是"七条轴各自的分数"，不是"残疾类别"、也不是"年龄" | Clarkson p377 |
| 2 | **量表已对齐** | 「has been aligned to ensure that equal scores broadly relate to equivalent levels of capability」 | Martin et al. 1988 | 没有对齐就无法合并七个分数。这条是全部量化方法的隐含前提，原文只说一次 | Clarkson p435 |
| 3 | **三轴 = 三段交互** | 「perception, cognition and motor functions (Card, Moran and Newell, 1983)」 | 人机交互模型 | 三轴不是三个感官，是"感知—决策—动作"三段。产品失败在哪一段，决定改哪一段 | Clarkson p115 |
| 4 | **等权重是建模假设** | 「Applying equal weight … implies a cubic representation」 | 立方体 | 等边长是几何必需，不是重要性判断；要排序必须回到七轴看人数 | Clarkson p115 |
| 5 | **诊断→行为的转译** | 「it is not very helpful for the designer to know that certain users have 'arthritis of the knee joint'」 | ONS 量表 | 把"关节炎"换成"能爬几级台阶"，设计者才用得上。这是能力谱的核心操作 | Clarkson p468 |
| 6 | **四点行为量表** | 「Full ability / Moderate ability / Partial ability / Minimal ability」 | Coleman ch12 | 三点优势：非专业者能听懂、每级对应一个设计动作、可快速评审 | Coleman p207–208 |
| 7 | **四点量表第四列才是价值** | 每级都跟一个设计响应（无需考虑/改细节/加冗余通道/专门方案） | — | 量表的输出不是"用户画像"，是"下一步动作" | Coleman p207–208 |
| 8 | **视距随龄延长** | 「8 em at around age l 0, to SO em at age SO, to l OOcm at age 60」 | Grandjean 1986 | 60 岁阅读距离≈1 m。一切手持标签与面板按 1 m 设计 | Clarkson p53 |
| 9 | **照度需求倍增** | 「twice as much light … at age 40 … three times as much light at age 60」 | 暗适应实验 | 暗适应后 60 岁需 10×、80 岁需 100× 才能"察觉有光" | Clarkson p54 |
| 10 | **蓝紫绿三重失效** | 「Blue-violet-green combinations should be avoided」 | 晶状体黄化 | 不是审美问题：滤蓝紫 + 对比不足 + 常见色觉异常三者叠加 | Clarkson p54 |
| 11 | **两点辨别退化** | 「a reduction in 2-point discrimination」 | 皮肤触觉老化 | 触觉编码必须按"间距"设计，不能按"凸起数量"设计 | Clarkson p56–57 |
| 12 | **认知靶点三项** | 处理速度、双任务、前瞻记忆 | 驾驶、洗衣机编程 | 不是"理解力"退化。三项恰好对应绝大多数产品的隐形难点 | Clarkson p59、p61、p62 |
| 13 | **双重动作高风险** | 「Double actions such as push and twist are particularly difficult」 | 关节炎用户 | 双手操作 = 另一只手无法维持平衡。从"方便"升级为"可及" | Clarkson p52、p126 |
| 14 | **最差三项加权** | 「worst + 0.4 (second worst) + 0.3 (third worst)」 | DFS 严重度分级 | 最差项决定命运（权重 1）；优化应"拉最差那项"，而非平均改善 | Clarkson p375、p436 |
| 15 | **耦合区不可单轴改进** | 「both vision and dexterity demand need to be reduced simultaneously」 | 壶 E vs 壶 F（1,880,000 人） | 若排除来自两轴耦合，只降一轴则人数几乎不变。这是改进优先级的唯一正确算法 | Clarkson p444 |
| 16 | **多轴远超单轴之和** | 单损 4,117,000 ＜ 去重后 8,126,000 | GB 16+ | 一半以上受损者是多轴受损；单障碍设计在人口上站不住 | Clarkson p379–p380 |
| 17 | **认知障碍偏年轻** | 「Communication, behavioural and intellectual function impairments were more common among those aged under 60」 | DFS | 包容性设计 ≠ 适老化设计；年轻障碍者主战场在认知与沟通 | Clarkson p376 |
| 18 | **自陈数据在灵巧度上失真** | 「there are no obvious measures of one's own dexterity performance」 | DFS 访谈法 | 灵巧排除率会被系统性低估；必须实测或专家判定 | Clarkson p376 |
| 19 | **金字塔塔身才是市场** | 轻微 34% / 中度 45% / 重度 21% | GB 8,582,200 人 | 只做"重度专用版"漏掉最大的中度层；商业论证必须落在塔身 | Clarkson p375、p439 |
| 20 | **连续统证明人人都在线上** | 「everyone has the material to be excluded」 | — | 连续统的用途不是分等级，是拆掉"我们/他们"的二分 | Clarkson p381 |
| 21 | **老年女性为首要目标人群** | 「Older women should therefore be a priority target group for inclusive design」 | Bassey 1997 | 力量 2/3 + 更矮 5–10cm + 人数占多，三项叠加。设计基准人应是"较矮的老年女性" | Clarkson p51 |
| 22 | **消除体力需求可能是帮倒忙** | 「may be a disservice to the average older person」 | 语音控制 | 三轴模型唯一一处明确的"轴间权衡"。全代劳设计对一般老人可能是损害 | Clarkson p52 |

---

## 2.7 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **2021 年之后的模型更新** | **不存在可用源**。原计划作现代补充的第三个文本文件经核验**不是包容性设计书**（其版权页原文为 `Handbook of Research on Applying Universal Design for Learning Across Disciplines`，是 UDL 教育书），且文本层为私有符号编码不可读。**该文件已弃用，本技能不含 2021 年版内容。** | 本技能时效止于 2007 年。2010 年后的 WCAG 2.1/2.2、EN 17161、EN 301 549、ISO 9241 新版请查对应标准原文 |
| 中国人群的能力数据 | **完全没有**。全部数字是 GB（Great Britain）16+ 人口 | 中国残联抽样调查、CHARLS、GB 10000—1988；`ergonomics-ding-yulan` 有人体尺寸但与能力量表不可直接对接 |
| 除听觉外六条轴的**完整逐级定义表** | **未展开**。原书只给了 Hearing 一轴的 8 级定义（p435）；其余六轴只给分数区间与点数 | Martin et al. (1988) OPCS 原始报告；Grundy et al. (1999) DFS 报告 |
| 认知轴的可操作细分量表 | **未展开**。原书把 Communication + Intellectual functioning 合成 Cognition，但**没有**给出类似 Hearing H1–H8 的逐级行为描述 | 需查 WHO ICF 与认知评估量表；本书只有严重度分数 |
| 三轴之间的**权重**是否应相等 | **未解决**。原文用 `Applying equal weight`，但也承认这是为了画立方体 | 无后续论证。这是本章第 4 条判据标注的已知薄弱点 |
| 老年女性"2/3"力量的原始测量方法 | **只引用不复述**（Bassey, 1997） | Bassey EJ (1997) Reviews in Clinical Gerontology 7: 289–297 |
| 认知负荷的定量阈值（如"多少秒算过快"） | **只有定性**：`Very rapid presentation of information should be avoided`（p62） | 无具体秒数。需查认知老化实验文献 |
| 触觉两点辨别的具体毫米阈值 | **未给出数值**。只说"需要更远" | 需查皮肤感觉阈值标准；本书缺失 |

---

## 2.8 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 七轴 + 三类别（p377、p439） | **ch03 §3.3** | 立方体三轴的直接来源 |
| 十级严重度 + 金字塔（p439） | **ch03 §3.4** | WINIT 人口模型的分层基础 |
| 「最差 + 0.4 + 0.3」加权（p375） | **ch04 §4.4** | 排除率合并的核心算式 |
| 耦合区（p444） | **ch04 §4.6** | 多重计数消除；改进优先级算法 |
| 四点量表（Coleman p207） | **ch06 §6.3** | 专家评审的速查口径 |
| 能力连续统（Coleman p221） | **ch07 §7.2** | 模拟工具被标定为"梯度"而非"二分"的理由 |
| 边界用户 / 极端用户 | **ch08 §8.1、ch08 §8.2** | 金字塔分层对应的用户选型 |
| 老年女性为首要目标（p51） | **ch02 内部** | 与百分位选择冲突，见下 |
| 诊断→行为转译（p468） | **ch09** | 用户研究里"问什么"的依据 |

### 2.8.1 跨技能挂钩（本机已有技能）

| 本技能内容 | 挂钩技能 | 关系与用法 |
|---|---|---|
| **第 5–95 百分位设计默认漏掉 10%（Clarkson p442：`the remaining 1 0% of users may be excluded, which in the UK corresponds to 4 600 000 adults`）** | **`ergonomics-ding-yulan`** | **这是两本书最紧的接口，必须连读。** 丁玉兰给方法：百分位怎么选、产品尺寸设计分三类（I 型取上限 / II 型取下限 / III 型取 P5–P95）、满足度怎么算。本技能给后果：那 10% 是谁、如何按七轴拆开、如何换算成 460 万英国人。<br>**合用判据：算完满足度之后，必须再问一句"被排除的那部分人属于哪几轴、人数多少、是否有耦合"。** |
| **"设计基准人应是较矮的老年女性"（Clarkson p51）** | **`ergonomics-ding-yulan`** | 丁玉兰的百分位表默认按性别分组，但不给"该选哪一组"的规范性建议。本技能补上：`Older women should therefore be a priority target group`。<br>**操作顺序：先用本技能定人群与轴 → 再用丁玉兰查该人群的 P5/P95 数值 → 再回本技能算排除率。** |
| **显示与听觉的定量需求（p54 照度 3×/10×/100×；p56 低频优先）** | **`ergonomics-ding-yulan`** | 丁玉兰 ch08「显示装置设计」有字符尺寸、视角、照度标准；本技能补"随年龄的倍数修正"。<br>**合用判据：按丁玉兰定基准值，再乘本技能给出的年龄倍率（60 岁 ×3 照度、视距 1 m）。** |
| **"双手操作是机动轴硬门槛"（p52、p126）** | **`product-structure-liubaoshun`** | 刘宝顺的壳体/连接/密封结构里，大量结构（旋锁瓶盖、卡扣、螺纹）天然要求双手或双重动作。本技能给"这是可及性红线"的人群判据，刘宝顺给"怎么改成单手可操作"的机构方案。<br>**判据：凡结构方案需要 push and twist，先过本技能这一关再谈结构优劣。** |
| **认知靶点三项（处理速度 / 双任务 / 前瞻记忆）** | **`design-psychology-norman`** | 诺曼的"行动七阶段"与"执行鸿沟/评估鸿沟"解释了**为什么**认知负荷会致错；本技能给了**哪三项**认知子能力在老化中退化最快、以及**怎么改**（逐步提示、自然频次、禁止多源竞争）。<br>**合用判据：用诺曼定位鸿沟在哪一阶段，用本技能判断该阶段的需求是否超出目标人群阈值。** |
| **能力谱的"行为而非诊断"原则（p468）** | **`design-psychology-norman`** | 诺曼强调"设计者不是使用者"，本技能给了"如何把使用者翻译成设计参数"的具体模板（Hearing H1–H8 那种写法）。<br>**操作：把诺曼的用户模型缺口，用本技能的量表填上。** |
