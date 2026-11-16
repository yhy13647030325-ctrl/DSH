# 可复用配方 P1–P10

> 每条配方给出：**什么时候用 → 需要什么输入 → 步骤 → 输出长什么样 → 判据与陷阱**
> 页码口径：**PDF 索引**（`===== PAGE N =====` 的 N）
> **时效止于 2007 年**。2010 年后的标准（WCAG 2.1/2.2、EN 17161、EN 301 549、ISO 21542）**本技能不含**，本文件也不会用到它们。

---

## P1 · 做一次排除率估算（四步法）

**何时用**：要回答"这个产品排除多少人"，或要给可及性改进做商业论证。

**输入**：产品 + 明确的使用语境（不是产品本身，是"在什么环境下、按什么动作序列用"）。

### 步骤

| 步 | 动作 | 产出 | 陷阱 |
|---|---|---|---|
| **1** | **写语境** | 环境假设 + 编号的动作序列（如：拿起→走到水龙头→注水→归位→开机→倒水） | **脱离语境的排除率只是一个数字，无法改进。** 同一台壶放在台面上 vs 放在吊柜里，是两个产品 |
| **2** | **七轴打分** | 每轴一个 0–13 分 + **一条 justification** | 无 justification 的分数不可复核、不可复用 |
| **3** | **评身体属性** | 尺寸/力判据（如"间隙 ≥ P95 指厚 = 16.6 mm"） | 尺寸与能力**不可互相替代**：能力够但够不到，只能靠 Step 3 抓 |
| **4** | **去重** | 用 `worst + 0.4×次差 + 0.3×第三差` 合并；或查耦合图 | **七轴人数不可相加**（相加会严重高估）；跨数据集合并原文说 `difficult, if not impossible` |

### 打分怎么做（量表无对应描述时）

**主观类比**：找一个已标定的相似动作做锚点。
> 原文实例：**按按钮 ≈ 挤海绵 = dexterity 8.0**（理由：都涉及手指施力）
> 其它现成锚点：听觉 5.5 ≈ `a person talking in a loud voice in a quiet room`；视觉 4.5 ≈ `read a large print book`；平衡需扶物者 locomotion 记 7.0

### 输出模板（照 Acoustiguide 表的结构）

```
产品描述：<一句话>
使用语境：<谁给的、给了什么说明、配件状态>
动作序列：1)… 2)… 3)…
七轴分数 + justification：
  Locomotion        <分>  <理由>
  Reach & Stretch   <分>  <理由>
  Dexterity         <分>  <理由>
  Vision            <分>  <理由>
  Hearing           <分>  <理由>
  Communication     <分>  <理由>
  Int. functioning  <分>  <理由>
一般评论：<发现了什么、怎么改>
评估耗时：约 30 分钟
```

**判据**：一份完整七轴评估约 **30 分钟**（Clarkson p438）。超过 1 小时说明拆得不够或纠结于无数据支撑的精度。

---

## P2 · 从极端用户反推主流设计

**何时用**：概念期没有方向；或产品已经"能用"但缺乏创新点。

### 步骤

**① 选人：选分布两端，不选典型**

判断价值的问题不是"他是不是目标用户"，而是：
> **"他在哪件事上比常人更懂？"**

原文四个正向例子：
| 极端 | 在哪件事上更懂 | 反推出了什么 |
|---|---|---|
| 因过度使用聊天室被开除两次的人 | 人从线上关系里获得了什么 | 社群服务的核心价值 |
| 靠水站导航全城的自行车快递员 | 城市里的补给我怎么走 | **我们都有的移动性需求** |
| 每天喝数品脱软饮的人 | 配方的微妙之处 | 新能量饮料 |
| 全球亲友拍的"人怎么带饮料"照片 | 便携容器的全部解法 | 新颖包装 |

**② 让"他们"变成"我们"**

验收判据：项目会议里谈到用户时用的是**"我们"还是"他们"**。若是"他们"，共情还没发生（Coleman p165）。

**③ 拿 coping 策略当创新源，不拿需求当创新源**

> 创新触发点不是"用户的需求"，是**"用户自己发明的办法"**（Clarkson p547）。

**④ 接受"不完美但基础包容"**

> 用户原话：`I don't want a spacey park`（Clarkson p545）
> **用户宁可要 80% 好用的主流产品，也不要 100% 贴合但一看就是"给他们做的"产品。**

### 陷阱

| 陷阱 | 说明 |
|---|---|
| **把极端用户当需求清单** | 他们的产出是"本质洞察"，不是"功能需求" |
| **只服务极端** | 极端用户是**探测仪**，不是**交付对象** |
| **招募来源单一** | 极端用户往往来自少数社群，极易互相认识 → 触发四条招募偏倚（见 P7） |

---

## P3 · 能力轴扫描清单（不接触用户也能做）

**何时用**：项目刚启动、无预算、无用户接触渠道。这是**成本最低的起点**。

**方法**：把设计者的"我试了一下觉得还行"升级为**结构化的交互图扫描**。

### 步骤

**① 建交互图**（每个组成动作标四列）

| 组成动作 | 产品特征 | 产品周围 | 环境影响 |
|---|---|---|---|
| 例：旋开瓶盖 | 盖子直径、滚花、扭矩 | 台面高度、是否有水渍 | 照明、是否戴手套 |

> **四列都要填。**很多排除不是产品造成的，是"产品 + 周围 + 环境"的组合造成的。

**② 逐格问"如果我做不了这一步会怎样"**

这一步的产物是 **coping 策略**——用户会怎么绕过设计。**不需要真实用户，只需要设计者被迫逐格推演。**

**③ 每格打七轴分数**（转入 P1）

**④ 标出通路任务**

通路任务 = 不做就无法使用其余功能的任务（首次设置、配对、激活、安全联锁）。
> **通路任务一律按最高标准评估，不允许"反正很少用"**（Coleman p188）。

### 判据

- 系统化方法的两个目标都是**降低遗漏概率**，不是保证正确（`minimising the possibility of overlooking`，Clarkson p472）
- 交互图只代表任务的**一个子集**（同上）

---

## P4 · 无障碍设计评审门禁（12 条否决项）

**何时用**：设计评审、打样前、上会前。**任一条命中即拦。**

| # | 否决项 | 原文依据 |
|---|---|---|
| **1** | 关键操作需要**双手** | `Tasks which require the use of two hands`（Coleman p173、Clarkson p126）|
| **2** | **推送 + 旋拧**复合动作 | `Double actions such as push and twist are particularly difficult`（Clarkson p52）|
| **3** | 状态只用**蓝—紫—绿**区分 | `Blue-violet-green combinations should be avoided`（Clarkson p54）|
| **4** | 关键数值用**百分比**表达 | `natural frequencies should be used in preference to percentages`（Clarkson p62）|
| **5** | 序列操作**需要记忆** | `The memory load can be eliminated by cueing each step`（Clarkson p62）|
| **6** | 视觉信息位于 **1 m 外**却按 40 cm 阅读设计 | 60 岁最佳视距 **100 cm**（Clarkson p53）|
| **7** | 关键操作件**未标 P95 尺寸** | P5–P95 默认排除 **10% = 460 万人**（Clarkson p442）|
| **8** | 只做**重度专用版**，无主流扩边 | `this approach dominates the cube`（Clarkson p108）；塔身占 45% |
| **9** | 被宣传成"为残障人士" | 用户不愿被看见用"被做得更容易用"的产品（Coleman p90）|
| **10** | 只在项目**末期**做一次评估 | 晚期评估必产补丁（`cumbersome and unattractive features that have been 'fixed'`，Clarkson p469）|
| **11** | 依赖**未标定的模拟器**排优先级 | 体感强度 ≠ 问题严重度（Coleman p222）|
| **12** | 把**七轴排除人数相加** | `the total exclusion will not be the sum`（Clarkson p439）|

### 附加十项高频缺陷（可直接当检查项）

小字（浅灰配白）/ 说明书小字低对比 / 读数面板暗且小 / 复杂菜单 / 光滑侧面旋钮 / 高灵巧度小控件 / 需过大力气 / 缺触觉反馈 / 多功能键困惑 / 双手操作
（Coleman p173）

---

## P5 · 尺寸超界检查（把百分位变成人数）

**何时用**：任何需要人体尺寸/力的决策点。

### 步骤

1. **确定选哪个百分位**（用 `ergonomics-ding-yulan` 的 III 型产品方法：取 P5–P95、满足度 90%）
2. **写出被排除人数**：
   - 默认 P5–P95 → **排除 10%**
   - 英国 16+ 口径：**10% = 4,600,000 人**（Clarkson p442）
3. **多尺寸产品要逐个算**：`for a complex design that requires contact with different parts of the body ... a different 1 0% may be excluded each time`（Clarkson p442）
4. **换算成几何约束**（可直接进图纸的句式）

### 几何判据的写法（模板）

> **"凡需要手指伸入操作的间隙/凹槽/拉手内空，其最小值应 ≥ 目标人群 P95 指厚。"**

原文实例（Clarkson p442）：

| 国家 | 性别 | 均值 | P5 | **P95** |
|---|---|---|---|---|
| UK | 男 | 14.5 mm | 12.5 | **16.6** |
| UK | 女 | 13.0 mm | 10.9 | 15.1 |
| USA | 男 | 14.6 mm | 12.5 | **16.7** |
| USA | 女 | 13.0 mm | 10.7 | 15.3 |

→ 壶 E 的开关间隙 **18 mm > 16.6 mm**，原书判定 `An effective design`。

### 陷阱

- **"按 P5–P95 设计"不是一个技术决定，而是一个人群决定**。必须连同被排除人数一起签字。
- **基准人不是"平均成年男性"**：老年女性力量约为男性 **2/3**、身高再低 **5–10 cm**、人数上占多数 → 原书明确 `Older women should therefore be a priority target group for inclusive design`（Clarkson p51）。
- 尺寸数据（Adultdata 的 266 项尺寸 + 28 项力量）**多国混合采集**，`difficult to correlate against the capability data`（Clarkson p436）——**不能直接与能力数据相乘**。

---

## P6 · 感官三通道冗余设计

**何时用**：任何有输出（提示、状态、警报）或输入（按键、识别）的界面。

### 原则：关键信息至少两条通道，且不依赖同一能力轴

| 通道 | 老年/残障侧的量化约束 | 出处 |
|---|---|---|
| **视觉** | 视距按 **1 m**（60 岁）；照度需 **3×**（60 岁）／**10×**（暗适应）；**禁蓝紫绿区分**；表面非反光、对比要高 | Clarkson p53–p54 |
| **听觉** | 优先用**低频**（高频神经细胞青春期即开始死亡、50 岁起一般性损失）；**音量与音调可调**；减少环境噪声 | Clarkson p55–p56 |
| **触觉** | **两点辨别退化**：触觉元素间距需按阈值而非"摸得出来"直觉；50 岁后**振动感知下降**（高频尤甚） | Clarkson p56–p57 |
| **多模态** | `Dangerous smells ... should be signalled where possible by strong messages from several sense modalities` | Clarkson p57 |

### 组合判据（原书原文）

- `A combination of audio and visual signals increases the chance that messages are received.`（Clarkson p56）
- `Surfaces should be non-reflective, and brightness and colour contrast high.`（Clarkson p54）
- `Stairs should have clearly marked edges.`（Clarkson p54）
- `Lower frequency sounds should be used to convey important messages.`（Clarkson p56）

### 陷阱

- **有功能但看不见 = 没有功能**。家政用品审计的实证：`product features designed to assist use were often not visible due to lack of colour contrast`（Coleman p216）
- **多语言化会制造新的视觉缺陷**：`instructions ... compromised by attempts to make packs multi-lingual, resulting in the use of small fonts and ﬁ gures`（Coleman p216）——**改进可以互相抵消**。

---

## P7 · 认知负荷分级与降载

**何时用**：菜单结构、设置流程、说明文本、多步操作。

### 先定位：认知退化集中在哪三项

| 子能力 | 走向 | 设计含义 |
|---|---|---|
| 词汇 / 专业知识 / 兴趣 | **稳定甚至上升** | **不要为老年用户简化成儿童语言** |
| 处理速度 | 明显下降 | 禁止极短呈现、快速轮播 |
| **双任务** | **下降最明显** | 禁止"边做 A 边做 B" |
| 数字能力 | 下降最多（纵向研究） | 用自然频次 |
| 回忆 vs 再认 | 回忆难得多 | 给可见选项，别让人凭记忆输入 |
| **前瞻记忆** | 明显下降 | **必须给提醒与逐步引导** |
| 执行功能 | 下降，但与教育与经验强相关 | 复杂决策鼓励咨询他人 |

（Clarkson p57–p62）

### 三条硬改写

| 改写 | 原文 |
|---|---|
| **① 序列操作逐步提示** | `Designs which impose a high demand on memory should be avoided ... The memory load can be eliminated by cueing each step`（Clarkson p62）|
| **② 数值用自然频次** | `1 in 1,000 is more readily understood at all ages than 0.1 %`（Clarkson p62）|
| **③ 禁多源竞争/极短呈现** | `Very rapid presentation of information should be avoided`；`Competing inputs from the same or different senses (e.g. CNN style presentation) are not well suited`（Clarkson p62）|

### 补充判据

- **新符号/缩写必须先给学习机会**：`Care should be taken when introducing novel symbols, acronyms etc. that there has been sufficient opportunity for learning`（Clarkson p62）
- **禁急促决策**：`The need to make rapid decisions should be avoided. High-pressure selling puts older people at a particular disadvantage.`（Clarkson p63）
- **复杂决策鼓励咨询**：`consultation with others should be encouraged`（Clarkson p63）

### 分级（四点量表口径）

| 级 | 认知负荷 | 设计动作 |
|---|---|---|
| **4 Full** | 日常无困难 | 保持 |
| **3 Moderate** | 若干情境有些困难 | **主力目标**：逐步提示 + 自然频次即可纳入 |
| **2 Partial** | 多数情境显著困难 | 需替代通道（分步向导、语音引导、可回退） |
| **1 Minimal** | 实际用途做不到 | 需专门方案（人工协助或专用界面） |

---

## P8 · 与可用性测试串接（把可及性塞进现有测试）

**何时用**：已经有可用性测试流程，不想另起一套。

### 步骤

**① 在招募表里用能力分数筛人，不用年龄或诊断**

按"能力分数接近产品需求分数"筛 → 这样筛出来的就是 **boundary users**。
> `Boundary users ... can most easily identify points of difﬁ culty and exclusion`（Coleman p213）

**② 测试前必须说一句话**

> **"被测的是设计，不是你。"**
> 原文：`aware that what is being tested is eventual difﬁ culties caused by poorly designed attributes and not the users themselves`（Clarkson p473）
> **不说这句，老年与残障用户的自我归因会掩盖设计问题**（`propensity of older people to blame themselves rather than poor design`，Coleman p178）。

**③ 分组，不要混组**

老年用户在有年轻人的焦点小组里`opinions can sometimes be eclipsed by younger more vociferous participants`（Coleman p178）。

**④ 时长与会次**

单场 **1.5–2 小时**，含茶歇（`keep the testing sessions to a reasonable length (1½−2 hours) and build in tea and rest breaks`，Coleman p182）。

**⑤ 问卷只问"哪里难用"，不问"你能做到吗"**

> `Users in general, and particularly older users, tend to either underestimate or overestimate their own functional performance`（Clarkson p475）
> `if emphasis is put on the problems that the design presents, it might be possible to get a more objective response`（Clarkson p475）

**⑥ 用户说"挺好用"时，必须补一次观察**

> `Some users are accustomed to experiencing difﬁ culty using products that they will nevertheless describe as being easy to use because they present no more difﬁ culty than other products in their experience`（Coleman p179）
> **没有比较基准时，困难会被描述成正常。**

**⑦ 观察不能兼职**

`It is better not to combine observations with other duties during a user test.`（Coleman p179）

### 样本量参考

| 目的 | 样本量 | 出处 |
|---|---|---|
| 研究级（每类特征） | **≥ 12 人** | Coleman p175 |
| 研究级（每次测试合计） | **≥ 50 人** | Coleman p175 |
| 设计实践（探索性） | 小样本可，**简单试验已被证明有效** | Clarkson p476 |

> **两者不冲突**：目的不同。研究要代表性结论，实践要发现方向。

### 预算参考（2007 年英镑）

| 项 | 值 |
|---|---|
| 一场焦点小组（全含） | **£3,000–4,500** |
| 专业访员 | **£150–175/天** + 差旅 |
| 参与者酬金 | 约 £25（含交通） |
| 专业主持（直聘） | 约 £500/天 |
| 招募 25 人 | **5 个工作日，摊在 4 周内** |

（Coleman p176、p182）

---

## P9 · 改进优先级排序（防"改了没用"）

**何时用**：审计做完了，有一堆问题，要决定先改哪个。

### 判据 A：先看耦合强度

| 耦合 | 正确改法 | 依据 |
|---|---|---|
| **弱** | 逐轴改，单轴独立生效 | `if the coupling is not significant, an improvement can be made by addressing each axis`（Clarkson p445）|
| **强** | **必须同时改两轴** | `if the coupling is significant, then both axes must be addressed simultaneously`（同上）|

> **只降一轴的后果**（原文精确表述）：`The reduction of vision demand will only include more bubbles hugging the vision axis, but not those in the coupling region`（Clarkson p444）
> **实证**：壶 E → 壶 F 的差距 = **1,880,000 人**，全在视觉×灵巧的耦合区。

### 判据 B：按边际收益，不按当前人数

> `a small decrease in visual demand would include a large number of additional people, while a similar decrease in dexterity demand would only include a few more`（Coleman p211）

**排序依据**：**每降一档需求能换回多少人**，而不是"当前哪轴排除人数最多"。

### 判据 C：先修通路任务

通路任务（不做就无法使用其余功能）**不打折**：
> `a single infrequent excluding task can compromise use of the whole product`（Coleman p188）
实物例：灶具的儿童安全联锁——不会"编程"就整台灶用不了。

### 判据 D：要"删步骤"，不要"优化步骤"

> `this (often dangerous) task step is avoided completely`（Coleman p160）
原文实例：加长杆让用户不必爬梯子——**不是让爬梯更安全，是不用爬了。**

### 输出格式（建议）

```
问题清单（按轴 × 通路与否）
├─ 通路任务 → 一律最高优先（不打折）
└─ 非通路任务
    ├─ 耦合强（两轴同现）→ 必须成对改，作为一个改造包
    └─ 耦合弱 → 按"每降 1 分换回人数"降序排
```

---

## P10 · 把"包容"从附录搬到 brief 上（组织动作）

**何时用**：设计做得动，但项目一直"没时间做可及性"；或客户不接受。

### 先确认一个残酷事实

> `designing solutions to be as inclusive as possible has never been a primary, secondary or even tertiary requirement of any`（Imagination 创意总监，Clarkson p547）
> 也就是说：**如果 brief 里没写，它就不会发生。**靠团队自觉是无效的。

### 四条可执行动作

**① 让客户亲身体验（最快的手段）**

> 模拟器最有价值的商业用途是 `raising the client's awareness regarding the levels of avoidable exclusion`（Coleman p230）
> 因为第 6 章已证明：**评估预算取决于客户是否理解**（`if the client is not conversant ... it is unlikely ... financial resources`，Clarkson p482）
> **最便宜的入门**：指关节粘纽扣 + 起雾眼镜 + 吸管爬楼，成本近零。

**② 用"早做比晚做便宜"论证，不用"应该做"**

> `Defining as much of the knowledge loop as possible in the shortest possible time will keep the overall design process swift and focused.`（Clarkson p453）
> 业界阻力是**成本认知**：`The most common such perceived problem is that of increased cost and time`（Clarkson p462）
> **回应方式不是否认成本，而是证明晚闭环的返工更贵**（晚期评估必产补丁）。

**③ 内部培养 user champion，而不是外购服务**

> `It is preferable to have an internal user champion present throughout the design process, rather than external 'hired help'`（Clarkson p479）
> 理由：可及性在项目里是**随时冒出的小决定**，外部顾问只在评审点出现，接不住。
> **验收判据（responsive designer）**：团队若还需要"额外做一次可及性检查"，说明尚未内化（Clarkson p462）。

**④ 把"最低即最高"这个陷阱写进采购条款**

> `a 'deemed to satisfy' approach to standards and guidelines could result in recommended minimum provision becoming the maximum in practice`（Clarkson p25）
> **对策**：用**过程标准**（如 BS 7000-6 的管理标准）替代**指标标准**——过程可随期望与技术演化，指标会被当作天花板（Clarkson p595）。

### 三条沟通话术（有原文支撑）

| 场景 | 话术 | 依据 |
|---|---|---|
| 客户说"这是公益议题" | `the user success rate was 56%`（普通电商用户，非残障用户） | Clarkson p530 |
| 客户说"目标用户不是老人" | Target 是 `an arbitrary definition`，不能用来论证包容性 | Clarkson p114 |
| 团队说"约束会限制创意" | `The more constraints there are, the more creative designers have to be`（DBA 团队一致回应） | Clarkson p545 |

---

## 附：十份配方的调用顺序（一个完整项目里）

```
立项
 ├─ P10 把包容写进 brief（否则后面都不会发生）
 ├─ P3 能力轴扫描（无预算也能做，定初步风险）
概念期
 ├─ P2 极端用户 → 反推主流方向
 ├─ P4 评审门禁（12 条否决项先过一遍）
设计发展
 ├─ P5 尺寸超界检查（每个尺寸决策点）
 ├─ P6 三通道冗余（每个输出/输入界面）
 ├─ P7 认知降载（每个多步流程）
评估期
 ├─ P1 排除率估算（算人数，做商业论证）
 ├─ P8 可用性测试串接（boundary users）
 └─ P9 优先级排序（决定改哪个）
迭代
 └─ 回到 P1 复测（原文要求：改完再做一次排除审计）
```

> **"改完要复测"是有原文依据的**：家政用品项目 `exclusion targets ... were set and a number of improved design concepts proposed, which were subsequently subjected to a further exclusion audit`（Coleman p215）。
