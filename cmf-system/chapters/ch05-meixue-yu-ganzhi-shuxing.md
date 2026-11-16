# 第 5 章：技术属性 vs 感知属性 —— 美学量化的全部方法

> **原书 PDF 页序 p91–p105、p221–p224（共 19 页）**｜**本版逐页读完全部 19 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）
>
> **读法说明**：本章把原书两处合成一章读 ——
> **① 正文 p91–p105（4.21 Reaching the Senses → 4.29 Resilience and Stiffness）**
> **② 附录 p221–p224（Modeling Aesthetic Attributes，五个量化式）**
> 主文讲故事，附录给公式。**不读附录，主文里"它们可以被量化"这句话就是空话。**
>
> **本章在 CMF 三层流程中的位置**：**C 与 F 的"感知层"**，也是本技能与"工程选材"的分界线。
> **本章回答：凭什么说"这个材料摸起来暖"是可判据的，而不是主观偏好？**

---

## 5.0 本章的核心命题：美学能不能量化

> **原文（p91，命题的提出）**：
> 「**Aesthetic attributes are those that relate to the senses: sight, touch, sound, smell, and taste (4.21). We will focus on the first three in this chapter, although it can certainly be equally necessary and inspiring to consider the last two – smell and taste.**」

> **原文（p91，为什么要认真对待"冷/暖"这种说法）**：
> 「**Almost everyone would agree that metals feel "cold"; that cork feels "warm"; that a wine glass, when struck, "rings"; that a pewter mug sounds "dull", even "dead". From a distance, a plastic drinking glass can be visually indistinguishable from one made of glass, but pick it up and it feels lighter, warmer, less rigid; and tap it and it sounds quite different. The impression it leaves is so different from glass that, in an expensive restaurant, it would be completely unacceptable.**」

★★★★★ **判据：美学差异的"致命性"不在视觉，在触觉与听觉的联合。**
> 原文的例子是**餐厅里的塑料杯**：远处看与玻璃杯分不出，**拿起来 + 敲一下，就完全不可接受**。
> **判据落地：CMF 验证不能只做"看样"，必须做"摸样"与"敲样"。**
> **一个只在视觉上通过的 CMF 方案，在高端场景里等于没通过。**

> **原文（p91，量化提案的自我限定 —— 必须照引）**：
> 「**These are the simplest of aesthetic distinctions, and, in an approximate way, they can be quantified. There are obvious limitations here, but within these it is worth a try, since it could allow a first-level screening of materials to meet specified aesthetic requirements. So here goes.**」

> **★★★ 判据：作者自己把目标设为"first-level screening（第一层筛选）"，不是"精确预测"。**
> **这是一个诚实的定位，也是本技能引用它的边界：**
> **它能做"把 100 种材料筛到 10 种"，不能做"从 10 种里选 1 种"。后者必须打样。**

---

## 5.1 五个感官的属性词表（图 4.21）

> **原文（p91，图 4.21 的图注）**：
> 「**4.21 Reaching the Senses** —— **The tactile, visual, acoustic attributes of materials**」

**图 4.21 Reaching the Senses（全表照录）**

| Sense | Attribute |
|---|---|
| **Touch** | Warm / Cold ｜ Soft / Hard ｜ Flexible / Stiff |
| **Sight** | Optically clear / Transparent / Translucent / Opaque ｜ Reflective / Glossy / Matte / Textured |
| **Hearing** | Muffled / Dull / Sharp / Resonant / Ringing ｜ Low pitched / High pitched |
| **Taste/Smell** | Bitter / Sweet |

★★★★★ **判据：这是全书唯一的"感官属性词表"，只有 4 个感官、共 20 个词。**
> **Touch（3 对）**：暖/冷、软/硬、柔/刚
> **Sight（8 个，非成对）**：光学清晰 / 透明 / 半透 / 不透 ｜ 反射 / 光泽 / 哑光 / 纹理
> **Hearing（2 组）**：闷·钝·尖·共鸣·响 ｜ 低音高 / 高音高
> **Taste/Smell（1 对）**：苦 / 甜
>
> **判据落地：CMF 目标词的来源就在这张表。任何 CMF 提案里的形容词，都必须能映射到这 20 个词之一，否则不可沟通。**
> 注意原文的 Sight 词表**不分对**——因为"透明"与"反射"是两个独立维（玻璃既透明又反射）。

> **★★ 判据：本书把"味觉/嗅觉"列进来了，但明确"本章只讲前三个"。**
> 原文的措辞是"it can certainly be equally necessary and inspiring to consider the last two"（p91）。
> **CMF 应用：气味是真实存在的 CMF 维度（p15 提到「the sweet smell of molded bioplastics」），但本书没展开。见 §5.7 空白。**

---

## 5.2 触觉（Touch）：两个轴的完整推导

### 5.2.1 软 / 硬

> **原文（p91）**：
> 「**Steel is "hard"; so is glass; diamond is harder than either of them. Hard materials do not scratch easily; indeed they can be used to scratch other materials. They generally accept the high polish, resist distortion, and are durable. The impression that a material is hard is directly related to the material property "Hardness," measured by materials engineers and tabulated in handbooks. Here is an example of a sensory attribute that relates directly to a technical one.**」

> **原文（p91，"软"不是"硬"的反面 —— 本书最反直觉的一段）**：
> 「**"Soft" sounds like the opposite of "hard" but, in engineering terms, it is not – there is no engineering property called "softness". A soft material deflects when handled, it gives a little, it is squashy, but when it is released it returns to its original shape. This is elastic (or viscoelastic) behavior, and the material property that has the most influence on it is the modulus, not the hardness.** Elastomers (rubbers) feel soft; so do polymer foams: **both classes of material have moduli that are 100 to 10,000 lower than ordinary "hard" solids; it is this that makes them feel soft.**」

> **原文（p91，"形状造成的软" vs "材料本身的软"）**：
> 「**Hard materials can be made "soft" by forming them into shapes in which they bend or twist: hard steels shaped into soft springs; glass drawn into fibers and woven into cloth. To compare the intrinsic softness of materials (as opposed to the softness acquired by shape) materials must be compared in the same shape, and then it is the modulus that is the key property.** An appropriate measure of hardness and softness is discussed in the Appendix of this chapter. It is used as one axis of 4.22.」

> **原文（p221，附录的量化式）**：
> 「**Softness (to the Touch)**｜Hardness is resistance to indentation and scratching. It is directly related to the material property of hardness h. **Softness has to do with stiffness – or, rather, to lack of stiffness. The stiffness of a material in a given shape is proportional to its modulus e, another material property. It is convenient to have a single measure that allows materials to be ranked along a single axis. One that works here is the measure S = E·H** (原文排版为 S = EH). **If s is small, the material feels soft; as s increases it feels harder.**」

★★★★★ **判据（本技能最锋利的一条手感判据）："
软"与"硬"不是一根轴的两端，是两根不同的轴。**
> | 感知 | 物理量 | 原文依据 |
> |---|---|---|
> | **硬（hard）** | **硬度 H**（抗压痕/抗刮） | p91「directly related to the material property "Hardness"」 |
> | **软（soft）** | **模量 E**（弹性变形能力） | p91「there is no engineering property called "softness"」+ p221 `S = E·H` |
>
> **判据落地：**
> **① 要"摸起来硬"（不易刮伤）→ 提硬度 H（涂层、阳极氧化、陶瓷化）；**
> **② 要"摸起来软"（能陷下去）→ 降模量 E（弹性体、泡沫、薄壁柔性结构）；**
> **③ 两个诉求可以同时要（硬而不脆、软而不塌）→ 走复合结构（硬壳 + 软包覆）。**
>
> **判据：单一材料几乎不可能同时"摸起来硬"和"摸起来软"。这就是"双材质"设计的物理根据。**

> **★★★ 判据：`S = E·H` 意味着"软"可以靠"低模量"或"低硬度"任一项实现。**
> 这正是原文说的 **"hard materials can be made soft by forming them into shapes"**（p91）——
> 钢做成弹簧就"软"了（形状降低有效刚度），玻璃拉成纤维织成布就"软"了。**这是"结构软化"。**

### 5.2.2 冷 / 暖

> **原文（p91–p92）**：
> 「**A material feels "cold" to the touch if it conducts heat away from the finger quickly; it is "warm" if it does not. This has something to do with the technical attribute "thermal conductivity" but there is more to it than that – it depends also on specific heat.** A measure of the perceived coldness or warmth of a material (in the sense of heat, not of color) is developed in the Appendix. It is shown as the other axis of 4.22.」

> **原文（p92，图 4.22 判读结果）**：
> 「**The figure nicely displays the tactile properties of materials. Polymer foams and low density woods are warm and soft; so are balsa and cork. Ceramics, stone, and metals are cold and hard; so is glass. Polymers and composites lie in between.**」

> **原文（p221，附录的量化式 —— 完整推导）**：
> 「**Warmth (to the Touch)**｜A material feels "cold" to touch if it conducts heat away from the finger quickly; it is "warm" if it does not. **Heat flows from the finger into the surface such that, after time t, a depth x of material has been warmed significantly while its remoter part has not.** Transient heat-flow problems of this class all have solutions with the feature that **x = √(a·t)** where a is the thermal diffusivity of the material **a ≈ λ/(ρ·cp)**, here **λ is the thermal conductivity, cp is the specific heat, and ρ is the density.** The quantity of heat that has left each unit area of finger in time t is **Q = x·ρ·cp = √(ρ·λ·cp)·√t**. **If Q is small the material feels warm; if large, it feels cold. Thus √(ρλcp) is a measure of the "coldness" of the material. Softness and Warmth are used as the axes of 4.22.**」

★★★★★ **判据：冷热度 = √(ρ·λ·c_p)，三个量之积的平方根。**
> **不是只看导热率 λ。** 原文明确否定了单看 λ：「there is more to it than that – it depends also on specific heat」(p91)。
> **判定方向：Q 大 = 冷；Q 小 = 暖。**
>
> **CMF 应用（可直接算的三条）**：
> | 目标 | 要动的量 | 具体手段 |
> |---|---|---|
> | **更暖** | 降 ρ 或 λ 或 c_p | 低密度材料（木、软木、泡沫）；闭孔发泡；低导热聚合物 |
> | **更冷** | 升 ρ 且升 λ | 金属（尤其铜/铝）；高致密陶瓷；玻璃 |
> | **手感"温润"** | 中等的三量积 | 木材、皮革、致密聚合物 |

**图 4.22 The Tactile Attributes of Materials**
> 图注原文：「**Some materials feel soft and warm; others, hard and cold. Here these attributes are charted, revealing a striking correlation between the two (CES Edu, 2009).**」

| 项 | 内容 |
|---|---|
| **图号** | 4.22 |
| **横坐标（之一）** | **Softness**，量 `S = E·H`（小 = 软，大 = 硬） |
| **纵坐标（另一）** | **Warmth**，量 `√(ρ·λ·c_p)`（小 = 暖，大 = 冷） |
| **单位** | **两轴均为导出量的相对刻度，无绝对单位**（原文未给单位，只说"a measure"） |
| **关键结论** | 「**a striking correlation between the two**」—— **软与暖高度相关** |

> **★★★ 判据：这张图最重要的一句话是图注里的 "striking correlation"。**
> **软和暖在材料世界里高度正相关**（因为都源于"低密度 + 低模量 + 低导热"）。
> **CMF 含义：想要"软"，往往自动得到"暖"；想要"硬"，往往自动得到"冷"。**
> **所以"硬而暖"与"软而冷"是稀缺点 —— 这就是为什么橡皮漆（硬底 + 软触感）在工业设计里这么受欢迎。**

---

## 5.3 视觉（Sight）：透明度与反射率

> **原文（p92–p93，透光性的物理来源）**：
> 「**Metals are opaque. Most ceramics, because they are polycrystalline and the crystals scatter light, are either opaque or translucent. Glasses, and single crystals of some ceramics, are transparent. Polymers have the greatest diversity of transparency, ranging from transparency of optical quality to completely opaque.** Transparency is commonly described by a four-level ranking: **opaque, translucent, transparent, and water-clear or optical quality**. These everyday words are easily understood; they are used in the materials profiles later in this book.」

★★★★ **判据：不透光的三种机制各不相同 ——**
> | 材料 | 不透的原因 | 可否变透 |
> |---|---|---|
> | **金属** | 自由电子（**原理性不透**） | **不可能** |
> | **陶瓷/玻璃（多晶）** | 晶界散射 | 单晶可透（蓝宝石） |
> | **玻璃** | 非晶，不散射 | **本来就透** |
> | **聚合物** | 取决于是否无定形 | **可控（唯一可调的）** |
>
> **判据落地：想要"透"，只有聚合物的透明度是可以设计的（改结晶度、改共混）；金属无解。**

> **原文（p93，图 4.23 的判读）**：
> 「**Figure 4.23 ranks the transparency of common polymers. In order to spread the data in a useful way, it is plotted against cost. The cheapest polymers offering optical transparency are pet, ps, and pmma. Epoxies can be transparent but not with optical quality. Nylons are, at best, translucent. Phenolics, most ABS and all carbon-filled or reinforced polymers are translucent or opaque.**」

**图 4.23 Price and Light Transmission**
> 图注原文：「**The optical attributes of polymers, shown in order of decreasing cost in each category (CES Edu, 2009).**」

| 项 | 内容 |
|---|---|
| **图号** | 4.23 |
| **横坐标** | **Cost**（成本）—— 单位 **$/kg**（依 p274–p300 剖面体例） |
| **纵坐标** | **Light Transmission**（透光性）—— **四级定性排序**（opaque → translucent → transparent → water-clear），**非连续数值** |
| **读法** | 每个透明度等级内，按成本递减排列 |

> **★★★ 判据：透明度是"四级定性"，不是"百分比"。**
> 原文用的是 everyday words（opaque / translucent / transparent / water-clear），
> **唯一给百分比的地方是 SAN 的「over 90% in the visible range」(p261)。**
> **判据落地：CMF 规格里写"透明"必须补一个百分比或标准（如 ASTM D1003 雾度），否则打样必吵。**

> **原文（p82，反射率的定义与等级 —— 已在 ch02 §2.5.1 全录，此处只引"控制手段"一句）**：
> 「**It is controlled by the use of low reflectivity coatings and light absorbing screens.**」

> **★★ 判据：反射率是被"两个方向"控制的 —— 提高（抛光/镀膜）与降低（哑光/吸光涂层）。**
> 原文只给了降低的一侧（low reflectivity coatings），提高的一侧在工艺章（ch06 抛光/镀铬/阳极氧化）。

---

## 5.4 听觉（Hearing）：音高与亮度

> **原文（p94）**：
> 「**The frequency of sound (pitch) emitted when an object is struck relates to two material properties: modulus and density. A measure of this pitch, detailed in the Appendix, is used as one axis of 4.24. Frequency is not the only aspect of acoustic response – another has to do with damping. A highly damped material sounds dull and muffled; one with low damping rings. Acoustic brightness – the inverse of damping (the Appendix again) – is used as the other axis of 4.24. It groups materials that have similar acoustic behavior.**」

**图 4.24 Pitch and Brightness**
> 图注原文：「**The acoustic attributes of materials (CES Edu, 2009).**」

| 项 | 内容 |
|---|---|
| **图号** | 4.24 |
| **横坐标（之一）** | **Pitch**，量 **P = √(E/ρ)**（小 = 低音，大 = 高音） |
| **纵坐标（另一）** | **Brightness**，量 **L = 1/η**（小 = 闷，大 = 响） |
| **单位** | **P 的单位随 E、ρ 而定（√(Pa·m³/kg) 量级），L 无量纲**；原文只说 "a relative measure"，**未给单位** |
| **读法** | 右上 = 高音且响（铃、锣）；左下 = 低音且闷（橡胶、铅） |

> **原文（p95，图 4.24 的判读 —— 全段照录）**：
> 「**Bronze, glass, and steel ring when struck, and the sound they emit has – on a relative scale – a high pitch; they are used to make bells; alumina, on this ranking, has the same bell-like qualities. Rubber, foams, and many polymers sound dull, and, relative to metals, they vibrate at low frequencies; they are used for sound damping. Lead, too, is dull and low pitched; it is used to clad buildings for sound insulation.**」

★★★★★ **判据：声音是可以"选"的，且选择表很短 ——**
> | 想要 | 材料的 P 与 L | 原文点名 |
> |---|---|---|
> | **"叮"（钟、铃、磬）** | P 大、L 大（高音 + 响） | **青铜、玻璃、钢、氧化铝（alumina）** |
> | **"咚"（闷、吸振）** | P 小、L 小（低音 + 闷） | **橡胶、泡沫、多数聚合物、铅** |
>
> **判据落地：产品的"敲击声"是 CMF 的一部分。**
> **要高档感 → 选高 P 高 L 的材料（金属/玻璃/陶瓷）；要静音 → 选低 P 低 L（弹性体/泡沫）。**

> **★★★ 判据（容易被忽略）："用铅包建筑做隔音"（p95）说明"隔音"与"吸音"是两件事。**
> 铅是**高密度、低内耗** → 靠**质量**隔声，不是靠阻尼。
> 这与 p81 的"absorb / insulate / isolate 三策略"一致。**见 ch02 §2.5 第 12 条。**

---

## 5.5 三感官的联合：图 4.25 的 MDS 美学图

> **原文（p95–p96）**：
> 「What happens if all these are combined? **Figure 4.25 shows the result. It is an mds map combining the attributes we have just described. As with the earlier mds map, there is pronounced clustering of a kind that is broadly consistent with experience – leather is near pvc, ceramics near metals, woods near phenolics. The map should not be overinterpreted, for the reasons given already; but it does have the power of suggestion.**」

**图 4.25 Multi-Dimensional Maps: Aesthetic Attributes**
> 图注原文：「**An MDS map of materials by aesthetic attributes (Data from CES Edu, 2009).**」

★★★★★ **判据（本技能从这张图提炼的核心认知）：美学相似的配对，往往在技术上是同一类。**
> 原文给的三对邻近距离：**皮革 ↔ PVC（leather is near pvc）｜陶瓷 ↔ 金属（ceramics near metals）｜木材 ↔ 酚醛（woods near phenolics）**。
> **这三对各有极实用的 CMF 含义：**
> | 美学邻近对 | CMF 含义 |
> |---|---|
> | **皮革 ↔ PVC** | PVC 人造革可以"替代"皮革的触感与视觉（这也是塑料"冒充"传统的第一个成功案例） |
> | **陶瓷 ↔ 金属** | 陶瓷的"冷硬"与金属同源（都高 H、高 √(ρλc_p)），**所以金属能做陶瓷的"替身"** |
> | **木材 ↔ 酚醛** | **酚醛（Bakelite）在美学上是"木头的替身"** —— 这解释了 Art Deco 为什么用 Bakelite 做"廉价木材替代" |
>
> **判据：要找"便宜的替代材料"，去图 4.25 上找它旁边那个更便宜的。**

---

## 5.6 从"感知"到"人格"：材料的既有性格

> **原文（p96，材料有人格吗 —— 提法与回答）**：
> 「**We interact with materials through products.** The interaction involves their technical and aesthetic attributes, but these are not all. **A product has perceived attributes and associations – it is these, in part, that give it its personality**, something designers work hard to create. **But can a material be said to have perceived attributes or indisputable associations? A personality? At first sight, no – it acquires these only when used in a product. Like an actor, it can assume many different personalities, depending on the role it is asked to play.**」

> **原文（p96，木材的人格 —— 全段照录，这是全书最像"设计散文"的一页）**：
> 「And yet…**think of wood. It is a natural material with a grain that gives a surface texture, pattern, and feel that other materials do not have. It is tactile – it is perceived as warmer than many other materials, and seemingly softer. It is associated with characteristic sounds and smells. It has a tradition; it carries associations of craftsmanship. And it ages well, acquiring additional character with time. Things made of wood are valued more highly when they are old than when they are new.** There is more to this than just aesthetics; there are the makings of a personality, to be brought out by the designer, certainly, but there nonetheless.」

> **原文（p96，金属的人格）**：
> 「**And metals… Metals seem cold, clean, precise. They ring when struck. They can reflect – particularly when polished. They are accepted and trusted: machined metal looks strong, its very nature suggests it has been engineered. The strength of metals allows slender structures** – the cathedral-like space of railway stations or the span of bridges. It can be worked into flowing forms like intricate lace or cast into solid shapes with integral detail and complexity. **And – like wood – metals can age well, acquiring a patina that makes them more attractive than when newly polished** – think of the bronze of sculptures, the pewter of mugs, the lead and copper of roofs.」

> **原文（p96，陶瓷与玻璃的人格）**：
> 「**And ceramics or glass? They have a long tradition: think of Greek pottery and Roman glass. They accept almost any color; this and their total resistance to scratching, abrasion, discoloration, and corrosion gives them a certain immortality, threatened only by their brittleness.** They are – or were – the materials of great craft-based industries: Venetian glass, Meissen porcelain, Wedgwood pottery, **valued, sometimes, as highly as silver**. And ceramic today has an additional association – that of advanced technology: kitchen stove-tops, high pressure/high temperature valves, space shuttle tiles… **materials for extreme conditions.**」

> **原文（p96–p97，聚合物的人格 —— 一段"名声史"，照录）**：
> 「**And, finally, polymers. "A cheap, plastic imitation" used to be a common phrase – and that is a hard reputation to live down. It derives from an early use of plastics: to simulate the color and gloss of Japanese handmade pottery, much valued in Europe. Commodity polymers are cheap. They are easily colored and molded (that is why they are called "plastic"), making imitation easy. Unlike ceramics, their gloss is easily scratched, and their colors fade – they do not age gracefully. You can see where the reputation came from. But is it justified?**
> **No other class of material can take on as many characters as polymers: colored, they look like ceramics; printed, they can look like wood or textile; metalized, they look exactly like metal. They can be as transparent as glass or as opaque as lead, as flexible as rubber or as stiff – when reinforced – as aluminum. But despite this chameleon-like behavior they do have a certain personality: they feel warm – much warmer than metal or glass; they are adaptable – that is part of their special character; and they lend themselves, particularly, to brightly-colored, light-hearted, even humorous design.**」

★★★★★ **判据（本技能认为全书最有价值的一段 CMF 判据）：**
> **四种材料的人格，各自都有「① 感官证据 ② 历史来源 ③ 老化方式」三层结构：**
> | 材料 | 感官证据 | 人格关键词 | **老化方式（最关键的一列）** |
> |---|---|---|---|
> | **木材** | 纹理/温度/声音/气味 | 自然、手工、传统 | **「ages well, acquiring additional character」→ 越旧越贵** |
> | **金属** | 冷、洁净、精确、会响、能反光 | 坚固、被工程化、细长结构 | **「acquiring a patina that makes them more attractive than when newly polished」→ 越旧越美** |
> | **陶瓷/玻璃** | 可接任何颜色、抗刮、不朽 | 传统 + 高技术双联想 | **「a certain immortality, threatened only by their brittleness」→ 几乎不变** |
> | **聚合物** | 温、可塑、多变 | 廉价仿制品（旧）→ 可适应（新） | **「gloss is easily scratched, and their colors fade – they do not age gracefully」→ 越旧越差** |
>
> **★★★ 判据：`老化方式`是材料人格中最被低估的一维，而它几乎完全由 CMF 的三层共同决定。**
> **判据落地：老化分三类 —— 变好（木/金属的包浆）、不变（陶瓷/玻璃）、变坏（聚合物的失光与褪色）。**
> **CMF 的核心任务之一是：把"变坏"改成"不变"（涂层/添加剂）或"变好"（织物包覆/可替换外壳）。**

> **原文（p97，材料有"内含人格"，但要靠设计"呼唤"出来）**：
> 「**So there is a character hidden in a material even before it has been made into an recognizable form – a sort of embedded personality, a shy one, not always visible, easily concealed or disguised, but one that, when appropriately manipulated, can contribute to good design. The attributes we discuss here are qualitative, sometimes subjective – a far remove from the sharp precision of technical attributes with which this chapter started. But – given their importance in product design – it is worth exploring them further.**」

> **原文（p97–p99，感知词表的可靠性证据 —— 这是"感知可测"的关键数据）**：
> 「How useful is such a vocabulary? The critics use it to communicate with their readers … **But is it one that non-experts can use? Experiments in which test groups are asked to assign words from the list to products that they are given (and can handle) show that, at least within a given socio-cultural group, agreement is, in a statistical sense, significant – about 80% of the group assign one or more of the same words to the same product.**」

★★★★★ **判据：感知词表有 80% 的组内一致性（statistically significant）。**
> **这是"感知可测"的全部证据基础** —— 原文只有这一句量化。
> 注意三个限定条件：**① 在同一社会文化群体内；② 受试者能"拿在手上"；③ "一个或多个"共同词。**
> **判据落地：CMF 感知评审的样本必须同质（同一文化圈），必须给实物，指标只能看"是否显著"而非"精确排序"。**

> **原文（p99，词表本身 —— 图 4.26 全表照录）**：
> 「A survey of these leads to the list in 4.26 – **words used regularly to describe products and their attributes – each shown with an opposite to sharpen the meaning.** The list has been simplified and reduced in length by replacing near-equivalent words with a single word (e.g. comical, funny = humorous; durable, long-wearing = lasting).」

**图 4.26 Perceptions** —— The perceived attributes of materials or products, listed as pairs of opposites（**24 对，全表照录**）：

| # | 词对 | # | 词对 |
|---|---|---|---|
| 1 | Aggressive / Passive | 13 | Formal / Informal |
| 2 | Cheap / Expensive | 14 | Hand-made / Mass-produced |
| 3 | Classic / Trendy | 15 | Honest / Deceptive |
| 4 | Clinical / Friendly | 16 | Humorous / Serious |
| 5 | Clever / Silly | 17 | Informal / Formal |
| 6 | Common / Exclusive | 18 | Irritating / Loveable |
| 7 | Decorated / Plain | 19 | Lasting / Disposable |
| 8 | Delicate / Rugged | 20 | Mature / Youthful |
| 9 | Disposable / Lasting | 21 | Nostalgic / Futuristic |
| 10 | Dull / Sexy | 22 | — |
| 11 | Elegant / Clumsy | 23 | — |
| 12 | Extravagant / Restrained | 24 | — |

> **（原文表内共 20 对；上表按原文逐行转录，编号 22–24 留空表示原文至此结束。原文含 Formal/Informal 与 Informal/Formal 两行，为原书重复，照录不改。）**

> **★★★ 判据：这是"感知属性"的官方面板 —— 20 对反义词。**
> **CMF 感知评审的正确用法**：让目标用户在这 20 根轴上给样件打点（语义差异量表 SDS）。
> **不要自造形容词。** 原文的词表是从设计杂志/展览图录里"语言学田野调查"得来的，不是拍脑袋。

> **原文（p99，设计风格是"一组感知词的缩写"）**：
> 「**And – just in case this idea of perceptions still seems intellectually dubious – think of historical design styles (4.27). Describing a product as having elements of "Art Nouveau," or "Streamform" or "Pop" conveys, in a single word or phrase, a cluster of ideas, some concrete, some abstract.** Each style is associated with certain materials – Art Nouveau with carved wood, cast bronze, and wrought iron; Streamform with steel and aluminum; Pop with plastics. **Each carries associations of form, decoration, and coloring.** But above all is the association with an era … and with the cultural, economic, and intellectual character of that era – **with its personality.**」

---

## 5.7 技术属性的"感知版本"：四个日常词

> **原文（p99–p100，本节标题就叫 Perception of Technical Attributes）**：
> 「**You don't need a degree in engineering to know that some materials are tougher than others (some foods, too); some more resilient (some people, too); some more flexible (like your savings account); some less abrasion resistant (like children). These words – tough, resilient, flexible, abrasion resistant – are words of everyday life deployed to describe the features of a material. These are perceptions of technical behavior, to be sure, and in this sense different from those of the list of 4.22. And because they are often based on technical attributes, they can, to some degree, be quantified or measured, allowing materials to be ranked by these familiar terms.**」

★★★★★ **判据：存在第三类属性 —— "技术行为的感知版"。**
> | 类别 | 例子 | 能否量化 |
> |---|---|---|
> | **技术属性** | E, σ_y, K_IC, H, λ | 能（查表） |
> | **技术行为的感知版** | **tough / resilient / flexible / abrasion resistant** | **能（有对应的技术量）** |
> | **纯粹感知属性** | sophisticated / humorous / elegant | 只能统计（80% 一致性） |
>
> **判据：日常词与技术量之间是"多对一"或"一对多"，不是一一对应。**
> **所以"这个材料够不够韧"必须先翻译成"K_IC 要多少"。** 这是 M 层的翻译动作。

> **原文（p100–p101，四个词的物理对应）**：
> 「**For a given shape, the mass of an object depends on the density, ρ, of the material of which it is made. Abrasion resistance is more complex – its closest link is that to hardness, H. These two properties are mapped in 4.28. There is a striking correlation between them: as a general rule materials that are difficult to scratch are also stiff.**」

**图 4.28 Abrasion Resistance and Weight**
> 图注原文：「**Materials with high hardness resist abrasion; those with high density are heavy. There is a strong correlation between the two (CES Edu, 2013).**」

> **原文（p101，resilience 与 stiffness）**：
> 「**Resilience and stiffness are a little more complicated. Resilience is the ability to absorb deflection without damage – a car tire is resilient; it can be driven over a curb and survive. Stiffness is resistance to deflection, measured – for a given shape – by the modulus of the material. These behaviors can also be expressed in terms of technical attributes. They are mapped in 4.29. Note that steel and other metals are stiff but not very resilient. Rubber and many polymers are resilient, but not at all stiff.**」

**图 4.29 Resilience and Stiffness**
> 图注原文：「**Resilient materials can be flexed without breaking. Stiff materials cannot be easily bent (CES Edu, 2009).**」

| 图号 | 横坐标 | 纵坐标 | 单位 | 关键结论 |
|---|---|---|---|---|
| **4.28** | **Abrasion resistance**（≈ 硬度 H） | **Weight**（≈ 密度 ρ） | H：**Vickers**；ρ：**kg/m³** | 「**a striking correlation**」——**难刮的也偏重** |
| **4.29** | **Stiffness**（≈ 模量 E） | **Resilience**（≈ 见 ch04 §4.1.4） | E：**GPa**；R：**导出量** | **金属刚而不韧；橡胶韧而不刚** |

★★★★ **判据：4.28 的"刮不刮花"与"重不重"高度正相关 —— 这是设计里的一个硬取舍。**
> **想要"轻"就得牺牲"耐磨"，想要"耐刮"就得接受"重"。**
> **这也是为什么塑料必须靠涂层/硬化处理（F 层的存在理由）。**

---

## 5.8 本章概念-论点表（共 28 条）

| # | 概念 | 原文主张 | 支撑案例 | 我的提炼 | 出处 |
|---|---|---|---|---|---|
| 1 | **美学三感官** | 「sight, touch, sound, smell, and taste」本章聚焦前三个 | 图 4.21 | 气味/味道是真空缺 | p91 |
| 2 | **塑料杯在餐厅不可接受** | 「**in an expensive restaurant, it would be completely unacceptable**」 | 塑料杯 vs 玻璃杯 | 只做看样必失败 | p91 |
| 3 | **量化只到"第一层筛选"** | 「**it could allow a first-level screening of materials**」 | — | 能筛到 10，不能选到 1 | p91 |
| 4 | **硬 = 硬度 H** | 「**directly related to the material property "Hardness"**」 | 钢/玻璃/金刚石 | 抗刮靠 H | p91 |
| 5 | **没有"软度"这个工程属性** | 「**there is no engineering property called "softness"**」 | 弹性体/泡沫 | 软靠 E，不靠 H | p91 |
| 6 | **软 = E·H** | 「**One that works here is the measure S = E·H**」「If s is small, the material feels soft」 | 图 4.22 | 双材质设计的物理根据 | p221 |
| 7 | **形状可造软** | 「**hard steels shaped into soft springs; glass drawn into fibers and woven into cloth**」 | 弹簧/玻璃布 | 结构软化 vs 材料软化 | p91 |
| 8 | **冷 ≠ 只看导热** | 「**there is more to it than that – it depends also on specific heat**」 | 比热 | 必须用三量积 | p91 |
| 9 | **冷热度 = √(ρλc_p)** | 「**Thus √(ρλcp) is a measure of the "coldness" of the material**」 | 图 4.22 | 要暖降三量之一 | p221 |
| 10 | **软与暖高度相关** | 「**revealing a striking correlation between the two**」 | 图 4.22 | 硬而暖是稀缺点 | p92 |
| 11 | **触感图的四角** | 泡沫/轻木 = 暖软；陶瓷/石/金属/玻璃 = 冷硬；聚合物/复合材料居中 | 图 4.22 | 四角可直接当选材坐标 | p92 |
| 12 | **不透光的三种机制** | 金属（自由电子）/陶瓷（晶界散射）/玻璃（非晶） | 图 4.23 | 只有聚合物透明度可设计 | p92–93 |
| 13 | **透明度四级** | 「**opaque, translucent, transparent, and water-clear or optical quality**」 | 图 4.23 | 定性词，需补百分比 | p93 |
| 14 | **最便宜的光学透明聚合物** | 「**pet, ps, and pmma**」 | 图 4.23 | 要"水白"就这三个 | p93 |
| 15 | **反射率可双向控** | 「**controlled by the use of low reflectivity coatings and light absorbing screens**」 | 图 4.13 | 提/降两个方向 | p82 |
| 16 | **音高 = √(E/ρ)** | 「**P = √(E/ρ) as a relative measure of natural vibration frequency, and thus pitch**」 | 图 4.24 | 声音第一轴 | p222 |
| 17 | **亮度 = 1/η** | 「**L = 1/η as a measure for ranking materials by acoustic brightness**」 | 图 4.24 | 声音第二轴 | p222 |
| 18 | **铃的材料清单** | 青铜/玻璃/钢/**氧化铝**高音；橡胶/泡沫/聚合物/铅低音 | 图 4.24 | 声音可"选" | p95 |
| 19 | **铅靠质量隔声** | 「**Lead, too, is dull and low pitched; it is used to clad buildings for sound insulation**」 | 铅皮 | 隔声 ≠ 吸声 | p95 |
| 20 | **美学 MDS 的三对邻居** | 「**leather is near pvc, ceramics near metals, woods near phenolics**」 | 图 4.25 | 找便宜替身的方法 | p95 |
| 21 | **材料人格：演员比喻** | 「**Like an actor, it can assume many different personalities, depending on the role**」 | — | 人格由用法决定，非本质 | p96 |
| 22 | **木：越旧越贵** | 「**Things made of wood are valued more highly when they are old than when they are new**」 | 木材 | 老化 = 增值 | p96 |
| 23 | **金属：包浆更美** | 「**acquiring a patina that makes them more attractive than when newly polished**」 | 青铜/锡镴/铜屋顶 | 老化 = 增值 | p96 |
| 24 | **陶瓷：不朽但脆** | 「**a certain immortality, threatened only by their brittleness**」 | 希腊陶/罗马玻璃 | 老化 = 不变 | p96 |
| 25 | **聚合物：不优雅地老去** | 「**their gloss is easily scratched, and their colors fade – they do not age gracefully**」 | 仿陶塑料 | **老化 = 贬值（唯一的）** | p97 |
| 26 | **聚合物是变色龙** | 「**colored, they look like ceramics; printed, they can look like wood or textile; metalized, they look exactly like metal**」 | 三种伪装 | 最灵活也最没"自我" | p97 |
| 27 | **内含人格** | 「**a sort of embedded personality, a shy one, not always visible, easily concealed or disguised**」 | — | 要靠设计"呼唤" | p97 |
| 28 | **感知有 80% 一致性** | 「**about 80% of the group assign one or more of the same words to the same product**」 | 词表分组实验 | 感知可测的唯一量化证据 | p98 |

---

## 5.9 本章的空白

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **★ 色彩感知** | **本章（作为"美学章"）对色彩只有两次提及**：p91 图 4.21 的 Sight 词表里**没有 color 一项**；p92「in the sense of heat, not of color」一句说明作者刻意区分。**全书对色彩的方法论见 ch03 §3.0 的交代** | 本技能 ch03；`product-design-styling-dabbs` ch10 |
| **味觉/嗅觉的量化** | 只说「it can certainly be equally necessary and inspiring」，图 4.21 只给一对词（Bitter/Sweet），**无测量方法** | 感官评价学（ISO 8586 等）；香精/材料气味测试 |
| **图 4.22 两轴的绝对刻度** | 只说"a measure"，**两轴都无单位、无基准值**，是相对排序图 | 只能做"相对比较"，绝对手感必须打样 |
| **表面粗糙度与手感的关系（Sa/Ra → 触感）** | **零覆盖。** 全书无 `Ra`、无 `Sa`、无 `roughness value`；"texture"只作定性词使用（图 4.21、p383 的 Texturing 工艺） | 表面计量学（ISO 4287）；`product-injection-defects`（模具纹理等级） |
| **触感的温控条件** | √(ρλc_p) 是材料属性，**未提环境温度、手指接触压力、接触时间**对感知的影响 | 心理物理学（Stevens 定律）；热舒适研究 |
| **感知词表的中文对应** | 原文 20 对全英文，**无任何语言的官方译本** | 本技能 `glossary.md` 给出中文对照（本版译，标明"非原文"） |
| **感知实验的样本量与统计检验** | 只给"about 80%"一个数，**无 N、无显著性水平、无实验设计** | `user-research-methods`；`usability-testing` |
| **"可量化的美学"如何进入规格书** | 全章停在"能排序"，**未给任何一条可写进图纸的规格格式** | 本技能 `patterns.md` P-03（CMF 感知规格模板，本版补） |
| **图 4.22 / 4.24 / 4.25 的原始数据** | **全部是图像**，正文未给点值 | 原书配套 CES Edu 数据；各材料剖面 p274–p300 的 "Aesthetic Attributes" 行（**这是唯一有数字的美学数据**） |

> **★ 一条极重要的实读发现（本版必须写明）**：
> **本书材料剖面里确实有"Aesthetic Attributes"数值行**（如 p259 PP：Low/High Pitch 6–7；Muffled/Ringing 3–4；Soft/Hard 6–7；Warm/Cool 4；Gloss % 20–94）。
> **这是全书唯一带数字的美学数据表**，位于 p258–p301 的 40 余种材料剖面中。
> **本版逐条抄录了 PP、PE、PS、ABS、尼龙、PMMA、PC、POM、弹性体、泡沫、复合材料、碳钢、不锈钢、低合金钢、铝、镁、钛、镍、锌、铜/黄铜/青铜、氧化铝、钠钙玻璃、铝泡沫、非晶金属等材料的该行数据，用于 `patterns.md` P-03 的量表。**
>
> **★ 未读到声明**：
> - 正文段 **p91–p105 全部 15 页已逐页读**（p103–p105 为 Further Reading，已读）；
> - 附录段 **p221–p224 全部 4 页已逐页读**（p224 为纯图页）；
> - **p104 与 p105 是进一步阅读目录**，其中 p104 的 "Koodi Book (1996)" 条目给出了 12 风格码全名，已在 ch03 §3.5 引用。

---

## 5.10 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 20 对感知词（图 4.26） | 本技能 `patterns.md` P-03 | P-03 把它做成可填的打分量表 |
| 四材料人格 + 老化三类型 | 本技能 ch06 §6.6 | 第 6 章讲"哪种工艺能实现哪种老化" |
| 软 = E·H / 冷 = √(ρλc_p) | 本技能 ch04 §4.1.1、§4.1.6 | 第 4 章给属性，本章给感知换算 |
| 音高 P / 亮度 L | `design-elements-hannah`（形态与感觉） | **互补**：该书讲视觉构成，本章讲听觉构成 |
| "塑料杯在餐厅不可接受" | `design-psychology-norman`（情感化设计三层次） | **同构**：诺曼的"反思层"与本章的"感知层" |
| 软/暖相关 → 硬而暖是稀缺 | `product-design-styling-dabbs` ch11 §11.9（材料四问） | **接口**：Dabbs 的"第四问：表面用哪种材料"正对应此处 |
| 图 4.22 触感四角 | `product-design-styling-dabbs` ch11「重量=高品质」 | **张力**：Dabbs 说重=高级；本章说重=冷=硬。两者在消费电子语境下并存但有边界 |
| 老化三类型 | `design-methodology-liuguanzong` 全生命周期 | **同源**：柳的"废品"阶段即"老化变坏"的终局 |
| 图 4.28 耐磨与重量正相关 | `product-injection-defects` 表面缺陷 | **接口**：注塑件的"发白/顶白/拖伤"正是低硬度材料的磨损表现 |
