# 第 1 章：可用性是什么，以及产品为什么难用

> **原书 PDF 页序 p41–p58（18 页）**｜**本版逐页读完全部 18 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N；实测书内印刷页 = PDF 索引 − 38）
>
> **读法说明**：按原书 `1.x` 小节逐节展开，不跳节。原书本章为 Part I 第 1 章。
> 每节含【原文摘录】+【判据提炼】。
> 引文说明：文本层把 `fi`/`fl` 抽取成了合字字形 `ﬁ`/`fl`，本版统一还原为普通字母；弯引号 `''` 还原为 `"`。**用词与数字一律未改。**

---

## 1.1 总纲：可用性不是"好看"，是"没有阻碍"

Rubin & Chisnell 全书的立论起点只有一句：可用性只有在**缺失**的时候才被感知到；因此不能用"感觉好不好"来判断，只能用"有多少处让人卡住"来测量。本章的任务是把"可用"拆成可测量的六个属性，再给出产品难用的五个结构性原因——后者决定了测试该盯住什么。

---

## 1.2 什么是"可用"

### 1.2.1 核心定义

> **原文（p42）**：
> 「In large part, what makes something usable is the **absence of frustration** in using it. As we lay out the process and method for conducting usability testing in this book, we will rely on this definition of "usability;" when a product or service is truly usable, **the user can do what he or she wants to do the way he or she expects to be able to do it, without hindrance, hesitation, or questions**.」

> **★★★ 判据：可用性 = 无阻碍 + 无迟疑 + 无提问**
> 三个可观测的红旗："hindrance"（走不下去）、"hesitation"（停下犹豫）、"questions"（回头问人）。
> 这三样都能在测试现场直接计数，不需要问被试"你觉得好用吗"。
> **推论**：任务执行过程中的**停顿**和**提问**本身就是数据，不是噪声。

### 1.2.2 六个属性

> **原文（p42）**：
> 「To be usable, a product or service should be **useful, efficient, effective, satisfying, learnable, and accessible**.」

| 属性 | 原文定义（p42） | 怎么测 |
|---|---|---|
| **Usefulness** | 「the degree to which a product enables a user to achieve his or her goals, and is an assessment of the **user's willingness to use the product at all**」 | 问"你会不会用它"，不看任务成败 |
| **Efficiency** | 「the quickness with which the user's goal can be accomplished accurately and completely and is **usually a measure of time**」 | 计时 |
| **Effectiveness** | 「the extent to which the product behaves in the way that users expect it to and the ease with which users can use it to do what they intend」，**usually measured quantitatively with error rate** | 计错误率 |
| **Learnability** | 「**a part of effectiveness**」，用户在既定训练量后能否达到既定熟练度；也指不常用用户隔一段时间能否重新学会 | 首次成功率 vs 复测成功率 |
| **Satisfaction** | 「the user's **perceptions, feelings, and opinions** of the product, usually captured through both written and oral questioning」 | 量表 + 口头 |
| **Accessibility** | 见 1.2.4 | 见 ch11 |

> **★★★ 判据：六个属性里有四个可以用"次数/秒数"测，只有 Usefulness 与 Satisfaction 必须问**
> 设计测试时先确定这一轮要测哪几个属性；属性不同，任务写法和记录表完全不同。

> **原文（p42）**：
> 「Interestingly enough, **usefulness is probably the element that is most often overlooked** during experiments and studies in the lab.」

> **★★ 判据：最容易漏测的是"有没有用"，因为它测不出来**
> 不可用的产品在实验室里会被"能不能完成任务"的指标掩盖；一个设计精良但没人需要的东西，任务成功率可以是 100%。
> **做法**：在招募筛选阶段就把 Usefulness 挡在门外（筛"真的会做这件事的人"，见 ch07），而不是在测试里补问。

### 1.2.3 数字不能替代判断

> **原文（p43）**：
> 「let us caution that making a product usable is never simply the ability to generate numbers about usage and satisfaction. While **the numbers can tell us whether a product "works" or not**, there is a distinctive qualitative element to how usable something is as well, which is hard to capture with numbers and is difficult to pin down.」

> **★★ 判据：数字负责"是不是坏了"，定性负责"为什么坏、怎么修"**
> 同一章用医生作比：任何人都能量血压脉搏，但"解释这些数字并为具体病人开处方"才是医生的价值。
> **对测试的后果**：只报"任务成功率 60%"的报告是没写完的；必须带"错在哪一步、为什么"。

### 1.2.4 无障碍是"兄弟"，不是"分支"

> **原文（p43）**：
> 「**Accessibility and usability are siblings.** In the broadest sense, accessibility is about having access to the products needed to accomplish a goal. But in this book when we talk about accessibility, we are looking at **what makes products usable by people who have disabilities**.」

> **原文（p43）**：
> 「Making a product usable for people with disabilities — or who are in special contexts, or both — **almost always benefits people who do not have disabilities**.」

> **★★★ 判据：为残障做的可用性改造，收益外溢到临时受限与情境受限**
> 原文列举的外溢对象：受伤（临时）、注意力被分割、强光或光线不足（情境）。
> **做法**：特殊人群的招募要求写进筛选问卷，不要留到测试当天才想起（详见 ch11 §11.4 与 `inclusive-accessibility-design` 技能）。

---

## 1.3 产品为什么难用：五个结构性原因

### 1.3.1 原因 1：开发聚焦于机器/系统

> **原文（p45）**：
> 「Because the development of a system or product is an attempt to improve human performance in some area, designers should consider these three components during the design process. All three affect the final outcome of how well humans ultimately perform. Unfortunately, of these three components, **designers, engineers, and programmers have traditionally placed the greatest emphasis on the activity component, and much less emphasis on the human and the context components**.」

Bailey 人因绩效模型的三要素，原文作三行列出（p45）：

> **原文（p45）**：
> 「The human」
> 「The context」
> 「The activity」

> **★★ 判据：测试的观察对象必须包含"人"和"场景"，只测"活动"就是重复开发者的偏见**
> 这解释了为什么"按说明书把任务做完"的测试经常什么也发现不了——它测的正好是开发者最擅长的那一维。

### 1.3.2 原因 2：目标人群在扩大和变化

> **原文（p46）**：
> 「Because of this similarity, the developers practiced "**next-bench**" design, a method of designing for the user who is **literally sitting one bench away in the development lab**.」

> **原文（p46）**：
> 「More important, **today's user is not even remotely comparable to the designer in skill set, aptitude, expectation**, or almost any attribute that is relevant to the design process.」

> **★★★ 判据："隔壁工位设计法"失效，是可用性测试存在的根本理由**
> 只要被试和设计者同质，测试就退化成了"自测"。**异质性（而非人数）才是样本质量的第一指标。**

### 1.3.3 原因 3：设计可用产品本身很难

> **原文（p47）**：
> 「The design of usable systems is a difficult, unpredictable endeavor, yet **many organizations treat it as if it were just "common sense."**」

> **原文（p47）**：
> 「This trivializing of usability creates a more dangerous situation than if product designers freely admitted that designing for usability was not their area of expertise」

> **★★ 判据：把可用性当"常识"，比承认不懂更危险**
> 后果是没人做操作化定义，于是也没有可验证的成功标准（对照 ch05 的 SCC）。

### 1.3.4 原因 4：专业分工不整合

> **原文（p48）**：
> 「Even more interesting is how often organizations unknowingly exacerbate this lack of integration by **usability testing each of the components separately**.」

> **★★★ 判据：分件通过 ≠ 整体可用**
> 原文结论：「it matters little if each component is usable within itself. Only if the components work well together will the product be viewed as usable」（p48 同段）。
> **做法**：测试任务必须**横跨**界面 + 帮助 + 文档，不能按组件切块测试。

### 1.3.5 原因 5：设计与实现不匹配

> **原文（p49）**：
> 「**Design, in this case, relates to how the product communicates, whereas implementation refers to how it works.**」

> **★ 判据：实现能力提升后，瓶颈转到"沟通"这一侧**
> 所以可用性缺陷越来越常出现在措辞、标签、层级、提示，而不是"功能做不出来"。测试的观察点要跟着转向。

---

## 1.4 本章概念-论点表（共 12 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | 可用（usable） | 「the user can do what he or she wants to do the way he or she expects to be able to do it, without hindrance, hesitation, or questions」 | 电商网站找货、查库存、查运费 | 可用性有三个可计数的负向指标：阻碍/迟疑/提问；不必问感受 | p42 |
| 2 | 六属性 | 「useful, efficient, effective, satisfying, learnable, and accessible」 | 全书通用 | 六属性里四个可量化、两个必须访谈；先定属性再定任务 | p42 |
| 3 | Usefulness 漏测 | 「usefulness is probably the element that is most often overlooked」 | 实验室研究 | "有用"要在招募阶段筛掉，不能靠测试补 | p42 |
| 4 | 数字的边界 | 「the numbers can tell us whether a product "works" or not」 | 医生看生命体征 | 量化判"坏没坏"，定性判"怎么修" | p43 |
| 5 | 无障碍 | 「Accessibility and usability are siblings.」 | 残障 / 临时受伤 / 强光 | 为残障改的东西外溢到所有情境受限者 | p43 |
| 6 | 不可测的可用性 | 「it is impossible to measure the usability of something. You can only measure how unusable it is」 | 全书方法论 | 只能数"卡住几次"，不能给"可用度打分" | p44 |
| 7 | 人因绩效三要素 | 三行为「The human」「The context」「The activity」，开发只重 activity | Bailey 模型 | 测试的观察维度必须覆盖人与场景 | p45 |
| 8 | next-bench design | 「designing for the user who is literally sitting one bench away」 | 早期计算机爱好者 | 样本同质 = 自测；异质性优先于人数 | p46 |
| 9 | 常识化陷阱 | 「many organizations treat it as if it were just "common sense."」 | Will Rogers 引语 | 不做操作化定义 → 无验收标准 | p47 |
| 10 | 分件测试谬误 | 「usability testing each of the components separately」 | 界面/帮助/文档分测 | 任务必须横跨组件 | p48 |
| 11 | 设计与实现 | 「Design ... relates to how the product communicates, whereas implementation refers to how it works.」 | 新一代开发工具 | 缺陷重心移到措辞与层级 | p49 |
| 12 | 测试在 UCD 中的位置 | 「Usability testing is not UCD itself; it is merely one of several techniques」 | ISO 13407 四项特征 | 测试是手段之一，不是目的 | p51 |

---

## 1.5 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| 六属性的量化阈值 | 只给定义与示例（如"95% 用户 10 分钟内完成"），未给行业通用阈值 | 本章未展开；阈值需按项目自定，见 ch05 §5.6 |
| 无障碍的具体标准条文 | 只给"是兄弟"的定位与伦理指向，未列 WCAG/Section 508 条款 | 本章未展开，见 ch11 §11.4 与 `inclusive-accessibility-design` 技能 |
| 五原因的经验证据 | 五个原因是作者归纳，未给实证数据 | 本章未展开（属作者判断，非研究结论） |
| 可用性经济性测算 | 只提"降低支持电话/提升复购"方向，无模型 | 本章 p44 只一笔带过；详见 ch02 §2.4 的盈利性列举 |
| 本章 p41–p58 中图 1-1/1-2/1-3 的原始图示 | 文本层只有图注，图形本身不可提取 | 已文字化模型三要素与整合/非整合对照，图形细节未录 |

---

## 1.6 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 六属性 → 测哪几个 | 本书 ch05 测试计划 | 属性决定数据采集项（判据表 §5.6） |
| Usefulness 在招募阶段筛 | 本书 ch07 找人与选人 | 筛选问卷是"有用性"的唯一入口 |
| 分件测试谬误 | 本书 ch08 任务场景设计 | 任务必须横跨组件，见"substantial amount of work" |
| 无障碍是兄弟 | 本书 ch11 变体 | 特殊人群测试的完整做法 |
| 无障碍与包容性 | `inclusive-accessibility-design` 技能 | 标准条文与人群细分，本章只给定位 |
| 三要素（人/场景/活动） | `ergonomics-ding-yulan` 技能 | 人机系统总体设计（ISO 6385）即此三要素的工程化版本 |
| "阻碍/迟疑/提问"三红旗 | `design-psychology-norman` 技能 | 对应执行鸿沟与评估鸿沟的可观测表现 |
