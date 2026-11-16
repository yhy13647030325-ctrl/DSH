# 第 8 章：测后——发现汇总、严重度评级、报告、复测

> **Rubin & Chisnell PDF 页序 p285–p330（分析 p285–p306、报告 p307–p330，共 46 页）**
> ｜**本版逐页读完全部 46 页**
> **Barnum PDF 页序 p284–p290、p323（严重度与发现汇总）**｜**已读**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N；Rubin 书内印刷页 = PDF 索引 − 38）
>
> **读法说明**：按原书 `11.x`（分析）→ `12.x`（报告）顺序展开，不跳节。
> 每节含【原文摘录】+【判据提炼】。
> **引文来源标注**：`（pN）` = Rubin & Chisnell；`（B pN）` = Barnum。
> 引文说明：合字 `fi`/`fl` 已还原，弯引号已还原为直引号；**用词与数字未改**。

---

## 8.1 总纲：测后要做四次转换

| 转换 | 从 → 到 | 对应小节 |
|---|---|---|
| 第一次 | 原始记录 → **可看模式的汇总** | §8.2 |
| 第二次 | 汇总 → **发现（findings）** | §8.3 |
| 第三次 | 发现 → **严重度/优先级** | §8.4–§8.5 |
| 第四次 | 排序后的发现 → **报告与建议** | §8.6–§8.7 |

> **原文（p285）**：
> 「**in all honesty it never goes as smoothly and as linearly as described here. It tends to be circular and iterative**, as some answers lead to more questions.」

> **★★ 判据：四步是"检查顺序"，不是"执行顺序"**
> 真实过程会反复回跳。**但每一步的产出物必须都能独立交付**，否则无法在中途叫停（项目常见）。

---

## 8.2 发现汇总：边测边汇

> **原文（p285）**：
> 「Begin Compiling Data as You Test」（节标题）
> 「The process of compiling involves placing all the data collected into a form that allows you to see patterns. **The compilation of data, whether you are creating a preliminary report or not, should go on throughout the test sessions.**」

> **原文（p285）**：
> 「This ongoing compilation of data takes advantage of the fact that **the test is still fresh in your mind so that you can remember odd quirks and events that happened during the day. Even with the best note taking ... some events simply are not captured, except in your memory, and they will fade unless you record them.**」

> **★★★★ 判据：当天不汇，细节就永久丢失——记录手段再好也救不回来**
> 原文点明：**记忆是唯一载体的事件**（怪异的操作、临时故障、被试的一句抱怨）无法从录像中还原其"当时的意味"。
> **落地**：每天收工前 30 分钟做"当日汇总"，写入运行中的汇总表。

### 8.2.1 汇总的三类统计（任务准确度）

> **原文（p288）**：
> 「Following are three types of statistics that relate to task accuracy:」
> - 「**Percentage of participants performing successfully, including those who required assistance.** ... If this number is very low, say **50 percent**, it indicates very serious problems with the product because participants could not perform successfully even with assistance and extra time.」
> - 「**Percentage of participants performing successfully.** ... indicates the percentage of participants who were at least able to muddle through the task well enough to complete it successfully.」
> - 「**Percentage of participants performing successfully within a time benchmark.** ... If **7 of 10** participants achieved success within the allotted time, then the task accuracy would be **70 percent**.」

> **★★★★ 判据：任务成功率必须报三个版本，不能只报一个**
> 三个口径的用途不同：
> | 口径 | 用途 | 危险 |
> |---|---|---|
> | 含协助的成功率 | 产品有没有"最底线可用性" | 会美化结果 |
> | 纯成功（可磕碰） | 实际可用程度 | 常用但掩盖效率问题 |
> | 基准内成功 | 效率 + 效果 | 最严，最接近验收 |
> **只报第二个 = 默认隐藏"靠帮忙才过"与"过了但超时"两类问题。**

> **原文（p296）**：
> 「One note of caution about using percentages with small sample sizes: If you only have 8 or 10 participants in your study, **talking in terms of percentages can sometimes seem to inflate an effect**. For example, an **83 percent** success rate sounds like a big deal. But saying that **10 of 12** participants completed tasks on prototype A grounds the finding in reality.」

> **★★★ 判据：小样本要同时报分数与百分比（"10 of 12"而非"83%"）**
> 原文给的写法直接可用：**先写分数，再括注百分比**。理由：百分比在小样本下会放大观感。

### 8.2.2 计时统计

> **原文（p289）**：
> 「**Mean time to complete.** For each task, calculate the average time required by all participants to complete it」

> **原文（p289）**：
> 「If it turns out that task times are **very skewed** either left or right — that is, the highest or lowest times are very different from the other times — **consider using the median score, instead of the mean**, as a comparison tool.」

> **★★ 判据：有小样本+离群值时用中位数，不用均值**
> 5 人样本里 1 人卡 20 分钟，均值就废了。**中位数是默认更稳的选择。**

### 8.2.3 汇总的最小工具：一张电子表格

> **原文（p286）**：
> 「One of our favorite tools is also one of the simplest and most available: **a spreadsheet program**. ... A spreadsheet program helps you generate counts, averages, medians, means, and percentages. ... However, it will also help you **sort and filter data**, which can lead you to recognizing important patterns that you may not be able to represent statistically.」

> **原文（p286）**：
> 「Even **laying text out in a spreadsheet** — such as answers to interview questions — can help you see true duplication as well as near matches that reveal useful insights.」

原文案例（p286，Dana 的问法可直接借用）：

> **原文（p286）**：
> 「in one study Dana asked participants "**When you tried to use the site before but couldn't find what you were looking for, what did you do then?**" In reviewing a dozen responses, she could see that the ultimate answer wasn't "go to the site map," as the team had hoped it would be, but instead was "**ask someone else**"」

> **★★★★ 判据：定性数据也能进表格——用"查找替换 + 变色"做主题计数**
> 原文做法：把转录文本放进一格一行 → 用 Find 找关键词 → 替换成彩色 → 软件报"改了多少处" → 得到主题频次。
> **这个方法的优点**：不需要任何质性分析软件，且**可复核**（别人能重跑）。

### 8.2.4 Barnum 的发现会（findings meeting）

> **原文（B p269）**：
> 「The log describes actions and comments from the participant but does not include codes or markers. Using the log, the team quickly reads down the column containing the actions' descriptions, looking for findings and calling them out **by the timestamp** so that everyone can see what finding is being identified. **Someone on the team writes a brief description of the finding on a sticky note and posts it to the whiteboard.**」

> **原文（B p269）**：
> 「The number on the sticky notes **refers to the participant**, making it easy to tie the finding back to a specific log.」

> **原文（B p269）**：
> 「Facilitate the process effectively. Participants go through different stages during the affinity process. These roughly include:」
> - 「Being **overwhelmed**, not sure where or how to begin.」
> - 「Getting into the groove and doing the gross categorization.」
> - 「Getting **frustrated** with the details of categorization, not sure where the process is leading.」
> - 「Seeing the magic of data transformed into information.」

> **★★★★ 判据：亲和图式的"发现会"是团队共识的载体，不是分析方法**
> 三个可操作要点：① 便签写"一句话发现" ② 便签带**被试编号** ③ 按时间戳回指原始日志。
> 原文的情绪曲线（overwhelmed → groove → frustrated → magic）是**主持这个会的人必须预期的四阶段**，不是抱怨。

---

## 8.3 什么算一条"发现"

> **原文（p307）**：
> 「The results of a usability test are not merely tables of data and lists of issues. ... **Results document the data you collected and analyzed. Findings are inferences you and your team draw from the observations you have made** along with analyzing the data.」

> **原文（p308）**：
> 「**Findings are often expressed in headline fashion or one-sentence statements that encapsulate the essence of the usability issue.** They are the centerpiece of the report. For example, "**The 'Go' label did not suggest 'refresh' or 'reload' to participants.**"」

> **★★★★ 判据：发现是"推断"，不是"事实罗列"**
> 分界线：
> - **结果（results）**：可数的东西（4/6 人点了 Back 按钮）
> - **发现（findings）**：一句可被反驳的判断（Back 按钮的标签没有表达"返回上一页"（此例为本文自拟的示意，非原文））
> **判据**：一条发现若不能被别人提出反例，它就还只是结果。

**四步成形（原文 p308）**：

| 步 | 原文 |
|---|---|
| 1 | 「Write out the findings.」 |
| 2 | 「Expand the discussion of each of the findings with **narrative, participant quotes, and illustrations**」 |
| 3 | 「Go back to the beginning of the results section ... to write a section describing **global findings and overall conclusions**」 |
| 4 | 「**Sort through the findings and group them** in some way that makes sense」 |

**四种分组方式（原文 p308）**：按「Task」「Research question」「Product section」「How the team is organized」

> **原文（p308）**：
> 「Dana often uses the **research questions as the top level of headings**. This accomplishes a few important things.」
> - 「Ensure that you have **answered the original questions**」
> - 「Tie the data gathered to the final findings and recommendations.」
> - 「Educate the team by connecting the plan and design to the outcomes.」

> **★★★ 判据：用"研究问题"当一级标题，比按界面模块分组更有效**
> 理由：它同时完成了"是否回答了原问题"的自检。**按模块分组会漏掉"某个研究问题没答上"这件事。**

**组内排序依据（原文 p309）**：
「Local versus global」「Impact on users」「Frequency」「Ability to work around or not」「Where in the product the problem occurred」「Task」「Visibility」「Cost to fix」「Level of embarrassment to the user」

> **★★ 判据：报告里至少要按"影响"和"频次"两个轴各排一次**
> 单一排序会误导：按频次排会把"罕见但致命"压到末尾。

---

## 8.4 严重度评级：Rubin 的口径

### 8.4.1 四点评分（Severity）

> **原文（p300）**：
> 「First, categorize a problem by severity. **We measure severity on a four-point scale**, with each problem ranked.」

> **原文（p300）**（图 11-9 全文文字化）：

| Severity ranking | Severity description | Severity definition |
|---|---|---|
| **4** | **Unusable** | 「The user either is not able to or will not want to use a particular part of the product because of the way that the product has been designed and implemented.」<br>例：「Product crashes unexpectedly whenever it is powered on at altitude.」 |
| **3** | **Severe** | 「The user will probably use or attempt to use the product, but will be severely limited in his or her ability to do so. The user will have great difficulty in working around the problem.」<br>例：「Synchronizing the device to another device can only happen when certain files are not in use. It isn't obvious when the files are in use.」 |
| **2** | **Moderate** | 「The user will be able to use the product in most cases, but will have to take some moderate effort in getting around the problem.」<br>例：「The user can make sure that all complementary applications are closed while syncing the two devices.」 |
| **1** | **Irritant** | 「The problem occurs only intermittently, can be circumvented easily, or is dependent on a standard that is outside the product's boundaries. Could also be a cosmetic problem.」<br>例：「The message area of the device's small screen is at the very top, dark blue, and often shaded by the frame of the screen.」 |

> **原文（p300）**（图 11-10，另一套四点口径）：
> 「**4 = Task failure**-prevents this user going further」
> 「**3 = Serious problem**-may hinder this user」
> 「**2 = Minor hindrance**-possible issue, but probably will not hinder this user」
> 「**1 = No problem**-satisfies the benchmark」

> **★★★★ 判据：严重度是四点量表，且"4"的定义核心是"用户不愿用或不能用"，不是"功能坏了"**
> 注意 4 分里含「**will not want to use**」——**意愿**也算不可用。这是最易被忽略的口径。
> 图 11-9 与图 11-10 是**两套并存的口径**：前者按"能不能绕过"分级，后者按"是否阻断该用户"分级。原文并列给出，未指定唯一权威。

### 8.4.2 频率评分（Frequency）

> **原文（p301）**（图 11-11 全文）：

| Frequency ranking | Estimated frequency of occurrence |
|---|---|
| **4** | 「Will occur **≥90%** of the time the product is used」 |
| **3** | 「Will occur **51–89%** of the time」 |
| **2** | 「Will occur **11–50%** of the time」 |
| **1** | 「Will occur **≤10%** of the time」 |

> **原文（p301）**：
> 「To arrive at your estimated frequency of occurrence, you need to account for two factors:」
> - 「The **percentage of total users affected**」
> - 「The **probability that a user from that affected group will experience the problem.**」

> **原文（p301）**：
> 「Therefore, if you feel that **10 percent of the target population** will encounter this problem about **50 percent of the time**, then there is only a **5 percent** estimated frequency of occurrence (**0.10 × 0.5 = 0.05 = 5%**).」

> **★★★★ 判据：频率 = 受影响人群比例 × 该人群遇到的概率**
> 原文给的算式可直接套：**0.10 × 0.5 = 5%**。
> 这条把"只有专家会遇到"和"所有人都偶尔遇到"区分开了——后者往往更该先修。

### 8.4.3 关键度 = 严重度 + 频率

> **原文（p299）**：
> 「**Criticality is defined as the combination of the severity of a problem and the probability that the problem will occur.** If you represented criticality as an equation, it would look like this:」
> 「**Criticality = Severity + Probability of Occurrence**」

> **原文（p301）**：
> 「Ascertaining a problem's criticality is then a simple matter of **adding the severity ranking and the frequency ranking** for that problem. For example, if a particular problem is ranked unusable (**severity ranking = 4**), but will only occur **5 percent** of the time (**frequency ranking = 1**), then that problem would receive a **priority of 5 (4 + 1)**. Similarly, if there were a problem that was simply an irritation but affected almost everybody, then that would also get a **5**.」

> **原文（p301）**：
> 「Using this method, the **very highest priority are assigned to problems that made the product unusable for everyone.**」

> **★★★★ 判据：优先级 = 严重度(1–4) + 频率(1–4)，**唯一最高分是 8**
> 8 分的唯一组合是 **4（Unusable）+ 4（≥90%）**——即"所有人都用不了"。
> 原文举的对称案例极有说服力：**"对所有人致命" 与 "对所有人小烦" 同得 5 分**。这意味着**关键度不是"越严重越优先"，而是"总体损害"**。
> **这会挑战很多团队的本能排序**（他们通常把所有 4 分排在最前，哪怕只影响 5% 的人）。

> **原文（p301）**：
> 「**Don't get nervous if this is hard — this is only an estimate.**」

> **原文（p301）**：
> 「Keep in mind that you can **develop your own hierarchy and definitions for criticality based on your organization's objectives** and the particular product you are testing.」

> **★★★ 判据：关键度的阈值必须由组织自定，但"算法结构"应保留**
> 原文明确允许自定义。**可自定义的是分档与权重，不该自定义的是"两个维度分别评再合成"这一结构**——单维打分最容易把"罕见致命"和"常见小烦"混为一谈。

### 8.4.4 简易替代法

> **原文（p301）**：
> 「For simple tests, there is an easier way to ascertain which problems are most critical and in most need of attention. That is to simply **ask participants during the debriefing session to tell you what was the most problematic situation for them.** If you find that **several participants are in agreement about priorities**, then that is an important indication about where to focus your resources.」

> **★★ 判据：3 人以下的小测试，可直接问被试"哪里最难"**
> 前提：**多人一致**才采信。单人偏好不进优先级。

---

## 8.5 严重度评级：Barnum 的口径（与 Rubin 并列）

### 8.5.1 先分"全局/局部"

> **原文（B p284）**：
> 「You now need to categorize them by **scope and impact**. That means」
> - 「determining whether a finding is **global or local**」
> - 「determining the **severity** of the finding」

> **原文（B p285）**：
> 「A finding that reflects an issue of this scope is called a **global finding**. A finding uncovered in one place may point to the need to fix it not only where you saw it but also throughout the product. Thus, **a global finding is usually a significant finding.**」

典型全局发现的三种（原文 B p285）：
- 「**Information architecture/navigation** — participants can't find what they're looking for because things aren't clearly seen or they are in the wrong place.」
- 「**Consistency** — items are called one thing in one place but something else in another place (terminology)」
- 「**Feedback** — participants complain about not knowing what to do or not understanding what happens when they perform an action」

> **原文（B p286）**：
> 「A **local finding** is one that occurs in only one place — that is, on a single screen or page of a website, in a particular step in instructions, or in a particular feature of a product.」

> **★★★★ 判据：先判全局/局部，再判严重度——顺序不能反**
> 理由（原文）：全局发现的"修复面积"远大于局部。**一个 2 分的全局问题，总修复成本可能高于 4 分的局部问题。**
> **三个高发全局类型**：信息架构/导航、一致性/术语、反馈。这三类几乎每次测试都会出现，可作为"必查项"。

### 8.5.2 三点评分表（Barnum，附完整定义）

> **原文（B p286）**：
> 「**Severity rating scales vary, but they all have an extreme condition on each end of the scale** with varying degrees of effect on user experience in between.」

> **原文（B p287）**：
> 「A simple **3-point severity rating scale** might look like this:」
> 「1. **Catastrophe** — user cannot complete task; or user can complete the process but expresses **extreme irritation** at the process; or user **needs assistance** (business goal is to make the process independent of user assistance).」
> 「2. **Serious problem** — user is frustrated but gets through it; suggests that others may be less inclined to put up with the inconvenience or that **frustration level will be high**.」
> 「3. **Cosmetic problem** — user may hesitate or pick the wrong option, but **user corrects it without incident**; or user expresses minor irritation or annoyance, but it doesn't affect ability to complete tasks.」

> **原文（B p287）**：
> 「A more finely tuned rating scale might have **four rating categories**, like this:」
> 「1. catastrophe」「2. major problem」「3. minor problem」「4. cosmetic problem」

> **原文（B p287）**：
> 「A very basic rating scale uses the following categories:」
> - 「high」「medium」「low」

> **原文（B p287）**：
> 「Of course, you also want a category for **positive findings**, since you don't want to ignore these. And, depending on the type of study you are doing, you might want to add other categories, such as "**bug**" and "**comment**"」

> **★★★★ 判据：Barnum 的 1 分（Catastrophe）含三种情形——完不成 / 完成但极度恼火 / 需要协助**
> 第三种最容易被漏掉：**「needs assistance」在业务目标是"自助完成"时，等同灾难**。
> 这与 Rubin 的 4 分（Unusable）口径在"需要协助"上**高度一致**，可交叉互证。

### 8.5.3 评级三维度

> **原文（B p286）**：
> 「The discussion surrounding the assignment of severity ratings to the findings is **strengthened when it is a team effort, since consensus is needed** on how to determine what a rating means. For instance, **you can rate findings by**:」
> - 「**Frequency of occurrence** — measured by how often you saw it or how often it is likely to occur.」
> - 「**Impact of the problem on user experience** — measured in terms of success or failure, as well as ease or difficulty of the process for users; ability to recover from error; and so forth.」
> - 「**Persistence of the problem** — measured by observing whether **users who experience a problem can learn to avoid or overcome the problem going forward.**」

> **★★★★ 判据：Barnum 比 Rubin 多一维——「持久性」**
> Rubin = 严重度 × 频率（两维）；Barnum = 频率 / 影响 / **持久性**（三维）。
> **持久性的含义**：被试第二次再遇到时还会不会栽。**"第一次栽、第二次就会了"与"每次都栽"严重度不同**——这一维在 Rubin 体系里没有独立位置。
> **本技能裁决**：两维作主线（Rubin，可算出优先级分），**持久性作为调整项**：持久性高 → 严重度上调一档。

### 8.5.4 Barnum 的四级实操口径

> **原文（B p323）**：
> 「The following **four levels of severity** we used to rate the findings:」
> - 「**Level 1** — **Prevented completion of a task**」
> - 「**Level 2** — **Frustrated participant and caused significant delay on a task**」
> - 「**Level 3** — **Had a minor effect on usability**」
> - 「**Level 4** — **Caused no significant impact on performance, but participant indicated a preference or a suggestion for future changes**」

> 同页表格（B p323）示例，含三列：`Usability problem` / `Number affected` / `Severity`，例如：
> "Confusion over how to find Course Reserves｜7｜1"（原文表格行，非连续句子）
> "User Support: Wanted explicit on-screen descriptions｜7｜2"（原文表格行）
> "Tutorial: Went too fast; couldn't stop it or change the pace｜6｜2"（原文表格行）

> **★★★★ 判据：Barnum 的 4 级口径自带"受影响人数"列——严重度必须与人次同框呈现**
> 这是本节最实用的一点：**只给级别不给人数，读者无法判断该不该修**。
> 注意 Barnum 的 4 级 = "无影响但有偏好/建议"，与 Rubin 的 1 级（Irritant）= "偶发/易绕过/装饰性"**不是一一对应**（见 §8.5.5）。

### 8.5.5 两本书严重度口径的对照与差异（并列，不合并）

| 项 | Rubin & Chisnell | Barnum |
|---|---|---|
| **量表点数** | **4 点**（4 Unusable / 3 Severe / 2 Moderate / 1 Irritant） | **3 点**（Catastrophe/Serious/Cosmetic）或 **4 点**（catastrophe/major/minor/cosmetic）或 3 档（high/medium/low） |
| **方向** | 4 = 最严重，1 = 最轻 | 1 = 最严重，4 = 最轻（**方向相反！**） |
| **"最重"的定义** | 「not able to **or will not want to** use」 | 「cannot complete task」；或「expresses **extreme irritation**」；或「**needs assistance**」（同一级别定义内的三个并列要件，本文分引） |
| **是否含"需要协助"** | 未单列（分散在 3 分「severely limited」） | **显式列入 1 分（最重）** |
| **是否含"意愿"** | **显式**（will not want to use） | 未显式 |
| **合成优先级的方法** | **Severity + Frequency（各 1–4）→ 2–8 分** | 无固定算式；三维度（频率/影响/持久性）用于讨论 |
| **范围维度** | 无独立"全局/局部"维度 | **有**（global / local 先分） |
| **呈现要求** | 图 11-1 汇总表含任务、成功率、均值、标准差 | 表格必含 **Number affected** |

> **★★★★ 判据：两本书的严重度量表方向相反，交叉引用时必须先声明方向**
> Rubin：**4 最重**；Barnum：**1 最重**。
> **这是本技能最容易出错的一处。** 若报告里写"严重度 4"，在 Rubin 口径下是"灾难"，在 Barnum 口径下是"仅偏好/建议"——**含义完全颠倒**。
> **本技能的统一约定**：报告正文一律写**文字级别**（"不可用/严重/中等/轻微"）并括注所用书与原始分值，例：`严重（Rubin 4 分 / Barnum Level 2）`。

> **★★★ 判据：两书都要求"评级是团队共识"，不是主持人独断**
> Rubin：「Criticality ... you can develop your own hierarchy ... based on your organization's objectives」（p301）
> Barnum：「strengthened when it is a team effort, since consensus is needed」（B p286）
> **落地**：评级会必须有开发/设计在场，且**评级标准的释义要先达成一致**（否则同一分在不同人心里不同）。

---

## 8.6 报告：结构与篇幅

> **原文（p311）**：
> 「There should be a **threefold logic** to the report. That is, the report should have a **beginning, a middle, and an end**. The beginning is composed of **why you did the test, and how you prepared**. The middle is composed of **what happened during the test**. The end is composed of **the implications of what happened**, that is, what you recommend doing about what happened.」

> **原文（p311）**：
> 「**General consensus among usability practitioners is to keep a formal written report in the range of 20 to 25 pages.**」

> **原文（p311）**：
> 「If you are very interested in standards and are working on a validation, comparative, or summative test, you may want to consult and use the **Common Industry Format (CIF) report format that is part of the ISO Standard 25062**.」

### 8.6.1 标准结构（原文 p312–p315）

| 节 | 原文要求 |
|---|---|
| **Executive Summary** | 「a brief synopsis of the test logistics, the major findings and recommendations, and further research required, and the overall benefits of the test. **Keep it to one page if you can**」 |
| **Method** | 「describe the nature of the research, how it was set up, participant characteristics, and the data collection methods used.」……「**If your test plan is comprehensive, simply paste it in as is** (updating the verb tenses, of course), with **one exception: Update it with exceptions to the original plan**」 |
| **Results** | 数据汇总（表 + 图），原文建议**不放原始数据**，只注明存放位置与保管人 |
| **Findings and Recommendations (Discussion)** | 见 §8.6.2 |

> **原文（p312）**：
> 「Dana sometimes simply creates a **table of the research questions on the left with one- or two-sentence answers on the right**」

> **★★★★ 判据：执行摘要=一页，且"研究问题→答案"两列表是最有效的形式**
> 理由：它同时满足"回答原问题"与"让不读全文的人拿到结论"。

> **原文（p313）**：
> 「we have found it useful to **leave out the raw data**, and we suggest that you do the same. Simply mention in the report the name of the person who holds the raw data or the location where it is stored」

> **★★ 判据：报告不放原始数据，但要写清谁保管、存在哪**
> 这样既减篇幅，又保住可追溯性。

### 8.6.2 发现的呈现格式

> **原文（p313）**：
> 「The design of this section should **enable someone to quickly pick out and grasp the findings and recommendations without having to read the supporting text**. Especially design this section **for usability**, by having **the findings in boldface or separated by space from the discussion**.」

> **★★★★ 判据：报告本身必须通过可用性测试的逻辑——"加粗发现、正文讨论"**
> 原文的自我要求：「Think a moment about **the incongruousness of receiving a report on a usability test that itself is hard to use.**」（p312）

> **原文（p314）**：
> 「You may find that you want to divide this section into **general findings and recommendations** followed by **specific findings and recommendations**.」

> **★★ 判据：报告用两段式——先全局（可成段），再具体（逐条）**
> 与 §8.5.1 的 global/local 对应。

### 8.6.3 必须有正面发现

> **原文（p315）**：
> 「**Be sure to include positive findings.** The nature of usability testing is to reveal problems so as to inform design, it's true. But **seasoned usability specialists try to include at least some positive findings.** Doing so **makes the "negative" findings more palatable for the team** by softening the blow and rewards them for putting in their best efforts going into the study.」

> **★★★★ 判据：报告里必须有正面发现，这不是客套而是策略**
> 原文给的理由是"让负面发现更容易被接受"。**没有正面发现的报告会触发防御，导致建议不被采纳。**

### 8.6.4 建议怎么写

> **原文（p315）**：
> 「While you can report findings and conclusions on your own, **making recommendations should not be a solo effort.**」

> **原文（p315）**：
> 「**However, we caution that this process is not a democratic one.** It is important that those who observed only a session or two **do not have a major say in recommendations.** ... **The test moderator who attended each session clearly has the broadest perspective, all of the data at hand, and the final say.**」

> **★★★ 判据：建议要集体讨论，但拍板权归主持人**
> 两个反方向的错误：① 主持人独断（建议缺乏认同，没人执行）② 全体投票（只看过一场的人权重过大）。

五条建议准则（原文 p315–p319）：

| # | 准则（原文标题） | 原文要点 |
|---|---|---|
| 1 | 「Focus on Solutions That Will Have the **Widest Impact**」 | 「**global changes affect everything and need to be considered first**」 |
| 2 | 「**Ignore Political Considerations** for the First Draft」 | 「if you concern yourself with politics prematurely, **you lose your objectivity**」 |
| 3 | 「Provide Both **Short-Term and Long-Term** Recommendations」 | 见下 |
| 4 | 「Indicate Areas Where **Further Research Is Required**」 | 「**Usability testing ... often results in new questions** ... This should not be considered a defeat.」 |
| 5 | 「**Be Thorough**」／「Make Supporting Material Available to Reviewers」 | 见原文 p319 |

> **原文（p318）**：
> 「**Short-term recommendations** are the types of changes that can be made **without slipping the schedule**.」
> 「**Long-term recommendations** are the types of changes that are **really required for long-term success.** It is important that the organization be aware that **stop-gap changes are just that**」

> **原文（p318）**：
> 「As one famous design firm practices, "**reality bats last**."」

> **★★★★ 判据：初稿不管政治，定稿再谈可行——顺序不能倒**
> 原文理由：过早考虑政治会「lose your objectivity, limit your recommendations」。
> **落地**：初稿写"应该做什么"；评审会再讨论"能做什么"。**两个清单都保留在报告里**（短期/长期）。

> **原文（p319）**：
> 「Consider a program in which you are **conducting some kind of usability test every two to six weeks**.」

> **★★★ 判据：复测节奏 2–6 周**
> 这是全书唯一给出的持续测试频率数字，直接可用于排期。

---

## 8.7 复测与迭代

> **原文（p66）**：
> 「Usability testing is most powerful and most effective when implemented as part of an **iterative** product development process.」

> **原文（p66）**：
> 「Even if important product flaws or deficiencies are missed during one test, **another testing cycle offers the opportunity to identify these problems**」

> **原文（p321–p322）**：
> 「Your findings and recommendations probably will introduce new elements that should be tested to ensure that **the remedies really do correct the issues and not just create new ones.**」

> **原文（p73）**：
> 「in the case of a verification test, to **confirm that problems discovered earlier have been remedied and that new ones have not been introduced**.」

> **★★★★ 判据：复测要验三件事，不是一件**
> ① 老问题修好了吗 ② **有没有引入新问题** ③ 修复本身有效吗（而不只是"变了"）
> 第二项最常被漏掉，而它恰恰是迭代设计的常见副作用。

> **原文（p120）**：
> 「if you are conducting iterative, ongoing testing, you will be **revising the benchmarks from test to test** as you learn more about realistic time frames for task completion.」

> **★★ 判据：复测时基准也要更新，否则前后轮不可比**
> 但**更新要留痕**：报告里写明"本轮调整了哪几个任务的基准，为什么"。

---

## 8.8 本章判据总表（共 26 条）

| # | 判据 | 出处 |
|---|---|---|
| 1 | 分析与报告是循环迭代的，但四步产出物都要能独立交付 | p285 |
| 2 | 当天汇总，否则只存在于记忆里的细节永久丢失 | p285 |
| 3 | 任务成功率必须报三个口径（含协助/纯成功/基准内） | p288 |
| 4 | 小样本同时报分数与百分比（"10 of 12"优于"83%"） | p296 |
| 5 | 有离群值时用中位数不用均值 | p289 |
| 6 | 定性数据也能进表格做主题计数（查找替换+变色，可复核） | p286 |
| 7 | 发现会三要素：一句话发现 / 带被试编号 / 回指时间戳 | B p269 |
| 8 | 发现会情绪四阶段（overwhelmed→groove→frustrated→magic）需预期 | B p269 |
| 9 | 发现是"推断"，结果才是"事实"；不可反驳的还不是发现 | p307–p308 |
| 10 | 用"研究问题"当一级标题，可自检是否答全 | p308 |
| 11 | 组内至少按"影响"和"频次"各排一次 | p309 |
| 12 | Rubin 严重度 4 点：4 Unusable／3 Severe／2 Moderate／1 Irritant | p300 |
| 13 | **4 分含"不愿用"（will not want to use），不只是"不能用"** | p300 |
| 14 | Rubin 频率 4 档：≥90%／51–89%／11–50%／≤10% | p301 |
| 15 | 频率 = 受影响人群比例 × 该人群遇到概率（0.10×0.5=5%） | p301 |
| 16 | **优先级 = 严重度 + 频率，最高 8 分（4+4）** | p299、p301 |
| 17 | "对所有人致命"与"对所有人小烦"同得 5 分——关键度看总损害 | p301 |
| 18 | 关键度分档可由组织自定，但两维结构应保留 | p301 |
| 19 | 3 人以下小测试可直接问被试"哪里最难"，需多人一致 | p301 |
| 20 | Barnum 先判全局/局部，再判严重度 | B p284–p286 |
| 21 | 三个高发全局类型：信息架构/导航、一致性/术语、反馈 | B p285 |
| 22 | Barnum 1 分含"需要协助"，与 Rubin 4 分可交叉互证 | B p287 |
| 23 | Barnum 三维度多出"持久性"（能学会就不再犯） | B p286 |
| 24 | **两书严重度方向相反（Rubin 4 最重 / Barnum 1 最重），引用须标方向** | p300 / B p323 |
| 25 | 严重度表必须与"受影响人数"同框（Barnum 表结构） | B p323 |
| 26 | 复测验三件事：老问题修好／无新问题／修复有效 | p73、p321–p322 |

---

## 8.9 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| 严重度的**唯一权威量表** | 两书各给多套（Rubin 两套四点、Barnum 三/四点+三档），互不统一 | 本章已并列；**不存在单一权威，须在报告里声明所用口径** |
| SUS / 标准量表的口径 | 本章两书均未展开 SUS 计分 | 本章未展开；`user-research-methods` 有问卷与量表章节 |
| 报告模板文件 | 只给节标题与示例片段 | 可按 §8.6.1 五节自建 |
| 统计检验的具体选择 | 只提「inferential statistics」存在（p265 节标题） | 本章未展开 |
| 建议的"可行性评分" | 只说"定稿再谈政治" | 本章未展开 |
| 星级/highlights 视频制作 | p283–p288 有步骤，本章未逐条录入 | 未逐条展开；如需制作，见原书该节 |
| Barnum 严重度的行业对比数据 | 未给 | 本章未展开 |

---

## 8.10 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 三个成功率口径 | 本书 ch03 基准 70/95/100 | 基准决定"哪个口径算通过" |
| 关键度 = 严重度+频率 | 本书 ch05 任务优先级 | 任务侧的"关键性/易损性"是事前版，本章是事后版 |
| 提示档位 | 本书 ch07 逐级提示四档 | "需要到第几档"可作为严重度上调依据 |
| 全局/局部发现 | 本书 ch01 五原因之四（分件测试谬误） | 全局发现正是"跨组件"问题 |
| 复测 | 本书 ch05 试点 | 试点测"测试本身"，复测测"修复效果" |
| 正面发现 | 本书 ch07 balanced praise | 同一原理：不给正面反馈会引发防御 |
| 发现汇总与亲和图 | `user-research-methods` 技能 | KJ 法/亲和图的完整做法，详见该技能 |
| 严重度与失误分类 | `design-psychology-norman` 失误六类 | 失误类型可作严重度的机理依据（哪类失误更难被发现） |
