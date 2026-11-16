# 第 1 章：研究问题与方法选择（把"想问什么"翻译成"用哪个方法"）

> **原书 PDF 页序 p7–p9、p11（共 4 页：导论 2 页 + AEIOU 入口 1 页 + A/B Testing 1 页）**｜**本版实读全部 4 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）；**书内印刷页 = PDF 索引 − 1**（全书实测偏移恒为 +1）
>
> **读法说明**：本书按方法名 A–Z 排列（100 个方法，每个方法占 1 页正文 + 1 页图例），**没有连续的方法论章节**。
> 本章按"方法选择"这一主题重组：先取导论 p7–p8 的方法谱系五维与设计五阶段，再用 p11、p9 两个方法条目演示"维度怎么落到具体方法上"。
> 每节含【原文摘录】+【判据提炼】。

---

## 1.1 总纲：这本书不是"方法大全"，而是"对话结构库"

作者在导论第一句就否定了"工具书"的定位：

> **原文（p7）**：
> 「Please note: this is not just a book about methods of design. Yes, we know what the cover says. But the truth is, we believe that the power of the methods and techniques included in this book is that each provides an opportunity to **structure conversations** that can help us better understand and empathize with people, and as a result build more meaningful products.」

> **★★★ 判据：选方法的第一问不是"哪个方法高级"，而是"我要和谁、在什么时候、谈成什么对话"。**
> 展开：方法的产出物（报告、图、画像）只是对话的副产品。把方法当"证据生产器"，
> 就会在错误的时点用正确的方法——这是研究设计里最常见的浪费。

作者进一步把"专家性"重新定义：

> **原文（p8）**：
> 「The work of design teams is not about expertise in any single type of method. It is also not about software, or the deliverables we develop. **Our work is about knowing how to structure the conversations we need** to inform the best design solutions for the work we do.」

> **★★★★ 判据：研究能力 = 编排能力，不是执行能力。**
> 这条判据决定了本技能的结构：**方法执行层交给 `usability-testing` 等专项技能，
> 本技能只负责"什么时候该用哪一类、最少要多少样本、产出物长什么样"。**

最后一句给出使用方法论：

> **原文（p8）**：
> 「Review them, try them, prioritize them, and sequence them based on the success criteria and focus of problems you want to solve. **Treat them as conversations.** We have.」

---

## 1.2 方法谱系五维（p7）——本书唯一的"方法选择坐标系"

这是全书最有操作价值的一段，也是本技能"方法选择"的骨架。原书用五个维度给 100 个方法打标签：

> **原文（p7）**：
> 「An info-graphic on the bottom left of each page characterizes the methods and techniques using several useful research facets. The **behavioral/attitudinal** facet suggests the type of content most appropriately targeted by the method. **Quantitative/qualitative** characterizes the form in which that content is typically collected and communicated. **Innovative/adapted/traditional** describes whether the method is original to design, adapted from other disciplines, or used traditionally across disciplines. **Exploratory/generative/evaluative** frames the methods by their primary purpose of early exploration, concept generation, or testing and evaluation. And finally, **participatory/observational/self-reporting/expert review/design process** describes the typical roles of the researcher and participant, with design process methods being those conducted by design teams as an integral part of an overall approach.」

拆成可查的表：

| # | 维度 | 两端 | 它回答的问题 | 选错这一维的后果 |
|---|---|---|---|---|
| 1 | **行为 / 态度** | Behavioral ↔ Attitudinal | 我要的是"人做了什么"还是"人怎么想" | 想验行为却只问态度 → 得到"说法"而非"做法" |
| 2 | **定量 / 定性** | Quantitative ↔ Qualitative | 我要"多少个"还是"为什么" | 样本 8 人却做统计分析 → 数字不可外推 |
| 3 | **创新 / 改编 / 传统** | Innovative ↔ Adapted ↔ Traditional | 方法来自设计本行还是借来的 | 借来的方法不改造 → 水土不服 |
| 4 | **探索 / 生成 / 评价** | Exploratory ↔ Generative ↔ Evaluative | 我在项目哪个目的上 | 探索期做评价 → 过早收敛 |
| 5 | **参与 / 观察 / 自报 / 专家评审 / 设计过程** | 五类角色 | 研究者与参与者各扮演什么 | 角色错配 → 数据被污染 |

> **★★★ 判据（维度 1）：行为与态度是两个数据源，不是两种精度。**
> 原文 p189 的三角验证一节把这条讲透了：「The most common occurrence of triangulation is to
> combine observational methods with self-report methods such as questionnaires or interviews.」
> **态度数据可以解释行为，但不能替代行为。**

> **★★★ 判据（维度 5）：「观察 / 自报 / 专家评审」是三档成本递增、真实性递减的替代关系。**
> - **专家评审**（认知走查、启发式评估）：**不需要用户**，成本最低，只能发现"基线问题"；
> - **观察**（观察、影子、情境访谈）：**要用户在场**，能看真行为；
> - **自报**（问卷、日记、焦点小组）：**用户不在场也能做**，但拿的是"人对自己行为的叙述"。
> 三者是**互补而非替代**——p33 认知走查那节明说：「using them together—rather than in lieu of one another—is always recommended.」

---

## 1.3 设计五阶段（p8）——方法的时间轴

> **原文（p8）**：
> 「Phase 　is **Planning, Scoping, and Definition**, where project parameters are explored and defined. Phase 　, **Exploration, Synthesis, and Design Implications**, is characterized by immersive research and design ethnography, leading to implications for design. Phase 　is **Concept Generation and Early Prototype Iteration**, involving participatory and generative design activities. Phase 　is **Evaluation, Refinement, and Production**, based on iterative testing and feedback. Phase 　is **Launch and Monitor**, the quality assurance testing of design to ensure readiness for market and public use, and ongoing review and analysis to course-correct when necessary.」

> **⚠ 文本层缺字的诚实说明**：上引原文中 `Phase 　` 后的**序号在提取文本里是缺失的**（原文逐字为 `Phase ` 后直接接 `is`／`, Exploration…`）。
> 这是 PDF 文本层的序号丢失（原书排版把数字做成了图元），**不是本书没写序号**。
> 本版**保留空缺不补数字**，按出现顺序标注为阶段 ①②③④⑤；
> 判断"哪个阶段是第几"所用依据是**句序**，而非原文可见的阿拉伯数字。

> **★★★ 判据：五阶段不是瀑布，而是"证据类型"的切换。**
> 阶段② 拿"含义"（implications），阶段③ 拿"概念"，阶段④ 拿"缺陷"，阶段⑤ 拿"趋势"。
> **同一个方法在错误阶段使用，产出的东西类型不对**——例如在阶段② 做木马（Wizard of Oz），
> 拿到的是"这个概念能不能用"，而阶段② 真正要的是"这个领域的问题结构是什么"。

**五阶段 ↔ 方法家族的对应（据 p8 与各方法条目自述的 Design Phase 标签）**：

| 阶段 | 目的 | 主力方法（本书方法号） | 典型产出物 |
|---|---|---|---|
| ① 规划、界定 | 界定项目参数 | 39 探索性研究、53 文献综述、80 利益相关者地图、51 KPI | 研究问题书、范围界定 |
| ② 探索、综合、含义 | 建立共情与领域认知 | 27 设计人种志、20 情境访谈、57 观察、59 参与式观察、76 影子跟踪、30 日记、24 文化探针、89 触石之旅 | 设计含义清单（design implications） |
| ③ 概念生成、早期原型迭代 | 生成并粗筛概念 | 44 生成式研究、21 创意工具包、41 弹性建模、14 拼贴、79 快速约会、58 并行原型、66 原型 | 概念方案、低保真原型 |
| ④ 评价、精化、量产 | 找缺陷并修 | 94 可用性测试、87 出声思维、68 RITE、46 启发式评估、13 认知走查、15 竞品测试、29 欲望测试 | 问题清单 + 严重度 |
| ⑤ 上市、监控 | 上线后校偏 | 01 A/B 测试、97 网站分析、83 调查、93 可用性报告（长期趋势） | 指标趋势、迭代建议 |

> **★★ 判据：阶段⑤ 的方法（A/B、分析）不能倒推回阶段②。**
> p9 A/B Testing 一节明说：「A/B testing won't help you understand **why** the design was
> preferred over the alternate.」它能告诉你"哪个赢"，永远不能告诉你"为什么"。

---

## 1.4 两个"维度落点"实例（p9、p11）

导论给了坐标系，真正落点是方法条目里那行小标签。取两个端点方法看：

**① A/B Testing（方法 01，p9）——纯评价、纯定量、纯行为**

> **原文（p9）**：
> 「Use A/B testing to compare two versions of the same design to see which one performs **statistically better** against a predetermined goal.」

> **原文（p9）**：
> 「The tests are run by randomly assigning different people down two paths—the "A" test and the "B" test—until a **statistically relevant sample size** is reached.」

> **★★★ 判据：A/B 的样本量不是"人数"，是"达到统计显著"——这是一个算出来的数，不是拍出来的数。**
> 本书**未给任何具体数值**（未给每臂最少人数、未给置信水平、未给检验方法）。
> 这一点必须诚实标注，不能替它补。

同时作者明确划出边界，这条边界正是"方法选择"的核心：

> **原文（p9）**：
> 「Even though there is a benefit to being able to measure which design generates better results, A/B testing won't help you understand why the design was preferred over the alternate. A/B testing is not a replacement for qualitative methods that can assess your customers' desires, attitudes, and needs, nor can it uncover larger problems like whether customers feel that they can trust your site or that it is credible.」

> **★★★★ 判据：任何单一方法都有"它结构上不可能回答的那类问题"。**
> 选方法前先问："这个问题，这个方法在原理上有没有能力回答？"
> 不是"这个方法好不好"，而是"这个方法能不能"。

**② AEIOU（方法 02，p11）——观察的编码骨架**

> **原文（p11）**：
> 「AEIOU is an organizational framework reminding the researcher to attend to, document, and code information under a guiding taxonomy of **Activities, Environments, Interactions, Objects, and Users**.」

五个字母的定义（逐字）：

> **原文（p11）**：
> 「• **Activities** are goal-directed sets of actions. What are the pathways that people take toward the things they want to accomplish, including specific actions and processes?
> • **Environments** include the entire arena in which activities take place. For example, what describes the atmosphere and function of the context, including individual and shared spaces?
> • **Interactions** are between a person and someone or something else, and are the building blocks of activities. What is the nature of routine and special interactions between people, between people and objects in their environment, and across distances?
> • **Objects** are the building blocks of the environment, key elements sometimes put to complex or even unintended uses, possibly changing their function, meaning, and context. For example, what are the objects and devices people have in their environments, and how do these relate to their activities?
> • **Users** are the people whose behaviors, preferences, and needs are being observed. Who is present? What are their roles and relationships? What are their values and biases?」

> **★★★ 判据：AEIOU 的价值不是"五个类别"，而是它强制区分了"物"与"环境"。**
> 多数观察记录会把"工具"和"空间"混为一谈。AEIOU 把 Objects（可被挪用的物）
> 与 Environments（不可挪动的场所氛围）分开——**产品设计最关心的恰恰是
> "用户怎样把 Object 用出它设计意图之外的功能"**（原文说 Objects「sometimes put to
> complex or even unintended uses, possibly changing their function, meaning, and context」）。

> **★★ 判据：AEIOU 是"提醒器"（reminding），不是"计数表"。**
> 原文定位为「an easy mnemonic for guiding and coding observations」与「As a heuristic, or rule of thumb」。
> 把它当编码本逐项打勾，会丢掉意外发现——这与 p121 观察一节对"预设分类"的警告同源。

---

## 1.5 本章概念-论点表（共 10 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | **方法即对话结构** | 「each provides an opportunity to **structure conversations** that can help us better understand and empathize with people」 | 全书 100 个方法 | 选方法 = 选"跟谁在什么节点谈什么"；产出物只是对话残余 | p7 |
| 2 | **研究能力 = 编排能力** | 「Our work is about knowing how to structure the conversations we need」 | 设计团队跨方法协作 | 会做不等于会用；本技能只做编排层 | p8 |
| 3 | **行为/态度维度** | 「The **behavioral/attitudinal** facet suggests the type of content most appropriately targeted by the method」 | 观察（行为）vs 问卷（态度） | 两类数据源，态度解释行为但不能替代 | p7 |
| 4 | **定量/定性维度** | 「**Quantitative/qualitative** characterizes the form in which that content is typically collected and communicated」 | A/B（定量）vs 访谈（定性） | 定性不是"小样本的定量"，是另一种数据形态 | p7 |
| 5 | **创新/改编/传统维度** | 「**Innovative/adapted/traditional** describes whether the method is original to design, adapted from other disciplines, or used traditionally」 | 情境访谈改编自民族志 | 借来的方法必须标注"改造点"，否则误用原文前提 | p7 |
| 6 | **探索/生成/评价维度** | 「**Exploratory/generative/evaluative** frames the methods by their primary purpose」 | 三阶段方法分组 | 目的决定方法；同一方法错阶段使用=证据类型错 | p7 |
| 7 | **五类研究者角色** | 「**participatory/observational/self-reporting/expert review/design process** describes the typical roles of the researcher and participant」 | 参与式设计 vs 专家评审 | 专家评审→观察→自报是"成本递增、真实性递减"的替代链 | p7 |
| 8 | **五阶段** | 「Phase 1 is **Planning, Scoping, and Definition**…Phase 5 is **Launch and Monitor**」 | 全书 TOC 的阶段标注 | 阶段切换=证据类型切换，不是流程美化 | p8 |
| 9 | **A/B 的解释力边界** | 「A/B testing won't help you understand **why** the design was preferred over the alternate」 | 注册转化率对比 | 单一方法有"原理上答不了"的问题类；先问"能不能"再问"好不好" | p9 |
| 10 | **AEIOU 的物/境分离** | 「Objects…sometimes put to complex or even unintended uses, possibly changing their function, meaning, and context」 | 观察工作现场 | 产品设计最关心"物被用出设计意图之外"的那部分 | p11 |

---

## 1.6 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **样本量的具体数字** | **导论与本章实读的 4 页中，一个具体人数都没有**；A/B 只写「statistically relevant sample size」 | 本书其余方法条目（部分给了，见 ch06 汇总）；统计学教材算 A/B 样本量 |
| **A/B 的统计方法** | **未展开**：未给显著性水平、检验类型、最小可检测效应 | 统计学/实验设计教材；本书 p83 Experiments（未实读） |
| **五阶段与工期的对应** | **未展开**：只给阶段名与目的，未给每阶段典型周数 | 项目管理资料；本技能不负责排期 |
| **方法条目的完整 100 个** | 本技能**实读 44 个完整条目**（每个 1 页正文），其余 56 个仅据 p5–p6 目录判定"与实体产品设计关系较远"后未纳入 | 原书 A–Z 全文；未读清单见 SKILL.md「实读范围」节 |
| **"如何写研究问题"** | **未展开**：本书假设研究问题已存在，只给方法 | 用户研究流程类专著（goodman 那本原有此内容，**本机缺失**，见 SKILL.md「源书缺失说明」） |

---

## 1.7 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 维度 5「观察/自报/专家评审」三档 | 本技能 ch03、ch04、ch09 | ch03=观察档，ch04=自报档，ch09=专家评审档；本章是总纲 |
| 五阶段的时间轴 | 本技能 ch06（样本量） | 阶段越往后，样本量越偏向"可算"，越往前越偏向"够用即止" |
| 行为/态度分离 | `design-psychology-norman` ch01（预设用途/可视性） | 诺曼讲"设计者以为的模型"，本章讲"怎么发现用户真实模型"；前者是理论，后者是取证手段 |
| 研究问题 → 方法 | `design-methodology-liuguanzong` ch03（事理学：先研究"事"再组织"物"） | 柳冠中的"外部因素"分析需要本章的方法来取证；本章提供取证的合法性与边界 |
| 探索阶段的共情 | `product-design-styling-dabbs` ch01（用户画像五问） | 本章 ch08 的人物画像给出"五问的答案从哪来" |
| 可用性测试的定位 | `usability-testing` 技能（执行层） | 本章只判"阶段 4 该不该上可用性测试"；**怎么测详见 usability-testing 技能** |
