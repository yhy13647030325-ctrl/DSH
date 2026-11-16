# 第 9 章：验证类方法——木马、可用性测试的定位、RITE、并行原型、快速约会、启发式评估

> **原书 PDF 页序 p205–p206、p195–p196、p143–p144、p123–p124、p165–p166、p99–p100（共 12 页）**｜**本版实读全部 12 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）；**书内印刷页 = PDF 索引 − 1**（全书实测偏移恒为 +1）
>
> **读法说明**：本章只回答一个问题——**在方法谱系里，什么时候选"验证类"方法，选哪一种**。
> **可用性测试的具体执行（招募、脚本、主持、报告）不在本技能范围，详见 `usability-testing` 技能。**
> 每节含【原文摘录】+【判据提炼】。

---

## 9.1 总纲：验证类方法的前提是"已经有东西可验"

> **原文（p75，Evaluative Research）**：
> 「**Evaluative research** involves the **testing of prototypes, products, or interfaces by real potential users of a system in design development**.」

> **原文（p75）**：
> 「evaluation research is **ideally iterative**, based on feedback from potential users in **cyclical rounds of concept and prototype development** to refine product and interface details. **Evaluation should never be reserved only for final product release**, when design changes are potentially **complicated and expensive**.」

> **★★★★ 判据：「不要只在发布前评估」——因为那时改动最贵。这是选验证时机的第一原则。**
> 原文用了「never be reserved **only** for」——不是"不能评估最终版"，而是"不能**只**评估最终版"。

> **原文（p75）**：
> 「The methodology of evaluation research may be **tightly controlled**, employing a **scientific, experimental model** typical in lab testing. The advantage of this model is **control over extraneous variables**, but this may come **at the expense of realism**. Depending on the fidelity of prototypes, testing can also be conducted using **flexible evaluations** by people using products or prototypes **in context or approximate conditions of real-world use**. The value of this approach is **realism**, but it may come **at the expense of control** over other influencing variables.」

> **★★★★ 判据：「控制」与「真实」是跷跷板，不可兼得——这是本技能对验证类方法的总纲。**
> 原文把两端说得很干净：**实验模型=控住干扰变量但失真；情境评估=真实但失控**。
> **选验证方法＝选你要哪一端。**

> **原文（p75）**：
> 「When evaluation research is conducted **following thorough exploratory and generative research**, it often needs only to serve a **verification purpose**, to assess **how well designers have responded to input from users** as they iterate and refine their designs.」

> **★★★ 判据：前面探索做透了，验证就退化成"核对"——工作量大幅下降。**
> 反向推论很重要：**探索没做透的项目，验证阶段会被迫补做探索**，表现为"问题层出不穷、每次都发现新方向"。

---

## 9.2 木马法（Wizard of Oz，方法 99，p205–p206 PDF）

### 9.2.1 定义与目的

> **原文（p205）**：
> 「In the **Wizard of Oz** technique, a researcher (the "**wizard**") **simulates system responses from behind the scenes**, while a participant engages with a system that **appears to be real**.」

> **原文（p205）**：
> 「Unseen by the participant, the researcher (i.e., the "wizard") is able to **intercept and shape the interaction** between the participant and the "system," **without having an actual system up and running**. The goal of the method is to **allow the user to experience a proposed product or interface before costly prototypes are built**.」

> **★★★★ 判据：木马的本质是"用人的临时代替系统的功能"——它买的是"不必先造出来"。**
> 原文的关键限定是「before costly prototypes are built」。
> **所以木马只在"造原型很贵/技术还没实现"时成立；能便宜造出来的原型，用木马是绕远路。**

### 9.2.2 它真正能捞到的东西

> **原文（p205）**：
> 「It also provides a framework to **gauge participants' openness and willingness to new ways of doing things**, and to **explore and discover boundary conditions** for **innovative and disruptive technologies**.」

> **★★★★ 判据：木马最独特的产出是"接受度"与"边界条件"，不是"可用性缺陷"。**
> 这两样别的方法都拿不到：可用性测试要真东西；问卷问不出边界条件。
> **判据化：要问"人愿不愿意接受这个新交互方式"，木马是首选。**

### 9.2.3 执行要点：位置分离 + 可观察 + 一致性

> **原文（p205）**：
> 「The research session setup requires that the participant be **in one location**, and the researcher who plays the "wizard" **in another**. To aid in the process of preparing an appropriate, timely system response, the researcher must be able to **observe participant activity** (either through **video or screen-sharing software**).」

> **原文（p205）**：
> 「In the early design phases, the wizard will **simulate the majority of the behaviors** of the system… As iterative improvements are made to the interface, **less and less intervention** from the researcher/wizard is required—usually just enough to **keep the process moving and bridge the gap** between what the current implementation actually provides, and the envisioned system.」

> **★★★★ 判据：「早期模拟大部分行为，后期只补缺口」——木马的干预量是随迭代递减的。**
> 这是一个可操作的进度指标：**如果做完几轮还需要巫师大量救场，说明原型成熟度不够，不是测试没做好。**

> **原文（p205）**：
> 「However, the **believability of the simulations hinge on the wizard's consistent behaviors** with respect to **timing, patterns, and system logic**.」

> **★★★ 判据：「时机、模式、系统逻辑」三项一致性决定木马是否可信——记在巫师个人身上是最大风险。**
> 换一个巫师，时机与逻辑就变了，数据不可比。**判据：同一轮研究必须由同一人扮演巫师。**

**巫师的三种角色（原文给全）**：

> **原文（p205）**：
> 「During the process, the wizard can take on different roles and simulate different behaviors, including:
> the **controller** who simulates **system intelligence**,
> the **supervisor** who **course-corrects and overrides** decisions that the system or participant makes, and
> the **moderator** who simulates **sensory data** and makes the envisioned experience feel complete.」

| 角色 | 模拟什么 | 什么时候用 |
|---|---|---|
| **控制者（controller）** | 系统智能 | 要验证"系统够不够聪明"时的核心角色 |
| **监督者（supervisor）** | 纠偏、否决 | 要验证"系统出错时的兜底" |
| **主持人（moderator）** | 感官数据、补齐体验 | 要让体验"像真的" |

> **★★ 判据：三个角色可以叠加，但叠加会削弱一致性。**
> 原文未给叠加规则（见 §9.9 空白）。

### 9.2.4 适用面

> **原文（p205）**：
> 「Consider using the WOz technique **anytime you need to gauge how people will feel about—and how they might perform while using—a proposed solution before investing time and money in an actual prototype**. WOz is **especially useful when designing digital applications and solutions that do not already have established design patterns** (e.g., **augmented reality systems, and ubiquitous computing applications**).」

> **★★★ 判据：「没有既有设计模式」是木马的高价值区。**
> 原文点名 AR 与普适计算。**因为用户没有经验可迁移，只能靠亲身体验才能说出感受**——
> 而问卷问"你会喜欢 AR 吗"，得到的全是想象。

**溯源（原文给了一段很好的命名史）**：

> **原文（p205，脚注 1）**：
> 「**John F. "Jeff" Kelly** from the **IBM Thomas J. Watson Research Center** originally coined the "**OZ Paradigm**" in **1980**… As it gained popularity in the fields of Human Factors, Experimental Psychology, and Usability Engineering, the name of the method changed to reflect the **1939 MGM movie *The Wizard of Oz***, in which an ordinary man hides behind a curtain, and uses technology to convince everyone he is an omnipotent wizard.」

| 方法 | 什么时候用 | 什么时候不能用 | 最少样本量 | 产出物 |
|---|---|---|---|---|
| **木马（Wizard of Oz）** | 原型/技术昂贵或未实现；要测"接受度"与"边界条件"；无既有设计模式（AR/普适计算） | 能便宜造出原型；需要绝对可重复（巫师人因不可控）；需要真实性能数据（延迟、精度） | **原书未给具体数字**。原文未提被试数，也未提巫师的场次上限 | 接受度证据、边界条件清单、体验描述、巫师行为日志（时机/模式/逻辑） |

---

## 9.3 可用性测试（方法 94）——**只写"什么时候选它"**

> ⚠ **本节定位**：只回答"在方法谱系里，什么时候该走到可用性测试这一步"。
> **具体执行（任务脚本写法、招募与筛选、主持话术、观察室、报告结构）详见 `usability-testing` 技能，本技能不重复。**

### 9.3.1 定义与它测什么

> **原文（p195）**：
> 「**Usability testing** focuses on **people and their tasks**, and seeks **empirical evidence about how to improve the usability of an interface**.」

> **原文（p195）**：
> 「Usability testing is an **evaluative method** that allows teams to **observe an individual's experience** with a digital application as he or she **walks through the steps of a given task** (or set of tasks). The method is designed to help teams **identify the parts of an interface that most regularly frustrate and confuse people** so that they can be **prioritized, fixed, and retested prior to launch**.」

> **★★★★ 判据：可用性测试是"评估类"（evaluative），不是"探索类"——这是选它的第一道闸。**
> 如果你还不知道该做什么，此时上可用性测试就是空转。
> **它回答的是"这个东西哪里不好用"，不是"我该做什么东西"。**

### 9.3.2 什么时候选它（判据清单）

据原文 p195 与 p75，可以整理出"该选可用性测试"的五个条件，全部满足才值得上：

| # | 条件 | 原文依据 |
|---|---|---|
| 1 | 已有可被测的对象（原型、产品、界面） | 「observe an individual's experience with a digital application」p195 |
| 2 | 已有明确的**任务**可让用户走 | 「walks through the steps of a given task」p195 |
| 3 | 目标是**改进可用性**，不是探索需求 | 「seeks empirical evidence about how to improve the usability」p195 |
| 4 | 能接受**控制换真实**（或明确选情境版） | 「control over extraneous variables…at the expense of realism」p75 |
| 5 | 有人能**看**（观察者/干系人在场） | 「require the attendance of developers and project stakeholders」p195 |

### 9.3.3 什么时候**不**选它

| # | 不选的理由 | 该改用什么 |
|---|---|---|
| 1 | 需求还没定（不知道做什么） | ch02 访谈、ch03 观察、ch04 日记 |
| 2 | 想知道"多少人会买/多久会用" | ch05 问卷、ch01 A/B |
| 3 | 想验证"接不接受这种新方式" | ch09 木马 |
| 4 | 想快速扫掉基线问题、用户又不好约 | ch09 启发式评估、认知走查 |
| 5 | 想看团队在被观察下的协作行为（非个人任务） | ch03 观察/影子 |

> **★★★★ 判据：可用性测试的独占价值是"看一个人在真实任务上失败的具体位置"。**
> 一旦问题不是"哪里失败"，就不该用它。

### 9.3.4 它特有的硬要求（选它前必须知道成本）

> **原文（p195）**：
> 「Aside from experiment validity, empiricism, and avoiding bias, the **key to successful usability testing is to require the attendance of developers and project stakeholders at research events**. Many teams are **making the usability test observation session the only opportunity to see and weigh in on prototypes prior to launch**.」

> **★★★ 判据：「开发与干系人必须在场」被原文列为成功的关键——这是它的隐性成本。**
> 组织不起这个场面，可用性测试的转化率会大幅下降（因为没人看见）。

> **原文（p195）**：
> 「Also, just as **the number of participants in the test directly impacts the number of problems that are detected**, so do the **number of evaluators—the more evaluators, the more problems will be detected**.」

> **★★★ 判据：问题发现量受两个数量驱动：被试数 × 评估者数。**
> **原文未给任何一个的具体数字**（只给"越多发现越多"的单调关系）。见 §9.9。

> **原文（p196，图注）**：
> 「Unlike **attitudinal studies**, **behavioral experiments such as usability tests can be used with fewer participants** to isolate enough problems to help teams confidently decide whether an interface needs to be revised, or is ready for release. When the testing process is **included early in the process, over several rounds of testing** the team will gain confidence in the usability of the interface **as fewer problems are identified**.」

> **★★★★ 判据：「可用性测试需要的被试少于态度研究」——但原文只给方向，没给数字。**
> 另给了停止信号：**逐轮少量发现问题 = 可以发版了。**

**原文列出的 8 类要观察的错误信号**（可直接当观察表）：

> **原文（p195）**：
> 「Some of the errors that observers and evaluators should try to detect include any instance where the participant:
> 1. **understands the task but can't complete it within a reasonable amount of time**;
> 2. **understands the goal, but has to try different approaches to complete the task**;
> 3. **gives up or resigns from the process**;
> 4. **completes a task, but not the task that was specified**;
> 5. **expresses surprise or delight**;
> 6. **expresses frustration, confusion, or blames themselves** for not being able to complete the task;
> 7. **asserts that something is wrong or doesn't make sense**; or
> 8. **makes a suggestion for the interface or the flow of events**.」

> **★★★★ 判据：第 5 项「surprise or delight」与第 8 项「建议」也被列为要捕捉的信号——不只有失败才算发现。**
> 这是很多观察表会漏的：**惊喜与建议同样是可用性数据**。

| 方法 | 什么时候用 | 什么时候不能用 | 最少样本量 | 产出物 |
|---|---|---|---|---|
| **可用性测试** | 已有对象与任务；要定位"哪里失败"；团队能到场观察 | 需求未定；要总体比例；要测接受度；用户约不到 | **原书未给具体数字**。只给两条方向：①「can be used with **fewer participants**」（比态度类少）②「the more evaluators, the more problems will be detected」。**具体人数详见 `usability-testing` 技能** | 问题清单（含频次/影响/持续性）、失败位置、改进建议、8 类信号记录 |

---

## 9.4 RITE（方法 68，p143–p144 PDF）

### 9.4.1 它是什么（形成性 vs 总结性）

> **原文（p143）**：
> 「**Rapid Iterative Testing and Evaluation (RITE)** is a **rigorous method** that can be used to **evaluate and identify interface problems, quickly fix them, and then empirically verify the efficacy of the fixes**, using a **rapid test–fix–test–fix approach**.」

> **原文（p143）**：
> 「**Formative** usability testing methods such as RITE are used to gain **exploratory insights into the user behavior** as it relates to the overall design direction, with the intention of **quickly iterating and fixing problems**, as opposed to **summative** goals, which seek to **find and measure** usability issues.」

> **★★★★ 判据：形成性＝边测边改；总结性＝测完给结论。RITE 是前者。**
> 选 RITE 就等于放弃"给出一份稳定基线报告"这个诉求。

> **原文（p143）**：
> 「For RITE, this distinction is important, as the power of the method depends on the **early identification of the big problems that block people from completing a task**, and on **uncovering issues that fail to meet one of the overarching goals of the design**.」

### 9.4.2 五条与常规可用性测试的差别（原文列表）

> **原文（p143）**：
> 「Other ways RITE as a formative method differs from traditional summative usability tests include the following:
> • RITE can be used **early in the design process** as a guide through the design solution space, rather than trailing behind development to identify usability problems in later phases.
> • **Prototypes are changed as soon as problems are identified and the team agrees to a solution—usually within a few hours of the session.** The fix is then retested with more participants.
> • **No usability reports are written**, as an updated prototype serves as the new design direction.
> • **The number of scheduled tests (and by extension, the number of participants you have to schedule) continues after each design change until there is a consecutive string of successful tests with no failures.**
> • It is preferred that **observers and facilitators have domain expertise over test facilitation expertise**. Domain knowledge can help observers **prioritize fixes based on their judgment of what is truly a problem versus what is an artifact of a particular participant**.」

| # | 差别 | 判据含义 |
|---|---|---|
| 1 | 用在中早期，不跟在开发后面 | 时机差异 |
| 2 | **几小时内就改原型** | 决定它必须是紧凑排期 |
| 3 | **不写报告**，新原型就是方向 | 交付物形态变了 |
| 4 | **按"连续成功"决定继续排期** | 样本量是规则，不是数 |
| 5 | **观察者要有领域专长，胜过主持专长** | 选人标准与常规测试相反 |

> **★★★★ 判据（第 3 条）：RITE 不写报告——因为它把"修好"当作交付物，而不是"发现问题"。**
> 原文：「No usability reports are written, as an **updated prototype serves as the new design direction**」。
> **如果你的组织必须有报告才能推进，RITE 会水土不服。**

> **★★★★ 判据（第 5 条）：领域专长优先于主持技巧——这是与常规测试最反直觉的差别。**
> 原文理由：领域知识帮助观察者判断「what is **truly a problem** versus what is an **artifact of a particular participant**」。
> **即：能分辨"真问题"和"这个被试的怪癖"，靠的是懂行，不是会主持。**

### 9.4.3 停止规则（数字在此，见 ch06 详表）

> **原文（p143）**：
> 「The number of scheduled tests…continues after each design change until there is a **consecutive string of successful tests with no failures**.」

**图 p143「An example test cycle using the RITE method」**：计数器规则为**连续 5 次成功**，任何失败重置为 5；
示例最终「**Totals: 11 participants / 4 revised prototypes**」。

> **★★★★ 判据：RITE 的样本量是"停止规则"（连续 5 次成功），不是预设人数。**
> 原文 p143 图里演示得很清楚：Test 0 试运行→设 5 → Test 1 成功（还需 4）→ Test 2 失败（重置 5）…→ Test 11 成功。

### 9.4.4 何时可用

> **原文（p143）**：
> 「RITE can be scheduled **as soon as you have a low-fidelity prototype to test**.」

> **★★★ 判据：低保真就能开始——这是它"早"的物理依据。**

| 方法 | 什么时候用 | 什么时候不能用 | 最少样本量 | 产出物 |
|---|---|---|---|---|
| **RITE** | 早期、要快速修大问题；团队能几小时内改原型；有领域专家可观察 | 需要稳定基线报告；组织必须有报告才能推进；改不动原型（硬件、模具）；问题主要是美学 | **停止规则：连续 5 次成功测试**（任何失败重置计数器，p142–p143）；示例用量 **11 人 / 4 版原型**（p143 图注） | 改进后的原型（替代报告）、修好的缺陷、领域判断记录 |

---

## 9.5 并行原型（方法 58，p123–p124 PDF）

> **原文（p123）**：
> 「**Parallel prototyping** is the process of **considering a range of potential design ideas simultaneously before selecting and refining one specific design approach**. When applied **before iterative design**, parallel prototyping enables teams to more fully experiment with and investigate a **wide range of opportunities in a design space**. It can also help designers to **avoid becoming fixated on a design**, and avoid "**hill climbing**" toward a **less superior result**, which has been a long-standing criticism of the **iterative design methodology**.」

> **★★★★ 判据：并行原型是针对"迭代法会爬错山头"（hill climbing）的解药。**
> 原文把矛头指向迭代设计本身：**迭代会优化你手上那个，但不保证它是最好的那个。**

> **原文（p123）**：
> 「Parallel prototyping asks that designers **quickly and independently create a range of low-fidelity prototypes**, and then submit designs to **testing by end users, or to heuristic evaluation by experts**. **The intention of these design evaluations is not to pick the "best" or "most preferred" design.** Rather, the evaluations should help the designers to **thoughtfully reflect and consider how people react to individual elements of the design**, and which accomplish the intended goals of the project. **The best qualities of all preceding designs can then be refined and merged** to inform a **superior, optimized design**.」

> **★★★★ 判据：并行原型的目的不是"选优"，是"取各家之长合并"。**
> 原文明确否定选优：「**not** to pick the "best" or "most preferred" design」。
> **判据化：如果评审会开成了投票选方案，就用错了这个方法。**

三条收益（原文列表重新组织）：

> **原文（p123）**：
> 「• **Encourages divergent explorations.** Because a goal of parallel prototyping is to create multiple design options, the method frees designers to explore and get feedback on a wide range of options, as opposed to locking in on and refining only their first idea.
> • **Shifts focus from the designer onto the design.** Parallel prototyping provides a **safe backdrop for giving and receiving constructive criticism**. When multiple designs are being considered side by side, **it is harder for the designer to feel defensive** about any one particular design. When practiced repeatedly, it can help sensitive or novice designers learn to **view their designs as separate from themselves**.
> • **Promotes team collaboration and builds rapport.** Designers collaborating on parallel designs will often **merge and refine others' concepts** into their subsequent designs. This sort of idea sharing on a team goes a long way toward **team building**, and also **minimizes internal competition** among team members.」

| # | 收益 | 机制 |
|---|---|---|
| 1 | **鼓励发散** | 目标是"多方案"，不是"锁定第一个想法" |
| 2 | **把焦点从设计师移到设计上** | 多个方案并置时，人不容易为某一个辩护 |
| 3 | **促进协作与默契** | 设计师会互相合并对方的想法，减少内耗 |

> **★★★ 判据：第 2 条的机制是"降低防御"——多个方案并置让批评不再指向人。**
> 原文由此推出一个成长目标：「view their designs as **separate from themselves**」。
> **这是设计评审方法论里最实用的一条心理学判据。**

> **原文（p123）**：
> 「Use parallel prototyping when working with teams that have a **tendency to "get stuck" on one design approach** in the early exploration and concept generation phases.」

| 方法 | 什么时候用 | 什么时候不能用 | 最少样本量 | 产出物 |
|---|---|---|---|---|
| **并行原型** | 早期容易"卡在一个方案"；评审会开成投票；团队防御心强 | 方案已定只待优化；资源只够做一个；要评估单一方案细节 | **原书未给具体数字**（未提方案个数、被试探人数） | 多个低保真原型、元素级反馈表（非投票结果）、合并后的优化方案 |

---

## 9.6 快速约会（Speed Dating，方法 79，p165–p166 PDF）

### 9.6.1 定义与适用面

> **原文（p165）**：
> 「**Speed dating** as a research method is inspired by the framework of its dating-scene namesake, but instead of people, researchers **rapidly "speed date" design opportunities with potential users**. The power of speed dating lies in **exposing people to future design ideas via storyboards and simulated environments before any expensive technical prototypes are built**.」

> **原文（p165）**：
> 「**Use speed dating when exploring environments and social contexts that are not readily available** (e.g., **homes with ubiquitous computing**). The method can **uncover risk factors** across a series of related enactments, and **focus design teams' efforts on understanding user needs before spending time and effort vetting and building expensive technological solutions**.」

> **★★★★ 判据：快速约会的适用条件是"环境/情境不可得"——你要研究的东西现场看不到。**
> 原文举例"普适计算的家庭"。**这把它与木马分开：木马模拟"系统"，快速约会模拟"情境与场景"。**

### 9.6.2 五步流程（原文给全，可直接照做）

> **原文（p165）**：
> 「**Conduct contextual field research.** Use methods such as interviews, role-playing, artifact analysis, directed storytelling, diary studies, and cultural probes to understand the people for whom you are designing. **Analysis efforts should focus on aligning the observed and verbalized needs of the participants**, so the team can identify opportunities where people **demonstrate and articulate a need**.
> **Create storyboards for each scenario.** Design storyboards to **elicit an emotional, empathic reaction** to the characters so that participants can easily identify with them. **Focus scenarios on the specific needs uncovered by research**, and show how each potential design would address the need. As with traditional scenarios, **the details of the technology itself should be downplayed**.
> **"Speed date" storyboards in a session.** Each storyboard should be **presented to a group of people in serial fashion**, and then followed by a **focus question** to help design teams understand **what is in the users' minds**. At the end of the session, **users rank how accurately the storyboards represent their needs**, as well as the **effectiveness of the proposed technology/solution** under evaluation.
> **Reflect and discuss.** Refocus conversations on **the needs that were expressed in both the field research and the storyboard sessions**. Instead of spending time **ranking and prioritizing existing concepts**, the team should use this time to **articulate misunderstandings, refine scenarios, and consider new design opportunities**.
> **Construct a simulated environment.** User enactments in a simulated space allow people to **act out a role from the revised scenarios**. Over the course of several acted-out scenarios, the team can observe users dealing with specific problems in context to how they could play out in real life.」

| 步 | 动作 | 关键要求 |
|---|---|---|
| 1 | **做情境田野研究** | 需求要对齐"观察到的"与"说出的" |
| 2 | **为每个场景画分镜** | 要引发**情感共鸣**；**淡化技术细节** |
| 3 | **"快速约会"分镜** | 逐个呈现 + 焦点问题 + 最后**排序**（代表性 / 有效性） |
| 4 | **反思与讨论** | **不要花时间给现成概念排序**，要纠误解、改场景、找新机会 |
| 5 | **搭建模拟环境** | 让用户**演出来**，观察真实问题如何发生 |

> **★★★★ 判据（第 2 步）：「淡化技术细节」是刻意的，因为要测的是"需求是否被满足"，不是"技术炫不炫"。**
> 原文两处强调：「the details of the technology itself should be **downplayed**」「**not** spending time ranking and prioritizing existing concepts」。

> **★★★ 判据（第 4 步）：第 3 步刚让用户排完序，第 4 步就说"别花时间排序"——因为它要的是"误解"而非"排名"。**
> 这是一对刻意的张弛：**收数据时排序，讨论时不排序**。

### 9.6.3 源案例的量化（原文脚注给了数字，但**不是人数**）

> **原文（p165，脚注 1）**：
> 「Researchers **Scott Davidoff, Min Kyung Lee, Anind K. Dey, and John Zimmerman** at the **Carnegie Mellon Human Computer Interaction Institute and School of Design** first developed the speed dating method in **2007** while exploring opportunities for ubiquitous computing in smart homes. During their study, they used speed dating to explore **over 100 concepts** and **prototype 27 variations over two weeks**. The results helped them to pinpoint "**showstopper**" issues before costly technical prototypes were built…」

| 项 | 数值 |
|---|---|
| 探索概念数 | **over 100** |
| 原型变体数 | **27** |
| 周期 | **two weeks** |
| 参与者人数 | **原书未给** |

> **★★★ 判据：这里的关键数字是"概念数/周期"，不是"人数"——别把 100 或 27 当样本量。**

| 方法 | 什么时候用 | 什么时候不能用 | 最少样本量 | 产出物 |
|---|---|---|---|---|
| **快速约会** | 目标情境不可得；要快速筛大量概念；要在造真机前找"showstopper" | 情境可直接进入（那去做田野）；需要真机性能数据 | **原书未给具体数字**（案例给的是概念数 100+、变体 27、周期 2 周，**非人数**） | 分镜集、代表性排序、有效性排序、误解清单、改进后的场景、模拟 enactment 记录 |

---

## 9.7 启发式评估（方法 46，p99–p100 PDF）

### 9.7.1 它不需要用户

> **原文（p99）**：
> 「A **heuristic evaluation** is an **informal usability inspection method** that asks evaluators to **assess an interface against a set of agreed-upon best practices, or usability "rules of thumb."** **Unlike usability tests that require participation of actual users**, heuristic evaluations **enlist members of the team**—from the **novice computer programmer to the expert usability professional**—to inspect an interface and **detect the baseline usability problems that should be fixed before user testing begins**.」

> **★★★★ 判据：「不需要用户」是它的定义性优势，也是它的效力上限——只能扫"基线问题"。**
> 原文把它定位为"用户测试之前"的前置清扫。
> **所以它不能替代可用性测试，它的位置在前面。**

> **原文（p99）**：
> 「Although the heuristic evaluation method will **rarely provide opportunities to identify breakthrough opportunities in the design**, it can help to **detect critical but missing dialogue elements early in the design process**.」

> **★★★ 判据：原文主动承认它"很少能发现突破性机会"——它是防守型方法，不是进攻型。**
> 这是又一处作者主动限制自方法效力（对比 ch04 文化探针）。

### 9.7.2 评估者人数（数字在此）

> **原文（p99）**：
> 「even though **double experts**—evaluators who are familiar with the **subject matter domain as well as in usability practices**—may be the most likely to identify usability issues, the method was designed to be used by **experts and novices (who are trained on heuristics) alike**. In an attempt to **hedge against the bias any one evaluator can bring** (based on their mindset or experiences), it is recommended that **three to five evaluators independently perform assessments** of the interface first, then **aggregate their findings into a single report**.」

> **★★★★ 判据：3~5 位评估者，且必须"独立"做、再"合并"——独立性是防偏差的关键。**
> 原文的理由：「hedge against the bias **any one evaluator** can bring」。
> **一起讨论着做，就变成了集体偏见。**

### 9.7.3 报告怎么写

> **原文（p99）**：
> 「Heuristic evaluation reports **list which problems are inconsistent with the heuristics**, and include **plenty of screenshots and call outs**. It is also common to **include examples and screenshots of heuristics that are working well** in the report. **Visually reporting both the positive and negative findings brings balance to the report**, recognizes the good work that is already represented in the design, and **serves as motivation to keep doing more heuristic evaluations**.」

> **★★★ 判据：报告要同时放"好的"和"坏的"——理由是"平衡"与"保持动力"。**
> 这与 ch08 §8.5 认知走查原文提到的"正面与负面并报"是同一处方（A 源 p99 启发式评估报告要「include examples and screenshots of heuristics that are **working well**」）。
> **注**：Usability Report（方法 93）位于 A 源 p193（PDF），**本章未逐页读该页**，故不引其原文。

### 9.7.4 十条启发式（图注还原，含具体例子）

**图 p99「Heuristics applied to iPhone apps」**（原图为尼尔森 1994 十原则的改编版，图内文字完整，逐项录出）：

| # | 启发式（原文） | 图内举例（原文） |
|---|---|---|
| 1 | **Visibility of app status** | 「The **redfin** app keeps people informed about how quickly their images are downloading.」 |
| 2 | **Match between app and the real world** | 「The **iHandy** app acts the way a traditional level does, providing measurements about the user's environment.」 |
| 3 | **User control and freedom** | 「The **iPod** provides users volume, fast forward, reverse, next, and previous song at all times.」 |
| 4 | **Error prevention** | 「The **Amazon** app requires two confirmations before removing a book from your wishlist.」 |
| 5 | **Consistency and standards** | 「Whether you are using **netflix** on a computer, TV, or as an app, the language and behaviors are consistent.」 |
| 6 | **Recognition rather than recall** | 「**iPod** provides visuals of all songs and albums to facilitate selection.」 |
| 7 | **Flexibility and efficiency of use** | 「**Maps** provide car, public transportation, and walking routes depending on the user's method of transit.」 |
| 8 | **Aesthetic and minimalist design** | 「**Facebook**'s "Upload Images" functionality contains no superfluous buttons or information.」 |
| 9 | **Help users recognize, diagnose, and recover from errors** | 「If you aren't using location services, **Bump** tells you both the issue and solution in plain language.」 |
| 10 | **Help and documentation** | 「If you need help using the **iHandy** level app, instructions are **contextual, concise, specific, and visual**.」 |

> **★★★ 判据：原文交代了这十条的来源与使用方式——「A good place to start is Nielsen's 1994 heuristics, which are adapted here」。**
> 即：**它们是"起点"，不是"标准答案"**，且原文说应先「thoughtfully written and carefully
> considered to reflect the **context of the product**」。

> **★★★★ 判据：启发式必须按产品情境改写，不能照搬。**
> 原文：「Heuristics should be **thoughtfully written and carefully considered to reflect the context of the product**。」
> **这条常被忽略：直接套尼尔森十条，等于用通用标准测专用产品。**

### 9.7.5 团队文化效应（一个长期收益）

> **原文（p99）**：
> 「When heuristics are **thoughtfully written, and applied repeatedly during an iterative design process**, the team's knowledge of usability heuristics can create a **disciplined yet practical culture** to finding and fixing certain classes of usability problems. **Rather than making design decisions based on intuition and personal preferences**, a set of **manageable and meaningful principles** can focus the team's efforts regarding the types of changes to fix. **Over time, the principles will become more intuitive to everyone on the interdisciplinary team.**」

> **★★★ 判据：启发式的复利在"团队共用一套语言"，不在单次报告。**
> 原文的对照是「rather than making design decisions based on **intuition and personal preferences**」。

| 方法 | 什么时候用 | 什么时候不能用 | 最少样本量 | 产出物 |
|---|---|---|---|---|
| **启发式评估** | 用户约不到/要省预算；低中保真即可；要在可用性测试前扫基线；要建立团队共同语言 | 要发现突破性机会；要真实用户行为；启发式未按产品改写 | **3~5 位评估者，独立评审后合并**（p99）。**注意：这是评估者数，不用用户** | 问题与启发式对照清单、截图与标注、正负两面发现、合并报告 |

---

## 9.8 本章概念-论点表（共 16 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | **不要只在发布前评估** | 「Evaluation should **never be reserved only** for final product release」 | 评估研究 | 那时改动最贵 | p75 |
| 2 | **控制 vs 真实** | 「control over extraneous variables…at the **expense of realism**」 | 实验 vs 情境评估 | 跷跷板，不可兼得；选方法＝选要哪端 | p75 |
| 3 | **验证退化为核对** | 「often needs only to serve a **verification purpose**」 | 探索充分的项目 | 探索没做透，验证阶段会被迫补做探索 | p75 |
| 4 | **木马的买点** | 「**before costly prototypes are built**」 | AR/普适计算 | 只在"造不出来/太贵"时成立 | p205 |
| 5 | **木马的真产出** | 「gauge participants' **openness and willingness**…**boundary conditions**」 | Quasi 机器人 | 产出是接受度与边界，不是可用性缺陷 | p205 |
| 6 | **巫师一致性** | 「believability…**hinge on the wizard's consistent behaviors**…timing, patterns, and system logic」 | 巫师三角色 | 同一轮必须同一人扮巫师 | p205 |
| 7 | **干预量递减** | 「**less and less intervention**…just enough to **bridge the gap**」 | 迭代中的木马 | 还需大量救场＝原型成熟度不够 | p205 |
| 8 | **可用性测试的属性** | 「**evaluative** method…**empirical evidence about how to improve**」 | 界面改进 | 它答"哪里不好用"，不答"该做什么" | p195 |
| 9 | **干系人必须到场** | 「the **key to successful** usability testing is to require the attendance of developers and project stakeholders」 | 观察室 | 组织不起场面，转化率大降 | p195 |
| 10 | **双数量驱动** | 「the number of participants…**directly impacts** the number of problems…so do the number of evaluators」 | 问题发现 | 被试数 × 评估者数；**原文未给任一具体数字** | p195 |
| 11 | **惊喜也是数据** | 「expresses **surprise or delight**」「makes a **suggestion**」 | 8 类信号 | 观察表常漏；正面信号同样算发现 | p195 |
| 12 | **RITE 不写报告** | 「**No usability reports are written**, as an updated prototype serves as the new design direction」 | Age of Empires II | 交付物是"修好"，不是"发现问题" | p143 |
| 13 | **领域专长优先** | 「**domain expertise over test facilitation expertise**」 | RITE 观察者 | 要能分辨"真问题"与"这个人的怪癖" | p143 |
| 14 | **对抗爬错山头** | 「avoid "**hill climbing**" toward a **less superior result**」 | 并行原型 | 迭代只保证优化手上那个，不保证它最好 | p123 |
| 15 | **不是选优** | 「**not** to pick the "best" or "most preferred" design」 | 并行原型评审 | 开成投票会就用错了 | p123 |
| 16 | **启发式是防守型** | 「**rarely** provide opportunities to identify **breakthrough opportunities**」 | 尼尔森十原则 | 只能扫基线；且必须按产品情境改写 | p99 |

---

## 9.9 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **可用性测试的人数** | **原文未给任何数字**。只有两句方向：「can be used with **fewer participants**」、「the more evaluators, the more problems」。原书 p195 脚注 4 引 Virzi 1992「How Many Subjects is Enough?」，但正文未给结论 | **`usability-testing` 技能**（本机有 Rubin 386 页、Barnum 405 页两本原书）；原书脚注所引 Virzi 论文 |
| **可用性测试的执行细节** | **本技能故意不写**：任务脚本、招募、主持、报告结构均未展开（原文 p195 只有 1 页正文） | **`usability-testing` 技能** |
| **木马的被试数与巫师上限** | **完全未给** | 原书未展开；需查 Kelly 1984、Dow 等 2005（原书 p205 脚注） |
| **认知走查的评估者数** | **未给**（对比启发式给了 3~5） | Wharton 等 1994（原书 p33 脚注 2） |
| **并行原型的方案个数** | 「a **range of**」——**未给具体个数** | Dow 等 2010/2011（原书 p123 脚注） |
| **RITE 的"连续成功"依据** | 5 这个数只在**图内**出现，**正文未论证为何是 5** | Medlock 等 2002（原书 p143 脚注 1）；本技能照录图内数字，不替它论证 |
| **快速约会的参与者人数** | **未给**（案例只给概念数/变体数/周期） | Davidoff 等 2007（原书 p165 脚注 1） |
| **评估者间分歧怎么裁决** | 只说"独立做后合并"，**未给合并规则** | 未展开 |

---

## 9.10 本章与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 「不要只在发布前评估」 | 本技能 ch01 §1.3（五阶段） | 阶段 4 的定位；本章给"评估必须多轮"的理由 |
| 控制 vs 真实 | 本技能 ch03（是否在场） | ch03 的"飞墙 vs 参与式"是同一跷跷板在观察方法上的版本 |
| RITE 的领域专长优先 | 本技能 ch01 §1.2（研究者角色） | 专家评审档的能力要求 |
| 启发式评估（3~5 评估者） | 本技能 ch06 §6.2.7 | 数字总账；注意它是评估者不是用户 |
| 并行原型"不是选优" | 本技能 ch07（分析） | 评审结论应落到"元素级反馈"，与 ch07 的编码粒度一致 |
| 可用性测试的 8 类信号 | `usability-testing` 技能 | **本章只给"什么时候选"，怎么执行详见该技能** |
| 认知走查四问 vs 可用性测试 | `design-psychology-norman`（行动七阶段） | 四问＝动机+执行+评估；诺曼给理论框架 |
| 木马模拟"系统" vs 快速约会模拟"情境" | `usability-testing` 技能 | 两者都在可用性测试家族内，执行层归该技能 |
| "showstopper" 概念筛除 | `ergonomics-ding-yulan`（人的可靠性与安全） | 安全相关的失败风险可借人机工程的可靠性方法量化 |
