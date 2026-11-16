# 第 6 章：找人与选人——用户画像、筛选问卷、几个被试够

> **Rubin & Chisnell PDF 页序 p153–p190（38 页，含 p190 空白页）**｜**本版逐页读完全部 37 个有字页（p190 为空白页）**
> **Barnum PDF 页序 p38–p40、p148–p150、p213（引用于 §6.5.2、§6.6.9）**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N；Rubin 书内印刷页 = PDF 索引 − 38）
>
> **读法说明**：按原书 `7.x` 小节逐节展开，不跳节。
> 每节含【原文摘录】+【判据提炼】。
> **引文来源标注**：`（pN）` = Rubin & Chisnell；`（B pN）` = Barnum。
> 引文说明：合字 `fi`/`fl` 已还原，弯引号已还原为直引号；**用词与数字未改**。
> 本章是全技能最关键的一章：**"几个被试够"的数字在此，两本书口径不同，已并列写明**。

---

## 6.1 总纲：选错人，后面全白做

> **原文（p153）**：
> 「The selection and acquisition of participants whose background and abilities are representative of your product's intended user is a crucial element of the testing process. ... **If you test with the "wrong" people, it does not matter how much effort you put into the rest of the test preparation. Your results will be questionable and of limited value.**」

> **★★★ 判据：样本错误是不可补救的，其他错误大多可补救**
> 主持失误可以靠多被试/多轮抵冲（ch04、§6.6），任务写错可以补问，但**被试不对，问什么都是错的**。

---

## 6.2 用户画像：先"看见一个人"，再列条件

### 6.2.1 企业里通常没有现成的画像

> **原文（p153）**：
> 「your first thought might be that the information describing the user profile should already exist and be written down somewhere within your organization ... While this is so in theory, **experience shows that this information is rarely collected systematically or written down.**」

> **原文（p154）**：
> 「go around and ask three or four different staff members in the product team to describe users of the product they are working on. Most likely, you will receive **three or four very plausible, but very different, descriptions** of the end user.」

> **原文（p154）**：
> 「**It is just this lack of a clear delineation of the characteristics of the end user that contributes to usability deficiencies of products in the first place.** ... Testing just happens to be one of the first activities that makes this lack of a clear end user characterization so **painfully obvious**.」

> **★★★ 判据：画像缺失本身就是缺陷的成因，测试只是把它照出来**
> 这条把"招人"从事务性工作提升为设计工作：**画像写得清，产品的一半问题就已经避免了。**

### 6.2.2 用一句话"看见"被试

> **原文（p154）**：
> 「Start by **visualizing and describing the person you want to be in the testing room with you**. This is a simple narrative sentence or short paragraph」

> **原文（p154）**：
> 「We want to find out where in the process of booking a room at one of our hotels travelers meet obstacles to completing reservations [the test objective]. The user of our web site reservation system travels at least a few times a year and stays in a hotel each time. He or she typically books his or her own travel online, especially leisure travel. He or she may belong to hotel rewards programs.」

> **原文（p154）**：
> 「That's exactly the idea: **See a person rather than a list of qualifications.**」

> **★★ 判据：画像的第一稿应是叙述句，不是条件表**
> 条件表（年龄/收入/职业）容易写成"人口统计套话"；叙述句迫使你写出**行为**，而行为才是可用性的相关变量。

### 6.2.3 买家 ≠ 用户

> **原文（p154–p155）**：
> 「make sure to **differentiate between the purchaser or buyer of the product and the actual end user** ... You probably would not want to bring in "purchasers" to test the product; **that will give you a very slanted view** of how the product is performing.」

> **原文（p155）**：
> 「Another potential pitfall is the fact that **the end user of the product and the end user of the documentation may differ.**」

> **★★★ 判据：要区分三种人——付钱的、用的、读文档的**
> 三者可能完全不同。测试对象应是**使用者**；若文档面向另一群人（如系统管理员），文档测试要单独招人。

### 6.2.4 画像的来源（六处）

| # | 来源（原文 p155–p157） | 要点 |
|---|---|---|
| 1 | 「Requirements and Specification Documents」 | 功能规格／BRD／设计规格／用例（「actors」） |
| 2 | 「Structured Analyses or Marketing Studies」 | 任务分析、营销研究 |
| 3 | 「Product Manager (R&D)」 | 「should have his or her finger on the pulse of the marketplace」 |
| 4 | 「Product Manager (Marketing)」 | 「Very often all the information you need is contained in reports of this type but in a form that is not all that accessible」 |
| 5 | 「Competitive Benchmarking and Analysis Group」 | 他们会同时了解自家与竞品的使用者 |
| 6 | 直接访谈上述人（推荐） | 「**interview these sources yourself rather than through a third party**, so that you can probe」 |

---

## 6.3 操作化定义：把"新手/专家"变成可筛的条件

### 6.3.1 不定义就等于没说

> **原文（p157）**：
> 「it is important to be **crystal clear about the meaning of such terms as "novice," "expert,"** and so forth. Often these terms are bandied about so indiscriminately that they are useless.」

> **原文（p157）**：
> 「**An operational definition should quantify a user's experience in terms of some objective reference point** such as complexity of typical tasks and the frequency with which a specific task is performed.」

### 6.3.2 时长 ≠ 熟练度（原文的反例）

> **原文（p157）**：
> 「It is tempting to use time and frequencies as a measure of expertise. **While these are measures of experience, they do not always describe expertise.**」

> **原文（p157）**：
> 「Though Dana expected that someone who had been using the web for a few years for **60 hours per week** would be an expert web user, this was not the case. One notable participant **did nothing on the web but play four specific games, getting to each from shortcut icons set up for her by her grandson. She didn't know how to use a web browser at all.**」

> **★★★★ 判据：使用时长与频次会系统性高估熟练度**
> 反例极强：60 小时/周 × 数年 = 被判定为专家，实际根本不会用浏览器（此句为我的译述，非原文）。
> **根因**：时间被花在**极窄的任务集**上。**筛人必须问"做过哪些不同的事"，不能只问"用了多久"。**

### 6.3.3 用矩阵代替自评

> **原文（p158）**：
> 「**It's more accurate to use criteria that are measurable, objective "facts" rather than subjective self-classifications** on the part of potential end users.」

> **原文（p158）**：
> 「**With self-rating, however, you run the risk of each end user having different interpretations of what is meant by such terms as novice or expert.** You are dependent on the user's self-image to guide the classification.」

原书图 7-1 的矩阵结构（p158 已文字化）：

| 任务（行） | Never (0) | Once per month (1) | Once per week (2) | Daily (3) | Several times a day (4) |
|---|---|---|---|---|---|
| Research health information such as conditions, treatments, or drugs at websites | | | | | |
| Take part in online auctions | | | | | |
| Play games alone or with others on websites | | | | | |
| Pay bills through a web site | | | | | |
| **Totals** | 勾数×0 | 勾数×1 | 勾数×2 | 勾数×3 | 勾数×4 |

> **原文（p158）**：
> 「The team can determine a "**score**" for how each combination of tasks and frequencies defines different levels of expertise.」

> **★★★★ 判据：筛熟练度用"任务 × 频次"打分行，不用自评标签**
> 三个好处：① 术语一致 ② 可复算 ③ 能落到筛选问卷的具体题项（见 §6.5）。
> **落地**：矩阵宜 4–6 行；行是**产品真正依赖的**任务，不是泛泛的上网行为。

### 6.3.4 需求（Requirements）与分类器（Classifiers）

> **原文（p159）**：
> 「**Requirements describe what participants must come into the session knowing already. Classifiers help you put study participants into categories (or groups) that may explain some effects you see in the test.**」

> **原文（p159）**：
> 「In this test, a participant must:」
> - 「**Stay at a hotel a few times a year**: We want people who would normally stay in a hotel rather than with friends or family or at a hostel」
> - 「**Book some travel and accommodations online**: Because this is an online reservation system, we want people who are familiar and com」……「fortable with doing searches and credit card transactions on the web.」（原文此处被页界断字，故用 `……` 标出接续。）

> **★★★★ 判据：Requirements 是"门槛"（不合格就淘汰），Classifiers 是"格子"（合格但要分组）**
> 二者在筛选问卷里的处理方式不同：
> - Requirements → 答案是"否"就 **Terminate**
> - Classifiers → 答案是任何值都保留，但**记录并配额**
> 混用会导致"把分类器当门槛"，从而招来一群同质的人。

---

## 6.4 矩阵设计：让每个格子都有人

> **原文（p163）**：
> 「consider a **matrix design** for the test that balances different variables or classifiers in such a way that **no particular user group or cell of the matrix is left out**.」

原书银行的例子（p163，原文表格已文字化）：

| USER GROUP | NOVICE | EXPERT |
|---|---|---|
| Teller | 4 | 4 |
| Back office clerk | 4 | 4 |

> **原文（p163）**：
> 「you might test **16 participants** whose job and experience level look like the ones in the table below」

> **原文（p163）**：
> 「You could look at the factors you use to determine expertise as **domain knowledge** (for example, what the participant knows about being a teller) or **tools knowledge** (for example, the efficiency and effectiveness with which the participant uses the software or other technology required in her job).」

> **★★★ 判据：矩阵的两轴要选"领域知识"和"工具知识"，它们会各自独立出错**
> 一个人可能懂业务但不会用软件（domain 高 / tools 低），也可能反之。二者混成一个"专家/新手"轴会丢掉这个交叉。

---

## 6.5 几个被试够（★本章核心，两本书并列）

### 6.5.1 Rubin 的口径

> **原文（p110）**：
> 「**For a true experimental design, you must use a minimum of 10 to 12 participants per condition.** However, for the purpose of conducting a less formal usability test, **research has shown that four to five participants who represent one audience cell will expose about 80 percent of the usability deficiencies of a product for that audience**, and that this 80 percent will represent most of the major problems.」

> **原文（p110）**：
> 「Of course, if you have the time and resources to study more than four or five participants, by all means do so. **It is possible that the additional 20 percent of deficiencies you might find could be important for your product.**」

> **原文（p110–p111，跨页）**：
> 「In one, **Jeff tested eight participants and discovered about 80 percent of the problems within the first four participants. However, participant 8, the last one, performed a particularly grievous error on one task that would have required a service call for the product. This would never have been uncovered**」
> 「**had we only tested four participants.**」

> **原文（p164）**：
> 「If, however, you are simply attempting to expose as many usability problems as possible in the shortest amount of time, then **test at least four to five participants of each user or audience cell**. Research indicates that testing four to five participants of each type or cell will expose the vast majority of usability problems. However, **we add that we are a bit uncomfortable testing only four participants, and we try to test at least eight participants if possible.** While you may expose most of the usability problems with four participants, **there is still a good chance you may overlook a problem that could have severe ramifications.**」

> **原文（p164）**：
> 「If you use a matrix design, try to test **at least four participants per user group** (one cell of the matrix equals a user group). If you cannot fill all cells with four participants, then consider **biasing toward the users who are like most users in your target population**.」

> **原文（p164）**：
> 「An important consideration is whether you will conduct **more than one test** during the product development life cycle. If you are going to conduct multiple tests, then **you can feel more confident testing fewer participants in each test**. For example, **if you conduct three tests with five participants each, you end up testing fifteen people.** If you will be conducting a single test, however, then you will be better served by having more participants for that lone test.」

**Rubin 的折中方案：discount 式迭代**

> **原文（p111）**：
> 「you may want to institute a practice of "**discount**" usability testing, in which you would run **several small, iterated usability tests over time**. That is, conduct a test with **4 or 5 participants from one cell and one or two conditions**, incorporate the findings into the interface, and then conduct another test with a similar set of participants and conditions. **Over three or four tests, you end up with a large sample of participants**, but the development team is able to accommodate changes in between tests.」

### 6.5.2 Barnum 的口径

> **原文（B p38）**：
> 「Nielsen and Landauer (both working as researchers at Bellcore at that time) determined that **the maximum cost-benefit ratio**, derived by weighing the costs of testing and the benefits gained, **is achieved when you test with three to five participants**, as shown in the classic "curve"」

> **原文（B p39）**：
> 「According to Nielsen, **you should stop after the fifth user because you are seeing the same things repeated**, and you will have reached **the optimal return of 85% of the findings** to be uncovered.」

> **原文（B p39）**：
> 「**Virzi and Lewis each found that small studies uncover 80% of the findings from a particular test. Nielsen and Landauer said the number was 85%.**」

> **原文（B p40）**：
> 「Putting these research findings together, **we can safely say that small studies can uncover 80-85% of the findings from a particular test. This result is not to be confused with uncovering 80-85% of usability findings for the entire product. That would take many, many studies.** However, the findings from a particular study can frequently be applied to other parts of the product not tested.」

> **原文（B p39）**：
> 「**The most striking truth of the curve is that zero users give zero insights.** As soon as you collect data from a **single test user**, your insights shoot up and you have already learned **almost a third** of all there is to know about the usability of the design.」

**Barnum 的试点口径（与样本量直接相关）**：

> **原文（B p213）**：
> 「**I typically recruit six people for a one-day study**, telling the client that **if we can't use the findings from the pilot user, we will still have enough to work with from five users from a single subgroup.**」

### 6.5.3 两本书的差异（并列说明，不合并）

| 项 | Rubin & Chisnell 2008 | Barnum 2010 |
|---|---|---|
| **最小可接受人数** | 「four to five participants **who represent one audience cell**」（p110）；「at least four to five participants of each user or audience cell」（p164） | 「**three to five** participants」（B p38，引 Nielsen & Landauer） |
| **"够"的定义** | 「expose about **80 percent** of the usability deficiencies of a product **for that audience**」（p110） | 「**80–85%** of the findings **from a particular test**」（B p40）；Nielsen 口径为 **85%**（B p39） |
| **作者自己的实践主张** | 「**we are a bit uncomfortable testing only four** ... **and we try to test at least eight participants if possible**」（p164） | 「I typically **recruit six** ... still have enough to work with from **five**」（B p213） |
| **停止判据** | 无明确停止点；建议**按单元格 4–5 人，能多则 8** | 「**stop after the fifth user** because you are seeing the same things repeated」（B p39，引 Nielsen） |
| **多轮替代** | 「three or four tests」× 4–5 人 →「a large sample of participants」（p111） | 「iterative testing」+ 小研究快跑（B p42） |
| **数字的适用范围** | 明确限定为「one audience cell」（单一人群格子） | 明确限定为「a particular test」（单次测试），**不是整个产品** |

> **★★★★ 判据（两书公认部分）：4–5 人/格子能发现约 80%，但没有"停止点"共识**
> 两本书在"4–5 人 × 单一人群格子 ≈ 80%"上完全一致（Rubin p110、Barnum B p38–p40）。
> **差异在三点**：
> 1. **下限**：Barnum 引 Nielsen 说 3–5 人即可（成本收益最优），Rubin 说 4–5 人。
> 2. **上限实践**：Rubin 主张"尽量 8 人"，Barnum 主张"招 6 人、按 5 人用"。
> 3. **停止规则**：Barnum 引 Nielsen"第 5 个之后停"，Rubin **不给停止点**，改为"多轮迭代累计样本"。
>
> **本技能的裁决（可执行）**：
> - 只做一轮 → 按 **Rubin：8 人/主格子**（保守）
> - 能迭代 3–4 轮 → 按 **Rubin discount：每轮 4–5 人/格子**
> - 预算极紧只做 1 轮 → 按 **Barnum：5 人**，但**必须在报告里写明"这是下限，未发现的 15–20% 可能含严重问题"**
> - **任何情况下不引"5 个就够"作为停止理由** —— 两本书都没有给出"够了"的判据，只给了"覆盖比例"。

> **★★★ 判据：80% 是"覆盖率"，不是"置信度"**
> Barnum 特别强调不要混淆：「This result is not to be confused with uncovering 80-85% of usability findings for the entire product.」（B p40）
> **误用后果**：把"本次测试发现 80% 问题"讲成"产品已达 80% 可用"——这两句完全不同。

### 6.5.4 数字的完整出处清单（供核验）

| 数字 | 含义 | 出处 |
|---|---|---|
| 4–5 人/格子 → 约 80% | Rubin 的核心建议 | Rubin p110 |
| 10–12 人/条件 | 真实验设计的最低要求 | Rubin p110、p62 |
| 至少 8 人 | Rubin 的实践偏好 | Rubin p164 |
| 4 人/格子（矩阵） | 矩阵设计的每格下限 | Rubin p164 |
| 15 人 | 3 轮 × 5 人 | Rubin p164 |
| 3–5 人 | 成本收益最优（Nielsen & Landauer） | Barnum B p38 |
| 80% | Virzi / Lewis 的口径 | Barnum B p39 |
| 85% | Nielsen & Landauer 的口径 | Barnum B p39 |
| 「almost a third」 | 第 1 个用户即获得的洞察比例 | Barnum B p39 |
| 80–85% | Barnum 的合并结论（限"单次测试"） | Barnum B p40 |
| 6 人（按 5 人用） | Barnum 的招募实践 | Barnum B p213 |

---

## 6.6 筛选问卷：逐步写出来

### 6.6.1 它的双重作用

> **原文（p164）**：
> 「The screening questionnaire is the means for **qualifying and selecting** participants to participate in the test. Its content is typically obtained from the characteristics, requirements, and classifiers that you included in the user profile and test plan.」

> **原文（p164）**：
> 「If you will be using a colleague, an outside consultant, or an agency to help you recruit participants, **the screening questionnaire is your primary way of describing the people you need in an unambiguous format.**」

> **原文（p164）**：
> 「While some agencies will develop their own screeners based on information you provide, **you must review their questionnaires before they begin using them**, to ensure that your instructions have been understood.」

> **原文（p165）**：
> 「developing the screening questionnaire **exposes any uncertainties and lack of clarity in one's own understanding of the end users. It forces you to express the background of your participants in precise, measurable terms.**」

> **★★★★ 判据：筛选问卷是"用户画像的可用性测试"**
> 写不顺 = 画像没想清。这与 ch05 §5.3.2 的 SCC 判据同构：**两个"写不出来"都指向同一个病根。**

### 6.6.2 七步流程（原文 p165）

| 步 | 原文 | 说明 |
|---|---|---|
| 1 | 「Review the profile to understand users' backgrounds.」 | 回到画像 |
| 2 | 「Identify specific selection criteria.」 | 抓产品特有属性 |
| 3 | 「Formulate screening questions.」 | 转成问题 |
| 4 | 「Organize the questions in a specific order.」 | 先放最可能淘汰的 |
| 5 | 「Develop a format for easy flow through the questionnaire.」 | 让打电话的人不需思考 |
| 6 | 「Test the questionnaire and revise it.」 | 自测 |
| 7 | 「Consider creating an "answer sheet."」 | 合格答案 + 配额 |

### 6.6.3 抓"产品特有"的，不抓"一般人口"

> **原文（p165）**：
> 「Focus on and pull out those characteristics that are **unique to your product and not just general categories of the population**. For example, experience using a cell phone and a camera may qualify as a requirement for a product that combines the two. But, **because the product will be used by all age groups, you need not screen for a particular age group** to include in your test sample. Later, as you are acquiring participants, you can simply make sure that you get a mix of different ages.」

> **★★★ 判据：只在"会改变行为"的维度上筛人；其余维度靠配额混搭**
> 年龄本身通常不构成门槛，但"是否用手机拍照"构成。**判据**：问自己"这个属性会让同一个人做出完全不同的操作吗？"答否 → 不做门槛，做配额。

### 6.6.4 问题的排列顺序

> **原文（p167）**：
> 「It makes sense to **place those questions that are most likely to disqualify a person first** on a questionnaire, while being mindful of basic telephone etiquette.」

> **原文（p167）**：
> 「if you are testing a graphic design product designed for seasoned end users with knowledge of color theory, you would not want to ask **20 very general questions** only to find out in question 21 that the person you are speaking with does not know saturation from hue.」

> **原文（p167）**：
> 「On the other hand, **that is not the type of high-level question you can ask first either. You need to work your way into it.**」

> **★★ 判据：淘汰性问题要早，但不能突兀——需要"过渡句"**
> 原文给的过渡法是先问一个可回答的具体事实，再由它推出能力判断。
> 例（p167）：不问"你会不会订酒店"，问「For your last three (or five; pick a number) trips, who made the arrangements?」

### 6.6.5 敏感信息用区间问

> **原文（p167）**：
> 「**Because people are often reluctant to divulge exact personal details, if you must gather personal information, such as age or salary, frame your questions in ranges.**」

原文示例（p167）：

> **原文（p167）**：
> 「instead of asking, "What is your annual household income?" ask instead:」
> 「"Into what category does your annual household income fall?"」

### 6.6.6 聚焦行为，不聚焦人口统计

> **原文（p169）**：
> 「Note also that **the questions focus on behaviors, not demographics.**」

> **★★★★ 判据：筛选问卷的主体应是行为题**
> 依据：§6.3.2 的 60 小时反例——**人口统计与自评都无法预测行为，只有已发生的行为能。**

### 6.6.7 自测筛问卷

> **原文（p169）**：
> 「**(Yes, you are right. This is a usability test of the screener!)** If it is a phone questionnaire, use the phone. You would be surprised, but it makes a difference. ... **Observe as a colleague tries it out** by answering the questions to see what types of answers you get.」

> **原文（p169）**：
> 「**Regardless of whom you use to help you acquire participants, control the process as much as possible** by being as specific as possible about your needs, anticipating miscommunications, and writing down the exact words you want the procurers to use. **It is your study, they are your results, and the whole affair is seriously compromised when the wrong people show up.**」

> **★★★ 判据：筛问卷本身要做可用性测试**
> 原文的自我指涉很到位。**做法**：让同事用真实渠道（电话就用电话）走一遍，看返回的答案是否可判定。

### 6.6.8 完整样例：小企业会计软件的筛选问卷（原文图 7-4，p168）

这份问卷可直接当模板改。原文的关键结构（**全部照录**）：

> **问题 1**：「How long have you been involved in your business (that is, how long since you founded, bought, or joined it)?」
> - 「Less than 3 months」→ **[Terminate]**
> - 「3–6 months」→ [Continue]
> - 「6–12 months」→ [Continue]
> - 「1–2 years」→ [Continue]
> - 「2 years or more」→ [Continue]

> **问题 2**：「Who in your company does the bookkeeping and accounting?」
> - 「Someone hired to do it/an employee」→ **[Terminate]**
> - 「My partner」→ **[Terminate]**
> - 「Me」→ [Continue]
> - 「I do some, someone else does the rest」→ [Continue]
> - 「My accountant/bookkeeper」→ [Continue]

> **问题 3**：「Do you use a PC with Windows or a Macintosh computer at work?」
> - 「Mac」→ **[Terminate]**
> - 「Windows」→ [Continue]
> - 「Don't use a computer at all」→ **[Terminate]**
> - 招募员注记：「[Recruiter: Must us a Windows-based PC at work.]」
> - 招募员注记：「[Recruiter: Recruit a mix.]」

> **问题 4**：「Which of the following do you currently use day-to-day as you do business? (Check all that apply.)」
> - 「Microsoft Word」「Corel WordPerfect or WordPerfect Office」「Microsoft Outlook/Outlook Express (email)」「Eudora (email)」「Microsoft Excel (spreadsheets)」「Quattro Pro (spreadsheets)」
> - 招募员注记：「[Recruiter: Participant must use at least two of the Microsoft products.]」

> **问题 5**：「Which of these activities do you complete for your business at least some of the time? (Check all that apply.)」
> - 「Track expenses」「Bill customers」「Track payments from customers」「Pay bills」「Track employee time」「Track accounts receivable」「Generate financial reports like Profit & Loss statements or Balance Sheets」「Check account balances」
> - 招募员注记：「[Recruiter: Accept only candidates who do at least three of the activities at least some of the time.]」

> **原文（p168）**：
> 「Note how the questions are intended to screen for a user who does **his or her own bookkeeping on a PC, and who has experience using other office-related software**.」

> **原文（p169）**：
> 「In administering a questionnaire like the sample one, **the caller should not offer the choices listed below the questions, but simply mark them** based on the respondent's answers.」

> **★★★★ 判据：筛选项的最优结构 = "问题 + 选项 + [Terminate]/[Continue] + 招募员注记"**
> 四个部件缺一不可：
> - 选项带 [Terminate]/[Continue]：让非专家也能判
> - 招募员注记：把"专家判断"外化为可执行规则（如"至少两个微软产品"）
> - 不给选项读出来：防止诱导（原文 p169）
> - 每题只问一件事

### 6.6.9 Barnum 的筛问卷（补充：可对照）

Barnum 书给了一份完整的筛问卷（数字有线电视机顶盒自安装研究，B p148–p150），结构与 Rubin 的一致，且多了**三类实用设计**：

| 设计 | 原文（B p148–p150） |
|---|---|
| 招募员开场白（含补偿与录制告知） | 「If you qualify for this study, we would like you to participate in a single one-hour session at our facility. You would be compensated $75.00 for your time.」 |
| 把"是否接受录像"做成终止项 | 「If selected, will you allow us to videotape you?  Yes (continue)  No (Terminate)」 |
| 用**情境题**筛意愿，而不是问"你想不想用" | 「It costs $41.95 for a professional installation ... If you do it yourself, the same package is only $9.95. However, if you are not able to perform the installation successfully ... you may be charged an additional $35.00 ... which would you choose?」其中「I would not choose to do it myself and would pay $41.95 for a professional installation.」→ **Terminate** |

> **★★★ 判据：用"带代价的选择题"筛真实意愿，比问"你会不会用"有效得多**
> Barnum 这道题的精妙处：把**失败风险**（可能被收 35 美元）写进情境，逼出真实偏好。
> 直接问"你愿意自己装吗"会得到社会赞许性答案。

> **原文（B p148）**：
> 「Recruiting Goal: 21 participants, plus backups」

> **原文（B p148）**：
> 「Special Notes for Recruiters:」
> - 「Equal gender distribution」
> - 「Some English-as-a-second-language speakers, preference for Spanish」
> - 「Representative age distribution (18 to 55 yrs)」
> - 「Representative education mix of no college / some college / college degree」

> **★★ 判据：筛问卷首页应写"招募目标 + 配额 + 招募员特别提示"**
> 这一段是**给招募员的施工图**，不是给被试的。放在最前面能防止"招来的人全一样"。

---

## 6.7 招募渠道与两个陷阱

### 6.7.1 渠道清单（原文 p131–p142）

| 渠道 | 原文要点 |
|---|---|
| Internal Participants | 内部人最快，但「best people」风险高（见 §6.7.2） |
| Qualified Friends and Family | 适合两端年龄 |
| Web Site Sign-Up | 需自我筛选 |
| Existing Customers from In-House Lists | 注意隐私与外泄 |
| Existing Customers through Sales Representatives | **高风险**（见下） |
| User Groups / Clubs / Churches | 热情高但存在热情偏差 |
| Societies and Associations | 可买名单，但有限制 |
| Referrals | 两端年龄最有效 |
| Craigslist | 量大，但「cheaters and repeaters」多 |
| College Campuses | 易招但同质，且「more willing to try new things」 |
| Market Research Firms | 「$125 to $300 and up per person」，且「recruit 12 for 10」 |
| Employment Agencies | 可找新到本国的外国人 |
| Newspaper Advertisements | 适合非技术人群，需长提前期 |

> **原文（p179）**：
> 「Typically, the firm will want to **over recruit by 20 percent** in order to ensure that you get the right number of people. ... (The lingo is "**recruit 12 for 10**.")」

### 6.7.2 陷阱一："只测到最好的人"

> **原文（p185）**：
> 「Very often when acquiring participants, and especially when you do not have primary control of participant selection, **you will be sent only the very "best" people** by your contact or recruiter. By "best," we mean ... **you are sent the cream of the crop, the high achievers.**」

> **原文（p185）**：
> 「The "best" end users typically possess the skills to **plow through even the most hard-to-use products** and perform admirably. Consequently, **the product "tests out" much better than it should, and provides a false sense of confidence** to the design and marketing team.」

三种高发场景（原文 p185）：
1. 「When you will be testing end users from within your own company」
2. 「When you are acquiring people directly from an established customer and **participation is seen as an enviable perk**」
3. 「When you are acquiring people from an established customer **through your own sales force**」

> **原文（p185）**：
> 「Your sales rep very often has strong relationships that he or she would like to further by using the testing as a perk. These relationships are often with **the best performers and most influential people** in your customer's organization. **You never see the average or poor performers.**」

> **原文（p185–p186，跨页）**：
> 「One or at」
> 「most **two of these people during a test is reasonable**, but if you see **three or four, it plays havoc with your test results.**」

> **原文（p174）**：
> 「one participant had obviously been primed by a sales rep. For his "test" of a new release of an existing product, he had **diligently studied the entire 300-page user guide** of the current product the night before. It seems that he took the notion of a usability "test" a mite too far.」

> **★★★★ 判据："明星被试"最多 1–2 个；3–4 个就毁掉结果**
> 原文给了可计数的红线。**识别特征**：能预判并绕过最麻烦的地方，「almost as if they knew they were there」；且会**淡化**自己遇到的问题。
> **落地**：登记每个被试的招募来源；同一来源连续出现"过于顺利"的人，立即换渠道。

### 6.7.3 陷阱二：漏掉"最不熟练用户"（LCU）

> **原文（p184）**：
> 「We have found that we learn an extraordinary amount by including **one or more least competent users (LCUs)** among participants, even if they do not make up a significant percentage of the eventual end users. **An LCU is defined as an end user who represents the least skilled person who could potentially use your product.**」

> **原文（p184）**：
> 「The LCU need not fall at the bottom of all the scales, but **the LCU should be at the bottom of the majority of them.**」

> **原文（p184）**：
> 「Why include LCUs even if the user profile is projected at mostly expert users? Simply this: **If your least expert group can successfully use the product, if they can muddle their way through the usability test, then you can assume that most other groups will also be able to use the product.**」

> **原文（p184）**：
> 「On the other hand, **if the LCUs cannot get through the test, that is not necessarily an indictment.** It does, however, **reveal clues on how to fix fundamental problems of intuitiveness, orientation, or organization**」

> **原文（p184–p185，跨页）**：
> 「during early product development and exploratory tests, **you learn much about the end user's mental models through the eyes of the LCU, before the LCU has been**」
> 「**"polluted" by previous experiences with similar products.**」

> **★★★★ 判据：每个测试样本里必须至少有 1 个 LCU**
> 理由有三层：① 上界验证（LCU 能过 → 大多数能过）② 下界诊断（LCU 卡住 → 暴露根本性的直觉/组织问题）③ **心智模型最干净**（未被同类产品"污染"）。
> **注意原文的克制**：LCU 失败**不是产品有罪的判决**，而是**修什么的线索**。

---

## 6.8 筛选访谈怎么做

### 6.8.1 用对话，不用照本宣科

> **原文（p181）**：
> 「We have found that **the quality of participants and the "show rate" is higher if you recruit in an apparently more casual and personable way, using a screener as a checklist during a more conversational interview.**」

四条理由（原文 p181）：
1. 「you build rapport with the candidate ... **They are more likely to show up for the session and be on time.**」
2. 「**it is less likely that the candidate will give an answer just because he or she thinks it is the correct one** to get into the study.」
3. 「you can ask follow-up questions that may expand or clarify something important to the」
4. 「you can make better **on-the-fly adjustments** to your selection criteria.」

> **原文（p182）** 的农场主案例：
> 「She wanted people from both rural and urban places (a classifier), but the study took place at harvest time. Many of the people in rural places would only be available **after sundown** ... or **if it rained**. If Dana had used only a scripted questionnaire, she might not have found out **why** people weren't available.」

> **★★★ 判据：脚本化的筛问卷会漏掉"为什么招不到"这一层信息**
> 对话式筛选能拿到**招募摩擦的原因**，从而现场调整标准（如改成晚上场、延后一周）。
> 代价：需记录偏差，且报告里要写明"标准被调整过"（原文 p186：「as long as you document them and account for any biases they may have introduced, it is fine to make them.」）

### 6.8.2 是否问完全部问题

> **原文（p182）**：
> 「There are **two schools of thought** about whether to go through a screening questionnaire completely with every respondent even if they don't meet all of the selection criteria. **One school recommends stopping the questioning as soon as someone hits a "reject" or "terminate" answer.** ... **The other school recommends going through the entire set of questions regardless** ... This approach has its plusses, mainly that **you have alternates available in case you do end up adjusting the selection criteria.** You can consider them "maybes" in case you run short of participants.」

> **★★ 判据：问完与早停的取舍取决于"标准会不会变"**
> 标准稳定 → 早停省时间；标准可能调整 → 问完留"备选池"。

### 6.8.3 打电话的五条规范（原文 p183–p184）

| # | 规范 | 原文 |
|---|---|---|
| 1 | 自报身份 | 「If the usability test is being run as an anonymous one ... the research firm or person calling should mention this fact」 |
| 2 | 说明来由与联系方式来源 | 「Michael Reel at the Franklin County Clerk's Office suggested I contact you about a research study I am working on.」 |
| 3 | **必须提前告知会被录像** | 「By all means, be sure to mention that the session requires the participant to be recorded, **because you want participants to raise any objections to being recorded now, and not when they arrive for testing.**」 |
| 4 | 说明问卷要花多久 | 「(If it is a really long questionnaire, fudge a little bit about how long it will take.」——原文此句在 p183 被页界切断，后半句「Many professionals simply say that it depends on the answers, which is true, we suppose.)」起于该页末 |
| 5 | 边问边标记 | 「There is nothing more embarrassing than **calling the same person and getting them out of the shower two days in a row.**」 |

> **★★★ 判据：录像同意要在电话里拿到，不能等到现场**
> 现场才提 = 被试已付出交通成本，难以拒绝 = 同意无效。**这既是伦理要求，也是数据质量要求。**

### 6.8.4 招募时间表（原文 p187 侧栏，可照抄）

> **原文（p187）**：
> 「**Give yourself a solid two weeks** to do recruiting and scheduling once the screening criteria are identified.」

| 周 | 原文步骤 |
|---|---|
| Week 1 | 「1. Identify participant characteristics and mix.」「2. Identify sources for participants.」「3. Write the screening questionnaire (screener)」「4. Test the screener.」 |
| Week 2–3 | 「5. Find participants.」（含：做招募贴/广告/邀请 → 发布 → 收响应 → 筛选排序）「6. Refine screener further, revise selection criteria if necessary.」「7. Select from responses.」「8. Send out more questions or ask follow-up questions if needed.」「9. Check the sample of respondents against mix matrix.」 |
| Week 3 | 「10. Select candidates, review the mix.」「11. Contact selected candidates with appointment dates and times.」「12. Confirm with participants, send session information including directions and forms.」 |

> **原文（p186）**：
> 「we recommend that you **collect their top three available dates and times as well but not make any immediate commitments**. This gives you greater flexibility in moving participants around on your personal scheduling Ouija board before finalizing the session schedule and mix of participants.」

> **原文（p186）**：
> 「If there are people in the pool whom you definitely want to be in the study, but they have limited or special times available, **schedule them first** and then schedule other people with more flexible schedules around them.」

> **原文（p187）**：
> 「Then **confirm, confirm, and confirm again.** The day before the participant is scheduled, do another reminder ... On the afternoon or evening before the participant's session, **phone him or her. Try very hard to get the person rather than leaving a message**」

> **★★★ 判据：招人要留 2 周；确认要做 3 次（确认信 → 前一天提醒 → 前夜电话）**
> 原文的"get the person rather than leaving a message"是可执行的差别：**留言与通话的到场率不同**。

---

## 6.9 报酬、隐私与伦理

> **原文（p189）**：
> 「this with the person is not a good idea, as it **plants a seed in the person's mind that he or she needs to be "positive,"** which may prevent the person from being critical.」

> **原文（p189）**：
> 「Some workplaces, unions, or professions **don't allow people to take incentives**, honoraria, or gifts. If someone wants to take part in your study but declines the incentive, **find another way to thank them** for their participation.」

> **原文（p189）**：
> 「**If you collect personal information about participants, you have a responsibility to protect that information and keep it private.** ... Don't include it in materials distributed to others, such as a schedule of sessions or the final report. **Do tell participants why you are collecting the personal information and what you are going to do with it. You should also tell them how long you are going to keep it.**」

> **原文（p189）**：
> 「**Don't use names to label recordings or files.** You will need to put names on session schedules ... However, **you should never use names — not even just first names — in reports. Refer to the participants by some other identifier, such as U1, U2, etc. ... or P1, P2, and so on**」

> **原文（p189）**：
> 「**Absolutely do not share video or audio recordings of participants for any reason other than the reasons that participants agreed to.** You should have participants sign recording permissions that spell out that you are using the recordings **only for data analysis and internal reports**. Once the sessions are complete, **store the recordings securely**, either on media that can be locked away or digitally protected with passwords.」

> **★★★★ 判据：报告里只用代号（P1/U1），且录像用途必须与同意书一致**
> 三条硬线：① 报告与日程表里不出现姓名 ② 录像不超范围使用 ③ 数据存储要加密或上锁。
> 第七条隐含要求：同意书里要写明"用于数据分析与内部报告"，**因此不能拿去做对外宣传片**。

> **原文（p186）**：
> 「What makes the situation even worse is when **the development team attending the test does not agree that these people are "ringers."** The team is more than happy to bask in the glow of receiving unexpected but excellent results.」

> **★★ 判据：明星被试的风险在"团队愿意相信"**
> 反驳失败 → 假阳性结论进入决策。**做法**：由主持人（而非团队）判定被试资格，并在报告的方法节记录来源与筛选偏差。

---

## 6.10 本章判据总表（共 24 条）

| # | 判据 | 出处 |
|---|---|---|
| 1 | 选错人不可补救，其他错误大多可补救 | p153 |
| 2 | 画像缺失本身是缺陷成因，测试只是照出来 | p154 |
| 3 | 画像第一稿写叙述句（看见人），不写条件表 | p154 |
| 4 | 区分三种人：付钱的、用的、读文档的 | p154–p155 |
| 5 | 画像六源，且要自己去访谈而非转述 | p155–p157 |
| 6 | "新手/专家"必须操作化定义，否则术语无意义 | p157 |
| 7 | 时长/频次会高估熟练度（60 小时/周仍可能不会用浏览器） | p157 |
| 8 | 用"任务 × 频次"矩阵打分，不用自评 | p158 |
| 9 | Requirements 是门槛（淘汰），Classifiers 是格子（配额） | p159 |
| 10 | 矩阵两轴用领域知识与工具知识，二者独立 | p163 |
| 11 | **4–5 人/单一人群格子 ≈ 80% 缺陷**（Rubin） | p110、p164 |
| 12 | **3–5 人为成本收益最优；Nielsen 口径 85%、Virzi/Lewis 80%**（Barnum） | B p38–p40 |
| 13 | Rubin 实践偏好"至少 8 人"；Barnum 实践"招 6 按 5 用" | p164 / B p213 |
| 14 | 真实验设计需 10–12 人/条件 | p110、p62 |
| 15 | 矩阵每格至少 4 人；填不满则向"最像主流用户"偏 | p164 |
| 16 | 多轮时可减每轮人数（3 轮 × 5 人 = 15 人） | p164 |
| 17 | 80% 是覆盖率，不是置信度；不等于"产品 80% 可用" | p110 / B p40 |
| 18 | 筛问卷的双重作用：选人 + 暴露画像不清 | p164–p165 |
| 19 | 只在"会改变行为"的维度设门槛，其余靠配额 | p165 |
| 20 | 淘汰性问题靠前，但需过渡句避免突兀 | p167 |
| 21 | 敏感信息用区间问 | p167 |
| 22 | 筛问卷聚焦行为，不聚焦人口统计 | p169 |
| 23 | 筛问卷自身要做可用性测试（用真实渠道） | p169 |
| 24 | **LCU（最不熟练用户）每个样本至少 1 人** | p184 |
| 25 | 明星被试（ringers）最多 1–2 个，3–4 个毁结果 | p186 |
| 26 | 用"带代价的选择题"筛真实意愿 | B p148–p149 |
| 27 | 优先用对话式筛选，能拿到招募摩擦的原因 | p181 |
| 28 | 录像同意必须在电话里拿到 | p183 |
| 29 | 招人留 2 周；确认做 3 次（信 → 提醒 → 前夜电话） | p187 |
| 30 | 报告只用代号；录像用途不得超同意书范围 | p189 |

---

## 6.11 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| 统计学的样本量公式 | 只给经验值（4–5/8/10–12），无公式推导 | 本章未展开；`user-research-methods` 有调查分层查表（非可用性测试口径） |
| "几个被试够"的**停止规则** | 两本书都不给停止判据，只给覆盖率 | 本章已并列两书口径；**该结论是空白，不要假装有** |
| 招募成本预算表 | 只给单个价格区间（$125–$300/人） | 本章未展开 |
| 筛问卷的信度/效度检验 | 只说"自测一遍"，无统计检验 | 本章未展开 |
| 残障/老年人/儿童的招募细则 | 本章只提"可联系残障组织"，细则在 ch11 | 见 ch11 §11.1 |
| 被试重复使用的记录机制 | 提到「cheaters and repeaters」与共享名单，无具体做法 | 本章未展开 |
| Barnum 书 p148–p150 的部分题目 | 已录可读的结构与关键题，少数选项在页边界被截 | 已录全部可读内容；未录处未猜测 |

---

## 6.12 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 样本量 4–5 人/格子 | 本书 ch04 §4.3.3 | 5 人时 1 个不适被试 = 20% 数据损失 |
| Requirements vs Classifiers | 本书 ch05 §5.3 | 分类器决定任务分层 |
| LCU | 本书 ch11 §11.1 特殊人群 | 残障/老年人常同时是 LCU |
| 筛选问卷 = 画像的测试 | 本书 ch05 §5.3.2 SCC | 同构判据："写不出来=没想清" |
| 方法论选择（何时用问卷而非测试） | `user-research-methods` 技能 | 问卷/焦点组的适用面，详见该技能 |
| 用户的"事"与场景 | `design-methodology-liuguanzong` 事理学 | 画像的叙述句实质是"事"的描述 |
| 无障碍人群招募 | `inclusive-accessibility-design` 技能 | 标准与人群细分，详见该技能 |
