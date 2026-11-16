# 第 3 章：C 层 —— 色彩（Color）：书里有什么、缺什么、怎么补

> **原书 PDF 页序 p42–p108（67 页，跨第 3、4、5 章及附录）**｜**本版逐页读完全部 67 页**
> 页码口径：**PDF 索引**（文本文件 `===== PAGE N =====` 的 N）
>
> **读法说明**：本书**没有独立的色彩章节**（这是最重要的事实，先声明）。
> 因此本章采取【跨章检索式读法】：把散落在技术属性、美学属性、工艺剖面、设计风格四处的"色彩相关内容"全部抽出，按 C 层的六个动作重组。
> 凡是原文没说的，一律在 §3.6 与 §3.7 标为空白，**不从常识补**。
>
> **本章在 CMF 三层流程中的位置**：**C 层。**但它在本技能里的角色特殊 ——
> **它既是"色彩怎么定"的章节，也是"这本书不能给你色彩"的诚实声明书。**

---

## 3.0 先立规矩：本书的色彩覆盖到底有多薄

> **原文（p93）—— 全书唯一一段直接讨论"颜色怎么量化"的话，一共 45 个词**：
> 「**Color can be quantified by analyzing spectra but this – from a design standpoint – doesn't help much. A more effective method is one of color matching, using color charts such as those provided by Pantone16; once a match is found it can be described by the code that each color carries.**」

**脚注 16（p93）**：
> 「Pantone (www.pantone.com.) provide detailed advice on color selection, including **color-matching charts and good descriptions of the associations and perceptions of color**.」

> **原文（p105，Further Reading 里的同一条）**：
> 「Pantone (2001) www.pantone.com. (Pantone provides detailed advice on color selection, including **color-matching charts and good descriptions of the associations and perceptions of color**.)」

★★★★★ **判据：本书对色彩的方法论贡献 = 一句话 + 一个外部工具名。**
> **① 光谱分析（spectral analysis）对设计"帮助不大"——原文明确否定这条路；**
> **② 有效方法是"颜色匹配 + 色号编码"（color matching + code）；**
> **③ 工具是 Pantone，而且本书把"颜色的联想与感知"直接外包给了它。**

> **★★★ 判据：这是本书最好的一条色彩方法论，也是最诚实的一条 ——**
> **色彩的可沟通性，来自"能被编号"。** 不能被编号的颜色，在 CMF 链条上传不下去。
> **判据落地：色彩规格的最小可交付单位不是"深空灰"，是"Pantone 编号 / RAL 编号 / 客户色卡号"。**

> **本技能对"色彩理论"的覆盖策略（明示）**：
> | 色彩知识 | 本书有无 | 本技能怎么处理 |
> |---|---|---|
> | 色相/明度/纯度（HSL 三属性） | **无** | 见 §3.7 空白表，指向 `product-design-styling-dabbs` ch10 |
> | 配色法则（互补/类似/三角） | **无** | 同上 |
> | 色彩对比与视觉分区 | **有间接证据**（p129、p128） | §3.3 用原文撑起 |
> | 色彩与材料的耦合（发色机理） | **有强内容**（p247、p254、p261） | §3.4 逐条引 |
> | 色差判定（ΔE） | **无** | §3.6 空白表 |
> | 色彩潮流/时代性 | **有**（p32、p34、p98、p142） | §3.5 |

---

## 3.1 色彩为什么在 CMF 里排第一位：一条来自"产品差异化"的证据

> **原文（p32，Swatch 案例）**：
> 「Desperate for recovery, Swiss watchmakers collaborated to design a watch that was as accurate, better made, and thinner than those from the East Asian countries, and was competitively priced. **More significantly, they devised the concept of the "collection", a series of products, technically identical, but differing in color, texture, pattern, and styling** (2.7, bottom). Artists were commissioned to design one or a series; and each new design was given a name ("Calypso Beach", "Lolita", "Graffiti"). By 1989 the image was established and successful, not only in broadening the market, but encouraging individuals to buy not one watch, but two, ten…, a hundred, even. **The brand has now launched some 1,000 designs of a single technical innovation.**」

★★★★★ **判据：CMF（尤其是 C）最成熟的商业用法，是"技术不动，只动 C/F，把单品变成系列"。**
> 原文给了完整配方：
> **① 技术完全相同的平台**（technically identical）
> **② 只变四个变量：color, texture, pattern, styling**（注意：**三个是 CMF，一个是造型**）
> **③ 每款命名**（"Calypso Beach" / "Lolita" / "Graffiti"）→ 把颜色变成可谈论的"人格"
> **④ 结果：一个技术平台卖出 1,000 个设计，人均购买从 1 件到多件。**
>
> **判据：CMF 系列的商业上限 = "同一技术平台 × 可编号的 C/F 变体 × 每个变体一个名字"。**

> **原文（p32）**：
> 「If a watch is to sell for more than $50 (and many, of course, do) **it must appeal in some way to the consumer's sense of style, taste, and individuality.**」

> **★★★ 判据：价格越过"功能溢价"线之后，卖的就是 CMF 了。**
> 原文把这条线画在 **$50**（2001 年的手表）。**这是"CMF 权重随价格上升"的定量表述。**

---

## 3.2 色彩与透明性：色彩光谱中的一个特殊轴

> **原文（p247，热塑性塑料）**：
> 「**Most accept coloring agents and fillers, and many can be blended to give a wide range of physical, visual, and tactile effects.** Their sensitivity to sunlight is decreased by adding uv filters, and their flammability is decreased by adding flame retardants.」
> 「**For transparency the polymer must be amorphous; partial crystallinity gives translucency. The most transparent polymers are acrylics, pc, ps, and pet.**」

★★★★ **判据：透明性不是"颜色"，但它是色彩决策的前置条件。**
> **因为不透明 = 底色由本体决定；透明/半透明 = 底色可以被"内部结构 + 光源 + 背景"改变。**
> 原文给的层级：**amorphous → 透明；partial crystallinity → 半透明。**

> **原文（p93，透明度的四级排序）**：
> 「Transparency is commonly described by a **four-level ranking: opaque, translucent, transparent, and water-clear or optical quality**. These everyday words are easily understood; they are used in the materials profiles later in this book.」

> **原文（p93，透明聚合物的价格排序，图 4.23）**：
> 「**The cheapest polymers offering optical transparency are pet, ps, and pmma.** Epoxies can be transparent but not with optical quality. Nylons are, at best, translucent. Phenolics, most ABS and all carbon-filled or reinforced polymers are translucent or opaque.」

**图 4.23 Price and Light Transmission**
The optical attributes of polymers, shown in order of decreasing cost in each category (CES Edu, 2009).

★★★★ **判据：透明度的四词标准 + 三个最便宜的光学透明聚合物（PET / PS / PMMA）。**
> **CMF 用法：需要"水一样透"（water-clear）时，可选项只有 PET、PS、PMMA、PC（PC 更贵更韧）。**
> **需要"半透到能看见内部"（translucent）时，PP、PE、SAN、尼龙都能做，成本低一档。**

---

## 3.3 色彩分区与对比：本书唯一的"色彩分层"证据

> **原文（p129，KOODI CODE 的三种风格码，Helsinki 1995）**：
> 「The task was to re-design a set of five small household appliances – a hair dryer, an iron, a shaver, a toaster, and a mixer – in **12 different stylistic "codes"**. **A code is a style-language that evokes certain associations and emotions through the use of form, color, and texture.**」

> **原文（p129，三种码的原文化描述 —— 这段是全书的 C+F 联合范式）**：
> 「For the first (6.17) the code is **conservative, discrete luxury, captured by the use of dark colors and wood-like textures contrasting with matte and gloss-finished metallic surfaces**. The second (6.18) adopts a **toy-like code eliciting simplicity, friendliness, and humor achieved through clear rounded forms and primary colors that distinguish functional parts.** For the third (6.19) the code is **rugged and uncomprisingly functionality, achieved through hard angular shapes with non-reflective blacked metal finish.**」

**图 6.17 Elements of Style** —— A familiar product (an iron) characterized by understated modernist form, subdued color, and subtle texture.（Source: The KOODI CODE, U. of Arts and Design, Helsinki, Finland）
**图 6.18 "Cute and friendly."** —— The Mixit mixer.
**图 6.19 "Robust, military-strength, no-nonsense functionality."** —— The Kalashnikov mixer.

★★★★★ **判据（本技能从原文提炼的最硬一条 C 层判据）：色彩分区（color zoning）的一种原始形态 ——**
> **"primary colors that distinguish functional parts"** = **原色用来"区分功能部件"**。
> 这是本书唯一一处明确说"颜色承担分区功能"的句子。
> **完整的 C 层三联：**
> | 码 | 色彩策略 | 表面策略 | 目标联想 |
> |---|---|---|---|
> | 保守奢华 | **dark colors**（暗色） | **wood-like textures + matte/gloss 金属对比** | 内敛、昂贵 |
> | 玩具友好 | **primary colors 分区** | 清亮的圆润形态、无纹理 | 简单、友好、幽默 |
> | 粗野功能 | **non-reflective blacked metal** | 哑光黑化金属 | 军事、无废话 |

> **★★★ 判据：颜色不是"涂上去的"，颜色是"和表面一起被选出来的"。**
> 三张码里，**每一张的色彩与表面都是配对的**（暗色 ↔ 木纹/哑光光泽对比；原色 ↔ 光滑；黑 ↔ 无反光）。
> **拆开单独看色卡，会得到三个"都不错"的配色；合到表面上看，只有一个对。**

> **原文（p128，压缩机案例的"工业强度"共同特征）**：
> 「All three epitomize "industrial strength" design expressed through **form, color, texture, and graphics**. They have certain features in common:
> **• Angular, straight-edged forms.**
> **• Repeated horizontal.**
> **• Upward-converging diagonals.**
> **• Subdued color.**
> **• Use of texture to create contrasts.**
> **• Minimal decoration**」

★★★★ **判据：`Subdued color` + `texture to create contrasts` 是"强度感"的标准配方。**
> 注意原文的机制：**不是用强色造强度，而是用"低饱和色 + 强纹理对比"造强度。**
> **这是反直觉的一条：想要"硬"，先降色、再加纹理。**

> **原文（p131，电子设备风格码）**：
> 「Designers of high fidelity equipment for the connoisseur use the visual prompts of this style – **understated rectangular form, matte-black finish, switches, and controls that mimic those of the professional equipment** – to suggest uncompromising technical leadership.」

> **原文（p131，航空航天风格码）**：
> 「There is a style that characterizes aerospace that goes beyond simple streamlining, **extending to color and material (polished or matte aluminum), shapes of windows and doors (rounded), and method of joining (riveting)**.」

> **★★★ 判据：风格码是可枚举的"四元组"：颜色 + 材料 + 形态 + 接合方式。**
> 原文列 aerospace 的四项：**(polished or matte aluminum) + (rounded) + (riveting)** ——
> **CMF 只覆盖前两项，另两项属造型与结构。这也是 CMF 必须和造型/结构同步评审的证据。**

---

## 3.4 色彩与材料/工艺的耦合（本书最强的部分）

### 3.4.1 聚合物怎么上色，以及"上不上去"的边界

> **原文（p247，热塑性）**：
> 「**Most accept coloring agents and fillers**, and many can be blended to give a wide range of physical, visual, and tactile effects.」

> **原文（p248，热固性 —— 一条硬约束）**：
> 「**Phenolics can be molded only in black or brown; urea, melamine, alkyd, and polyester compounds are available in a wider range of colors.**」

★★★★★ **判据：材料的"色域"是有硬边界的，不是设计想定就定。**
> **酚醛（Phenolic / Bakelite）：只有黑与棕。** 原文用 "only"。
> **脲醛 / 三聚氰胺 / 醇酸 / 聚酯：色域宽。**
> **CMF 含义：如果产品定了"必须酚醛"（因为耐热或成本），色彩方案就只剩两个色系。**
> **判据：材料锁定 = 色彩空间锁定。这条必须写进约束表，不能等到打样才发现。**

> **原文（p261，ABS —— "吃色"能力的典型）**：
> 「**abs has the highest impact resistance of all polymers. It takes color well. Integral metallics are possible (as in ge Plastics' Magix).** abs is uv resistant for outdoor application if stabilizers are added.」

> **原文（p261，SAN / ASA 的光学与颜色）**：
> 「**san (styrene-acronitrile) has the good processing attributes of polystyrene but greater strength, stiffness, and chemical and heat resistance.** … **It is transparent (over 90% in the visible range but less for uv light) and has good color. Depending on the amount of acrylonitrile that is added this can vary from water white to pale yellow, but without a protective coating, sunlight causes yellowing and loss of strength**, slowed by uv stabilizers.」
> 「**asa (acrylic-styrene-acrylonitrile) has very high gloss; its natural color is off-white but others are available.**」

★★★★ **判据：三种"吃色"能力的排序，直接决定选材 ——**
> | 材料 | 色彩能力 | 附加约束 | 出处 |
> |---|---|---|---|
> | **ABS** | 「It takes color well」+ **可做整体金属色**（Integral metallics） | 需 uv 稳定剂才能户外 | p261 |
> | **ASA** | **极高光泽**，本色 off-white | — | p261 |
> | **SAN** | **可见光透光 >90%**，颜色好 | **不涂保护层会黄变、失强** | p261 |
>
> **判据：SAN 的"水白到淡黄"是可漂移的 —— 同一个牌号，不同批次可能不在一个色号上。**
> **这是 C 层最容易被忽略的失效模式：不是"颜色不对"，是"颜色会变"。**

> **原文（p259，PP 的色域优势）**：
> 「It is more easily molded than pe, **has good transparency and can accept a wider, more vivid range of colors.**」

> **原文（p258，PE 的色域与短板）**：
> 「It accepts a wide range of colors, can be transparent, translucent, or opaque, **has a pleasant, slightly waxy feel**, can be textured or metal coated, **but is difficult to print on.**」

★★★★ **判据：`能上色` ≠ `能印刷`。PE 两个都能……除了印刷。**
> 原文对 PE 的评价是"接受广色域 + 可纹理 + 可镀金属，**但难印刷**"。
> **CMF 含义：如果设计需要丝印 logo，PE 从一开始就得排除或改工艺（见 ch06 电晕/火焰处理类方案，本书未展开）。**

### 3.4.2 玻璃：唯一给出"发色剂-颜色"对照表的材料

> **原文（p246，玻璃着色）**：
> 「Glass is a mix of oxides, principally silica, SiO2, that does not crystallize when cooled after melting. **When pure it is crystal-clear, but it is easy to color by adding metal oxides.**」

> **原文（p254，玻璃的金属氧化物发色表 —— 全书唯一的"配方级"色彩数据）**：
> 「**Adding metal oxides produces colored glass. Nickel gives a purple hue, cobalt a blue, chromium a green, uranium a green-yellow, iron a green-blue.** The addition of iron gives a material that can absorb wavelengths in the infrared range so that heat radiation can be absorbed. **Colorless, non-metallic particles (fluorides or phosphates) are added from 5 to 15% to produce a translucent or an almost opaque white opalescence in glass and glass coatings.**」

**玻璃发色表（据 p254 原文整理）**：

| 发色剂 | 颜色 |
|---|---|
| Nickel（镍） | purple（紫） |
| Cobalt（钴） | blue（蓝） |
| Chromium（铬） | green（绿） |
| Uranium（铀） | green-yellow（黄绿） |
| Iron（铁） | green-blue（蓝绿） |
| 无色非金属颗粒（氟化物/磷酸盐）5–15% | translucent 到 nearly opaque 的乳白（opalescence） |

★★★★★ **判据：玻璃的颜色是"配方"，不是"涂层"。**
> 这是 C 层里唯一一种**颜色写在材料本体里、磨掉也不会掉色**的路径。
> **判据：要求"永不褪色/可打磨修复"的产品，色彩必须走本体着色（玻璃/陶瓷釉/整体着色塑料），不能走涂层。**

> **原文（p254，玻璃的三种"变色"玻璃）**：
> 「**Photochromic glass changes color when exposed to uv** (it sometimes fades when heated); **photosensitive glass turns from clear to opal when exposed to uv or heated.** Filter glass protects from intense light and uv radiation – it is used in visors for welding. **Dichroic coatings and thin laminations give color modulation.**」

> **★★★ 判据：色彩可以是"响应式"的——随光/热变化。**
> photochromic（光致变色）/ photosensitive（光敏）/ dichroic coating（二向色）/ thermochromic（热致变色，见 p80）。
> **这是 C 层被严重低估的一格：动态色彩。**

### 3.4.3 陶瓷与釉：光泽与颜色的耦合点

> **原文（p252）**：
> 「**Glazes can be applied to ceramics for a smooth, glossy surface; patina surfaces are also possible.**」

> **★ 判据：陶瓷的"色"与"光泽"是同一道工序（施釉）的两个产物 —— 改颜色必然改光泽。**
> 这与塑料不同（塑料可先染色再调模面光泽）。**陶瓷/玻璃的 C 与 F 不可拆。**

### 3.4.4 金属的色彩：本质是"表面"而非"本体"

> **原文（p82，图 4.13 的金属反射率表）**：Aluminum 60% / Beryllium 49% / Carbon steel 57% / Invar 41% / Magnesium 72% / Stainless steel 70% / Titanium 56%。

> **原文（p372，阳极氧化）**：
> 「**The oxide is micro-porous, allowing it to absorb dyes, giving metallic reflectivity with an attractive metallic, colored sheen; and it can be patterned.**」
> 「The ability of the film to accept dyes depends on **alloy composition: pure aluminum and Al-5 Mg alloys are well suited.**」

★★★★★ **判据：铝的"颜色"其实是"氧化膜的微孔吸了什么染料"，而吸色能力由合金成分决定。**
> **判据落地：选铝的着色方案时，先定合金（纯铝 / Al-5Mg 最适合染料），再定氧化膜厚度与染色。**
> **换了合金，同一色号的成品色会变。**

> **原文（p368，电镀的色彩维度）**：Electro-plating 的 "Functions" 第一项就是 **Color, texture, reflectivity**。

> **原文（p365，气相金属化/Vapor Metalizing）**：
> 「**Metalizing is widely used to give a reflective metallic finish on bulk and film polymers, metal, glass, and ceramic.**」

> **★★★ 判据：要在塑料上得到"金属色"，三条路各有代价 ——**
> | 路径 | 原文依据 | 得到的"金属感" | 主要代价 |
> |---|---|---|---|
> | **本体金属色粒（Integral metallics）** | ABS「Integral metallics are possible」(p261) | 均匀、无接口 | 只有部分聚合物支持 |
> | **气相金属化（PVD）** | p365「reflective metallic finish on bulk and film polymers」 | 高反射、可做镜面 | 需真空设备；涂层薄（1–80μm） |
> | **电镀** | p368「Color, texture, reflectivity」 | 最像真金属 | 塑料需先导电化；有内应力、可能剥落 |

### 3.4.5 印刷与膜内装饰：色彩的第二条传导链

> **原文（p360，丝网印刷）**：
> 「**Functions** Color, reflectivity, texture.」
> 「Multiple colors can be printed, but **each requires a separate screen.**」
> 「**Epoxy inks give protection against scratching** and can be used with products that attack standard enamel inks.」

> **原文（p361，移印）**：
> 「**The advantages of pad printing are the ability to print on irregular surfaces (such as a golf ball) and to print wet on wet multi-colors. Its excellent quality of detail makes pad printing attractive for flat items. Pad printing is limited to relatively small images compared to screen printing – usually less than 0.1 m².**」

> **原文（p362，曲面印刷/水转印）**：
> 「**Cubic printing is very versatile; complex, curved shapes can be printed and the image can be multi-colored. Registration is difficult, so the image is usually applied in a single operation, and designed so that precise registry is not necessary.**」

> **原文（p366，膜内装饰 IMD）**：
> 「**In-mold decoration (imd) allows accurately registered colors, designs, and print to be applied to injection molded components without any secondary processing.** The image, which can be full color, is printed onto a polyester or polycarbonate film called the "foil."」
> 「**By printing the graphics on the second surface, the design is held within two thin polymer layers, protecting it from wear and tear. Change of decoration simply requires a change of foil, without changing the mold or the material.**」

> **原文（p365，烫印）**：
> 「A heated metal die (250–300 C) is pressed against a colored carrier foil and the component being printed. … **The pressure from the die creates a recess for marking, which protects the stamped letter from abrasion**, and heat makes the marking medium adhere to the product.」
> 「**A range of decorating finishes is available, including metallic foils, wood grain finishes, and multi-colored graphics.**」

**四种色彩传导工艺的量化对比（据 p360–p366 的 Attributes 表）**：

| 工艺 | 表面硬度（Vickers） | 涂层厚度（μm） | 曲面覆盖 | 加工温度（°C） | 出处 |
|---|---|---|---|---|---|
| **Screen printing** | 5–10 | 10–100 | **Poor** | 15–25 | p360 |
| **Pad printing** | 5–10 | 6–10 | **Good** | 15–30 | p361 |
| **Cubic printing** | 5–10 | 6–10 | **Good** | 15–30 | p362 |
| **Hot stamping** | 5–50 | 1–50 | **Poor** | 150–300 | p365 |
| **In-mold decoration** | 5–15 | 10–500 | **Avg. to Good** | 125–200 | p366 |

★★★★★ **判据（C 层的工艺选择表，全书最有用的四列）：**
> **① 平面/小面积高精度 → 移印**（曲面 Good，但 <0.1 m²）
> **② 平面大面积多色 → 丝印**（曲面 Poor，每色一版）
> **③ 三维曲面 → 水转印**（曲面 Good，但套准差，只能一版一次）
> **④ 要耐磨且不能有二次工序 → IMD**（涂层最厚 10–500μm，图象在两层膜之间被保护）
> **⑤ 要"凹陷保护"的金属字 → 烫印**（硬度最高 5–50，且压出凹槽保护）
>
> **判据：所有印刷类工艺的表面硬度都只有 5–10 Vickers，远低于固化漆（10–16）与阳极氧化（600–1000）。**
> **结论：印刷不是"耐久表面"，是"装饰表面"。要耐久，必须叠加清漆或改用 IMD。**

---

## 3.5 色彩的"时代性"：会过期的不是颜色，是联想

> **原文（p98）**：
> 「**But we are bound by language – it is the most important way in which we communicate. So it is worth a try.**」
> 「They are subjective; they depend on the product itself, and, importantly, on **the context and the culture in which it is used**. They are sometimes ambiguous, and **their meaning changes with time: a product that appears aggressive or luxurious today can seem humorously retro or just plain ugly tomorrow (think of car styling).**」

> **原文（p98，设计风格谱系图 4.27）**：
> 「And – just in case this idea of perceptions still seems intellectually dubious – think of historical design styles (4.27). **Describing a product as having elements of "Art Nouveau," or "Streamform" or "Pop" conveys, in a single word or phrase, a cluster of ideas, some concrete, some abstract. Each style is associated with certain materials** – Art Nouveau with carved wood, cast bronze, and wrought iron; Streamform with steel and aluminum; Pop with plastics. **Each carries associations of form, decoration, and coloring.**」

**图 4.27 Design Styles** —— A chronology of selected movements in design, sometimes linked to material innovations：

| 年代组 | 风格 | 年份 |
|---|---|---|
| 1900 and Before | Art Nouveau | 1890 |
| | Arts and Crafts | 1890 |
| | Functional | 1900 |
| 1900 to 1950 | Modernist | 1900 |
| | Futurist | 1910 |
| | Art Deco | 1920 |
| | Streamform | 1930 |
| | Contemporary | 1945 |
| 1950 and After | Pop | 1960 |
| | Retro | 1960 |
| | Classic | 1970 |
| | Post-Modernist | 1970 |
| | Memphis | 1980 |

★★★★ **判据：风格 = 材料 + 形态 + 装饰 + 色彩 的四元组，且带年代。**
> **每一代风格背后是一次材料创新**（Art Nouveau 靠可雕木材与铸青铜；Streamform 靠钢与铝；Pop 靠塑料）。
> **CMF 的"复古"动作，本质是把四元组里的一项拉回旧时代 —— 只拉色彩不拉材料，会变成"假古董"。**

> **原文（p131，Art Deco 与 Bakelite —— 材料-色彩-形态三者绑定的最佳案例）**：
> 「**Art Deco was the first style movement to make expressive use of polymers. Bakelite (a phenolic resin), the first commercial plastic that could accept a wide range of colors and textures, lent itself to the adventurous curved and terraced shapes of the Art Deco movement** – shapes that would be hard to make from wood. At one extreme, that of the portable radio, the use of plastic, chrome, steel, and aluminum allowed a range of cheap mass-produced products. At the other, that of state rooms of great ocean liners and grand hotels, the use of exotic hardwoods, leather, ivory, glass, and bronze created a décor for the very rich. **The associations of Art Deco are those of cosmopolitan luxury, industrial progress and power, faith in technology, and futurism.**」

> **★★★ 判据（与 p248"酚醛只有黑与棕"对照，形成一个重要张力）：**
> **p131 说 Bakelite 是"第一个能接受广色域与纹理的商业塑料"；p248 说"酚醛只能模成黑或棕"。**
> **两处并不矛盾：前者说的是"相对当时（1900s）的其他材料"的历史突破；后者说的是"相对当代聚烯烃"的技术现状。**
> **判据：读材料史必须带"相对谁"这个参照系，否则会得出互相打架的结论。**
> （本书未对此矛盾作说明，此处为本版读法提示。）

> **原文（p34，Bang & Olufsen 自述 —— 厂家的色彩哲学，原文照录）**：
> 「"**Most of our products come in a range of colors to present you with a choice, just as if you were buying a new sofa… Our colors don't follow fashion, but they will match your furniture... Surface textures are another design element which some would regard as secondary, but which we care about deeply**… We have but one rule: **Bang & Olufsen products must create an immediate understanding of their performance.** We aim to surprise with unusual initiatives, to escape the sense of boredom of mass product development…"」

★★★★★ **判据：这是全书唯一的"企业色彩策略"原文，且它反潮流：**
> **「Our colors don't follow fashion, but they will match your furniture」** ——
> **色彩策略有两类：① 追潮流（Swatch 模式）② 不追潮流、只求"与你家家具配得上"（B&O 模式）。**
> 后者把色彩锚定在**"用户的室内环境"**而不是**"当季流行色"**上。
> **判据：选哪一类，取决于产品的"换机周期"与"摆放环境"。**

> **原文（p129，KOODI 的 12 码全名，p104 脚注给出）**：
> 「**12 styles – folklore, deluxe, kitsch, porno, toy, cartoon, sport, pseudo-eco, army, professional, space, and "white"** – as part of the Industrial Design Program at Helsinki.」

> **★★★ 判据：12 个风格码就是 12 套 CMF 配方。这张表可以直接当"风格码字典"用。**
> 注意 **"white"** 是独立的一个码 —— 说明"白色"在这套体系里不是缺省值，而是一种风格主张。
> （原文未给 12 码各自的 C/M/F 明细，只给了其中 3 码的文字描述；其余 9 码为空白，见 §3.7。）

---

## 3.6 C 层判据总表（共 24 条）

| # | 判据 | 出处 |
|---|---|---|
| 1 | **★★★★★ 光谱分析对设计帮助不大**：「Color can be quantified by analyzing spectra but this – from a design standpoint – **doesn't help much**」 | p93 |
| 2 | **★★★★★ 有效方法是颜色匹配 + 色号**：「A more effective method is one of **color matching**, using color charts such as those provided by Pantone; **once a match is found it can be described by the code that each color carries**」 | p93 |
| 3 | **★★★★ 色彩联想被外包给 Pantone**：「**good descriptions of the associations and perceptions of color**」 | p93 / p105 |
| 4 | **★★★★★ 技术不动只动 C/F 做系列**：「a series of products, **technically identical, but differing in color, texture, pattern, and styling**」 | p32 |
| 5 | **★★★★ 系列要命名**："Calypso Beach" / "Lolita" / "Graffiti"；「**some 1,000 designs of a single technical innovation**」 | p32 |
| 6 | **★★★ 价格过线后卖 CMF**：「**it must appeal in some way to the consumer's sense of style, taste, and individuality**」 | p32 |
| 7 | **★★★★ 透明度四级**：「**opaque, translucent, transparent, and water-clear or optical quality**」 | p93 |
| 8 | **★★★★ 最便宜的透明聚合物**：「**pet, ps, and pmma**」；酚醛/多数 ABS/碳填充为半透或不透 | p93 |
| 9 | **★★★ 透明的前提是无定形**：「**For transparency the polymer must be amorphous; partial crystallinity gives translucency.**」 | p247 |
| 10 | **★★★★★ 原色用于区分功能部件**：「**primary colors that distinguish functional parts**」 | p129 |
| 11 | **★★★★ 强度感靠低饱和 + 强纹理**：「**Subdued color.**」「**Use of texture to create contrasts.**」 | p128 |
| 12 | **★★★★ 暗色 = 内敛奢华**：「**conservative, discrete luxury, captured by the use of dark colors and wood-like textures contrasting with matte and gloss-finished metallic surfaces**」 | p129 |
| 13 | **★★★★ 无反光黑化金属 = 粗野功能**：「**achieved through hard angular shapes with non-reflective blacked metal finish**」 | p129 |
| 14 | **★★★ 哑光黑 = 专业设备**：「**understated rectangular form, matte-black finish**」 | p131 |
| 15 | **★★★ 航空航天码含色彩**：「**extending to color and material (polished or matte aluminum)**」 | p131 |
| 16 | **★★★★★ 酚醛只有黑与棕**：「**Phenolics can be molded only in black or brown**; urea, melamine, alkyd, and polyester compounds are available in a wider range of colors」 | p248 |
| 17 | **★★★★ ABS 吃色 + 可做整体金属色**：「**It takes color well. Integral metallics are possible**」 | p261 |
| 18 | **★★★★★ SAN 会黄变**：「**depending on the amount of acrylonitrile … can vary from water white to pale yellow, but without a protective coating, sunlight causes yellowing and loss of strength**」 | p261 |
| 19 | **★★★★ PE 能上色不能印刷**：「accepts a wide range of colors … **but is difficult to print on**」 | p258 |
| 20 | **★★★★★ 玻璃颜色是配方不是涂层**：「**Nickel gives a purple hue, cobalt a blue, chromium a green, uranium a green-yellow, iron a green-blue**」 | p254 |
| 21 | **★★★★ 铝的着色靠膜孔吸染料，且看合金**：「The oxide is **micro-porous, allowing it to absorb dyes** … The ability of the film to accept dyes depends on **alloy composition: pure aluminum and Al-5 Mg alloys are well suited**」 | p372 |
| 22 | **★★★ 陶瓷改色必改光泽**：「**Glazes can be applied to ceramics for a smooth, glossy surface; patina surfaces are also possible**」 | p252 |
| 23 | **★★★★ 印刷类表面硬度只有 5–10**（丝印/移印/水转印）；IMD 10–500μm 膜内保护 | p360–p366 |
| 24 | **★★★★★ 颜色的意义会随时间变**：「**a product that appears aggressive or luxurious today can seem humorously retro or just plain ugly tomorrow**」 | p98 |

---

## 3.7 本章的空白（C 层必须诚实交代的部分）

> **这一节是本技能最重要的诚实声明。本书不是色彩书，以下逐项交代。**

| 缺什么 | 书中情况 | 该去哪查 |
|---|---|---|
| **色彩理论本身：色相/明度/纯度三属性** | **全书零覆盖。** grep `hue`/`saturation`/`color wheel`/`Itten` 全库仅命中：p235「Chromatic Series. Develop a chromatic series of materials, **as Itten suggested to his students in the Bauhaus course**」一句**作业题**、p254 玻璃发色的 `hue` 一词、p231 的颜料条目 | **`product-design-styling-dabbs` ch10 色彩**（含 Pantone 潮流、深色弱化、金属强调、语义选色） |
| **配色法则（互补/类似/分裂互补/三角）** | **零覆盖** | 同上；基础色彩学教材（Itten《色彩的艺术》） |
| **色彩对比的视觉机制（同时对比、边缘对比、面积效应）** | **零覆盖** | `visual-dynamics-industrial-design`（色彩与形态的视觉动力）；`design-elements-hannah`（视觉构成关系） |
| **色差判定标准（ΔE、容差）** | **零覆盖**。全书无 `ΔE`、无 `color difference`、无容差数值 | 印刷/涂料标准：ASTM D2244、ISO 12647；企业内部色差规程 |
| **色彩体系（NCS / Munsell / RAL / 中国国家标准色卡）** | **零覆盖**，只提 Pantone | 各体系官方色卡；Pantone 官方 |
| **色彩的心理/生理效应（冷暖、重量感、进退感）** | **只有两条联想例**：「the color black of death, the color red of weddings」(p45)；以及 p96「They accept almost any color」（陶瓷/玻璃） | `design-psychology-norman`（感知与情感）；色彩心理学专著 |
| **同色不同材质的"同色异谱"（metamerism）** | **零覆盖**。书中只说光泽取决于"材料与光滑度"(p82)，未提跨材质配色会走样 | 涂料/塑料配色实务；分光测色仪厂商技术手册 |
| **CMF 色板怎么做（实物色板、光照条件、观察者条件）** | **零覆盖**。只有 p79 一句「experiments show that **the best legibility** is given by a san serif typeface such as Helvetica or Arial, the use of lower-case letters except for initials, and **high contrast**」（讲的是文字可读性，不是配色） | 本技能 `patterns.md` P-01（实物色板配方）；`product-design-styling-dabbs` ch11 §11.9 的"打样验证" |
| **12 个 KOODI 码各自的完整 C/M/F 配方** | **只给了 3 码的文字描述**（保守奢华 / 玩具友好 / 粗野功能），其余 9 码（folklore, kitsch, porno, cartoon, sport, pseudo-eco, army, professional, space, "white"）**只有名字，无描述** | 原书引用源：University of Art and Design Helsinki (1995) "koodi Code", uiah Books, isbn 951-9384-97-9（见 p133 Further Reading） |
| **"动态色彩"的实现细节** | 只给品类名（photochromic / photosensitive / thermochromic / electrochromic），**无工艺参数、无寿命、无响应时间** | 特种涂料/玻璃供应商技术资料；本技能 §3.4.2 已列出原文所提的四个种类 |

> **★ 未读到声明**：本章覆盖的 p42–p108 区间**全部 67 页已逐页读**（含 p84–p92 的能量/CO₂ 段与 p99–p108 的 Further Reading 段）。
> **★ 另需声明**：为找齐色彩线索，本版额外 grep 了全库 391 页的 `colou?r`（命中见 §3.1–§3.5 各条），
> **未发现被遗漏的色彩方法论章节** —— 本书确实没有色彩章。这是书的空白，不是读的空白。

---

## 3.8 与其他章的连接

| 本章内容 | 关联章 | 关系 |
|---|---|---|
| 颜色要"能被编号"（p93） | 本技能 ch06 §6.6 | F 层同样要"能被编号"（光泽六级、涂层厚度μm） |
| 色彩与表面成对出现（p129 三码） | 本技能 ch06 §6.1 | 第 6 章展开"表面工艺决定色彩表现" |
| 色彩的分区功能（primary colors distinguish functional parts） | `product-design-styling-dabbs` ch10 色彩对比分区 | **互补**：Dabbs 讲"分区怎么切"，本章讲"分区用什么色" |
| 色彩的时代性与风格码 | `world-modern-design-history`（各运动与年代） | **同源**：p98 的风格谱系图与设计史教材的断代一致 |
| 色彩的联想（黑=死亡、红=婚礼） | `design-psychology-norman`（概念模型与文化限制） | 诺曼的"文化限制"解释为什么红在一种文化是婚礼在另一种是危险 |
| 玻璃/陶瓷本体着色不可修复 | `product-injection-defects`（色差脏污、发白顶白） | **接口**：涂层类色彩失效（掉漆/褪色）在注塑缺陷里是"色差脏污"类 |
| 12 风格码 → 12 套 CMF 配方 | 本技能 `patterns.md` P-04 | 本章给字典，patterns 给配方 |
| 色彩潮流锚定"当季"还是"家庭环境" | 本技能 ch07 §7.3（意向索引） | 第 7 章用"意图"来决定锚点 |
