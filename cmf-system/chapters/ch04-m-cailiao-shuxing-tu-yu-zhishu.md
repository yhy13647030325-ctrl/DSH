# 第 4 章：M 层（一）—— 材料属性空间、属性图与材料指数

> **原书 PDF 页序 p69–p78、p201–p230（共 40 页）**｜**本版逐页读完全部 40 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）
>
> **读法说明**：本章把原书两处合成一章读 ——
> **① 正文 p72–p76（4.4 Mapping Technical Attributes / 4.5 MDS）**
> **② 附录 p201–p230（Chart 1–7 六张属性图 + 7A.1–7A.5 选材分析的数学）**
> 二者是同一件事的"讲故事版"与"数据版"，必须一起读才成立。
>
> **本章在 CMF 三层流程中的位置**：**M 层的"筛"环节**。
> 它回答一个极具体的问题：**给定 CMF 约束，怎么把 100,000 种材料筛成 5 种？**
>
> **⚠ 关于「形状因子（shape factor）」的重要声明**：
> **本书全库 grep `shape factor` / `shape efficiency` / `shape parameter` 均为 0 命中。**
> 这是 Ashby 在另一本书（*Materials Selection in Mechanical Design*）里的工具，**本书没有**。
> 本版按"不许编"原则，**不虚构形状因子的定义与数值**，只在 §4.7 用原文能支持的"截面形状"近似替代，并把完整空白写进 §4.8。

---

## 4.0 为什么要"画图"，而不是"查表"

> **原文（p72）**：
> 「Asking if two colors are "similar" can be answered by comparing their wavelengths. But if by "similar" you mean a larger set of properties, you are asking for something more difficult: **recognition of a pattern of behavior. The brain is better at pattern recognition when the input is visual rather than text-based. So: how can we make technical attributes visible? One way is by plotting them in pairs, to give a sort of map of where they lie.**」

★★★★ **判据：属性图的价值不是"精确读数"，是"让大脑做模式识别"。**
> **判据落地：CMF 评审现场不要拿材料数据表（几十行数字），要拿属性图（一张气泡图）。**
> 因为评审要做的是"这批材料像不像一类东西"，那是模式识别任务，不是算术任务。

> **原文（p72）**：
> 「Figure 4.4 is an example. Here the first two of the attributes from 4.3 – **elastic modulus, E, measuring stiffness, and density, ρ, measuring weight – are mapped, revealing the layout of the E-ρ landscape. The dimensions of the little bubbles show the range of moduli and density of individual classes of material; the larger envelopes enclose members of a family.** Metals cluster into one part of the map, polymers into another, ceramics, woods, foams, elastomers into others. **Like maps of a more conventional kind, it condenses a large volume of information into a single, easily readable, image.**」

★★★★ **判据：属性图的三个视觉元素，每个都有确定含义 ——**
> **① 气泡（bubble）= 一个材料类（class）的属性范围**（气泡宽 = E 的范围，高 = ρ 的范围）
> **② 大包络（envelope）= 一个材料家族（family）**
> **③ 空白区 = 没有材料能到达的区域**（原文 p201：「the oceans in between that are empty」）

> **原文（p201，附录开篇 —— 属性图的哲学）**：
> 「The six charts shown here are maps of technical attributes. **They show the islands and continents, so to speak, that are occupied and the oceans in between that are empty. Parts of these oceans can be filled by making composites, sandwich structures, and other configured materials (foams, for instance) that combine the properties of two or more single materials – there is still uncharted water here. Other parts cannot be reached at all, for fundamental reasons to do with the physics of the way in which atoms are bonded in solids.**」

★★★★★ **判据：属性图上的"空白海"分两类 —— 可填的海 与 不可填的海。**
> **可填**：靠复合、夹芯、发泡等"构型化"手段（composites, sandwich structures, foams）—— **这是 M 层的创新空间**；
> **不可填**：受原子键合的物理限制—— **这是 M 层的物理天花板**。
> **判据：M 层提案时先问"这个位置上有没有材料"；若空着，再问"是物理不允许，还是还没人造"。**

---

## 4.1 六张属性图：横纵坐标、单位与读法（逐图说明）

> **原文（p201，图目录）**：
> 「Chart 1 – Elastic Modulus/Density｜Chart 2 – Strength/Density｜Chart 3 – Fracture Toughness/Elastic Modulus｜Chart 4 – Elastic Modulus/Strength｜Chart 5 – Loss Coefficient/Elastic Modulus｜Chart 6 – Thermal Expansion/Thermal Conductivity｜Chart 7 – Strength and Stiffness of Fibers」

> **原文（p201，标签缩写说明 —— 读图必须先读这段）**：
> 「Some of the labels have been shortened for the sake of space: thus, **tsPolyester is thermosetting polyester, tpPolyester is thermoplastic, and elPolyester is elastomeric; fpu is a flexible polyurethane foam, rpu is rigid foam, spu a structural foam, ocpu is open cell, and ccpu is closed cell.**」

> **★★ 判据：属性图的横纵坐标都是对数刻度，气泡是"范围"不是"点"。**
> **所以不要从图上"读出一个数值"**，只能读"在哪个数量级区间"。这与 §4.0 的"模式识别"目的一致。

---

### 4.1.1 Chart 1 — 弹性模量 E / 密度 ρ（Elastic Modulus–Density）

> **原文（p203，Chart 1 的正文说明）**：
> 「**If a solid is deformed elastically, it springs back to its original shape when released. The atoms of solids are held together by atomic bonds – think of them as little springs linking the atoms. If the springs are hard to stretch, the solid is stiff; if they are easy to stretch, the solid is compliant. Young's modulus is a measure of the stiffness or compliance of the bonds.** Metals and ceramics are stiff; polymers are much more compliant. Foams and elastomers are even more compliant, and for a new reason: **their structure allows additional deflection (cell wall bending, molecular rearrangement) which, nonetheless, is recovered when the loads on the material are released.**」

> **原文（p203，为什么 ρ 的跨度远大于 E 的跨度）**：
> 「**Interatomic spacings in materials do not vary very much: they are all within a factor of 3 of 0.3 nm (3 × 10⁻¹⁰ m). The densities of materials – the mass per unit of their volume – vary far more widely, simply because some atoms are heavy (copper, iron – and thus steel) and others are light (hydrogen, carbon – and thus polymers like polyethylene, (CH2)n).**」

> **原文（p74，图 4.4 的图注）**：
> 「**A chart of Elastic Modulus and Density for materials, showing the clustering of metals, polymers, ceramics, foams, woods, etc.** (CES Edu, 2009).」

| 项 | 内容 |
|---|---|
| **图号** | Chart 1（正文中为图 4.4） |
| **横坐标** | **Elastic Modulus, E**（弹性模量 / 杨氏模量） |
| **横坐标单位** | **GPa**（正文 p73 图 4.3 的 "El. modulus, gpa"；对数刻度） |
| **纵坐标** | **Density, ρ**（密度） |
| **纵坐标单位** | **kg/m³**（正文 p73 图 4.3 的 "Density, kg/m"；对数刻度） |
| **图的物理意义** | 「the layout of the **E-ρ landscape**」(p72)；「the "springs" linking atoms」的软硬 vs 原子的轻重 |
| **气泡含义** | 一个小气泡 = 一个材料类的 E 与 ρ 范围；大气泡包络 = 一个家族 |
| **等值线** | 本图**无斜线等值线**（Chart 1 原文未给）；斜线出现在 Chart 4 与 Chart 3 |

> **★★★ CMF 读法（本版提炼）：这张图在 CMF 里的用途是"重量感 vs 硬挺感"的定位图。**
> | 区域 | E 低 ρ 低 | E 高 ρ 高 | 对应感知 |
> |---|---|---|---|
> | 金属 | 中–高 E，高 ρ | **高密度 → "重"、"冷"、"贵"** | 与 p96「machined metal looks strong」一致 |
> | 聚合物 | 低 E，低 ρ | **低密度 → "轻"、"暖"、"廉"** | 与 p97「they feel warm – much warmer than metal or glass」一致 |
> | 陶瓷 | 高 E，中 ρ | **最硬挺 → "冷"、"脆"** | p96「Ceramics, stone, and metals are cold and hard」 |
> | 木材/软木 | 低–中 E，极低 ρ | **轻且暖** | p92「balmy and soft」 |
> | 泡沫 | 极低 E，极低 ρ | **软且暖** | p92「Polymer foams and low density woods are warm and soft」 |

> **★★★★ 判据：`E/ρ` 是"触感硬与重"的联合指标，不是单一属性。**
> 原文从未说"E 决定手感"——它说 **"softness has to do with stiffness – or, rather, to lack of stiffness"**（p221），
> 而 **"warmth" 由 √(ρλc_p) 决定**（p221）。**两个轴各管一件事，不可混。**

---

### 4.1.2 Chart 2 — 强度 σ_f / 密度 ρ（Strength–Density）

> **原文（p205，Chart 2 的正文说明）**：
> 「**Strength is different from stiffness – think of it as a measure of the force needed to break atomic bonds.** In brittle materials (glasses, ceramics) breaking means just that: the solid fractures. But in ductile materials (metals, many polymers) the bonds break, the atoms or molecules move, and new bonds form, leaving the material just as it was before, but with a new shape. **This ability to reform bonds gives ductility and thus the ability to be shaped by rolling, drawing, molding, and stretching.**」

> **原文（p205，"strength"在此图上的确切定义 —— 五个材料类各用不同定义，极重要）**：
> 「**"Strength," here, means the 0.2% offset yield strength for metals. For polymers it is the stress at which the stress-strain curve becomes markedly non-linear – typically a strain of about 1%. For ceramics and glasses, it is the compressive crushing strength; remember that this is roughly 15 times larger than the tensile fracture strength. For composites it is the tensile strength. For elastomers it is the tear strength.**」

| 项 | 内容 |
|---|---|
| **图号** | Chart 2 |
| **横坐标** | **Strength, σ_f**（强度） |
| **横坐标单位** | **MPa**（正文 p73 图 4.3 的 "Yld. strength, mpa"；对数刻度） |
| **纵坐标** | **Density, ρ**（密度） |
| **纵坐标单位** | **kg/m³**（对数刻度） |
| **各材料类的"强度"定义** | 金属 = 0.2% 屈服；聚合物 = 应力-应变曲线明显非线性处（约 1% 应变）；陶瓷/玻璃 = **抗压碎强度（约抗拉的 15 倍）**；复合材料 = 抗拉；弹性体 = 抗撕裂 |
| **配套图** | 图 7A.4「**A strength-density chart. Materials with low values of ρ/σy lie above the diagonal line, at the top left**」(p228) |

★★★★★ **判据：不同材料家族的"强度"根本不是一个东西，直接横比是错的。**
> 陶瓷取的是**抗压**（因为抗拉会被微裂纹拉垮），且**比抗拉大 15 倍**。
> **判据落地：在 Chart 2 上把陶瓷与金属横着比，会让陶瓷"看起来很强"；实际它是脆的。**
> **要判"会不会摔碎"，必须看 Chart 3（断裂韧性 K_IC），不能看 Chart 2。**

---

### 4.1.3 Chart 3 — 断裂韧性 K_IC / 弹性模量 E（Fracture Toughness–Elastic Modulus）

> **原文（p207，Chart 3 的正文说明 —— 全章最生动的一段）**：
> 「**If you nick the edge of a cellophane wrapper or scratch the surface of a plate of glass, it will crack or tear from the nick or scratch. If you do the same to copper or steel, it won't. That is because the first two have low fracture toughness, Kic, the property that measures the resistance to the propagation of a crack.** Materials with low fracture toughness are strong when they are perfect (that's why it's so difficult to get the cellophane wrapper off a new cd or packet of biscuits), **but as soon as the surface is damaged they break easily. Materials with high fracture toughness are crack tolerant; they still carry loads safely even when cracked.**」

> **原文（p207，等值线）**：
> 「**The chart shows fracture toughness, Kc, plotted against modulus e. The "toughness", G, is related to Kic by G = K²_IC/E – shown as a set of diagonal contours.**」

| 项 | 内容 |
|---|---|
| **图号** | Chart 3 |
| **横坐标** | **Elastic Modulus, E**（弹性模量） |
| **横坐标单位** | **GPa**（对数刻度） |
| **纵坐标** | **Fracture Toughness, K_IC**（断裂韧性） |
| **纵坐标单位** | **MPa·m^½**（正文 p73 图 4.3 的 "Toughness, kj/m€" 为笔误；各材料剖面的标准单位是 MPa·m½，见 p274–p300 全部剖面） |
| **等值线** | **G = K²_IC / E** 的一组斜线（"toughness" G） |
| **读法** | 等值线上 = 相同 G（相同能量吸收能力） |

★★★★★ **判据：这张图是"会不会摔碎/能不能做薄"的唯一判据图。**
> **CMF 应用：任何"跌落"、"铰链"、"薄壁"、"卡扣"的产品，M 层第一步就是看 Chart 3。**
> **原文给了配套案例（p151）**：CD 盒用 PS 会裂，替换候选物的排序指标就是 **K_IC/E（resilience）**。
> 「the measure we need is **the resilience – it measures the amount the material can be bent before it breaks**… the property used here for resilience is **K_IC/E**」(p151 与脚注 4)

> **★★★ 判据：韧性差 10 倍，在图上就是差一格；在手感上就是"这壳一按就裂"。**
> **CMF 要点：韧性是"看不见的 CMF 属性"，但它决定了外壳能有多薄，从而决定了造型语言。**

---

### 4.1.4 Chart 4 — 弹性模量 E / 强度 σ_f（Elastic Modulus–Strength）

> **原文（p209，Chart 4 的正文说明）**：
> 「**There are no new properties here. The value of the chart is that many designs depend on one or another combination of e and σf.** Thus **resilience – the ability to bend without damage (like leather) is measured by the combination σf/e, shown as one set of contours on the chart. The ability to store and return elastic energy (something rubber is good at) is measured by σ²f/e (not shown).** Materials with large values of these combinations perform well in these functions.」

| 项 | 内容 |
|---|---|
| **图号** | Chart 4 |
| **横坐标** | **Strength, σ_f**（强度） |
| **横坐标单位** | **MPa**（对数刻度） |
| **纵坐标** | **Elastic Modulus, E**（弹性模量） |
| **纵坐标单位** | **GPa**（对数刻度） |
| **等值线 ①** | **σ_f / E** = **resilience**（可弯而不坏，如皮革） |
| **等值线 ②** | **σ²_f / E** = 储存并回弹弹性能的能力（橡胶强项）—— **本图未画出，原文明确"not shown"** |

> **★★★ 判据：`σ_f/E` 大 = 能弯到很大曲率不坏（皮革、弹簧钢）；`E/σ_f` 大 = 一弯就断（玻璃）。**
> **CMF 应用：产品有没有"需要弯"的地方（卡扣、活铰、包边）？有 → 直接读 σ_f/E 等值线。**

> **原文（p222，Resilience 的另一种度量 —— 与 §4.1.3 对照会产生矛盾，须说明）**：
> 「**Resilience is the ability to accept large deflection without damage. Deflection is limited either by yield (permanent deformation) or by fracture, that is, by the more limiting of the two quantities σy/E and KIC/E.** We use the quantity **R = √(σy·KIC) / E** as a measure of resilience.」

> **★★ 判据（本版发现的一处内部张力）：**
> **p209 说 resilience 用 `σ_f/E` 度量；p222 说用 `√(σy·KIC)/E` 度量；p151 脚注 4 说 CD 盒用 `KIC/E`。**
> **三处并不一致** —— 因为"韧性"在单轴屈服主导 vs 裂纹扩展主导时是两个不同的物理机制。
> **判据：选哪个，取决于失效模式是"屈服"还是"断裂"。**
> **本书未对这处不一致作说明，本版据三段原文并列呈现，不擅自统一。**

---

### 4.1.5 Chart 5 — 损耗系数 η / 弹性模量 E（Loss Coefficient–Elastic Modulus）

> **原文（p211，Chart 5 的正文说明 —— 这张图直接对应"声音好不好听"）**：
> 「**If a hard steel ball is dropped onto the surface of a material, it bounces back. The height to which it bounces is a measure of the loss of energy in the material: the higher it bounces, the less is the loss. Low loss coefficient materials return almost all the energy of the ball so that it will bounce many times (as many as 1000) before it comes to rest. High loss materials bring the ball to rest almost immediately. Choose low loss materials for springs, vibrating reeds, strings for musical instruments, and precision suspension systems; choose high loss materials for vibration damping.**」

| 项 | 内容 |
|---|---|
| **图号** | Chart 5 |
| **横坐标** | **Elastic Modulus, E**（弹性模量） |
| **横坐标单位** | **GPa**（对数刻度） |
| **纵坐标** | **Loss Coefficient, η**（损耗系数，**无量纲**） |
| **纵坐标单位** | **无**（纯数，对数刻度） |
| **读法** | η 低 = 声音"响/清亮"；η 高 = 声音"闷/钝" |

> **原文（p94，图 4.24 的声学亮度换算）**：
> 「The frequency of sound (pitch) emitted when an object is struck **relates to two material properties: modulus and density**… **Frequency is not the only aspect of acoustic response – another has to do with damping. A highly damped material sounds dull and muffled; one with low damping rings. Acoustic brightness – the inverse of damping – is used as the other axis of 4.24.**」

> **原文（p222，声学两轴的精确定义）**：
> 「**Pitch (of Sound)**｜**Sound frequency (pitch) when an object is struck relates to the modulus, e, and density, ρ, of the material of which it is made. We use the quantity P = √(E/ρ) as a relative measure of natural vibration frequency, and thus pitch. If p is small the material's pitch is low; as p increases the material's pitch becomes higher.**」
> 「**Brightness (of Sound)**｜**Sound attenuation (damping or muffling) in a material depends on its loss coefficient, η. We use the quantity L = 1/η as a measure for ranking materials by acoustic brightness. If l is small the material sounds muffled; as l increases the material rings more.**」

★★★★★ **判据：声音的两个轴都有公式 —— 音高 P = √(E/ρ)，亮度 L = 1/η。**
> **这是 CMF 里唯一被完全公式化的感知轴。**
> **CMF 应用：要"叮"一声（金属/玻璃）→ 找 P 大（高 E/ρ）且 η 小（L 大）；
> 要"咚"一声（橡胶/泡沫）→ 找 P 小且 η 大。**
> **原文的例子（p95）**：「**Bronze, glass, and steel ring when struck … they are used to make bells; alumina, on this ranking, has the same bell-like qualities. Rubber, foams, and many polymers sound dull**…**Lead, too, is dull and low pitched; it is used to clad buildings for sound insulation.**」

---

### 4.1.6 Chart 6 — 热膨胀系数 α / 导热系数 λ（Thermal Expansion–Thermal Conductivity）

> **原文（p213，Chart 6 的正文说明 —— 含装配约束）**：
> 「**Expansion and conductivity are the two most important thermal properties of materials for product design. They vary greatly: the chart shows that metals and certain ceramics have high conductivities together with low expansion. Polymers and elastomers have conductivities that are 1000 times less, and they expand at least 10 times more. It is important to match expansion coefficients when joining different materials that will be used at high temperature; if this is not done, damaging stresses appear when the temperature is changed.** High thermal conductivity is valuable in heat exchangers and heat sinks, and when a uniform temperature is required (as in a cooking vessel). Low conductivity is valuable when the aim is to insulate against heat.」

| 项 | 内容 |
|---|---|
| **图号** | Chart 6 |
| **横坐标** | **Thermal Conductivity, λ**（导热系数） |
| **横坐标单位** | **W/m·K**（正文 p73 图 4.3 的 "Th. conductivity, w/m.c"；对数刻度） |
| **纵坐标** | **Thermal Expansion Coefficient, α**（热膨胀系数） |
| **纵坐标单位** | **10⁻⁶/K**（正文 p73 图 4.3 的 "Th. expansion, /c. 10-fl"；对数刻度） |
| **物理规律** | 金属/部分陶瓷：**高 λ + 低 α**；聚合物/弹性体：**λ 小 1000 倍、α 大至少 10 倍** |
| **装配约束** | 异种材料接合时**必须匹配 α**，否则温度变化产生破坏性应力 |

★★★★★ **判据：异种材料接合的第一条物理约束是 α 匹配，不是粘接强度。**
> **CMF 应用：任何"塑料壳 + 金属饰件"、"玻璃 + 金属框"的设计，先查 Chart 6 上两者 α 差多少倍。**
> **原文给了量级：聚合物 α 是金属/陶瓷的 10 倍以上，λ 只有 1/1000。**

> **原文（p221，触感冷暖的公式 —— Chart 6 与 Chart 2 之 §2.5 的连接点）**：
> 「**Warmth (to the Touch)**｜A material feels "cold" to touch if it conducts heat away from the finger quickly; it is "warm" if it does not. … **The quantity of heat that has left each unit area of finger in time t is Q = x·ρ·cp = √(ρ·λ·cp)·√t. If Q is small the material feels warm; if large, it feels cold. Thus √(ρλcp) is a measure of the "coldness" of the material. Softness and Warmth are used as the axes of 4.22.**」

> **原文（p221，触感软硬的公式）**：
> 「**Softness (to the Touch)**｜Hardness is resistance to indentation and scratching. It is directly related to the material property of hardness h. Softness has to do with stiffness – or, rather, to lack of stiffness. The stiffness of a material in a given shape is proportional to its modulus e. … **One that works here is the measure S = E·H. If s is small, the material feels soft; as s increases it feels harder.**」（注：原文此处表达式排版为 "S = EH"，符号 e 与 E 混用）

★★★★★ **判据：触感的两条公式，全在附录里，主文没写 ——**
> **① 冷热度 = √(ρ·λ·c_p)**（密度 × 导热 × 比热，三者之积的平方根）
> **② 软硬度 = E·H**（模量 × 硬度）
> **判定方向：Q 小 = 暖；Q 大 = 冷。S 小 = 软；S 大 = 硬。**
> **CMF 应用：这是"摸起来什么感觉"唯一的定量入口。要更暖 → 降 ρ、降 λ、降 c_p 任一项。**

---

### 4.1.7 Chart 7 — 纤维的强度与刚度（Strength and Stiffness of Fibers）

> **原文（p215，Chart 7 的正文说明）**：
> 「**Fibers play a key role in design. They are matted into felt and paper, spun into thread and rope, and woven into cloth. Many have exceptionally high strength and stiffness, exploited in fiber-reinforced composites. Man-made fibers include glass, carbon, and Kevlar (aramid). Natural fibers, derived from plants and animals, include coir (from coconut husks), cotton, flax, hemp, jute, kenaf, ramie, sisal, and wool. This chart shows their tensile strength and modulus. Man-made fibers are stiffer and stronger than those of nature, but they are also heavier. When strength and stiffness per unit weight are important, natural fibers compete with those made by man.**」

| 项 | 内容 |
|---|---|
| **图号** | Chart 7 |
| **横坐标** | 纤维的 **Tensile Strength**（抗拉强度）—— 单位 **MPa** |
| **纵坐标** | 纤维的 **Modulus**（模量）—— 单位 **GPa** |
| **读法** | 天然纤维 vs 人造纤维：人造更硬更强但**更重**；**比强度/比刚度**上天然纤维有竞争力 |

> **★★ 判据：这张图的横纵坐标原文未在主文重复写出（只写 "This chart shows their tensile strength and modulus"）。**
> **单位由前六图的体例（MPa / GPa）与本书记载纤维属性的数值区间推定，标注为"依体例推定"，不作原文引用。**

---

## 4.2 多变量图：MDS（Multi-Dimensional Scaling）

> **原文（p73）**：
> 「So visual presentation of data can reveal similarities that are hard to see in other ways. And that makes you wonder if you could go one step further and, **instead of mapping many separate pairs of attributes, find a way of combining them all to make a single super-map – a global overview.** Well, yes and no. … **It is called multi-dimensional scaling, or mds.**」

> **原文（p73，MDS 的算法直觉）**：
> 「**First, calculate the "distance" between each material and every other in the group, taken in pairs. "Distance" is a measure of dissimilarity: if all the attributes of two materials are identical, the distance between them is zero. If all but one are identical, and the odd one out differs by 10 units, the distance might be given the value 10.** If all are different, and by varying degrees, each difference is given a value and all the values are aggregated to give a single number: **this is the overall "distance" between the two materials.** The output of this step is a table, showing the distances between each material and every other.」

> **原文（p75，MDS 的"拉伸-挤压"算法）**：
> 「But now add a fourth material. In general, you can't find a place where it exactly fits … **But suppose you could stretch some of the distances and squeeze others, you could go on doing so until there was a position in which the fourth material would fit – although the map is now distorted, an approximation, no longer an exact visualization of the distances.** … **if you had an algorithm that minimized, at each step, the total stretch and squeeze, you could keep the distortion to a minimum. And that is exactly what multi-dimensional scaling does.**」

> **原文（p75，MDS 的三个警告 —— 必须照引）**：
> 「**The maps that emerge have to be interpreted with caution – they are approximations. The "distance" measure on which they depend rolls many attributes into a single number; and in doing so it throws away a great deal of information ("does a distance of 20 mean that all attributes differed a little, or that most were identical and one was very different?").** But the method does produce interesting pictures, in which clustering is clearly evident.」

> **原文（p75，图 4.5）**：
> 「Figure 4.5 is an example. **It is an MDS map for engineering materials based on 15 of their mechanical and thermal attributes.** Ceramics, metals, and polymers each fall into separate groups; and within polymers, thermoplastics and elastomers form overlapping groups. **The analysis has led to groupings that in most ways resemble the families and classes of material science.**」

**图 4.5 Multi-Dimensional Maps: Mechanical Attributes** —— This map shows similarity between materials based on their mechanical attributes (Data from CES Edu, 2009).

> **原文（p95，图 4.25 美学属性的 MDS —— C/M/F 的联合图）**：
> 「What happens if all these are combined? **Figure 4.25 shows the result. It is an mds map combining the attributes we have just described. As with the earlier mds map, there is pronounced clustering of a kind that is broadly consistent with experience – leather is near pvc, ceramics near metals, woods near phenolics. The map should not be overinterpreted, for the reasons given already; but it does have the power of suggestion.**」

**图 4.25 Multi-Dimensional Maps: Aesthetic Attributes** —— An MDS map of materials by aesthetic attributes (Data from CES Edu, 2009).

> **原文（p93 脚注 5，MDS 的任意性 —— 照引）**：
> 「Many arbitrary decisions are involved. "Distance" can be measured and aggregated in more than one way. An example: **normalize all data to a set range - say -10 to 10 – calculate the individual distances for each attribute of a material, then aggregate by forming the root-mean-square of these (Euclidean aggregation).** Minimizing the stretch and squeeze, too, allows many alternatives. … **If you want to use the method, read Kruskal and Wish (1987) first.**」

★★★★★ **判据：MDS 图是"启发式"，不是"判据式"。**
> 原文自己给了三重免责：
> **① 是近似（approximation）**；
> **② 距离把多属性压成一个数，丢掉了大量信息**；
> **③ 聚合方式有任意性（归一化区间、欧氏聚合、拉伸最小化目标都可换）**。
> **判据落地：MDS 图只能用于"这批材料像不像"，绝不能用于"该选哪一个"。**
> **判断"选哪个"必须回到 Chart 1–6 的两两属性图 + 材料指数。**

---

## 4.3 材料指数（Material Index）：从"属性"到"指标"

> **原文（p226，材料指数的定义 —— 全书最精确的一句）**：
> 「**Everything here is specified except the term in the square brackets – and it depends only on the choice of material. The mass is minimized (and performance maximized) by choosing materials with the smallest value of ρ/σy, which is called a material index.**」

> **原文（p226，材料指数的普适性）**：
> 「**Each combination of function, objective, and constraint leads to a performance metric containing a group of material properties or material index; the index is characteristic of the combination.** Table 7A.3 lists some of these; their derivation is detailed in the companion text. **The point of interest here is that materials with extreme values of certain indices are well suited to meet certain sets of design requirements.**」

> **原文（p226，换材料的性能增益公式）**：
> 「**Indices allow comparisons. If the spoke is at present made from a reference material Mo and has a mass mo, a competing material m1 with mass m1 will be lighter than mo, for the same load-carrying capacity, by the factor m1/m0 = (ρ1/σy1)/(ρ0/σy0), giving a direct measure of the gain in performance achieved from switching from mo to m1.**」

**表 7A.3 Material Indices（p227，全表照录）**
> 「When you want to optimize material choice to meet purely technical requirements, indices act as a guide.」（ρ = density; e = Young's modulus; σy = elastic limit）

| Function | Objective | 场景（原文案例） | **Minimize index** |
|---|---|---|---|
| **Tie**, minimum weight, stiffness prescribed | 最小重量 | Cable support of a lightweight tensile structure | **ρ/E** |
| **Beam**, minimum weight, stiffness prescribed | 最小重量 | Aircraft wing spar, golf club shaft | **ρ/E^½** |
| **Beam**, minimum weight, strength prescribed | 最小重量 | Suspension arm of automobile | **ρ/σ_y^(2/3)** |
| **Panel**, minimum weight, stiffness prescribed | 最小重量 | Automobile door panel | **ρ/E^(1/3)** |
| **Panel**, minimum weight, strength prescribed | 最小重量 | Table top | **ρ/σ_y^(1/2)** |
| **Column**, minimum weight, buckling load prescribed | 最小重量 | Push-rod of aircraft hydraulic system | **ρ/E^½** |
| **Spring**, minimum weight for given energy storage | 最小重量 | Return springs in space applications | **E·ρ/σ_y²** |
| **Natural hinge**, maximum distortion, flexure without failure | 最大变形 | Inexpensive hinges | **E/σ_y** |

★★★★★ **判据：材料指数是"功能 + 目标 + 约束"的三元组函数，不是属性本身。**
> **原文的措辞：`Each combination of function, objective, and constraint leads to ... a material index`。**
> **判据落地（CMF 版）：**
> **同一个材料，在"梁要轻且刚"里指数是 ρ/E^½，在"板要轻且刚"里变成 ρ/E^(1/3)，在"活铰要能弯"里变成 E/σ_y。**
> **所以"这个材料好不好"这句话没有意义 —— 必须说"对哪个功能、哪个目标、哪个约束"。**

> **★★★ 判据：`E/σ_y` 小的材料适合做"活铰（natural hinge）"（p227 最后一行）。**
> 这条对 CMF 极其实用：**PP 活铰（living hinge）正是靠低 E/σ_y。**
> 也解释了为什么 p152 建议 CD 盒改用 **PVC 的 living hinge** —— 它在 E/σ_y 上合适。

---

## 4.4 选材四步：Ashby 的原始措辞

> **原文（p141，Selection by Analysis 的四步 —— 这是全书对"选材流程"最权威的表述，逐字照录）**：
> 「Technical engineers are trained in analysis – it is one of the tools of the trade. The inputs here are the technical requirements. **The analysis proceeds in four steps.**
> **• Translation of the requirements, often expressed initially in non-technical terms, into a statement of the objectives and constraints the design must meet.**
> **• Analysis of the component for which a material is sought, identifying performance metrics and expressing these as equations that measure performance.**
> **• Identification, from these equations, of the material properties that determine performance.**
> **• Screening of a database of materials and their properties, eliminating those that fail to meet the constraints, and ranking those that remain by their ability to maximize the performance metrics.**」

> **★★★ 重要声明（本版必须诚实交代）**：
> **本书的原文四步是：`Translation → Analysis → Identification → Screening + Ranking`。**
> **流行说法里的简写 `translate → screen → rank → document` 在本书中并不存在** ——
> 全库 grep `document` 无一条与选材步骤相关；"Translation" 是第一步，但 "screen" 只出现在第四步的 "Screening"，而后两步（identification/ranking）被并进了第四步。
> **本技能以 p141 原文四步为准，并在 §4.9 的空白表里注明"document（记录成档）这一步本书未单列"。**

> **原文（p141，四步的实例：自行车辐条，图 7.4）**：
> 「Thus – to take a simple example – **the choice of a material for the spoke of a lightweight bicycle wheel might proceed in the way shown in 7.4. The first three design requirements impose limits on material attributes, screening out unsuitable candidates. Those that remain are ranked by the fourth requirement – that of strength at minimum mass (here mass is the metric of performance).** This must be balanced against cost, using trade-off methods.」

**图 7.4 Technical Analysis for a Bicycle Spoke** —— 表格照录：

| Inputs | Path to Material Selection |
|---|---|
| Impact resistant | Fracture toughness, **kic > 20 mpa.mH** |
| Corrosion resistant | No materials that corrode in water |
| Available as rod | None that cannot be extruded or drawn |
| Light and withstand design load | **Rank by ratio of strength to density** |

> 图注原文：「**Constraints, listed in the top three lines, allow screening, eliminating materials incapable of providing the function. The objective of minimizing mass allows those that survive to be ranked.**」

★★★★★ **判据：四步的实操形态，是"三行约束做筛，一行目标做排"。**
> **约束（constraint）= 二值判断（能/不能）** → 剔除
> **目标（objective）= 连续排序（好/更好）** → 排队
> **判据落地：CMF 约束表必须把每条约束写成二值形式**（"能过 FDA" / "不能"），
> **不能写"食品安全性好"** —— 那不是约束，是形容词。

> **原文（p141，分析法的三个强项与一个致命弱项）**：
> 「**The method of analysis has great strengths. It is systematic. It is based on a deep ("fundamental") understanding of the underlying phenomena. And it is robust – provided the inputs are precisely defined and the rules on which the modeling is based are sound. This last provision, however, is a serious one. It limits the approach to a subset of well-specified problems and well-established rules.**」
> 「In engineering, as in all other aspects of life, it is sometimes necessary to base decisions on imprecisely specified inputs and imperfectly formulated rules. **Then the analytical method breaks down; methods of a different sort are needed.**」

> **原文（p142）**：
> 「**Synthesis has its foundations in previous experience and analogy.** Here the inputs are design requirements expressed as a set of features describing intentions, aesthetics, and perceptions. **The path to material selection exploits knowledge of other solved problems ("product cases") that have one or more features in common with the new problem, allowing new, potential solutions to be synthesized and tested** for their ability to meet the design requirements.」

★★★★ **判据：分析法在"输入不精确"时失效 —— 而 CMF 的输入（美学/感知）天然不精确。**
> **这就是为什么本技能的 M 层流程是"分析 + 合成"并用，而不是纯分析。**
> 原文给了完整的四法（by analysis / synthesis / similarity / inspiration），见 ch07。

---

## 4.5 附录里的分析框架：Function / Objective / Constraint / Free Variable

> **原文（p225）**：
> 「**Any engineering component has one or more functions: to support load, to contain a pressure, to transmit heat, and so forth. In designing the component, the designer has an objective: to make it as cheap as possible, perhaps, or as light, or as safe, or some combination of these. This must be achieved subject to constraints: that certain dimensions are fixed, that the component must carry a given load or pressure without failure, that it can function safely in a certain range of temperature, and in a given environment, and many more.** Function, objectives, and constraints (7A.1) define the boundary conditions for selecting a material and – in the case of load-bearing components – **a shape for its cross-section.**」

**图 7A.1 Details of Analysis** —— 四问照录：

| 项 | 原文问句 |
|---|---|
| **Function** | **What does a component do?** |
| **Objective** | **What is it to be maximized or minimized?** |
| **Constraints** | **What non-negotiable conditions must be met?** |
| **Free Variables** | **Which control variables are we free to adjust?** |

> **原文（p225，目标函数的写法）**：
> 「**The performance of the component, measured by performance metrics, p, depends on control variables.** The control variables include the dimensions of the component, the mechanical, thermal, and electrical loads it must carry, and the properties of the material from which it is made. **Performance is described in terms of the control variables by one or more objective functions.** An objective function is an equation describing a performance metric, p, expressed such that **performance is inversely related to its value, requiring that a minimum be sought for p.**」
> 「**P = f[(Loads, F), (Geometry, G), (Material, M)]**」
> 「**Optimum design is the selection of the material and geometry which minimize a given performance metric, p. Multi-objective optimization is a procedure for simultaneously optimizing several interdependent performance metrics, p, q, r.**」

★★★★★ **判据：所有目标函数都被写成"求最小值"的形式（原文：`performance is inversely related to its value, requiring that a minimum be sought`）。**
> **CMF 含义：任何"要最大化"的目标必须先取倒数。** 比如"要最耐久" → 写成"最小化失效速率"。
> **这不是数学洁癖，而是因为"约束"和"目标"必须能用同一种语言比较。**

> **原文（p229，多目标优化与 trade-off 面）**：
> 「Greater discrimination is possible by plotting trade-off diagrams of which 7A.5 is a simple example. **Here the material group ρ/σy is plotted on the vertical axis, and material cost/kg on the horizontal one. The plot allows materials to be compared on the basis both of performance and of cost. The most attractive candidates lie on or near the trade-off surface (solid line); these offer both low mass and low cost.**」

**图 7A.5 Trade-Off Analysis** —— 「**Here a compromise is sought between minimizing weight and cost. The materials at or near the trade-off surface are the candidates; the final decision depends on how much each attribute is valued** (ces Edu, 2009).」

★★★★ **判据：trade-off 面（折衷面）上的材料才是候选；面外的看都不用看。**
> **CMF 应用：CMF 的常见 trade-off 面是"外观等级 vs 单位成本"。**
> **判据：把候选工艺画在"光泽等级（p82 六级）vs 成本"上，面上的才是可选的。**

---

## 4.6 价格：图上没有的那一维

> **原文（p148，办公室家具案例 —— 价格如何进入选材）**：
> 「**A light, stiff frame, loaded in bending (as this frame is) is best made of a material with a low value of ρ/E^1/2 (see Appendix) where ρ is the material density and E its modulus.** This group of properties characterizes the weight of the frame. **Cost, obviously, is a consideration. The material index ρ/E^1/2 is plotted against material price/kg in 7.12, on to which a trade-off surface has been sketched. Materials on or near this surface offer the best combination of low weight and low cost.**」

> **原文（p148–p149，案例的结论 —— 一条真实的 CMF 决策链）**：
> 「**The incumbent material – carbon steel – is marked. It is low in cost but it is also relatively heavy. Aluminum alloys, easily extruded to square section tube, are more expensive, but considerably lighter. Magnesium alloys allow a further reduction in weight, but at a considerable increase in price. Lighter still are gfrp and, particularly, cfrp – but cfrp is expensive.**」
> 「**The first three of these are mass-produced products that command substantial market; they boost confidence that 6000 series aluminum holds no unpleasant surprises, and point to ways in which they can be joined (welding and adhesives) and finished (powder coated). This would be the safe choice – one already used in other, similar, designs. The small additional weight saving offered by the aluminum matrix composites does not justify its cost.**」

★★★★★ **判据：真实选材的胜负手常常不在"最优"，而在"已有人用过，所以没有意外"。**
> 原文对 6000 系铝判词是：**"boost confidence … holds no unpleasant surprises"** + **"the safe choice"**。
> **CMF 含义：材料替换的最大阻力不是性能，是"未知的失效模式"。**
> **判据：M 层提案必须回答"这个材料在别人产品上用过没有？用在哪？用了多久？"**

---

## 4.7 "形状"：本书能支持到什么程度

> **原文（p225，唯一一处明确说"形状"的位置）**：
> 「Function, objectives, and constraints (7A.1) define the boundary conditions for selecting a material and – **in the case of load-bearing components – a shape for its cross-section.**」

> **原文（p226，截面作为自由变量）**：
> 「The inputs to the model … are the cross-sectional area, A and the choice of material. … **The length l is given but the section a is free; reducing it reduces the mass. But if it is reduced too far it will no longer carry the load f and this constrains the section.**」

> **原文（p121，空心管效应 —— 本书对"形状换性能"唯一给出的量化例证）**：
> 「Early bicycles had a solid hickory frame joined by adhesives – they were light but not very durable. **Solid steel is 10 times denser than wood, but shaped into a hollow tube and joined by brazing it is as light as wood for the same stiffness and strength** (form 1 of 6.13).」

> **原文（p126，材料刚性差 → 截面必须变大 → 外观变笨 —— 这是"形状与 CMF 互相绑架"的原文证据）**：
> 「Form 3 uses injection molding to integrate parts into a single unit; here both the frame and wheels are single nylon moldings. Made in large numbers, moldings can be cheap, and nylon, unlike steel, does not rust. **There is, however, a problem: nylon, even when filled, is more that 50 times less stiff and 10 times less strong than high strength steel, requiring that the cross-sections have to be larger. The chunky, heavy appearance of a polymer bicycle is the result; it looks clumsy – an unfortunate personality for a bicycle.**」

> **原文（p127，工艺反过来决定截面形状）**：
> 「If not injection molding, why not die-casting? Magnesium is light and easy to die-cast. **But tubes can't be die-cast; an I-section of equivalent stiffness can. Form 4 is the result – a form dictated by the choice of process and material.**」

★★★★★ **判据：本书用"材料 → 截面 → 外观"三段论替代了"形状因子"。**
> **① 材料模量低 50 倍 → ② 截面必须大 → ③ 外观"笨重 clumsy" → ④ 感知"unfortunate personality"**
> **这条链的终点是感知，起点是模量 —— 这就是 CMF 中 M 与 C/F 的因果链原文版本。**
> **判据落地：选低模量材料（PP/PE/尼龙）时，必须预算"截面必定变粗"的外观代价；**
> **选高模量材料（金属/CFRP）时，可以换来"纤细"这一视觉资产。**

---

## 4.8 本章概念-论点表（共 26 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | **视觉优于文本** | 「**The brain is better at pattern recognition when the input is visual rather than text-based**」 | 图 4.4 | 评审拿图不拿表 | p72 |
| 2 | **气泡与包络** | 「**The dimensions of the little bubbles show the range** … **the larger envelopes enclose members of a family**」 | 图 4.4 | 气泡是范围，不能读单值 | p72 |
| 3 | **空白海分两类** | 可填（复合/夹芯/泡沫）vs 不可填（原子键合物物理） | 图 201 | 提案先问"物理不允许还是还没人造" | p201 |
| 4 | **E–ρ 图（Chart 1）** | 「the **E-ρ landscape**」 | 图 4.4 | 重量感 vs 硬挺感的定位图 | p72 / p203 |
| 5 | **原子间距变化小、密度变化大** | 「all within a factor of 3 of 0.3 nm」vs "densities … vary far more widely" | Cu/Fe vs PE | 密度的跨度是 E 的十倍级 | p203 |
| 6 | **强度非刚度** | 「**Strength is different from stiffness – think of it as a measure of the force needed to break atomic bonds**」 | 玻璃 vs 铜 | 别用强度代替韧性 | p205 |
| 7 | **五个家族"强度"定义不同** | 金属 0.2% 屈服；陶瓷 = **抗压碎强度（抗拉的 15 倍）** | Chart 2 | 陶瓷横比会"看起来很强" | p205 |
| 8 | **K_IC 是抗裂纹扩展** | 「**the property that measures the resistance to the propagation of a crack**」 | 玻璃纸 vs 铜 | 跌落/薄壁/卡扣先看 Chart 3 | p207 |
| 9 | **G = K²_IC/E 等值线** | 「shown as a set of diagonal contours」 | Chart 3 | 同 G = 同吸能能力 | p207 |
| 10 | **σ_f/E = resilience** | 「resilience – the ability to bend without damage (like leather) is measured by **σf/e**」 | Chart 4 | 要能弯 → 读这条等值线 | p209 |
| 11 | **σ²_f/E = 弹性能储存** | 「The ability to store and return elastic energy (something rubber is good at) is measured by **σ²f/e (not shown)**」 | 橡胶 | 本图未画 | p209 |
| 12 | **resilience 三处定义不一** | p209 `σ_f/E`；p222 `√(σy·KIC)/E`；p151 `KIC/E` | CD 盒 | 按失效模式（屈服 vs 断裂）选 | p209 / p222 / p151 |
| 13 | **η 低 = 响，η 高 = 闷** | 「**Low loss coefficient materials return almost all the energy of the ball** … as many as 1000 bounces」 | Chart 5 | 音色选材的第一轴 | p211 |
| 14 | **音高 P = √(E/ρ)** | 「**We use the quantity P = √(E/ρ) as a relative measure of natural vibration frequency, and thus pitch**」 | 钟/锣 | 声音被公式化了 | p222 |
| 15 | **亮度 L = 1/η** | 「**We use the quantity L = 1/η as a measure for ranking materials by acoustic brightness**」 | 铃 vs 泡沫 | 声音第二轴也被公式化 | p222 |
| 16 | **异材接合必须匹配 α** | 「**It is important to match expansion coefficients when joining different materials**」 | Chart 6 | 塑+金、玻+金的第一约束 | p213 |
| 17 | **冷热度 √(ρλc_p)** | 「**Thus √(ρλcp) is a measure of the "coldness" of the material**」 | 图 4.22 两轴之一 | 要暖 → 降 ρ/λ/c_p | p221 |
| 18 | **软硬度 E·H** | 「**One that works here is the measure S = E·H. If s is small, the material feels soft**」 | 图 4.22 另一轴 | 要软 → 降模量或硬度 | p221 |
| 19 | **MDS 可做超图** | 「**instead of mapping many separate pairs … make a single super-map – a global overview**」 | 图 4.5 | 15 个力学热学属性压成两维 | p73 |
| 20 | **MDS 三重免责** | 「**they are approximations**」「**throws away a great deal of information**」「aggregated in more than one way」 | 图 4.5 / 脚注 5 | 只能看"像不像"，不能定"选哪个" | p75 / p93 |
| 21 | **美学属性 MDS** | 「**leather is near pvc, ceramics near metals, woods near phenolics**」 | 图 4.25 | C/M/F 的联合定位图 | p95 |
| 22 | **材料指数的定义** | 「**choosing materials with the smallest value of ρ/σy, which is called a material index**」 | 辐条 | 指数 = 功能+目标+约束的产物 | p226 |
| 23 | **指数是三元组的函数** | 「**Each combination of function, objective, and constraint leads to a performance metric containing a group of material properties or material index**」 | 表 7A.3 八行 | 同一材料在不同场景指数不同 | p226 |
| 24 | **选材四步（原文）** | Translation → Analysis → Identification → **Screening + Ranking** | 辐条图 7.4 | **不是 translate-screen-rank-document** | p141 |
| 25 | **约束二值 / 目标连续** | 「**Constraints, listed in the top three lines, allow screening** … **the objective of minimizing mass allows those that survive to be ranked**」 | 图 7.4 | 约束写成能/不能 | p140–141 |
| 26 | **安全选择压过最优** | 「**holds no unpleasant surprises**」「**This would be the safe choice**」 | 6000 系铝 | 阻力来自未知失效，不是性能 | p150 |

---

## 4.9 本章的空白（M 层"筛"环节的诚实边界）

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **★ 形状因子（shape factor φ）** | **全书 0 命中。** grep `shape factor` / `shape efficiency` / `shape parameter` 全部为空。本书只有 p225「a **shape for its cross-section**」与 p226「the section a is free」两处提及"截面形状"，**从未给出形状因子的定义、符号或数值** | **Ashby《Materials Selection in Mechanical Design》**（本书 p160 Further Reading 明确指向它：「presenting **a large number of material property charts**」）；本技能只在 §4.7 用原文的"空心管 vs 实心"与"模量低→截面大"替代 |
| **选材流程的"document（成档）"一步** | **原文四步止于 Screening + Ranking，无独立的记录/成档步骤。** 全文无 "document the selection" 类表述 | 本技能 `patterns.md` P-02（CMF 选材档案模板，本版补）；ISO 9001 设计记录要求 |
| **材料属性的"感知"量化阈值** | 只有属性轴与公式（P、L、√(ρλc_p)、E·H），**没有"多少算冷""多少算暖"的绝对刻度**。图 4.22 是相对排序图 | 本技能 ch05 §5.4（感知词对量表） |
| **Chart 7 的坐标轴与单位** | 原文只写 "**This chart shows their tensile strength and modulus**"，**未复述坐标轴与单位** | 依 Chart 1–6 体例推定（MPa / GPa），已在 §4.1.7 标注"依体例推定" |
| **六张图的原始数值表** | 六张图**全是图像，正文未给点数据**。唯一有数值的是各材料剖面（p274–p300，共 40 余种材料的属性区间） | 本技能 ch04 只用区间；精确值见原书 p274–p300 各剖面表 |
| **MDS 的软件与参数** | 只说「constructed using the ces Edu (2009) software」(p201)，**无参数、无归一化设定、无距离度量选择** | Kruskal & Wish (1987)（原文 p93 脚注 5 与 p104 均指定此书） |
| **价格数据** | **六张 Chart 全部不含价格轴**。价格只出现在 trade-off 图（7.12 / 7A.5）与材料剖面表里 | 原书 p148（7.12）、p229（7A.5）、p274–p300 各剖面的 "Price, $/kg" 行 |
| **"约束冲突时怎么排优先级"** | 只说 multi-objective optimization 是"同时优化多个互相依赖的指标"(p225)，**未给权重法、未给 Pareto 前沿的具体构造** | 本技能 ch07 §7.2；多目标优化教材 |
| **复合材料的属性图读法** | p73 只说「adding glass fibers to the nylon gives a material with stiffness and density that **lies somewhere in between**」，**未给混合法则（rule of mixtures）公式** | 复合材料教材；本技能 ch04 §4.5 只作定性陈述 |

> **★ 未读到声明**：
> - 正文段 **p69–p78 全部 10 页已逐页读**；
> - 附录段 **p201–p230 全部 30 页已逐页读**（含 p202/p204/p206/p208/p210/p212/p214/p216 这 8 页**纯图页**——这 8 页在文本文件中只有页码、无正文，已在 §4.1 各表中以图注方式还原其标题与坐标）；
> - **p224 为纯图页**（无文字），p223 为 Resilience 定义页，均已读。

---

## 4.10 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 属性图 = 模式识别 | 本技能 ch07 §7.1 | 第 7 章把"图"升级为"索引结构" |
| Chart 3（K_IC）决定薄壁与跌落 | `product-structure-liubaoshun` 壳体壁厚章节 | **接口**：该书给壁厚准则，本章给"壁厚下限由韧性决定" |
| Chart 6（α 匹配） | `product-structure-liubaoshun` 连接与固定 | **接口**：异材固定（金属嵌件入塑料）的热应力 |
| 触感两公式（√(ρλc_p)、E·H） | 本技能 ch05 §5.3 | 第 5 章把公式变成"手感坐标图" |
| 材料指数 ρ/E^½ 等八项 | 本技能 ch07 §7.3 | 第 7 章把指数嵌到产品场景里 |
| 选材四步（Translation → … → Ranking） | 本技能 ch07 §7.1 | 第 7 章把四步接到 CMF 的完整流程 |
| 安全选择压过最优（6000 系铝） | `product-injection-defects` 全书的"已知缺陷 → 已知对策"逻辑 | **同构**：两者都用"已见过的失效"做决策，而非理论最优 |
| 模量低→截面大→外观笨（p126） | `product-design-styling-dabbs` ch03 比例、ch07 体积 | **同构**：Dabbs 讲"视觉分离度"，本章讲"为什么塑料件看起来笨" |
| 材料指数的"求最小值"约定 | `design-methodology-liuguanzong` 有限理性 | **互补**：柳讲"约束下的合理"，本章讲"约束怎么写成不等式" |
