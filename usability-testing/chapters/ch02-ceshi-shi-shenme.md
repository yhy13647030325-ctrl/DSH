# 第 2 章：可用性测试是什么，以及它的边界

> **原书 PDF 页序 p59–p64（6 页）**｜**本版逐页读完全部 6 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N；书内印刷页 = PDF 索引 − 38）
>
> **读法说明**：按原书 `2.x` 小节逐节展开，不跳节。
> 每节含【原文摘录】+【判据提炼】。
> 引文说明：合字 `fi`/`fl` 已还原为普通字母，弯引号已还原为直引号；**用词与数字未改**。

---

## 2.1 总纲：给"可用性测试"划一条可操作的定义线

这一章只回答四件事：**什么算可用性测试（什么不算）｜为什么要做｜用什么方法论｜做不到什么**。最后一项尤其重要——作者明确拒绝"经典实验法"，也明确列出测试的四条局限。

---

## 2.2 定义：必须有代表性用户

> **原文（p59）**：
> 「Throughout this book we use the term usability testing to refer to a process that employs people as testing participants **who are representative of the target audience** to evaluate the degree to which a product meets specific usability criteria. This inclusion of representative users eliminates labeling as usability testing such techniques as **expert evaluations, walk-throughs**, and the like that do not require representative users as part of the process.」

> **★★★★ 判据：一条硬线——有没有"代表性用户"在场**
> 有代表性用户 → 可用性测试。没有 → 专家评估、走查、启发式评估，都**不是**可用性测试。
> 这条线把方法论分成了两个族：
> - **用户在场族**：可用性测试、访谈、观察、出声思维
> - **专家在场族**：启发式评估、走查、认知走查（详见 `user-research-methods` 的方法选择层）
> **两者的错用后果不同**：专家评估便宜但会漏掉"真实的人会怎么错"；用户测试能暴露真实错误但没有专家视角的系统性。

> **原文（p59）**：
> 「Usability testing is a research tool, **with its roots in classical experimental methodology**. The range of tests one can conduct is considerable, from true classical experiments with large sample sizes and complex test designs to very informal qualitative studies with **only a single participant**.」

> **★★ 判据：样本量从 1 到数百都在合法区间内**
> 决定规模的不是"严谨度"，而是**研究问题需要多强的推断**（见 ch03 四种测试类型）。

---

## 2.3 为什么测：三层目标

### 2.3.1 第一层：为了设计（Informing Design）

> **原文（p60）**：
> 「The overall goal of usability testing is to **inform design** by gathering data from which to identify and rectify usability deficiencies existing in products and their accompanying support materials **prior to release**.」

配套的产品质量目标（p60 列举）：
- 「Are useful to and valued by the target audience」
- 「Are easy to learn」
- 「Help people be effective and efficient at what they want to do」
- 「Are satisfying (and possibly even delightful) to use」

### 2.3.2 第二层：消除挫败（Eliminating Design Problems and Frustration）

> **原文（p60）**：
> 「When you minimize the frustration of using a product for your target audience by remedying flaws in the design ahead of product release, you also accomplish these goals:」
> - 「Set the stage for a positive relationship between your organization and your customers.」
> - 「Establish the expectation that the products your organization sells are high quality and easy to use.」

> **★★ 判据：测试的商业价值主要不在"发现问题"，而在"建立预期"**
> 这一点在向管理层争取资源时比"我们能查出 N 个 bug"更有效——它把测试从成本项变成品牌项。

### 2.3.3 第三层：为了盈利（Improving Profitability）

> **原文（p61）**：
> 「**Minimizing risk.** Actually, all companies and organizations have conducted usability testing for years. Unfortunately, the true name for this type of testing has been "**product release**," and the "testing" involved trying the product in the marketplace.」

> **★★★★ 判据：不做测试 ≠ 不测试，只是把测试推迟到发布之后，由市场来做**
> 这是全书最有说服力的一句论证。它的实操含义：测试的对照基线不是"零成本"，而是"发布后返工/客服/退货的成本"。
> 向老板陈述时用这个框架，不要用"我们做了测试所以更好"。

其余盈利条目（p60–p61）：
- 「Creating a historical record of usability benchmarks for future releases.」
- 「Minimizing the cost of service and support calls.」
- 「Increasing sales and the probability of repeat sales.」
- 「Acquiring a competitive edge because usability has become a market separator for products.」

---

## 2.4 方法论：为什么**不**用经典实验法

### 2.4.1 经典实验法的五条要求

> **原文（p61–p62）**：
> 「Employing a true experimental design, these studies require that:」
> - 「A hypothesis must be formulated.」
> - 「Randomly chosen (using a very systematic method) participants must be assigned to experimental conditions.」
> - 「Tight controls must be employed.」
> - 「Control groups must be employed.」
> - 「The sample (of users) must be of sufficient size to measure statistically significant differences between groups.」

### 2.4.2 五条不适用理由

> **原文（p62）**：
> 「It is **often impossible or inappropriate** to use such a methodology to conduct usability tests in the fast-paced, highly pressurized development environment」

> **原文（p62）**：
> 「It is inappropriate because the purpose of usability testing is **not necessarily to formulate and test specific hypotheses**, that is, conduct research, but rather to **make informed decisions about design** to improve products.」

> **原文（p62）**：
> 「Lacking such information, one may need to test **10 to 12 participants per condition** to be on the safe side, a factor that might require one to test **40 or more participants** to ensure statistically significant results.」

> **★★★ 判据：用"决策"而不是"假设"来定义测试的目的**
> 假设检验要回答"哪个更好"；设计决策要回答"下一步改什么"。二者的样本量、控制强度、记录方式全都不同。
> **判据的二值化**：如果你的测试报告结论是"无法证明 A 优于 B"，那它没有完成设计决策任务；如果结论是"在第 3 步有 4/6 人卡住，因为标签不匹配"，那它完成了。

> **原文（p63）**：
> 「Last, and probably most important, the classical methodology is designed to obtain **quantitative proof** of research hypotheses that one design is better than another, for example. It is **not designed to obtain qualitative information on how to fix problems and redesign products**.」

### 2.4.3 本书主张的七要素

> **原文（p63）**：
> 「**Basic Elements of Usability Testing**」
> - 「Development of research questions or test objectives rather than hypotheses.」
> - 「Use of a representative sample of end users which may or may not be randomly chosen.」
> - 「Representation of the actual work environment.」
> - 「Observation of end users who either use or review a representation of the product.」
> - 「Controlled and sometimes extensive interviewing and probing of the participants by the test moderator.」
> - 「Collection of quantitative and qualitative performance and preference measures.」
> - 「Recommendation of improvements to the design of the product.」

> **★★★★ 判据：七要素里第 7 条是"必须给出改进建议"**
> 这条把可用性测试与"研究"彻底区分开：**没有改进建议的测试，在本书的方法论里是不完整的交付物。**
> （对照 ch09 的报告章节——建议不是可选项。）

---

## 2.5 边界：测试做不到什么

> **原文（p64）**：
> 「Testing does not guarantee success or even prove that a product will be usable.」

四条局限（p64）：

| # | 局限（原文） | 实操含义 |
|---|---|---|
| 1 | 「**Testing is always an artificial situation.** Testing in the lab, or even testing in the field, still represents a depiction of the actual situation of usage and not the situation itself.」 | 实验室里的"成功"不等于现场的成功；外推要打折 |
| 2 | 「**Test results do not prove that a product works.** ... Statistical significance is simply a measure of the probability that one's results were not due to chance.」 | 显著性 ≠ 可用；不要把 p 值当验收 |
| 3 | 「**Participants are rarely fully representative of the target population.**」 | 代表性受限于你"能不能把目标人群说清楚" |
| 4 | 「**Testing is not always the best technique to use.** ... in some cases it is more effective both in terms of cost, time, and accuracy to conduct an expert or heuristic evaluation」 | 早期粗制滥造的原型，先做专家评估 |

> **原文（p64）**：
> 「It is simply unnecessary to bring in many participants to reveal the obvious.」

> **原文（p64）**：
> 「in spite of these limitations, usability testing, when conducted with care and precision, **for the appropriate reasons, at the appropriate time in the product development lifecycle**, and as part of an overall user-centered design approach, is an almost infallible indicator of potential problems and the means to resolve them. ... **it is better to test than not to test.**」

> **★★★ 判据：局限性要在测试计划里预先声明，不在报告末尾道歉**
> 四条局限是"方法论的一部分"，不是"免责声明"。写法：在测试计划的 Method 段写明本次测试**不能**外推到什么范围。

---

## 2.6 本章概念-论点表（共 10 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | 可用性测试的定义线 | 「representative of the target audience」；不含这条线的专家评估/走查不算 | 专家评估、walk-through | 判"是不是可用性测试"只看有没有代表性用户在场 | p59 |
| 2 | 规模光谱 | 从经典实验到「only a single participant」都合法 | 全书 | 规模由"要多强推断"决定，不由"要多严谨"决定 | p59 |
| 3 | 总目标 | 「inform design」，且在「prior to release」 | 全书流程 | 测试的交付物是"改什么"，不是"评分" | p60 |
| 4 | 商业价值 | 「Set the stage for a positive relationship」 | 客户关系 | 测试价值的一半在品牌预期，可用来争取资源 | p60 |
| 5 | 隐性测试 | 「the true name for this type of testing has been "product release"」 | 市场即测试场 | 不做测试只是把测试外包给市场，成本更高 | p61 |
| 6 | 经典实验五要求 | 假设、随机分配、严密控制、对照组、足够样本 | 学术研究 | 五条在工业环境几乎全不可满足 | p61–p62 |
| 7 | 目的错位 | 「not necessarily to formulate and test specific hypotheses」 | 40 人以上的实验成本 | 用"决策"而非"假设"定义测试目的 | p62 |
| 8 | 七要素 | 含「Recommendation of improvements to the design」 | 全书 | 没建议的测试是不完整交付 | p63 |
| 9 | 四条局限 | 「Testing is always an artificial situation.」等 | 实验室 vs 现场 | 局限写进计划，不写进免责声明 | p64 |
| 10 | 最终立场 | 「it is better to test than not to test」 | 全书 | 完美测试不如有测试；与"少样本多次迭代"配套 | p64 |

---

## 2.7 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| 具体样本量计算 | 只说经典实验需「10 to 12 participants per condition」，未给工业场景的公式 | ch05 §5.6 给"4–5 人/单元"的经验值；统计公式本章未展开 |
| 专家评估与用户测试的量化对比 | 只说"有时专家评估更划算"，无数据 | 本章未展开；见 `user-research-methods` 方法比较 |
| 盈利性的财务模型 | 只列方向（减少客服、提升复购），无测算 | 本章未展开 |
| "何时不该测"的判据 | 本章只提一句「for the appropriate reasons」，未列清单 | 见 ch05 §5.2「When Not to Test」 |
| 「single participant」的研究设计 | 承认合法，但未说明单人测试能得出什么结论 | 本章未展开；见 ch07 §7.5 与 ch11 |

---

## 2.8 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 四种测试类型（探索/评估/验证/比较） | 本书 ch03 | 本章只提"规模光谱"，类型学在 ch03 |
| 「for the appropriate reasons」 | 本书 ch05 §5.2 | 不该测的六种理由 |
| 七要素中的"代表性样本" | 本书 ch07 | 招募与筛选的完整流程 |
| 七要素中的"改进建议" | 本书 ch09 报告章节 | 建议的组织与优先级 |
| 专家评估 vs 用户测试 | `user-research-methods` 技能 | 方法选择层，写"详见" |
| 局限 1（人为情境） | `design-methodology-liuguanzong` 事理学 | 实验室抽离了"事"的场景，外推必失真 |
| 局限 4（何时不用测试） | `inclusive-accessibility-design` 技能 | 无障碍可先用标准条文做合规审查，再上测试 |
