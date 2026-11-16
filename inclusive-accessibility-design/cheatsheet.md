# 一页速查 · 包容性设计 / 无障碍设计

> 源：Clarkson《Inclusive Design》(2003) ＋ Coleman《Design for Inclusivity》(2007)
> 页码口径：**PDF 索引**（`===== PAGE N =====` 的 N）
> **时效止于 2007 年**：WCAG 2.1/2.2、EN 17161、EN 301 549、ISO 21542 等**本技能不含**

---

## 一、总公式（唯一的不等式）

```
Demand（产品需求） > Capability（用户能力）  →  Exclusion（排除）
```
（Coleman p187）

**左右两侧可独立描述、分别修改。**

---

## 二、能力谱：七条轴 → 三条 → 一把尺

| 大类 | 三条轴 | 严重度区间 | 产品侧含义 |
|---|---|---|---|
| **Motion** | Locomotion | 0.5–11.5 | 走到、站立、上下楼 |
| | Reach & Stretch | 1.0–9.5 | 够到货架、举手过头 |
| | **Dexterity** | 0.5–10.5 | 抓握、旋拧、按压 |
| **Sensory** | Vision | 0.5–12.0 | 读标签、辨色、看屏 |
| | Hearing | 0.5–11.0 | 听提示音、听懂语音 |
| **Cognition** | Communication | 0.5–12.0 | 理解说明、表达 |
| | Intellectual functioning | 1.0–13.0 | 理解结构、记住步骤 |

（Clarkson p377）
> **分数 0 = 完全有能力；13 = 最重。分数越高 = 该产品对能力要求越高。**
> **对齐性质（关键前提）**：`equal scores broadly relate to equivalent levels of capability`（p435）——没有这条，七个数不能合并。

### 听觉轴量表（8 级，可直接照抄用于给其它轴建表）

| 级 | 行为 | 分数 |
|---|---|---|
| H1 | Cannot hear sounds at all | 11.0 |
| H2 | Cannot follow a TV programme with the volume turned up | 8.5 |
| H3 | Has difficulty hearing someone talking in a loud voice in a quiet room | 6.0 |
| H4 | Cannot hear a doorbell, alarm clock or telephone bell | 5.5 |
| H5 | Cannot use the telephone | 4.0 |
| H6 | Cannot follow a TV programme at a volume others find acceptable | 2.0 |
| H7 | Difficulty hearing someone talking in a normal voice in a quiet room | 1.5 |
| H8 | Difficulty following a conversation against background noise | 0.5 |

（Clarkson p435）**注意：全部是行为描述，无一个病因。**

### 四点行为量表（评审用，非量化用）

| 级 | 判据 | 设计动作 |
|---|---|---|
| **4 Full ability** | 日常活动够用 | 无需特殊考虑 |
| **3 Moderate ability** | 若干日常情境有些困难 | **主力目标：改细节即可纳入** |
| **2 Partial ability** | 多数日常情境显著困难 | 需替代通道（冗余模态、可调参数） |
| **1 Minimal ability** | 实际日常用途做不到 | 需专门方案 |

（Coleman p207–p208）
> **第三列才是价值**：每级对应一个设计动作，不是一种人。

---

## 三、合并与分档

### 严重度算式（全书唯一算式）
```
Overall severity = worst + 0.4 × (second worst) + 0.3 × (third worst)
```
（Clarkson p375、p436）
- **最差项权重 1，决定命运**
- 第二、第三差仍有实质加成
- **第四名以后权重 0**
> **优化顺序：拉起最差那一项，不要平均改善。**

### 用户金字塔（十级 × 人口）

| 层 | 分数 | 名称 | 占受损人口 | 人数（基数 8,582,200） | 设计响应 |
|---|---|---|---|---|---|
| 顶 | 7–10 | Severe | **21%** | ≈ 1,802,000 | Special purpose |
| 中 | 3–6 | Moderate | **45%** | ≈ 3,862,000 | Customisable / modular |
| 底 | 1–2 | Mild | **34%** | ≈ 2,918,000 | User-aware |

（Clarkson p375、p439）
> **底数 = 8,582,200 人 = 英国成年人口 20%**
> **只做"重度专用版"会漏掉最大的中度层（45%）。**

---

## 四、排除率：关键数字

| 数字 | 含义 | 出处 |
|---|---|---|
| **5.3%** | 典型 1.7L 不锈钢水壶排除率（GB 15+） | Coleman p195 |
| **< 500,000** | "像用杯喝水一样简单"的理想壶排除人数 | Coleman p195 |
| **> 2,000,000** | **能用杯喝热饮却用不了壶的人**（设计性排除） | Coleman p195 |
| **1%–6%** | 日常小家电排除率区间；"5 分"产品排除 6% ≈ 51 万人 | Clarkson p439 |
| **10% / 4,600,000** | **默认 P5–P95 设计主动排除的英国成年人** | Clarkson p442 |
| **8,126,000 / 17.3%** | 有任何一轴受损（去重后） | Clarkson p380 |
| **50%** | 机动 × 感官耦合率 | Clarkson p380 |
| **1,880,000** | 壶 E 与壶 F 的差距人数（全在视觉×灵巧耦合区） | Clarkson p444 |
| **56%** | 电商任务成功率（Nielsen，20 站 496 次尝试） | Clarkson p530 |
| **66%** | 美国人因"太复杂"而对某技术产品失去兴趣的比例 | Clarkson p186 |

### 七轴人数**不可相加**
Acoustiguide 七轴相加 = 254.6 万，去重后远小于此（Clarkson p439）。
> 相加会严重高估。跨数据集合并原文说 `difficult, if not impossible`。

---

## 五、四步排除评估法（30 分钟一份）

| 步 | 内容 | 要点 |
|---|---|---|
| **1** | **定语境** | 环境假设 + 完整动作序列（编号） |
| **2** | **评能力需求** | 七轴打分 + **报两个数**：被排除者 + 处于劣势但未排除者 |
| **3** | **评身体属性** | 尺寸/力；判据示例：间隙 ≥ 目标人群 P95 指厚 |
| **4** | **消除多重计数** | 只用同一数据集内去重；跨集合并须标注"含未消除重复" |

**每个分数必须配一条 justification。**量表无对应描述时用**主观类比**：
> 原文实例：**按按钮 ≈ 挤海绵 = dexterity 8.0**（理由：都涉及手指施力）
> 其它锚点：听觉 5.5 ≈ `a person talking in a loud voice in a quiet room`；视觉 4.5 ≈ `read a large print book`

**一份完整七轴评估耗时：30 分钟**（Clarkson p438）。

---

## 六、改进优先级：两条判据

### 判据 A：先看耦合强度
| 耦合 | 正确改法 |
|---|---|
| **弱** | 逐轴改，单轴独立生效 |
| **强** | **必须同时改两轴**；只降一轴，"只会让贴着该轴的气泡被纳入，耦合区的不会"（Clarkson p444） |

### 判据 B：按边际收益排序
> `a small decrease in visual demand would include a large number of additional people, while a similar decrease in dexterity demand would only include a few more`（Coleman p211）
**排序依据不是"当前哪轴人数多"，是"每降一档换回多少人"。**

---

## 七、WINIT 五层 + 六比值

| 字母 | 名称 | 定义 | 谁能改 |
|---|---|---|---|
| **W** | Whole | 全体人口 | 不可改 |
| **I** | Ideal | 剔除法定的/安全的/不可弥补的之后的上限（必须 **solution-neutral**） | 换品类或辖区 |
| **N** | Negotiable maximum | 需求规格所纳入的 | **需求制定者** |
| **I** | Included | 实际能用的 | **设计团队** |
| **T** | Target | 原定目标（`an arbitrary definition`） | 管理层 |

**关键比值**：
- **Included ÷ N → `should approach unity`** ← 唯一有收敛目标；设计团队唯一可正当免责的边界
- **Included ÷ I** ← `probably the most important`（可跨产品比较）

### 两类排除的判别
> **换一个设计决定，这个人还能不能用？**
> - **能** → **设计性排除**（不可辩护，设计团队的责任）
> - **不能** → **需求性排除**（须提交管理层决定，**不是免责理由**）

---

## 八、7-Level 流程（2 + 3 + 2）

| Stage | Level | 目标（aim） | 验证动作 |
|---|---|---|---|
| **1 问题定义** | **L1 用户期望** | 找出完整问题 | validate problem definition |
| | **L2 用户需求** | 定功能规格 | verify functional definition |
| **2 系统定义** | **L3 感知** | 最小但足够的系统状态表征 | verify user **perception** |
| | **L4 认知** | 结构匹配用户期望 | verify user **understanding** |
| | **L5 机动** | 控制质量与输入 | verify user **comfort** |
| **3 系统验证** | **L6 实用可接受性** | 效用+可用性+可及性 | **正式用户试验（`essential`，不可省）** |
| | **L7 社会可接受性** | 匹配用户期望 | **回扣 L1** |

> **可迭代，不可跳级。**
> **L3 与 L5 用同一张三维度检查表**（媒介性质与可调性 / 对功能的适配性 / 物理布局），方向相反。
> **L4 依赖 L3**：说"不知道现在什么状态"是 L3 病，先补输出再谈理解。

---

## 九、三类用户分工

| 类型 | 能力位置 | 用在哪 | 为什么是他们 |
|---|---|---|---|
| **Extreme users** | 分布两端（重损） | **概念期（早期）** | 逼出创造性提问、示范应对策略；破除刻板印象 |
| **Boundary users** | **正卡在能不能用的边缘** | **评估期** | 最能识别"就差这一点"；严重者已发展替代策略，健全者碰不到边界 |
| **Able-bodied** | 无/轻微 | 全程 | 基线反馈 |

（Clarkson p213、ch04 §4.7.2）
> **招募标准：用能力分数筛人（接近产品需求分数），不用年龄或诊断。**

**判断价值的一句话**：不问"他是不是目标用户"，问**"他在哪件事上比常人更懂"**。

---

## 十、否决项（出现即拦）

| # | 否决项 | 原文依据 |
|---|---|---|
| **1** | 需要**双手**完成关键操作 | `Tasks which require the use of two hands`（Coleman p173、Clarkson p126）|
| **2** | **推送 + 旋拧**的复合动作 | `Double actions such as push and twist are particularly difficult`（Clarkson p52）|
| **3** | 状态只用**蓝—紫—绿**区分 | `Blue-violet-green combinations should be avoided`（Clarkson p54）|
| **4** | 用百分比表达关键数值 | `natural frequencies should be used in preference to percentages`（Clarkson p62）|
| **5** | 序列操作**需要记忆** | `The memory load can be eliminated by cueing each step`（Clarkson p62）|
| **6** | 视觉信息放在**1 m 之外**却按 40 cm 阅读设计 | 60 岁最佳视距 **100 cm**（Clarkson p53）|
| **7** | 关键操作件**未标 P95 尺寸** | P5–P95 默认排除 **10% = 460 万人**（Clarkson p442）|
| **8** | 只做**重度专用版**，无主流扩边 | `this approach dominates the cube`（Clarkson p108）；塔身 45% |
| **9** | 产品被宣传成"为残障人士" | `people do not necessarily want to be seen with a phone that looks as though it has been made easier to use`（Coleman p90）|
| **10** | 只在项目**末期**做一次可及性评估 | `cumbersome and unattractive features that have been 'fixed'`（Clarkson p469）|
| **11** | 依赖**模拟器**做优先级排序而未标定 | `designers may feel more physically affected ≠ more urgent`（Coleman p222）|
| **12** | 把**七轴排除人数相加** | `the total exclusion will not be the sum`（Clarkson p439）|

---

## 十一、数字速查（可直接引用）

### 视觉
| 项 | 值 | 出处 |
|---|---|---|
| 最佳视距 | 10 岁 **8cm** → 50 岁 **50cm** → 60 岁 **100cm** | Clarkson p53 |
| 正常照明需光量 | 40 岁 **2×**、60 岁 **3×**（相对 20 岁） | Clarkson p54 |
| 暗适应后探测到光源 | 60 岁 **10×**、80 岁 **100×** | Clarkson p54 |
| 色彩 | 禁蓝紫绿组合；晶状体滤蓝紫 | Clarkson p53–p54 |

### 听觉
| 项 | 值 | 出处 |
|---|---|---|
| 高频神经细胞开始死亡 | **青春期** | Clarkson p55 |
| 一般性听力损失 | **约 50 岁** | Clarkson p55 |
| 对策 | **优先用低频传重要信息** | Clarkson p56 |

### 触觉
| 项 | 值 | 出处 |
|---|---|---|
| 两点辨别退化 | 随龄加重，两点需更远才辨为两点 | Clarkson p56 |
| 振动感知下降 | **50 岁后**，高频尤甚 | Clarkson p57 |

### 机动
| 项 | 值 | 出处 |
|---|---|---|
| 握力峰值 | **约 25 岁**；**45–54 岁**明显下降 | Clarkson p50 |
| 75+ 握力 | **< 年轻人的一半** | Clarkson p50 |
| 女性力量 | **约男性 2/3** | Clarkson p51 |
| 65–74 岁平均身高 | 比 16–24 岁**低 5cm**；75+ **近 2 倍** | Clarkson p51 |
| 首要目标人群 | **老年女性**（力量 2/3 + 更矮 + 人数占多） | Clarkson p51 |

### 认知
| 项 | 走向 | 出处 |
|---|---|---|
| 词汇/专业知识/兴趣 | **稳定甚至上升** | Clarkson p57 |
| 处理速度 | 明显下降 | Clarkson p57 |
| **双任务** | **最明显下降** | Clarkson p59 |
| 数字能力 | 下降最多（纵向研究） | Clarkson p59 |
| **前瞻记忆** | 明显下降 → 必须给提醒 | Clarkson p61 |
| 替代表达 | `1 in 1,000` 优于 `0.1%` | Clarkson p62 |

### 调研成本
| 项 | 值 | 出处 |
|---|---|---|
| 一份七轴评估 | **30 分钟** | Clarkson p438 |
| 每类特征样本量 | **≥ 12 人** | Coleman p175 |
| 每次测试总样本量 | **≥ 50 人** | Coleman p175 |
| 招募 25 人 | **5 个工作日，摊在 4 周内** | Coleman p176 |
| 单场测试时长 | **1.5–2 小时**（含休息） | Coleman p182 |
| 一场焦点小组（全含） | **£3,000–4,500** | Coleman p182 |
| 专业访员 | **£150–175/天** | Coleman p182 |

---

## 十二、三句话记住

> **1. 只应排除被需求排除的人；其余都是设计造成的。**
> **2. 优先级由"人数 × 边际收益"决定，绝不由"体感强度"决定。**
> **3. 耦合强则必须同时改两轴；能删掉的步骤不要优化它。**
