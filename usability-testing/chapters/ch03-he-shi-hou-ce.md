# 第 3 章：什么时候测——四种测试类型与生命周期

> **原书 PDF 页序 p65–p82（18 页）**｜**本版逐页读完全部 18 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N；书内印刷页 = PDF 索引 − 38）
>
> **读法说明**：按原书 `3.x` 小节逐节展开，不跳节。
> 每节含【原文摘录】+【判据提炼】。
> 引文说明：合字 `fi`/`fl` 已还原，弯引号已还原为直引号；**用词与数字未改**。

---

## 3.1 总纲：测试类型由"三个变量"决定，不由名字决定

> **原文（p65）**：
> 「Some type of usability testing fits into every phase of a development lifecycle. The type of testing is distinguished by **the research questions asked, the state of the completeness of the product, and the time available for implementing solutions** to problems revealed in testing.」
> **★★★★ 判据：判断该做哪种测试，只问三个问题**
> ① 我要回答什么问题？② 产品完整到什么程度？③ 发现问题后还有多少时间可改？
> 三个答案定了，类型就定了。**不要按"我们上次做的是哪种"来选。**

> **原文（p65）**：
> 「We discuss three tests — exploratory (or formative), assessment (or summative), and validation (or verification) tests — at a high level, according to the approximate point in the product development lifecycle at which each would be administered. **The fourth type of test, the comparison test, can be used as an integral part of any of the other three tests and is not associated with any specific lifecycle phase.**」

> **★★★ 判据：比较测试不是一个"阶段"，而是一个"叠加维度"**
> 前三类按生命周期排序；比较测试横切三者——探索期可以做"两个概念稿比"，验证期可以做"新旧版本比"。
> **四个类型不是四选一，是 3＋1**：3 个阶段类型 + 1 个横切类型。

### 3.1.1 术语对照（原文的并称写法）

原文用斜杠把同义术语并列，这是**术语混乱的正面回应**（p65 明说「Often, different terms are used to describe identical testing techniques. Needless to say, this can be extremely confusing.」）：

| 原文写法 | 中文 | 生命周期位置 |
|---|---|---|
| exploratory / **formative** | 探索性 / 形成性 | 早期，概念未定 |
| assessment / **summative** | 评估性 / 总结性 | 中早期，高层设计已定 |
| validation / **verification** | 验证性 / 确认性 | 后期，临近发布 |
| comparison | 比较 | 可叠加于任一类 |

> **★★ 判据：formative 与 exploratory 在本书是同义词，不要当成两个概念**
> Barnum 书里 formative/summative 是主分类（见 §3.6），Rubin 书里是 exploratory/assessment 的别名。**两本书的术语体系不同，交叉引用时必须写清是哪本书的口径。**

---

## 3.2 探索性/形成性测试（Exploratory or Formative）

### 3.2.1 何时做

> **原文（p67）**：
> 「The exploratory study is conducted **quite early in the development cycle**, when a product is still in the preliminary stages of being defined and designed (hence the reason it is sometimes called "formative").」

原文给的时间点条件：用户画像与使用模型（或任务分析）应已定义；团队正在纠结功能规格与早期模型；或需求规格刚完成、设计即将开始（p67）。

### 3.2.2 目标

> **原文（p67）**：
> 「The main objective of the exploratory study is to examine the effectiveness of **preliminary design concepts**. If one thinks of a user interface or a document as being divided into a **high-level aspect** and a more detailed aspect, the exploratory study is concerned with the former.」

原文列出的高层问题（p67–p68），可作为任务设计的上游清单：

| 面向 | 原文问题 |
|---|---|
| Web/软件界面 | 「Supports users' tasks within a goal.」「Communicates the intended workflow.」「Allows the user to navigate from screen to screen and within a screen.」 |
| 文档 | 「Overall organization of subject matter」「Whether to use a graphic or verbal approach」「How well the proposed format supports findability」 |
| 用户假设 | 「What do users conceive and think about using the product?」「Does the product's basic functionality have value to the user?」「How easily do users make inferences about how to use this user interface, based on their previous experience?」 |

> **原文（p68）**：
> 「The importance of this type of early analysis and research cannot be over emphasized, for **this is the point in time when critical design decisions set the stage for all that will follow**. ... Similarly to building a house, once you lay the foundation for one type of model, you cannot simply build a totally different model without first ripping out the existing framework.」

> **★★★ 判据：探索期的错误是"地基错误"，越早越便宜**
> 判据的实操含义：探索期测试的目标不是"找 bug"，而是**验证关于用户的假设**。若假设错了，后面所有测试都只是在一个错地基上挑毛病。

### 3.2.3 方法要点

> **原文（p69）**：
> 「Exploratory tests usually dictate **extensive interaction** between the participant and test moderator to establish the efficacy of preliminary design concepts.」

关键做法（p69）：
- **保真度可以极低**：静态屏、纸质草稿、2D/3D 泡沫板、黏土、塑料模型
- **只需实现到能回答测试目标的深度**：「one need only show enough functionality to address the particular test objective」
- **横向 vs 纵向原型**：「This type of prototype is referred to as a "**horizontal representation**," since the user can move left or right but is limited in moving deeper.」反之需要深入则做「vertical representation」
- **可以只做走查不做任务**：「if it is too early to perform tasks, then the user can simply "walk through" or review the product」
- **主持人与被试并肩坐**：「the test moderator and participant can sit side by side」

> **原文（p69）**：
> 「Unlike later tests where there is more emphasis on measuring how well the user is able to perform by collecting quantitative data, here you **strive to understand why the user performs as he or she does by collecting qualitative data**.」

> **★★ 判据：探索期优先收集"为什么"，量化数据是副产品**
> 这与评估期正好相反。混用会导致：探索期过早锁定指标 → 错过概念层面的问题。

### 3.2.4 探索期脚本实例（原文 p71）

> **原文（p71）**：
> 「The purpose of our session today is to review the design for a new web site and get your opinions about it. As we review this design together, I will be asking you a series of questions about what you see and how you expect things to work. ... There are no wrong answers or stupid questions. This product is in a very preliminary stage; do not be concerned if it acts in unexpected ways.」

> **★★ 判据：探索期脚本必须显式声明"产品很初步"**
> 这句话不是客套：它解除被试"我操作错了"的心理负担，从而让"我以为它会…"这类最有价值的话说出来。

---

## 3.3 评估性/总结性测试（Assessment or Summative）

### 3.3.1 何时做

> **原文（p72）**：
> 「The assessment test is probably **the most typical type of usability test** conducted. Of all the tests, it is probably the simplest and most straightforward for the novice usability professional to design and conduct. Assessment tests are conducted either early or midway into the product development cycle, usually **after the fundamental or high-level design or organization** of the product has been established.」

### 3.3.2 目标

> **原文（p72）**：
> 「The purpose of the assessment test is to expand the findings of the exploratory test by evaluating the usability of **lower-level operations and aspects** of the product. If the intent of the exploratory test is to work on **the skeleton** of the product, the assessment test begins to work on **the meat and the flesh**.」

> **★★★ 判据：骨架 vs 血肉——两阶段的观察对象不同**
> 探索期看"结构对不对"，评估期看"结构已定，实现得好不好"。
> 反过来用会浪费：在评估期质疑骨架，等于要求重做；在探索期抠细节，等于在纸上谈兵。

### 3.3.3 方法：与探索期的三条差异

> **原文（p73）**：
> 「Unlike the exploratory test:」
> - 「The user will **always perform tasks** rather than simply walking through and commenting upon screens, pages, and so on.」
> - 「The test moderator will **lessen his or her interaction** with the participant because there is less emphasis on thought processes and more on actual behaviors.」
> - 「**Quantitative measures will be collected.**」

---

## 3.4 验证性/确认性测试（Validation or Verification）

### 3.4.1 何时做

> **原文（p73）**：
> 「The validation test, also referred to as the verification test, is usually conducted **late in the development cycle** and, as the name suggests, is intended to measure usability of a product **against established benchmarks** or, in the case of a verification test, to **confirm that problems discovered earlier have been remedied and that new ones have not been introduced**.」

> **★★★ 判据：validation 与 verification 是两件事，原文用 "or" 连在一起但语义分叉**
> - **validation**：对照"预设基准"打分（够不够格）
> - **verification**：确认"老问题修好了、没引入新问题"（对不对得上）
> 一次测试可以同时做，但**报告里必须分开陈述**，否则无法判断"没通过"是因为本来就不达标，还是修坏了。

### 3.4.2 目标与基准来源

> **原文（p73）**：
> 「The objective of the validation test is to evaluate how the product compares to some predetermined usability standard or benchmark, either a **project-related performance standard, an internal company or historical standard, or even a competitor's standard** of performance. ... The standards usually originate from the usability objectives developed early in the project. These in turn come from **previous usability tests, marketing surveys, interviews with users, or simply educated guesses by the development team**.」

> **★★ 判据：基准可以"猜"，但必须写明是猜的**
> 原文承认基准可来自「simply educated guesses」。要求是**可追溯**，不是"精确"。

### 3.4.3 基准的数值口径（关键）

> **原文（p81）**：
> 「Verify that **70 percent** of participants can meet established successful completion criteria for each major task scenario.」

> **原文（p81）**（括注）：
> 「The 70 percent benchmark is something that Jeff has personally evolved toward over time, and that Dana has used effectively. It provides a **reasonably challenging test while still leaving the design team some work to do before product release to move that number toward a more acceptable and traditional 95 percent benchmark**. A benchmark of **100 percent is probably not realistic** except for tasks involving danger or damage to the system or possible loss of life, and should never be used lightly. In the 1960s **NASA found that achieving 100 percent performance cost as much as 50 times the cost of achieving 95 percent performance**.」

> **★★★★ 判据：三段式基准 70% → 95% → （100% 只在危害生命时）**
> - **首轮/迭代测试用 70%**：留出改进空间
> - **发布目标 95%**
> - **100% 的代价是 50 倍**（NASA 1960s 数据），只在危险/损毁/生命风险时使用
> **注意**：70% 是"单个主要任务场景"的通过比例，不是"整体成功率"。

---

## 3.5 比较测试（Comparison）

> **原文（p75）**：
> 「The basic methodology involves the **side-by-side comparison of two or more clearly different designs**. Performance data and preference data are collected for each alternative, and the results are compared.」

### 3.5.1 两种做法

> **原文（p75）**：
> 「The comparison test can be conducted informally as an exploratory test, or it can be conducted as a tightly controlled classical experiment, with one group of participants serving as a control group and the other as the experimental group.」

### 3.5.2 一个反直觉的结论

> **原文（p75）**：
> 「Inevitably, when comparing one or more alternatives in this fashion, one discovers that **there is no "winning" design per se. Rather, the best design turns out to be a combination of the alternatives, with the best aspects of each design used to form a hybrid design.**」

> **原文（p76）**：
> 「For exploratory comparison tests, experience has shown that the best results and the most creative solutions are obtained by **including wildly differing alternatives**, rather than very similar alternatives.」

> **★★★★ 判据：比较测试的产出通常是"混血方案"，不是"冠军"**
> 所以**不要设计成锦标赛**（谁赢用谁）。正确问法是：
> - 每个方案的**最好之处**是什么？
> - 每个方案的**最坏之处**是什么？
> - 哪些可以合并？
> **另**：方案差异越大越好，趋同的方案对比会退化为"挑细节"，逼不出对基本前提的质疑。

---

## 3.6 生命周期串讲：三次测试的实例（原文 p77–p82）

原文给了一个贯穿全生命周期的假想案例：个人信息管理器（日历/联系人/任务）＋文档。

| 轮次 | 类型 | 产品状态（原文） | 主要研究问题（原文摘录） |
|---|---|---|---|
| Test 1 | 探索 / 比较 | 「about 30 to 40 percent of the proposed functions work」，无文档 | 「Which of the two interface styles/concepts is the most effective?」「For which tasks will users need help, further instructions, or supporting documentation?」 |
| Test 2 | 评估 | 「approximately 60 to 80 percent of its eventual functionality」，有帮助主题、有简版文档（有目录无索引） | 见 p79–p81（验证低层操作） |
| Test 3 | 验证 | 临近发布 | 「Verify that 70 percent of participants can meet established successful completion criteria for each major task scenario.」 |

> **原文（p79）**：
> 「As is typical of comparison tests at this point, **there was no "winner" per se. Rather, the result was an interface with the best attributes of both prototypes.**」

> **原文（p81–p82）**：
> 「Every major task passed the 70 percent successful completion criteria **with the exception of two**. The team felt that the problems associated with those tasks could be corrected prior to release, and wanted to schedule a very quick test to confirm. **Twenty recommendations** from the test were identified for implementation prior to release, and **at least fifteen recommendations** were diverted to future releases.」

> **★★★ 判据：三轮测试的"产出形态"不同，不能都用同一个模板汇报**
> - Test 1 → 概念取舍 + 支持材料需求清单
> - Test 2 → 具体缺陷清单 + 量化指标
> - Test 3 → 基准比对结论 + 建议分流（发布前 / 下个版本）
> 第三轮的"分流"（20 条立即改 / 15 条延后）是验证期报告的必要结构。

### 3.6.1 迭代的合法性说明

> **原文（p66）**：
> 「Usability testing is most powerful and most effective when implemented as part of an **iterative** product development process.」

> **原文（p67）**：
> 「**One test is almost always better than none**, and it is better to focus on what you can do than on what you cannot do.」

> **原文（p66）**：
> 「one need not be concerned about applying the tests at exactly the correct moment. Rather, **consider what it is that you need to understand about your product, and let that drive your test objectives** and the appropriate application of a particular test method.」

> **★★ 判据：类型是"由问题推出"的，不是"由日历推出"的**
> 不要因为"现在是设计阶段"就做探索测试；要看"我现在需要知道什么"。

---

## 3.7 本章判据总表（共 14 条）

| # | 判据 | 出处 |
|---|---|---|
| 1 | 选测试类型只问三件事：要回答什么问题、产品多完整、还有多少时间可改 | p65 |
| 2 | 前三个类型按生命周期排；比较测试是横切维度，不占阶段 | p65 |
| 3 | formative ≡ exploratory，summative ≡ assessment（本书口径），跨书引用要标口径 | p65 / p67 |
| 4 | 探索期测"关于用户的假设"，不是找 bug | p67–p68 |
| 5 | 探索期优先定性；过早量化会锁死概念层面的发现 | p69 |
| 6 | 探索期原型只需做到能回答测试目标即可，可横向/纵向 | p69 |
| 7 | 探索期可只做走查不做任务 | p69 |
| 8 | 探索期脚本必须声明"产品很初步" | p71 |
| 9 | 评估期用户必须真做任务，主持人减少互动，采集量化数据 | p73 |
| 10 | 探索=骨架，评估=血肉；反用会浪费测试 | p72 |
| 11 | validation（对基准）与 verification（老问题修没修）要分开陈述 | p73 |
| 12 | 基准可来自"educated guess"，但必须可追溯 | p73 |
| 13 | 基准三段式：首轮 70%／发布 95%／100% 仅在危害生命时（NASA 50 倍成本） | p81 |
| 14 | 比较测试产出"混血方案"，且方案差异越大越好 | p75–p76 |

---

## 3.8 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| 四类型与"有主持/无主持""实验室/远程"的正交组合 | 本章只讨论生命周期维度，未把主持形态作为交叉轴 | ch11 §11.2（远程/自动）与 ch04 §4.3（sit-by vs 观察室） |
| 每类型的最小样本量 | 只给"4–5 人/单元"通用值（p110/p164），未按类型细分 | ch05 §5.6 与 ch07 §7.4 并列了两本书的口径 |
| 探索期"多少个概念稿才够比" | 只说"差异越大越好"，未给数量 | 本章未展开 |
| 验证期基准如何从历史测试推导 | 只说来源有四类，未给推导方法 | 本章未展开；benchmark 估算见 p119–p120 侧栏（乘 2.5 常数法） |
| 第二轮（评估期）的完整研究问题清单 | p79–p81 有实例，但部分在页边界处被图打断 | 已录可读部分，图 3-5/3-6 为界面示意（图不清，未录图形） |

---

## 3.9 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 70%/95%/100% 基准 | 本书 ch07 分析 | 成功率阈值直接决定"哪些任务算未达标" |
| 探索期需极度互动 | 本书 ch04 主持人技能 | sit-by 布局与出声思维的必要性 |
| 比较测试 | 本书 ch05 测试设计 | within-subjects / between-subjects 与 counterbalancing |
| 类型 → 数据采集项 | 本书 ch05 §5.7 | 绩效测量 vs 偏好测量的选择 |
| formative / summative 的主分类 | Barnum 书 ch01（p45） | 术语体系不同，两书并列使用 |
| 迭代 = 设计-测-改 | `design-methodology-liuguanzong` 设计思维六步 | "评价"步与"归纳"步的工程化 |
| 探索期验证"关于用户的假设" | `user-research-methods` 技能 | 假设澄清可用访谈/观察，不必上测试 |
