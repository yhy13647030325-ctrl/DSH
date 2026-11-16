# 第 5 章：测试计划与任务设计

> **原书 PDF 页序 p103–p130（28 页）**｜**本版逐页读完全部 28 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N；书内印刷页 = PDF 索引 − 38）
>
> **读法说明**：按原书 `5.x` 小节逐节展开，不跳节。
> 每节含【原文摘录】+【判据提炼】。
> 引文说明：合字 `fi`/`fl` 已还原，弯引号已还原为直引号；**用词与数字未改**。

---

## 5.1 总纲：计划不是文档，是"冻结设计的机制"

> **原文（p103）**：
> 「The test plan is **the foundation for the entire test**. It addresses the how, when, where, who, why, and what of your usability test.」

> **原文（p103）**：
> 「prior to the test you need to set **a reasonable deadline after which the test plan may not change**. Let that date also serve as the point at which **the product can no longer change until after the test**.」

> **★★★★ 判据：测试计划最重要的功能是"截止日"，不是"写下来"**
> 计划书本身是手段；真正起作用的是它锚定的两个冻结：**计划冻结**（问什么不再变）与**产品冻结**（测什么不再变）。
> 没有冻结日 → 测的是"某个移动中的版本" → 结论无法归因。

> **原文（p103）**：
> 「If you are pressured to revise the test after the cutoff date, **make sure that everyone understands the risks involved**. The test may be invalidated, and the product may not work properly with changes made so close to the test date.」

### 5.1.1 四个作用

| # | 作用（原文 p104 标题） | 原文要点 |
|---|---|---|
| 1 | It Serves as a Blueprint for the Test | 「the test plan describes exactly how you will go about testing your product」 |
| 2 | It Serves as the Main Communication Vehicle | 「the document that all involved members of the development team ... should review」 |
| 3 | It Defines or Implies Required Resources | 「Either directly or by implication」 |
| 4 | It Provides a Focal Point for the Test and a Milestone | 「forces you to approach the job of testing systematically」 |

> **原文（p105）**：
> 「**Remember to keep the end user in mind as you develop the test plan.** If you are very close to the project, there is a tendency to forget that **you are not testing the product, you are testing its relationship to a human being with certain specific characteristics.**」

> **★★★ 判据：测试对象是"人—产品关系"，不是产品**
> 这条决定了任务写法（见 §5.5）：任务必须从人的目标出发，不能从功能清单出发。

---

## 5.2 计划的九个组成部分

> **原文（p105）**：
> 「the following are the typical sections to include」
> - 「Purpose, goals, and objectives of the test」
> - 「Research questions」
> - 「Participant characteristics」
> - 「Method (test design)」
> - 「Task list」
> - 「Test environment, equipment, and logistics」
> - 「Test moderator role」
> - 「Data to be collected and evaluation measures」
> - 「Report contents and presentation」

### 5.2.1 Purpose：要写"为何此刻"，不是"要测什么"

> **原文（p106）**：
> 「you need to describe at a high level **the reasons for performing this test at this time**. ... The important point is that **the testing be tied to business goals within the organization** and that testing is the most appropriate technique for addressing the problem or opportunity.」

原文给的正当理由样例（p106，以问句形式）：
- 「Is the test attempting to resolve problems that have been reported by the company's call center or support desk?」
- 「Have server logs or web usage statistics shown that visitors to your company's web site leave the site at a particular point in a process that leaves a transaction incomplete?」
- 「Has a new policy recently been instituted stating that all products must be tested before release?」

### 5.2.2 不该测的六种理由（关键清单）

> **原文（p106）**：
> 「Following are some rather vague, inappropriate reasons for usability testing a product. These are rarely placed on paper but are usually communicated via word of mouth. They are not sound reasons for testing, and invariably they often come back to sabotage the project.」

| # | 不该测的理由（原文） | 为什么站不住（原文） |
|---|---|---|
| 1 | 「You can improve the user experience」 | 「you may be able to test one part of the customer experience but not all the touch points your company has with customers」 |
| 2 | 「Everyone else has a usability testing program」 | 「everyone else has many things」 |
| 3 | 「The meeting rooms used for testing are available the third week of the month」 | 「so is the cafeteria every evening」 |
| 4 | 「Lou just went to the latest ACM SIGCHI ... conference and learned about this really neat testing technique」 | 「let Lou promote the technique's benefits to the organization first」 |
| 5 | 「You want to see if there is a need for this type of product in the marketplace」 | 「backwards logic; a focus group or survey is a more appropriate technique early on」 |

> **原文（p107）**：
> 「you must tie testing to the needs of the product and to the organization's overall business needs. Otherwise, **you run the risk of your testing becoming one more fad**, one more of the latest approaches that come and go with the seasons.」

> **★★★ 判据：五种"伪理由"的共同点是"手段倒置"**
> 都在用"我们有能力测"替代"我们需要知道"。第 5 条尤其重要：**市场需求有无不属于可用性测试**，那是焦点小组/问卷的活（详见 `user-research-methods`）。

### 5.2.3 Research questions：计划里最重要的一节

> **原文（p107）**：
> 「This section is **the single most important one in the test plan**, because it describes the issues and questions that need to be resolved and focuses the research」

> **原文（p107）**：
> 「It is essential that the research questions be **as precise, accurate, clear, and measurable (or observable) as possible**. Even when conducting exploratory testing in the early stages of developing a product, which is typically less structured, **you still need to accurately describe what you hope to learn**.」

> **原文（p107）**：
> 「Without a clear succinct research question(s), you might find yourself in the unenviable position of **conducting a wonderful test that neglects to answer**」

> **★★★★ 判据：研究问题必须是"可观察"的，不是"可描述的"**
> 反例（本文自拟，不是原文）："测试这个界面是否易用"——不可观察。
> 正例（原文 p110 图 5-2 的实际写法）：
> - 「How easily and successfully do travelers get started with making a reservation on the site?」
> - 「What paths do travelers take to completing a booking?」
> - 「What obstacles do travelers encounter on the way to completing a booking, whether using a credit card or rewards?」
> 特征：每句都能对应到"看什么"和"记什么"。

---

## 5.3 任务清单（Task List）：团队内部版

### 5.3.1 两个阶段

> **原文（p117）**：
> 「There are two stages to developing these tasks. In the early stages of developing the test, **the task list description is intended only for members of the project team and not for eventual participants.** ... Later, you will expand the tasks into full-blown **task scenarios**, which are presented to the participants.」

> **★★★ 判据：任务清单与任务场景是两个交付物，不可合并**
> 任务清单是给团队看的（含成功标准、材料状态、基准时间）；任务场景是给被试看的（只有情境与目标）。
> **合并的后果**：把成功标准或功能名写进被试看到的文本 → 直接泄题（见 §5.5.3）。

### 5.3.2 任务的四个部分

> **原文（p117）**：
> 「For the test plan, you need only touch on four main components of each task:」

| # | 部分（原文 p117–p118） | 写法要求 |
|---|---|---|
| 1 | 「A brief **Description** of the Task」 | 「A one-line description is usually enough.」 |
| 2 | 「The **Materials and Machine States** Required to Perform the Task」 | 要写明被试是否需要文档、界面上哪些部分被用到 |
| 3 | 「A Description of **Successful Completion** of the Task」 | SCC（成功完成标准） |
| 4 | 「**Timing** or Other Benchmarks」 | 超时上限或错误率上限 |

> **原文（p118）**：
> 「It is amazing how much disagreement there will be over this question and how often **developers have differing opinions on what represents successful completion of a task**. When you include successful completion criteria (SCC) with the task description, you add precision to what you are measuring」

> **原文（p118）**：
> 「**When you have difficulty ascertaining the SCC, it reflects the development team's confusion about the product design.** Establishing and documenting the SCC is a good exercise just for that reason alone.」

> **★★★★ 判据：写不出成功标准 = 设计本身还没想清**
> 这是**测试对设计团队的第一个价值**：在测之前就把含混暴露出来。
> 落地用法：写 SCC 时如果团队吵起来了，别急着测——先把这个设计问题解决掉。

### 5.3.3 计时基准（benchmark）怎么定

原文侧栏（p119–p120）给了一套可复制的做法：

> **原文（p119）**：
> 「Benchmarks help to evaluate participant performance during a test. While they are **not absolutely necessary**, they can help you to monitor and evaluate the results of a test session more precisely」

> **原文（p119）**：
> 「it should be emphasized that they **need not be deadly accurate**. In fact, if you are conducting iterative, ongoing testing, you will be revising the benchmarks from test to test」

四个来源（p119）：
- 「Any original case studies, interviews, or customer visits you may have performed」
- 「Any usability objectives that were included as part of the product or functional specification」
- 「Any usability data from previous tests that were performed」
- 「Polling in-house end users who fit the user profile in one's own company」

**Jeff 的实际做法（p120，可直接照抄）**：

> **原文（p120）**：
> 「Jeff had **three engineers** provide estimates of the maximum time that they felt a user would need to correctly perform each task on the test. He also had **three technical writers** on the project give the estimates because their perspective on the end user was different. He then **averaged all estimates**, and, to give everyone the benefit of the doubt, he **multiplied the average for each task by a constant of 2.5** to come up with the maximum time for a participant to complete the task.」

> **原文（p120）**：
> 「As it turned out, **some of the tasks took up to three times longer than even these generous benchmarks**, which really drove home the point about difficulties.」

> **★★★★ 判据：计时基准 = 六人估算均值 × 2.5（故意给宽）**
> 这个 2.5 是"防争议"用的：宽到没人能说"你没给够时间"，结果任务仍然超时 3 倍——**反而成为最有力的证据**。
> 注意：原文明确说这个常数「rather arbitrary and quite generous」。

> **原文（p120）**：
> 「**Measuring time on tasks is not always the best, most accurate measure of task success.** If you are asking participants to think out loud, doing so takes time and unnaturally lengthens the duration.」

> **★★★ 判据：出声思维 × 计时 = 互斥组合**
> 二选一。要计时就别让被试出声，要出声就别拿时间当指标（改数错误数与提示次数）。

### 5.3.4 任务如何取舍（四种优先级）

> **原文（p123）**：
> 「Due to time constraints, **very rarely do you actually test the full range of tasks** that comprise an entire interface, documentation, or both together. ... Instead, you typically face a situation of testing **a representative sample** of the product's functions.」

| # | 优先级依据 | 原文口径 |
|---|---|---|
| 1 | **频率** | 「the most frequently performed tasks ... possibly up to **75 to 80 percent** of the time」；通不过 75% 线的任务才算次要 |
| 2 | **关键性** | 「if performed incorrectly or missed, have serious consequences either to the end user, to the product, or to the reputation of the company」 |
| 3 | **易损性** | 「those tasks that you suspect, even before testing, will be hard to perform or that have known design flaws」 |
| 4 | **就绪度** | 「you may simply have to go with functions that are ready」／「to be tested or forgo testing entirely」（原文跨 p124/p125 页界） |

> **原文（p124）**：
> 「If you cannot fill all cells with four participants, then consider biasing toward the users who are like most users in your target population.」

> **原文（p124）**：
> 「Often, tests are filled with a series of obscure tasks that **less than 5 percent** of the end user population will ever find, never mind use. Why? Our theory is that **the development team finds those "five percenters" the most interesting and challenging tasks to implement**, because they are usually the leading edge of the product.」

> **★★★★ 判据：警惕"五个百分点任务"——开发者偏爱的东西用户根本不用**
> 这是任务清单最常见的污染源。**自检问法**：这个任务，多少比例的真实用户一年会做一次？答不上来就别测它。
> 原文给的补充线：覆盖完 75% 的任务后，若还有时间，再加「at least 25 percent of your end user population perform regularly」的任务。

> **原文（p124）**：
> 「Sometimes, developers pretend, in the name of "being unbiased," that all functions work equally well (or poorly) ... **tasks that are obviously hard to perform and that represent whole components, web pages, or sections of a document are left out of the test** and prove to be albatrosses much later when there is no time to fix them.」

> **★★★ 判据："一视同仁"可能是一种回避**
> 所有功能都测 = 优先级缺失。真正的公正做法是**按易损性显式挑选**，并把"为什么挑它"写进计划。

---

## 5.4 出声思维（Think-Aloud）：三种变体

这是"测中"技术的核心，也是本书与 Barnum 书重合最多的部分。**必须区分三个变体**，因为它们的适用条件与代价完全不同。

### 5.4.1 变体一：同步出声思维（concurrent think-aloud）

> **原文（p242）**：
> 「The "thinking aloud" technique is a simple technique intended to **capture what the participants are thinking while working**. To implement this technique, have the participants provide a running commentary of their thought process by thinking aloud while performing the tasks of the test.」

**优点（原文 p242 四条）**：
- 「You are able to **capture preference and performance information simultaneously**」
- 「The technique can help some participants to **focus and concentrate**」
- 「You are constantly receiving **early clues about misconceptions and confusion** before they manifest as incorrect behaviors」
- 「Participants can reveal **how they are thinking** about doing a task and why things work or don't work for them」

**缺点（原文 p243 三条）**：
- 「Some participants find the technique **unnatural and distracting**」
- 「Thinking aloud **slows the thought process, thus increasing mindfulness**. Normally, this is a good effect, but in this case it **can prevent errors that otherwise might have occurred** in the actual workplace」
- 「it is just plain **exhausting** to verbalize one's thought process for very long」

> **★★★★ 判据：出声思维的代价是"它让被试变得更小心"**
> 这是最反直觉也最重要的一条：**出声思维会减少错误**，因为说话这个动作提高了专注度。
> 后果：**不要用出声思维去测真实错误率**。它会系统性地高估产品（把错误测没了）。
> 原文的原始表述更狠：「Ideally, you want your participants to pay **neither more nor less** attention to the task at hand than they normally would.」

> **原文（p243）**：
> 「**Avoid using it for very short or pointed tests** where the unusual aspect of the technique does not have time to wear off.」
> 例（p243）：Jeff 测"用户是否注意到硬件上的某个标签"，每次会期仅 10 分钟；「The very act of saying, "Now I'm loading the paper. Now I'm pulling out the tray," made the process unusually deliberate. Consequently, he **stopped using this method after the second participant**」

**五条增强做法（原文 p243–p244）**：
| # | 做法 | 原文 |
|---|---|---|
| 1 | 先示范 | 「Demonstrate the technique first, so that participants feel less self-conscious」 |
| 2 | 不强推 | 「Do not force the technique if you encounter strong resistance」 |
| 3 | 注意沉默 | 「**Pay attention to where participants become quiet.** This can indicate that they are concentrating on solving some problem」 |
| 4 | 回声确认 | 「Acknowledge that you are listening ... by periodically repeating comments back」 |
| 5 | 有意义地沉默 | 「Count to **20 or 30** before asking for clarification」 |

> **★★★ 判据：被试沉默时不要打破沉默——沉默是"正在思考"的证据**
> 原文做法：记下时间点，稍后再问，而不是当场打断。
> 「It's almost always better if the participant verbalizes unprompted.」

### 5.4.2 变体二：回溯复盘（retrospective review）

> **原文（p92）**：
> 「An alternative to having participants think aloud is to **replay the test with the participant after all of the tasks are done**.」

> **原文（p93）**：
> 「**Review can be a good tool to use with participants for whom talking and working might be difficult**, such as **small children, very old adults, and people with cognitive disabilities**.」

> **原文（p93）**：
> 「A serious drawback to performing a review is **the time it takes to do**. ... **It can take as much time as or more time than the main part of the session** actually took. Some practitioners also avoid retrospective review because it **gives some participants opportunity to revise and rationalize their behavior** rather than simply reporting on what happened and why.」

> **★★★ 判据：回溯复盘的适用人群 = "边说边做"有困难的人**
> 原文点名的三类：幼儿、高龄老人、认知障碍者。
> **代价两条**：耗时翻倍；被试会"事后合理化"（记忆被现在的理解改写）。

### 5.4.3 变体三：协同发现（co-discovery，两人同时）

> **原文（p306）**：
> 「This technique uses **two participants simultaneously** during a usability test instead of a single participant. The participants are encouraged to communicate with each other during the test session, and it is this communication that is the key difference during a session.」

> **原文（p306）**：
> 「The act of participants talking to each other offers **an alternative to a moderator prompting one participant to think aloud**. Some practitioners believe that this exchange between peers to be **more natural, and therefore more reliable**, than the typical moderator-participant relationship.」

> **原文（p307）**：
> 「usually one person will work on the product, while the other offers advice. At scripted points during the session, they should **trade places**.」

> **原文（p307）**：
> 「This technique can be especially effective with some special audiences, such as **children**. Whether they know each other or not, children may be more willing to play together ... than to try something alone with an adult who is a stranger to them.」

> **★★ 判据：协同发现的适用条件是"真实场景里本来就两人一起用"**
> 原文举例：化学分析（一人定方法、一人跑软件）。**若真实使用是单人，两人同时在场会制造出不存在的行为。**
> 风险（原文 p307）：需注意配对性格，「you may have to intervene in a session if one person is dominating the session」。

### 5.4.4 三变体对照表（本章核心速查）

| 维度 | 同步出声 | 回溯复盘 | 协同发现 |
|---|---|---|---|
| **人数** | 1 | 1 | 2（可互换角色） |
| **拿到"为什么"的时点** | 实时 | 事后 | 实时（被试之间对话） |
| **最大优点** | 绩效+偏好一次拿全；早发现误解 | 适用于边说边做困难者 | 对话自然，不靠主持人催 |
| **最大代价** | **减少错误**（提高专注） | 耗时翻倍 + 事后合理化 | 制造"双人协作"这一非真实情境 |
| **不能用于** | 计时任务；极短任务；只需 10 分钟的任务 | 长会话（前段记不住） | 单人使用的产品 |
| **出处** | p242–p244 | p92–p93 | p306–p307 |

---

## 5.5 任务场景（Task Scenarios）：给被试看的版本

### 5.5.1 定义与五个要素

> **原文（p220）**：
> 「Task scenarios are **representations of actual work** that the participants would conceivably perform using your product. Task scenarios are **expanded versions of the original task list** ... adding **context and the participant's rationale and motivation** to perform those original tasks.」

> **原文（p220）**：
> 「In many cases, **one task scenario will comprise several tasks from the task list grouped together because that is the way that people perform their work on the job**.」

任务场景应描述（原文 p220 五项）：
1. 「The **result** that the participant will strive to achieve」
2. 「**Motives** for performing the work」
3. 「**Actual data and names** rather than generalities」
4. 「The **state of the system** when a task is initiated」
5. 「**Readouts of displays and printouts** that the participants will see」

> **★★★ 判据：一个场景可以包住多条任务，因为真实工作就是这样**
> 这与 §5.3 的"一任务一行"清单相反。**清单求可管理，场景求真实**。

### 5.5.2 五条写法准则

| # | 准则（原文标题 p221–p223） | 原文要点 |
|---|---|---|
| 1 | 「Provide **Realistic Scenarios**, Complete with Motivations to Perform」 | 「The closer that the scenarios represent reality, the more reliable the test results.」 |
| 2 | 「**Sequence** the Task Scenarios in Order」 | 按真实执行顺序，能「Expose the snowballing effects of errors and misconceptions」 |
| 3 | 「**Match** the Task Scenarios to the Experience of the Participants」 | 新手不该被要求走高级功能；专家不该被要求走基础功能 |
| 4 | 「**Avoid Using Jargon and Cues**」 | 见 §5.5.3 |
| 5 | 「Try to Provide a **Substantial Amount of Work** in Each Scenario」 | 见 §5.5.4 |

> **原文（p221）**：
> 「if a participant misnames a file in an early task, that is not all that serious. However, when in a later related task that same participant uses that file name as the basis for naming **20 subordinate files**, the problem's ramifications become serious indeed」

> **原文（p221）**：
> 「If sequential order is not crucial to performance, then consider **varying the order of presentation** of scenarios to different participants. This approach, known as **counterbalancing**」

### 5.5.3 不许泄题：不提按钮名、菜单名、屏幕标题

> **原文（p222）**：
> 「Avoid product jargon or cues that serve as giveaways of the correct results. **Avoid wording that includes actual button names, menu items, and screen titles.**」

> **原文（p222）**：
> 「For example, even asking a novice participant to save a file is a giveaway if there is a "**Save**" command on the product. It points the participant in the right direction. Instead, say something like "**Ensure that the phone number of the person you just spoke with is retained in your phone.**"」

> **原文（p222）**：
> 「(We know this sounds ridiculous, and the participant may look at you funny and say "Do you want me to save the number?" If the participant does, just say yes, and realize that sometimes it is **necessary to make a fool of yourself in the interest of science**.)」

> **★★★★ 判据：任务的措辞不得包含界面上的任何字面**
> 检验方法：把任务文本与界面文案逐词比对，**凡重合的名词/动词都是嫌疑**。
> 例外（原文明确）：早期探索测试**可以**故意让被试找某个具体命令，但「that is a different kettle of fish entirely」——**要明确声明这是"找得到吗"的类型，不是"会不会用"的类型**。

### 5.5.4 一个场景要做"一大块活"

> **原文（p222）**：
> 「**Do not guide the participants through the product piecemeal**, unless your product is in such a primitive state that you must work that way. Rather, **provide a goal, clearly stated in simple language, and let participants do the rest.**」

原书示例（p222）：

> **原文（p222）**：
> 「"**Using this web site, you want to send some books to your nephew for his birthday.**"」

> **原文（p223）**：
> 「To accomplish this task, it is implied that the participants must either learn or exhibit the following skills:」
> - 「Search for and select books.」
> - 「Review the list of items being ordered.」
> - 「Enter the recipient's address.」
> - 「Specify the appropriate billing address.」

> **原文（p223）**：
> 「Whether the participants can perform or figure out these intermediate steps in order to complete the goal of the scenario is **precisely what you want to learn** from the usability test. If you simply ask them to search for and select books and then fill out the addresses needed, **you never see whether the participants can put it all together, as they must on the job**.」

> **原文（p223）**：
> 「**Remember, from the participant's viewpoint, the product is always considered a means to an end.** The participant's central focus is the work and the procedures required to perform that work. The product being tested is incidental to that, not central.」

> **★★★★ 判据：拆成小步 = 替被试做掉了最难的部分**
> 一个"整活"场景测的是**串联能力**；一串小步测的只是**每步的局部可用性**。
> 而真实使用中出问题最多的恰恰是串联（记住上一步、带着上下文进下一步）。
> **判据的二值化**：如果某一步失败后，下一步的任务文本需要你重写，说明你拆得太碎。

### 5.5.5 念给被试听，还是让被试自己读

> **原文（p223–p224）**：
> 「**Reading Task Scenarios to the Participants**」的优点：「you can interact with the participants and make sure they understand what to do」「enables you to **control the pace**」
> 「**Letting the Participants Read Task Scenarios Themselves**」的适用：「if you are testing from another room or if you want to **minimize contact** with the participants, as you would during a **validation test**」

> **原文（p224）**：
> 「Decide if you want the participants to see **only one scenario at a time**. If there are many scenarios or if the scenarios are very complex, viewing them all at one time could be **intimidating and distracting**.」

> **★★ 判据：一次只给一个场景（防止"预读"污染）**
> 原文给了可自动化的做法：让被试在电脑上逐条读取，离开该屏即开始计时，完成后回来勾掉即停止计时。

---

## 5.6 试点测试（Pilot Test）

> **原文（p253）**：
> 「Ideally, you should use a "**real**" participant, perhaps someone who is on the **lower end of the expertise scale** for what you are doing in this test. Doing so should give you a good feeling for how long it will take most users to do tasks (**a beginner being more likely to take longer**).」

> **原文（p253）**：
> 「Conduct **the entire test**, including reading the orientation script and providing the test scenarios. Practice the various data collection techniques you will be using. Instruct the participants to fill out all questionnaires that are part of the test.」

> **原文（p253）**：
> 「**The importance of conducting one or more pilot tests cannot be overstated. Do not cut this step short**, or you will find that your first one or two real participants will be used "to get the bugs out" of your testing process, essentially acting as the pilot test.」

> **★★★★ 判据：不跑试点，前 1–2 个真被试就是你的试点**
> 这句把"要不要跑试点"变成了成本问题：**省下的时间会以真实样本的形式还回去**。
> 落地：试点至少 1 人，且必须走完全流程（含脚本、问卷、记录表）。

### 5.6.1 试点的第二个作用：先修产品

> **原文（p253）**：
> 「Yes, **revise the product** or prototype or whatever it is you are testing. ... After all, **why waste valuable time testing those features and functions that you know are broken?**」

> **原文（p253）**：
> 「A note of caution is in order though. **Be careful about making too many product changes just prior to the start of the usability test**, especially software or firmware changes. Too many changes without adequate QA may cause the product to crash」
> 原文的教训（p253）：Jeff 允许程序员改到测试前一天，结果「the product was buggy and would not work longer than **five minutes without crashing**」，测试取消。

> **★★★ 判据：试点的产出是"改两样东西"——改测试材料，也改产品；但改产品要留调试时间**
> 原文的失败案例给的是硬约束：**测试前不要动产品代码**，除非留够 QA 窗口。

### 5.6.2 试点的时间安排

> **原文（p215）**：
> 「Conduct a pilot test」
> 「The point here is to know what you're testing and to feel comfortable that your session script matches up with what you want to happen in the testing room.」
> （清单项与说明句在同一页，中间夹清单条目，故分行照录。）

三份清单（原文 p214–p218，图 9-1/9-2/9-3 已文字化）：

**清单 1：测试前约一周**
- 「Take the test yourself」
- 「Conduct a pilot test」
- 「Revise the product」
- 「Check out all the equipment and the testing environment」
- 「Request that, if possible, the product be "frozen" for the test period」

**清单 2：测试前一天**
- 「Check that the video equipment is set up and ready」
- 「Check that the product, if software or hardware, is working」
- 「Assemble all written test materials」
- 「Check on the status of your participants」
- 「Double-check the test environment and equipment」

**清单 3：测试当天**
- 「Scan your customized checklist」
- 「Prepare yourself mentally」
- 「Greet the participant」
- 「Have the participant fill out and sign any preliminary documents」
- 「Read the orientation script and set the stage」
- 「Have the participant fill out any pretest questionnaires」
- 「Move to the testing area and prepare to test」
- 「Start recordings」
- 「Establish protocol for observers in the room」
- 「Provide any prerequisite training if your test plan includes it」
- 「Either distribute or read the written task scenario(s) to the participant」
- 「Record start time, observe the participant, and collect all critical data」
- 「Have the participant complete all posttest questionnaires」
- 「Debrief the participant」
- 「Close the session」
- 「Organize data collection and observation sheets」
- 「Debrief with observers」
- 「Provide adequate time between test sessions」
- 「Prepare for the next participant」

> **原文（p252）**：
> 「**Take your own usability test** and look for design flaws. Try to assume the mind set of your prospective users. Take timings to ensure that the test is achievable in the time allotted.」

> **★★★ 判据：试点前先"自己测自己"**
> 顺序是：**自测 → 试点 → 改产品 → 冻结**。自测是最便宜的一轮，能筛掉大部分笔误与流程断裂。

> **原文（p254）**：
> 「If at all possible, development should be stopped during the period in which you conduct usability test sessions. Any changes may affect the participant tasks or the scenarios for the test. In addition, a "freeze" stabilizes the product to **a known set of bugs that you can script around**, if needed.」

> **★★ 判据：冻结的实质是"把 bug 变成已知量"**
> 不冻结 → bug 集在测期中变化 → 被试之间的条件不一致 → 无法比较。

---

## 5.7 本章判据总表（共 20 条）

| # | 判据 | 出处 |
|---|---|---|
| 1 | 测试计划的核心功能是设"计划冻结日 + 产品冻结日" | p103 |
| 2 | 计划有四个作用：蓝图、沟通载体、资源界定、里程碑 | p104 |
| 3 | 测的对象是"人—产品关系"，不是产品 | p105 |
| 4 | 计划的九个标准小节（Purpose→报告内容） | p105 |
| 5 | Purpose 要写"为何此刻"，并绑到业务目标 | p106 |
| 6 | 五种伪理由的共同点是"手段倒置"（有手段代替有需求） | p106 |
| 7 | 研究问题是计划里最重要的一节，必须可观察 | p107 |
| 8 | 任务清单（给团队）与任务场景（给被试）是两个交付物 | p117 / p220 |
| 9 | 每个任务写四部分：描述／材料与机器状态／成功标准／基准 | p117–p118 |
| 10 | 写不出成功标准（SCC）= 设计团队还没想清 | p118 |
| 11 | 计时基准 = 六人估算均值 × 2.5，故意给宽 | p119–p120 |
| 12 | 出声思维与计时互斥；出声会拉长时长 | p120 |
| 13 | 任务按频率（75–80%）／关键性／易损性／就绪度取舍 | p123–p125 |
| 14 | 警惕"五个百分点任务"——开发者偏爱但用户不用 | p124 |
| 15 | "所有功能都测"是回避优先级，不是公正 | p124 |
| 16 | 出声思维会**减少错误**，不可用于测真实错误率 | p243 |
| 17 | 沉默不要打断（数 20–30 秒）；不打断时被试会自发说出来 | p244 |
| 18 | 回溯复盘适用"边说边做困难者"（幼儿/高龄/认知障碍），代价是耗时与事后合理化 | p93 |
| 19 | 协同发现只适用于真实场景本就两人共用；单人产品会造假行为 | p306–p307 |
| 20 | 不跑试点则前 1–2 个真被试变成试点；试点可改产品但须留 QA 窗口 | p253 |

---

## 5.8 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| 测试计划的完整模板（可填表） | 只给九个节标题与各节示例片段（图 5-1~5-9），无空白模板 | 可按 §5.2 九节自行搭表 |
| 研究问题的"好/坏"对照 | 只有正例（图 5-2 的 7 条），无系统反例 | 判据按 §5.2.3 的三问自检 |
| 任务场景的字数上限 | 只说"给一大块活"，无长度规范 | 本章未展开 |
| 出声思维的培训话术原文 | 只有"先示范"一条方向，示范说什么未给 | 本章未展开；话术见 ch07 §7.3 |
| 协同发现的配对规则 | 只说"注意性格，主导时要干预" | 本章未展开 |
| 试点的样本量与是否计入分析 | 只说"至少 1 人、下限能力者优先"，未说能否计入 | 见 ch06 §6.6（Barnum p190/p213 有"6 人里 1 人做试点"的口径） |

---

## 5.9 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| SCC 与基准 | 本书 ch08 严重度与达标判定 | 70% 阈值以 SCC 为前提 |
| 任务写法的"不泄题" | 本书 ch07 §7.3 主持话术 | 现场念任务时的同一原则 |
| 出声思维 × 计时互斥 | 本书 ch06 §6.6 样本量 | 计时类测试要走定量路线（人多） |
| 试点 | 本书 ch08 复测 | 试点是"测的测"，复测是"改的测" |
| 任务生成 | `design-psychology-norman` 七原则 | **接口见 §5.10** |
| 方法选择（何时不该用测试） | `user-research-methods` 技能 | 伪理由第 5 条即方法错配 |
| 任务的"真实工作"要求 | `design-methodology-liuguanzong` 事理学 | "事"的结构决定任务的串法 |

---

## 5.10 接口：把诺曼七原则翻译成测试任务

`design-psychology-norman` 给了**诊断词汇**（可视性、预设用途、概念模型、匹配、反馈、七阶段、两类鸿沟、四类限制、六类失误）；本书给**验证流程**。二者不是并列关系，而是"假设—检验"关系：**七原则负责生成"应该在哪里出问题"的预期，本流程负责把它变成可观察的任务**。

**翻译规则（四步）**：

| 步 | 动作 | 例（以微波炉/APP 通用写法） |
|---|---|---|
| 1 | 取一条原则 | 「可视性」 |
| 2 | 问：若违反，用户会**做什么错事**？ | 用户会找不到"取消"而拔电源 |
| 3 | 把这个错事写成**可观察的成功标准**（SCC） | 任务中途取消，须在 30 秒内用界面完成，无需断电 |
| 4 | 写**不含界面字面**的场景（§5.5.3） | 自拟示例（非原文）："你放错了食物，想让它立刻停下来" |

**七原则 → 任务形态对照**（供出题时逐条过）：

| 诺曼原则 | 会以什么形态暴露 | 任务该怎么写 | 观察什么 |
|---|---|---|---|
| **可视性** | 找不到入口/状态 | 只给目标，不给入口位置 | 首次注视点、搜索时长、误点 |
| **预设用途** | 按错/拧反/插不进 | 要求完成一次装配或插入操作 | 手部动作方向、试错次数 |
| **概念模型** | 用错模式、以为会同步 | 让用户跨两个功能做一次连贯操作 | 是否建立"东西去哪了"的预期 |
| **匹配** | 控制与结果不对应 | 让用户调一个连续量（音量/温度） | 调错方向、过冲、来回修正 |
| **反馈** | 不知道成没成，重复提交 | 让用户完成一次有延迟的提交 | 重复点击次数、口头疑问 |
| **限制因素** | 能做出危险/无效操作 | 故意给一个不该被允许的操作 | 系统是否拦住；用户是否困惑 |
| **行动七阶段** | 意图对但动作错（失误），或目标本身错（错误） | 用七阶段切分任务步骤，逐步给分 | 断点落在哪一阶段 |

> **★★★ 判据：七原则的产物是"预期缺陷清单"，不是"测试结论"**
> 用七原则写出来的东西一律标为**假设**，必须由本流程检验后才能进报告。
> 反用（把七原则当结论直接写进报告）是本机 13 个技能最容易发生的串味——`design-psychology-norman` 管"应该"，本技能管"是不是"。

> **判据的第二层用法**：若某条原则在测试中**完全没暴露问题**，要在报告里明写"该原则相关任务全部通过"。这条阴性结果对下一轮设计同样有价值，而它只有"先有假设"才写得出来。

**与行动七阶段的对接**（接口细化）：

| 七阶段 | 测试中的观察点 | 记录什么 |
|---|---|---|
| 确定目标 | 被试是否理解场景的动机 | 复述场景时的偏差 |
| 确定意图 | 是否知道"要做什么"而非"点哪里" | 第一句话的措辞 |
| 明确行动内容 | 是否能在界面上定位候选操作 | 搜索路径、悬停 |
| 执行 | 动作是否落在预期控件上 | 误操作 |
| 感知外部世界状况 | 是否注意到状态变化 | 是否看提示区 |
| 解释外部世界状况 | 是否读懂反馈含义 | 对提示的解读 |
| 评估行动结果 | 是否判断自己完成了 | 是否需要问"我这样对吗" |

> **★★ 判据：七阶段的断点位置决定"缺陷类型"**
> 断在"执行"前（找不到）→ 可视性问题；断在"评估"（不知成没成）→ 反馈问题。
> 这个映射让严重度评级（ch08）有了机理依据，而不是凭感觉打分。
