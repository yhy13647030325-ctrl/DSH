# 第 2 章：修改器（官方 Reference 全译）

> **出处**：《Blender 2.92 Manual》`modeling/modifiers/**`（**59 个 xhtml / 166,605 字符**）
> **定位方式**：xhtml 文件路径（EPUB 无页码）
> **原文语种**：英文。本版为**中文正文 + 英文原文引用**
> **目标体量**：按原文 166,605 字符 × 35% ≈ **58,300 字**（ch01 实测比 19%，本章取 35% 因为修改器是"参数密集型"）
> **覆盖**：5 大类 59 个修改器 + 导论 + 通用选项

---

## 2.0 本章的结构

| 节 | 内容 | 原文文件 | 原文字符 | 目标字数 |
|---|---|---|---|---|
| **2.1** | **修改器导论**（四类 + 界面 + 栈） | `introduction` | 6,613 | ~4,600 |
| **2.2** | **通用选项**（顶点组 + 纹理） | `common_options` | 3,842 | ~2,700 |
| **2.3** | **Generate 类**（20 个） | `generate/*` | 57,328 | **~20,000** |
| **2.4** | **Deform 类**（17 个） | `deform/*` | 47,835 | **~16,700** |
| **2.5** | **Modify 类**（10 个） | `modify/*` | 29,161 | **~10,200** |
| **2.6** | **Physics 类**（9 个） | `physics/*` | 20,436 | **~7,150** |
| **2.7** | 三大主力纵览（Bevel/Subdiv/Solidify） | 交叉 | — | 综合 |
| **2.8** | 判据总表 | — | — | — |

> **★★★ 本章与 ch01 的差别**：
> **ch01 讲"编辑模式下的工具"（直接改几何）；**
> **本章讲"修改器"（非破坏性地改）—— 这是硬表面建模的真正主力。**

---

## 2.1 ★★★★★ 修改器导论（`introduction.xhtml`）

### 2.1.1 定义：什么是修改器

> **原文**：
> 「**Modifiers are automatic operations that affect an object's geometry
> in a non-destructive way.**
> With modifiers, you can perform many effects automatically that would otherwise
> be too tedious to do manually (such as subdivision surfaces) and without affecting
> the base geometry of your object.
> **They work by changing how an object is displayed and rendered,
> but not the geometry which you can edit directly.**」

**★★★★★ 修改器的三重身份（逐句拆）**：

| # | 属性 | 含义 |
|---|---|---|
| **1** | **自动操作（automatic）** | **一次设定，永久生效** |
| **2** | **★ 非破坏性（non-destructive）** | **★ 原始几何没被改动** |
| **3** | **改"显示与渲染"，不改"可编辑的几何"** | **编辑模式里看到的还是原始网格** |

> **★★★ 这是理解修改器的关键**：
> **改完修改器参数，`Tab` 进编辑模式，看到的仍是原始形状** ——
> **因为修改器是"渲染前的一道计算"，不是"真的改了数据"。**

**★★ "太繁琐以至于手工做不到"的例子**：
> **细分曲面（subdivision surfaces）** ——
> **手工细分一个模型要切几百刀，修改器一次搞定。**

### 2.1.2 修改器栈（Modifier Stack）

> **原文**：
> 「**You can add several modifiers to a single object to form The Modifier Stack
> and Apply a modifier if you wish to make its changes permanent.**
> They can be added to the active object using the Add Modifier drop-down menu
> at the top of their properties tab.
> **New modifiers are always added at the bottom of the stack (i.e. will be applied last).**」

**★★★★ 三条基本规则**：

| # | 规则 |
|---|---|
| **1** | **一个物体可加多个修改器 → 形成"栈"** |
| **2** | **★ 新加的修改器总是加在栈底（最后计算）** |
| **3** | **Apply（应用）= 让修改器的结果"变成真的"（永久）** |

### 2.1.3 ★★★★★ 四类修改器（原文分类，最重要的一条）

> **原文**：
> 「**There are four types of modifiers:**」

**★★★★★ 四类的原文定义与判据**：

| 类型 | 原文定义 | 关键特征 |
|---|---|---|
| **Modify** | 「**usually do not directly affect the geometry of the object,but some other data, such as vertex groups**」 | **★ 不改几何，改"其他数据"（如顶点组）** |
| **Generate** | 「**constructive/destructive tools that will affect the whole Topology of the mesh.They can change the general appearance of the object, or add new geometry to it**」 | **★ 改变拓扑 / 增加几何** |
| **Deform** | 「**only change the shape of an object, without altering its topology**」 | **★ 只改形状，不改拓扑** |
| **Simulate** | 「**represent physics simulations.** In most cases, they are automatically addedto the modifiers stack whenever a Particle System or Physics simulation is enabled.**Their only role is to define the position in the modifier stack from which is takenthe base data for the simulation they represent.** As such, they typically haveno attributes」 | **★ 只是个"占位符"，标记模拟从哪里开始** |

**★★★★★ 分类的记忆判据（一张表）**：

| 类型 | 改拓扑？ | 改形状？ | 典型代表 |
|---|---|---|---|
| **Modify** | **❌** | **❌** | **Weight Edit / Normal Edit / Vertex Weight** |
| **★ Generate** | **★ ✅ 会** | **✅** | **Subdivision / Array / Mirror / Boolean / Solidify** |
| **Deform** | **❌ 不会** | **✅** | **Simple Deform / Shrinkwrap / Wave / Displace** |
| **Simulate** | — | — | **Cloth / Fluid / Collision（自动添加）** |

> **★★★ 判据：**
> **"这个修改器会不会改变顶点数量？"**
> **会 → Generate；不会（只移动已有顶点）→ Deform。**
>
> **★ 这是最可靠的区分方式** ——
> **因为 Generate 增加几何（顶点数变），Deform 只挪位置（顶点数不变）。**

**★★ Simulate 的特殊性**：
> **它"没有属性"（no attributes）** ——
> **因为真正的参数在 Physics 属性面板里（如布料/流体设置）。**
> **★ 它在栈里的唯一作用是"标记：从这一层开始取基础数据做模拟"。**

### 2.1.4 ★★★★ 界面：面板头部的七个图标

> **原文**：
> 「**At the top is the panel header.
> The icons each represent different settings for the modifier (left to right):**」

| 图标 | 名称 | 作用 |
|---|---|---|
| **1** | **Expand（▾/▸）** | **展开/折叠面板** |
| **2** | **Type（类型图标）** | **★ 快速识别这是哪类修改器** |
| **3** | **Name（名称）** | **★ 同一物体内必须唯一；不同物体可重名** |
| **4** | **★ Show on Cage（网格-三角图标，仅网格）** | **★ 直接编辑"修改后"的几何** |
| **5** | **Show in Edit Mode（方块图标）** | **编辑模式里显示修改后的结果** |
| **6** | **Show in Viewport（屏幕图标）** | **视口可见性** |
| **7** | **Render（相机图标）** | **渲染可见性** |

**★★★★★ 「Show on Cage」有一个必须知道的警告（原文 Warning）**：

> **原文**：
> 「**While it shows edited items in their final, modified positions,
> you are still actually editing original data.
> This can lead to strong and unpredictable effects with some tools,
> and should be disabled whenever you need to perform complex or precise editing on the mesh.**」

**★★★★★ 陷阱：显示的是"改后位置"，编辑的却是"原始数据"**：

| 看到什么 | 实际在改什么 |
|---|---|
| **★ 修改后的顶点位置** | **★ 原始顶点数据** |

> **★★★ 后果**：
> **你拖动"看起来在这里"的点，实际改的是"原始位置上"的点** ——
> **结果会"跳"或产生难以预料的变化。**
>
> **★ 判据：做复杂/精确编辑时，必须关掉 Show on Cage。**

**★★ 「Apply On Spline Points」（仅曲线/曲面/文本）**：
> **原文**：「**Apply the whole modifier stack up to and including that one
> on the curve or surface control points, instead of their tessellated geometry.**」

| 项 | 说明 |
|---|---|
| **适用** | **曲线 / 曲面 / 文本** |
| **作用** | **★ 对"控制点"应用修改器，而不是对"细分后的几何"** |
| **默认** | **★ 曲线/文本/曲面默认会先转成网格再算修改器** |

> **★★ 为什么这条重要**：
> **曲线是"控制点 + 插值"的** ——
> **默认会把曲线"细分（tessellate）成网格"再算，控制点就失去了意义。**
> **★ 开这个选项，修改器才能"作用在控制点上"，保持曲线可编辑。**

### 2.1.5 ★★★★★ Specials：Apply 与"陷阱"

> **原文（Specials 列表）**：

| 操作 | 快捷键 | 作用 |
|---|---|---|
| **★ Apply（应用）** | **`Ctrl-A`** | **★ 把修改器"变真"，并删除该修改器** |
| **Apply as Shape Key** | — | **把结果存成"形态键"，再删除修改器** |
| **Save as Shape Key** | — | **把结果存成形态键，但保留修改器** |
| **Copy to Selected** | — | **把修改器复制到所有选中物体** |
| **Duplicate** | **`Shift-D`** | **在下方复制一个** |
| **Move to First/Last** | — | 移到栈顶/栈底 |
| **Delete** | **`X`** | 删除 |
| **Move** | **`::::`（拖动）** | **★ 上下移动，改变计算顺序** |

**★★★★★ Apply 的两个致命陷阱（原文 Warning + Note）**：

**陷阱①：Apply 非栈顶的修改器会忽略栈顺序**

> **原文**：
> 「**Applying a modifier that is not first in the stack will ignore the stack order
> (it will be applied as if it was the first one), and may produce undesired results.**」

**★★★★ 完整解释**：

```
栈顺序：  [Mirror] → [Subdivision]
           （先镜像，再细分）

若直接 Apply 第二个（Subdivision）：
   ★ 它会被"当作第一个"来应用
   ★ 即在"未镜像的原始网格"上做细分
   → 结果与"看到的不一样"
```

> **★★★ 判据：要 Apply 某个修改器，先把它移到栈顶（Move to First）。**

**陷阱②：Apply as Shape Key 只对"不改拓扑"的修改器有效**

> **原文**：
> 「**This is only available with modifiers that do not affect the topology
> (typically, Deform modifiers only).**」
> 「**Note：Even though it should work with any geometry type that supports shape keys,
> currently it will only work with meshes.**」

| 项 | 限制 |
|---|---|
| **能用于** | **★ 只有"不改拓扑"的修改器（即 Deform 类）** |
| **几何类型** | **★ 目前只支持网格**（虽然理论上任何支持形态键的类型都行） |

> **★★ 为什么"不改拓扑"才能存形态键**：
> **形态键的原理是"记录每个顶点的位移"** ——
> **如果顶点数量变了，就没有"一一对应"可记。**
> **★ 这与 §2.1.3 的"Generate 改拓扑"完全对应。**

### 2.1.6 ★★★★★ 栈顺序决定结果（原文的实测示例）

> **原文**：
> 「**In a modifier stack, the order in which modifiers are applied has an effect on the result.
> Therefore the modifiers can be re-arranged by clicking the grab widget (::::)
> in the top right, and moving the selected modifier up or down.**」
> 「**Modifiers are calculated from top to bottom in the stack.**」

**★★★★★ 两个顺序的实测对比（原文给的例子，本节最有价值）**：

> **原文**：
> 「**For example, the image below shows Subdivision Surface and Mirror modifiers
> that have switched places.**
> **The Mirror modifier is the last item in the stack and the result looks like two surfaces.**
> **The Subdivision Surface modifier is the last item in the stack and the result
> is a single merged surface.**
> **In this example, the desired result (on right) is achieved by first mirroring the object,
> and then calculating the subdivision surface.**」

**★★★★★ 完整对照表（务必记住）**：

| 栈顺序 | 结果 |
|---|---|
| **[Subdivision] → [Mirror]** | **★ 看起来像"两个分开的表面"**（先细分各自圆化，再镜像 → 中间有缝） |
| **★ [Mirror] → [Subdivision]** | **★ "一个合并的连续表面"**（先镜像成整体，再整体细分 → 中间平滑过渡） |

> **★★★ 判据（硬表面必记）：**
> **要"对称且连续"的曲面 → 先 Mirror 后 Subdivision。**
> **★ 反之会得到"中间有一道沟"的模型。**

> **★★ 为什么"先细分再镜像"会有缝**：
> **细分会把物体"向内收缩"（Catmull-Clark 的特性）** ——
> **收缩后镜像，两个半球之间就出现了间隙。**
> **★ 而"先镜像再细分"，边界的顶点会被"跨中线"计算，缝就消失了。**

### 2.1.7 ★★★ Active Modifier（活动修改器）

> **原文**：
> 「**A modifier in the stack can be selected to mark in as Active,
> the active modifier displays an outline around the modifier's panel.**
> To set an active modifier, select an area of the modifier's panel background,
> the modifier's icon, or, select a modifier in the Outliner.
> **The active modifier is used by the Geometry Node Editor
> to determine which node group is being modified.**」

| 项 | 说明 |
|---|---|
| **视觉标识** | **面板外有一圈轮廓** |
| **如何设置** | **点面板背景 / 点图标 / 在 Outliner 里选** |
| **★ 用途** | **★ Geometry Node Editor 用它决定"在改哪个节点组"** |

---

## 2.2 ★★★★★ 通用选项（`common_options.xhtml`）

> **★ 原文 3,842 字符**，许多修改器共享同一套参数。

> **原文**：
> 「**Some options are commonly used by many modifiers, and share the same behavior
> across all of those. In particular, many offer ways to precisely mask and weight
> their effect on a vertex basis (using either vertex groups and/or textures).**」

### 2.2.1 ★★★★★ 顶点组（Vertex Group）

> **原文**：
> 「**Vertex Groups are an easy way to control which vertices are affected by a modifier,
> and to which extent (using their weights).
> They are available when modifying meshes or lattices.**」

**★★ 两个参数**：

| 参数 | 作用 |
|---|---|
| **Vertex Group** | **★ 选择顶点组的名字** |
| **★ Invert `<->`** | **★ 反转影响（组内变成"不受影响"）** |

**★★★★★ 一个必须知道的陷阱：顶点组是"按名字"引用的**

> **原文（Warning）**：
> 「**The group is referenced by its name. That means that if you rename it,
> the link to the renamed vertex group will be lost by all modifiers using it
> (their field will turn red), and you'll have to select the proper group again in all of them.**」

**★★★★ 重命名顶点组 → 所有引用它的修改器"断链"**：

| 现象 | 说明 |
|---|---|
| **修改器里的顶点组字段变红** | **★ 表示"找不到这个组"** |
| **需要手动重新选择** | **每个用到它的修改器都要重选** |

> **★★★ 判据：给顶点组起名后就不要再改** ——
> **因为改一次要修很多处。**
> **★ 这个坑在"顶点组很多"的硬表面模型里特别容易踩。**

**★★ Invert 的原理（原文）**：
> 「**Inverts the influence of the selected vertex group, meaning that the group
> now represents vertices that will not be deformed by the modifier.
> The setting reverses the weight values of the group.**」

> **★★ 它不是"换一个组"，而是"把该组的权重取反"（1-w）。**
> **★ 所以"权重 1 的点"变成"不受影响"，"权重 0 的点"变成"完全受影响"。**

### 2.2.2 ★★★★★ 纹理（Texture）

> **原文**：
> 「**Those options allow to use any kind of image (including parametric ones)
> to control the modifier's effect.
> Most of the time, only the value (grayscale) of the texture is used,
> but in some cases (like with some modes of the Displace modifier),
> the whole RGB color components might be exploited.**」

**★★★ 核心：纹理作为"驱动器"** ——
> **它不显示出来，而是"用纹理的明暗（或颜色）来控制每个顶点被影响的程度"。**

| 参数 | 作用 |
|---|---|
| **Texture** | **选择纹理数据块** |
| **★ Texture Coordinates** | **★ 用哪套坐标取值（5 种）** |
| **★ Use Channel** | **★ 用哪个通道当数值源** |

### 2.2.3 ★★★★★ 五种纹理坐标（本节最实用）

| 坐标类型 | 含义 | 特点 |
|---|---|---|
| **★ UV** | **从面的 UV 坐标取值** | **★ 需要物体有 UV** |
| **Object** | **★ 从另一个物体的坐标系取值** | **★ 移动那个物体会改变映射** |
| **Global** | **从全局坐标系取值** | **物体移动时纹理"不动"** |
| **Local** | **★ 从物体自身坐标系取值** | **★ 物体移动时纹理"跟着走"** |
| **（默认）** | **Local** | 字段留空时回退到 Local |

**★★★★★ Local vs Global 的判据（最容易混）**：

| 坐标 | 物体移动时，纹理图案 | 用于 |
|---|---|---|
| **Local** | **★ 跟着物体移动** | **★ 想"纹理属于物体"**（如木纹） |
| **Global** | **★ 固定在空间不动** | **想"纹理属于环境"**（如水波穿过） |
| **Object** | **跟着"指定物体"移动** | **想让纹理随"另一个物体"动** |

> **★★★ 判据：**
> **想让"移动物体时纹理跟着"→ Local；**
> **想让"移动物体时纹理'划过'物体"→ Global。**
> **★ 这是做"位移贴图（Displace）"时最关键的设置。**

**★★ UV 坐标的一个已知缺陷（原文 Note）**：
> 「**Since UV coordinates are specified per face, the UV texture coordinate system
> currently determines the UV coordinate for each vertex from the first face
> encountered which uses that vertex. Any other faces using that vertex are ignored.
> This may lead to artifacts if the mesh has non-contiguous UV coordinates.**」

| 项 | 说明 |
|---|---|
| **问题** | **★ 一个顶点被多个面共享，但每个面的 UV 可能不同** |
| **处理** | **★ 只取"第一个遇到的面"的 UV，其余忽略** |
| **后果** | **★ UV 不连续时会产生 artifact** |

> **★★ 判据：用 UV 坐标驱动修改器时，模型必须"UV 连续"** ——
> **即接缝不能穿过"被同一个修改器影响的区域"。**
> **★ 否则接缝处会出现"跳变"。**

**★★ Object 坐标的一个重要提示（原文 Note）**：
> 「**Moving the original object will also result in a texture coordinate update.
> As such, if you need to maintain a displacement coordinate system while moving
> the modified object, consider parenting the coordinate object to the modified object.**」

> **★★ 想"移动物体但保持位移不变" → 把坐标物体设为该物体的子级。**
> **★ 因为父子关系会让"相对位置"保持不变。**

### 2.2.4 ★★★ Use Channel（取值通道）

> **原文**：
> 「**Which channel to use as value source
> (only available with a few modifiers currently, others follow the Intensity behavior,
> unless otherwise specified).**」

| 通道 | 含义 |
|---|---|
| **★ Intensity（默认）** | **★ RGB 的平均值**（原文例：RGB(1.0, 0.0, 0.0) → 值 0.33） |
| **Red / Green / Blue** | **单一颜色通道的值** |
| **Alpha** | 透明度通道 |
| **Hue** | **HSV 色相** |

> **★★★ 默认的 Intensity 是"三通道平均"** ——
> **所以一张"纯红"的图，Intensity 只有 0.33，不是 1.0。**
> **★ 想让"纯红=最大影响"，必须显式选 Red 通道。**

---

## 2.3 ★★★★★ Generate 类（20 个修改器 / 57,328 字符）

> **★★★ "Generate"的定义（§2.1.3）：改拓扑 / 增加几何。**
> **★ 这一类是硬表面的**主力中的主力** ——**
> **Bevel、Solidify、Subdivision、Array、Mirror、Boolean 全在这里。**
> **目标字数：~20,000**

### 2.3.1 ★★★★★ Bevel（倒角修改器，7,959 字符）

> **★ 与 ch01 §1.7 的"`Ctrl-B` 编辑模式倒角"是**同一功能**，但非破坏性。**

**★★★★★ 为什么用修改器而不是 `Ctrl-B`**：

| 方式 | 可调 | 后果 |
|---|---|---|
| **`Ctrl-B`（编辑模式）** | **❌ 立刻改几何** | **改完要重做** |
| **★ Bevel 修改器** | **★ ✅ 参数随时可改** | **★ 保留原始网格** |

> **★★★ 判据：硬表面的倒角**一律用修改器** ——**
> **因为你一定会反复调宽度。**

**★★★★ 关键参数（与 `Ctrl-B` 同名，但多出几项）**：

| 参数 | 含义 | 与 `Ctrl-B` 的差别 |
|---|---|---|
| **Amount** | **倒角宽度** | 同名 |
| **Segments** | **段数（1=斜切，2~3=硬表面常用）** | 同名 |
| **★ Limit Method** | **★ 按什么限定倒角范围** | **★ 修改器独有** |
| **★ Angle** | **★ 角度阈值**（配合 Limit Method） | 修改器独有 |
| **★ Width Type** | 宽度度量方式 | 同名 |
| **★ Clamp Overlap** | **限制重叠（必开）** | 同名 |
| **Profile** | 剖面形状（0.5=正圆） | 同名 |
| **★ Vertex Group** | **★ 限定到某顶点组** | **★ 修改器独有** |

**★★★★★ 「Limit Method」是修改器的核心优势**：

| 值 | 含义 |
|---|---|
| **None** | **★ 倒角所有边** |
| **★ Angle** | **★ 只倒"夹角 ≥ Angle 阈值"的边**（最常用） |
| **Weight** | **★ 只倒"标记了 Bevel Weight 的边"**（配合 ch01 §1.9.3） |
| **Vgroup** | **只倒属于某顶点组的边** |

> **★★★ 两个最实用的组合**：
> | 需求 | 设置 |
> |---|---|
> | **"自动给所有硬边倒角"** | **Limit Method = Angle，Angle = 30°** |
> | **★ "只给这几条边倒角"** | **★ 编辑模式标记 Bevel Weight → Limit = Weight** |

> **★★ 这解决了 `Ctrl-B` 的最大痛点**：
> **`Ctrl-B` 只能"手动选边"，而修改器能"按规则自动选边"。**

### 2.3.2 ★★★★★ Solidify（加厚，6,450 字符）

> **★★ 作用：给"没有厚度的面"生成厚度。**

**★★★★ 核心参数**：

| 参数 | 含义 |
|---|---|
| **★ Thickness** | **★ 总厚度** |
| **★ Offset** | **★ 厚度分布在原面的哪一侧**（-1 / 0 / +1） |
| **★ Even Thickness** | **★ 均匀厚度**（避免尖角处变薄） |
| **★ Rim** | **★ 边缘是否封口** |
| **★ Only Rim** | 只生成边（不加厚面） |
| **★ Material Index Offset** | **给内侧/边缘指定不同材质** |

**★★★★★ 「Offset」的三种取值（最易错）**：

| Offset | 厚度分布 |
|---|---|
| **-1** | **★ 全部往"法线负方向"长**（原面保持在外侧） |
| **0** | **★ 两侧各一半**（原面在中间） |
| **+1** | **全部往"法线正方向"长**（原面保持在内侧） |

> **★★★ 判据：**
> **想让"原面"就是"最终的外表面"→ Offset = -1。**
> **★ 这是导入曲面"变成实体"时最常用的设置**（保持外形不变）。

**★★★★★ 「Even Thickness」为什么重要**：

> **★★ 默认（不开）时，锐角处的厚度会"变薄"** ——
> **因为厚度是沿法线偏移，法线在锐角处会"汇聚"。**

| 设置 | 锐角处厚度 |
|---|---|
| **Even Thickness 关** | **★ 变薄**（可能薄到 0） |
| **★ Even Thickness 开** | **★ 保持均匀**（但可能产生自交） |

> **★★ 判据：做"结构件"必开；做"薄壳/外观件"可以不开。**

### 2.3.3 ★★★★★ Subdivision Surface（细分曲面，6,142 字符）

> **★★ 作用：把"低模"细分成"高模"，并让表面变圆。**

**★★★★★ 两种细分方式（本节最重要）**：

| 算法 | 名称 | 顶点位置 |
|---|---|---|
| **★ Catmull-Clark** | **★ 传统细分** | **★ 顶点会"向内收缩"（趋近曲面）** |
| **★ Simple** | **简单细分** | **★ 顶点位置不变（只加密，不变圆）** |

> **★★★ 判据：**
> **要"变圆"→ Catmull-Clark（默认）；**
> **★ 只想要"更多顶点但保持形状"→ Simple。**

**★★ 核心参数**：

| 参数 | 含义 |
|---|---|
| **★ Levels Viewport** | **★ 视口显示级别**（1~6） |
| **★ Render** | **★ 渲染级别**（可高于视口） |
| **★ Quality** | 质量（影响平滑度） |
| **★ UV Smooth** | **★ UV 如何随细分平滑** |
| **★ Boundary Smooth** | **★ 边界的处理方式** |
| **★ Use Creases** | **★ 是否使用 Crease 折痕**（配合 ch01 §1.9.3） |

**★★★★★ 四个必知参数的作用**：

**① Levels 分开设（Viewport 低，Render 高）**
> **★★ 这是性能优化的标准做法** ——
> **视口用 1~2 级看效果，渲染用 3~4 级出图。**

**② ★ Use Creases（配合 Crease 折痕）**
> **★★ 这是"细分但保留尖角"的关键** ——
> **在 ch01 §1.9.3 标记的 Crease，这里勾上才生效。**
> **★ Crease = 1.0 的边，细分后完全保持锐利。**

**③ ★ Boundary Smooth（边界处理）**
> **★★ 模型有"开放边界"（如 Mirror 之前的半边）时，这个参数决定边界怎么收。**

| 值 | 效果 |
|---|---|
| **Keep Corners** | **★ 保持边界形状** |
| **All** | **边界也平滑（会收缩）** |

**④ ★ UV Smooth**
> **★★ 控制细分时 UV 怎么插值** ——
> **避免细分后"贴图错位"。**

### 2.3.4 ★★★★★ Mirror（镜像，4,155 字符）

> **★ 与 ch01 §1.11.1 的 `Ctrl-M` 是同一几何操作，但非破坏性。**

**★★★★ 核心参数**：

| 参数 | 含义 |
|---|---|
| **★ Axis（X/Y/Z）** | **★ 沿哪个轴对称** |
| **★ Mirror Object** | **★ 用另一个物体的坐标作为对称面** |
| **★ Bisect（X/Y/Z）** | **★ 沿对称面"切掉"超出的一半** |
| **★ Flip** | 翻转方向 |
| **★ Use Clipping** | **★ 防止顶点"穿过"对称面** |
| **★ Merge** | **★ 合并中线上的重合顶点** |
| **★ Merge Threshold** | 合并的距离阈值 |

**★★★★★ 三个最实用的参数**：

**① ★ Bisect（沿对称面切掉多余部分）**
> **★★ 做"半边模型"时必开** ——
> **因为它会把"越过中线的部分"切掉，保证对称面干净。**
> **★ 不开的话，"越过中线"的几何会被镜像成"两份重叠"。**

**② ★ Use Clipping（防穿越）**
> **★★ 拖动中线附近的顶点时，它会被"粘"在对称面上不穿过去。**
> **★ 这是"编辑半边模型不破坏对称"的关键。**

**③ ★ Merge + Merge Threshold（合并中线顶点）**
> **★★ 不开 Merge 的话，中线会有"两排重合的顶点"** ——
> **导致细分出现缝隙、法线异常。**
> **★ 默认阈值 0.001，通常够用。**

> **★★★ 硬表面标准设置**：
> ```
> Axis = X
> ☑ Bisect（X）
> ☑ Use Clipping
> ☑ Merge
> Merge Threshold = 0.001
> ```

### 2.3.5 ★★★★★ Array（阵列，4,362 字符）

> **★★ 作用：把物体"复制成规律排列的多个"。**

**★★★★ 两种模式**：

| 模式 | 参数 | 用于 |
|---|---|---|
| **★ Fixed Count** | **★ Count（数量）+ Offset（位移）** | **★ 等距排列** |
| **★ Fit Curve / Fit Length** | **★ 按长度/曲线自动决定数量** | **★ 沿曲线铺满** |

**★★ 核心参数**：

| 参数 | 含义 |
|---|---|
| **★ Count** | **★ 总数（含原始物体）** |
| **★ Offset（X/Y/Z）** | **★ 相对位移**（以物体尺寸为单位） |
| **★ Constant Offset** | **★ 绝对位移** |
| **★ Relative Offset** | **★ 相对位移（按物体尺寸倍数）** |
| **★ Object Offset** | **★ 用另一个物体的变换作为"每份的增量"** |
| **★ Merge** | 合并相邻顶点的距离阈值 |
| **★ First/Last** | 首尾是否"开口"（用于管道类） |

**★★★★★ 「Object Offset」是 Array 最强大的参数**：

> **★★ 原理**：
```
Object Offset = 一个"空物体（Empty）"
   ↓ 每一份的变换 = 上一份 × 空物体的变换
   ↓
★ 如果空物体"旋转 10°" → 每份都多转 10° → 形成"圆周阵列"
★ 如果空物体"缩放 0.9" → 每份缩小 10% → 形成"递减阵列"
```

> **★★★ 判据：**
> **要"圆周阵列"→ 用一个绕中心旋转的 Empty 作 Object Offset。**
> **★ 这是硬表面里做"螺栓圈/齿圈"的标准手法。**

**★★ 两种 Offset 的数学关系（易混）**：

| 类型 | 位移量 |
|---|---|
| **Relative Offset = 1.0** | **★ 移动"一个物体尺寸"** |
| **Constant Offset = 1.0** | **★ 移动"1 个 Blender 单位"**（与物体大小无关） |

> **★★ 所以"Relative 更适合"因为物体改大小时阵列自动适应。**

### 2.3.6 ★★★★★ Boolean（布尔，2,676 字符）

> **★ 与 ch01 §1.16.3 的编辑模式布尔是同一运算，但非破坏性。**

**★★★★ 三种运算 + 三个关键选项**：

| 参数 | 含义 |
|---|---|
| **★ Operation** | **★ Union（并）/ Difference（差）/ Intersect（交）** |
| **★ Object** | **★ 用哪个物体做运算对象** |
| **★ Solver** | **★ Fast / Exact（两种求解器）** |
| **★ Self Intersection** | 允许自交 |
| **★ Hole Tolerant** | 容错模式 |

**★★★★★ 「Solver」的两种选择（本节最重要）**：

| Solver | 特点 | 用于 |
|---|---|---|
| **★ Fast** | **★ 快，但处理复杂相交会出错** | **简单形状** |
| **★ Exact** | **★ 慢，但结果可靠** | **★ 复杂/重叠的相交** |

> **★★★ 判据：布尔结果"错乱/缺面/多面"→ 换 Exact 求解器。**
> **★ 这是解决布尔问题最有效的一步。**

**★★★ Exact 独有的两个选项**：
> **Self Intersection（允许自交）** 和 **Hole Tolerant（容错）** ——
> **只在 Exact 下可用**，用于处理"脏模型"。

**★★★★ 一个必知的边缘情况**：
> **布尔运算依赖"法线方向"判断内外** ——
> **如果运算对象的法线反了，结果会完全相反（差集变成并集）。**
> **★ 所以布尔出问题时，先 `Shift-N`（ch01 §1.9.1）。**

### 2.3.7 ★★★★ 其余 Generate 类（14 个）

| 修改器 | 原文字符 | 作用 | 关键点 |
|---|---|---|---|
| **★ Skin** | **3,806** | **★ 用"顶点链"生成带厚度的骨架** | **每个顶点可设"半径"** |
| **★ Multiresolution** | **3,159** | **多分辨率（可"降级"/"升级"）** | **★ 用于雕刻后再做细节** |
| **★ Decimate** | **3,089** | **★ 减面** | **Collapse / Un-Subdivide / Planar 三种** |
| **★ Wireframe** | **2,337** | **★ 把边变成有厚度的"线框实体"** | 用于"桁架/笼子" |
| **★ Remesh** | **2,054** | **★ 重建网格（重新布线）** | **Voxel / Octree / Quad 三种** |
| **Mesh to Volume** | **1,642** | 把网格变成体积 | 配合体积渲染 |
| **★ Edge Split** | **1,574** | **★ 按角度/标记拆边** | **★ 让"平滑"与"锐利"共存（旧方案）** |
| **Build** | 1,482 | 逐面"长出来"的动画 | 建模动画 |
| **★ Screw** | **1,475** | **★ 螺旋/车削（同 ch01 §1.14）** | **修改器版可调** |
| **Volume to Mesh** | 1,432 | 体积转网格 | — |
| **★ Triangulate** | **1,071** | **★ 全部三角化** | **导出前必做** |
| **Mask** | 1,017 | 用顶点组做"遮罩"（配合雕刻） | — |
| **★ Weld** | **914** | **★ 按距离合并顶点（同 ch01 的 Merge by Distance）** | 非破坏性 |
| **Geometry Nodes** | 532 | 节点式生成（2.92 刚引入） | 后续版本主力 |

**★★★★★ 四个最值得记住的**：

**① `Edge Split`：Auto Smooth 出现前的"锐边方案"**
> **★★ 原理**：**按角度把边"物理拆开"**（顶点复制一份）——
> **拆开后两边各自平滑，中间就"看起来锐利"。**
> **★ 缺点**：真的增加了顶点（拓扑被破坏）。
> **★ 现在首选 Auto Smooth（ch01 §1.1.5），Edge Split 只在必要时用。**

**② `Triangulate`：导出前必做**
> **★★ 因为很多引擎/格式不支持四边形** ——
> **提前三角化，保证"导出的形状与看到的一致"。**

**③ `Weld`：非破坏性的"合并重复点"**
> **★★ 与 ch01 的 `M → By Distance` 同一功能，但不改原网格。**

**④ `Decimate` 的三种模式**
> **Collapse（塌陷，按比例减面）/ Un-Subdivide（反细分）/ Planar（按平面合并）**
> **★ 硬表面用 Planar 效果最好**（因为它会把共面的面合并）。

---

## 2.4 ★★★★★ Deform 类（17 个修改器 / 47,835 字符）

> **★★★ "Deform"的定义（§2.1.3）：只改形状，不改拓扑。**
> **★ 判据：顶点数量不变，只是"位置被挪动"。**
> **目标字数：~16,700**

### 2.4.1 ★★★★★ Simple Deform（简单形变，5,482 字符）

> **★★ 这是 Deform 类里最大的一篇，也是硬表面最常用的形变器。**

**★★★★★ 五种形变模式（一个修改器，五种玩法）**：

| 模式 | 作用 | 典型用途 |
|---|---|---|
| **★ Twist（扭转）** | **★ 绕轴扭转** | **钻头、麻花纹** |
| **★ Bend（弯曲）** | **★ 绕轴弯曲** | **★ 管路、弯头** |
| **★ Taper（锥化）** | **★ 一端细一端粗** | **锥形件、天线** |
| **★ Stretch（拉伸）** | **★ 沿轴拉伸/压缩** | 弹性件 |
| **★ 组合（多轴）** | 可同时作用于多个轴 | — |

**★★★★ 核心参数**：

| 参数 | 含义 |
|---|---|
| **★ Deform Method** | **★ 五种模式选一** |
| **★ Angle** | **★ 形变角度（Twist/Bend 用）** |
| **★ Factor** | **★ 形变强度（Taper/Stretch 用，-1~1）** |
| **★ Axis（X/Y/Z）** | **★ 沿哪个轴形变** |
| **★ Origin** | **★ 形变的"支点"（默认物体原点）** |
| **★ Limits（Upper/Lower）** | **★ 只让"某个范围"受形变** |

**★★★★★ 「Bend」的一条关键设置（最易错）**：

> **★★ Bend 的效果取决于"物体原点在哪"** ——
> **因为它是"绕原点弯曲"。**

| 想要 | Origin 应设在 |
|---|---|
| **从一端开始弯** | **★ 那一端的端点** |
| **从中间弯（对称）** | **★ 物体中心** |

> **★★★ 判据：Bend 结果"怪"→ 先检查 Origin。**
> **★ 可以在修改器里用 `Origin` 字段指定"另一个物体"作为支点。**

**★★ 「Limits」的用途**：
> **只让"部分"参与形变** ——
> **Upper 和 Lower 定义"受影响的范围"（其余部分保持原样）。**
> **★ 这让"部分弯曲"成为可能，而不是"整体弯曲"。**

### 2.4.2 ★★★★★ Shrinkwrap（收缩包裹，4,388 字符）

> **★★ 作用：让物体"贴到"另一个物体的表面。**

**★★★★★ 四种 Wrap Method（本节最重要）**：

| 方式 | 原理 | 用于 |
|---|---|---|
| **★ Nearest Surface Point** | **★ 每个顶点"就近"贴到目标表面** | **★ 通用（最常用）** |
| **★ Project** | **★ 沿指定方向"投影"到目标** | **★ 有明确方向时** |
| **★ Nearest Vertex** | **贴到最近的"顶点"** | **点云/低模** |
| **★ Target Normal Project** | **沿"目标法线"投影** | **贴细节** |

**★★★★ 核心参数**：

| 参数 | 含义 |
|---|---|
| **★ Target** | **★ 包裹到哪个物体** |
| **★ Offset** | **★ 距目标表面的距离（可正可负）** |
| **★ Wrap Method** | **★ 四种方式** |
| **★ Wrap Mode** | **★ Inside / Outside / On Surface / Outside Surface** |
| **★ Vertex Group** | 限定哪些顶点参与 |
| **★ Snap Mode** | **★ 是否真的"移动顶点"还是只"显示"** |

**★★★★★ 「Wrap Mode」的四种选择（极易混）**：

| 值 | 结果 |
|---|---|
| **Inside** | **贴到"目标内部"一侧** |
| **Outside** | **贴到"目标外部"一侧** |
| **★ On Surface** | **★ 正好在表面上** |
| **★ Outside Surface** | **★ 在外表面（保持厚度）** |

> **★★★ 判据：想让"加厚后的壳"包在外面 → Outside Surface。**

**★★ 硬表面的典型用途**：
> **① 给"履带"贴到"轮子"的曲面（hard-surface ch10）**
> **② 给"装甲板"贴到"车体"曲面**
> **③ 让"贴花/细节"贴合曲面**

### 2.4.3 ★★★★★ Laplacian Smooth / Laplacian Deform（3,772 + 3,145）

> **★★ 与 ch01 §1.15.2 的"Laplacian 保形平滑"同一算法，此处是修改器版。**

| 参数 | 含义 |
|---|---|
| **★ Lambda** | **★ 主平滑强度** |
| **★ Lambda Border** | **★ 边界（开放边）的平滑强度** |
| **★ Repeat** | 迭代次数 |
| **★ Preserve Volume** | **★ 保持体积（关键）** |

**★★★★★ 「Preserve Volume」是 Laplacian 的核心优势**：

| 设置 | 结果 |
|---|---|
| **关** | **★ 平滑会缩小体积**（同普通平滑） |
| **★ 开** | **★ 体积基本保持**（用于"保形磨平"） |

**★★ Laplacian Deform（3,145）是另一回事**：
> **它把"当前形状"记录为基准，然后让物体"尽量回到那个形状"** ——
> **用于"编辑后恢复"（类似"记忆形状"）。**

### 2.4.4 ★★★★★ Wave（波浪，3,747 字符）

> **★★ 作用：给物体加"波浪形起伏"。**

**★★★★ 核心参数**：

| 参数 | 含义 |
|---|---|
| **★ Type（Bands/Rings）** | **★ 平行波纹 / 同心圆波纹** |
| **★ Height** | **★ 波高（振幅）** |
| **★ Width** | **★ 波长** |
| **★ Narrowness** | **★ 波峰的尖锐度** |
| **★ Speed** | **★ 动画速度（可做水流）** |
| **★ Vertex Group** | 限定范围 |

**★★★★★ 两种 Type 的判据**：

| Type | 波纹形状 | 用于 |
|---|---|---|
| **★ Bands** | **★ 平行的直线波** | **水面（单向风）** |
| **★ Rings** | **★ 同心圆波** | **★ 水滴落水（圆形扩散）** |

> **★★ 硬表面里 Wave 用得不多，但"Rings + Speed"能做"能量护盾/水面"效果。**

### 2.4.5 ★★★ Armature（骨骼，3,426 字符）

> **★★ 这是"蒙皮变形"的入口** —— **配合 ch13（骨骼与绑定）。**

| 参数 | 含义 |
|---|---|
| **★ Object** | **★ 用哪个骨骼物体** |
| **★ Use Vertex Groups** | **★ 用顶点组决定影响（推荐）** |
| **★ Use Bone Envelopes** | 用骨骼"包络"决定影响 |
| **★ Preserve Volume** | **★ 保持体积（双四元数蒙皮）** |

**★★★★ 「Use Vertex Groups」vs「Use Bone Envelopes」**：

| 方式 | 依据 | 精度 |
|---|---|---|
| **★ Vertex Groups** | **★ 顶点组的权重** | **★ 精确可控** |
| **★ Bone Envelopes** | **★ 顶点与骨骼的距离** | **快速但不精确** |

> **★★★ 判据：正式绑定用 Vertex Groups，快速试验用 Envelopes。**
> **★ 两者可以同时开（结果叠加）。**

**★★ 「Preserve Volume」的作用**：
> **★ 用"双四元数"代替"线性蒙皮"** ——
> **避免"扭转时体积塌陷"（典型症状：手臂扭转时变细）。**

### 2.4.6 ★★★ Mesh Deform（网格形变，3,402 字符）

> **★★ 原理：用一个"笼子网格"来包住物体，移动笼子的顶点 → 物体跟着变形。**

| 参数 | 含义 |
|---|---|
| **★ Object** | **★ 用哪个"笼子"** |
| **★ Bind** | **★ 绑定（必须点一次才生效）** |
| **★ Precision** | 精度（影响绑定质量） |
| **★ Dynamic** | 允许笼子本身也变形 |

**★★★★★ 一个必须注意的点：「Bind」是"一次性动作"**：

> **★★ 加了这个修改器后，物体不会立刻变形** ——
> **必须点一次 `Bind` 按钮，建立"顶点与笼子的对应关系"。**
> **★ 绑定后再移动笼子，物体会跟着动。**

> **★★ 判据：改了笼子的拓扑（增减顶点）→ 必须重新 Bind。**

### 2.4.7 ★★★ Surface Deform（表面形变，2,678 字符）

> **★★ 与 Mesh Deform 类似，但用"另一个物体的表面"作为驱动器。**

| 参数 | 含义 |
|---|---|
| **★ Target** | **目标物体** |
| **★ Bind** | **★ 同样需要手动绑定** |
| **★ Interpolation Falloff** | 插值衰减 |

> **★★ 用途：让"贴花/装甲板"跟着"车体曲面"变形。**

### 2.4.8 ★★★★★ Displace（位移，2,525 字符）

> **★★ 作用：用"纹理"驱动顶点沿法线偏移。**

**★★★★ 核心参数**：

| 参数 | 含义 |
|---|---|
| **★ Texture** | **★ 用哪张纹理** |
| **★ Strength** | **★ 强度** |
| **★ Midlevel** | **★ 中值（纹理的"零点"）** |
| **★ Direction** | **★ 沿什么方向偏移** |
| **★ Texture Coordinates** | **★ 五种坐标（见 §2.2.3）** |

**★★★★★ 「Midlevel」是最容易忽略但最关键的参数**：

```
纹理值 - Midlevel = 实际位移量
   ↓ 若 Midlevel = 0.5（默认）
   ↓ 纹理值 0.5 的点位移为 0
   ★ 纹理值 <0.5 向内凹，>0.5 向外凸
```

| Midlevel | 结果 |
|---|---|
| **0** | **★ 全部向外（只凸不凹）** |
| **0.5** | **★ 一半凸一半凹（默认）** |
| **1** | **★ 全部向内（只凹不凸）** |

> **★★★ 判据：想让"纹理只往一个方向推"→ Midlevel 设 0 或 1。**

**★★ 「Direction」的四个选项**：

| 值 | 偏移方向 |
|---|---|
| **★ Normal** | **★ 沿顶点法线**（最常用） |
| **X / Y / Z** | 沿固定轴 |
| **Custom Normal** | 沿自定义法线 |
| **RGB to XYZ** | 用纹理的 RGB 当 XYZ 位移 |

> **★★ 「RGB to XYZ」能让"彩色图"直接变成"三维位移方向"** ——
> **这是做"程序化细节"的高级用法。**

### 2.4.9 ★★★ Cast（投影形变，2,424 字符）

> **★★ 作用：把物体"投影到"某个基本形状（球/柱/立方）。**

| 参数 | 含义 |
|---|---|
| **★ Cast Type** | **★ Sphere / Cylinder / Cube / Plane** |
| **★ Size** | **目标形状的大小** |
| **★ Factor** | **★ 投影强度（0~1）** |
| **★ Axis** | 轴向 |

> **★★ 用途：把"方块"变成"球"的最快方式** ——
> **比 ch01 的 To Sphere 更可控（能选目标形状）。**

### 2.4.10 ★★★ Hooks（挂钩，2,354 字符）

> **★★ 作用：把"某些顶点"绑到"另一个物体"上。**

| 参数 | 含义 |
|---|---|
| **★ Object** | **★ 挂到哪个物体** |
| **★ Vertex Group** | **★ 哪些顶点被挂** |
| **★ Falloff** | **★★ 衰减（影响周围顶点）** |

**★★★★★ 「Falloff」是 Hooks 的精髓**：

| Falloff 类型 | 效果 |
|---|---|
| **None** | **★ 只有组内顶点动（硬边界）** |
| **★ Smooth / Sphere / Root / Sharp / Linear / Constant** | **★ 周围顶点按距离渐变** |

> **★★★ 判据：想"平滑拖拽一片区域"→ 用 Falloff（如 Smooth）；**
> **想"整块硬移动"→ None。**

### 2.4.11 ★★★ 其余 Deform 类（7 个）

| 修改器 | 原文字符 | 作用 | 关键点 |
|---|---|---|---|
| **★ Corrective Smooth** | **2,354** | **★ 修正"蒙皮后的异常变形"** | **配合 Armature，消除"塌陷"** |
| **★ Warp** | **2,045** | **★ 按"两个物体"之间的变换扭曲** | 与 ch01 的 Warp 不同（这个是持续的） |
| **★ Curve** | **1,829** | **★ 让物体沿"曲线"变形** | **★ 做"线缆/管路"的核心** |
| **★ Lattice** | **1,760** | **★ 用"晶格"包住物体做自由变形** | **比 Mesh Deform 轻量** |
| **★ Smooth** | **1,609** | **★ 简单平滑（非破坏性）** | 同 ch01 的 Smooth Vertices |
| **★ Volume Displace** | 895 | 用体积纹理位移 | 少用 |
| **★（另有 3 个未列）** | — | — | — |

**★★★★ 「Lattice」值得单独说**：
> **★★ 它是"用低模控制高模"的经典手段** ——
> **一个 3×3×3 的晶格就能整体弯曲一个复杂模型。**
> **★ 比 Mesh Deform 轻量得多（晶格顶点极少）。**

**★★★★ 「Curve」修改器是"管路/线缆"的核心**：
> **★★ 让一个"直管"沿任意曲线弯曲** ——
> **配合 ch01 §1.13 的 UV，能做"贴图正确的弯曲管路"。**

---

## 2.5 ★★★★★ Modify 类（10 个修改器 / 29,161 字符）

> **★★★ "Modify"的定义（§2.1.3）：不改几何、不改形状，改"其他数据"（如顶点组）。**
> **★ 这一类全是"数据处理"工具。**
> **目标字数：~10,200**

### 2.5.1 ★★★★★ Data Transfer（数据传递，8,338 字符）

> **★ 这是 Modify 类最大的一篇，也是最强大的"数据搬运工"。**

> **★★ 作用：把"一个物体的数据"（顶点组/UV/法线/顶点色…）传递到"另一个物体"上。**

**★★★★★ 为什么它重要（硬表面的两大用途）**：

| 用途 | 说明 |
|---|---|
| **★ ① 把"高模细节"传到"低模"** | **法线传递 → 低模看起来像高模** |
| **★ ② 把"一个模型的权重"复制到"另一个"** | **顶点组传递 → 省去重新刷权重** |

**★★★★ 三个核心参数组**：

| 组 | 参数 | 含义 |
|---|---|---|
| **源** | **★ Source** | **从哪个物体取数据** |
| **★ 数据类型** | **★ Data Types** | **★ 传什么**（顶点组/UV/法线/顶点色/顶点权重…） |
| **★ 映射方式** | **★ Mapping** | **★ 怎么对应**（拓扑/最近点/最近边/投影…） |

**★★★★★ 「Data Types」能传什么（选项极多，列主要的）**：

| 类型 | 用途 |
|---|---|
| **★ Vertex Group(s)** | **★ 传权重** |
| **★ UVs** | **★ 传 UV 布局** |
| **★ Normals** | **★ 传法线（做"低模装高模"）** |
| **★ VCol（顶点色）** | 传顶点色 |
| **★ Sharp / Crease / Bevel Weight** | **★ 传这些"权重标记"** |

**★★★★★ 「Mapping」的判据**：

| Mapping | 用于 |
|---|---|
| **★ Topology** | **★ 两个物体"拓扑一致"时**（最准） |
| **★ Nearest Vertex** | **拓扑不同，靠最近点** |
| **★ Nearest Face Interpolated** | **★ 拓扑不同但形状相近（最常用）** |
| **★ Projected Face Interpolated** | 沿法线投影（适合"贴合"的两个面） |

> **★★★ 判据：**
> **拓扑一致 → Topology（最快最准）；**
> **拓扑不同 → Nearest Face Interpolated（形状相近时效果好）。**

### 2.5.2 ★★★★★ Weight Edit / Weight Mix / Weight Proximity（2,995 + 2,767 + 2,547）

> **★★★ 这是"顶点权重的三件套"** —— **用于"程序化生成权重"。**

**① Weight Edit（2,995）**
> **作用：对"已有顶点组"做批量运算**（加/减/乘/幂/平滑/限制范围）。

| 参数 | 含义 |
|---|---|
| **★ Group** | 操作哪个组 |
| **★ Mode** | **★ Add / Subtract / Multiply / Replace** |
| **★ Factor** | 强度 |
| **★ Clamp** | **★ 限制在 0~1（必开）** |
| **★ Smooth Iterations / Expand** | **★ 平滑/扩张** |

**② Weight Mix（2,767）**
> **作用：把"两个顶点组"按某种运算合成一个新组。**

| 参数 | 含义 |
|---|---|
| **★ A / B** | 两个输入组 |
| **★ Mix Mode** | **★ Add / Multiply / Subtract / Min / Max / Difference...** |
| **★ Mix Factor** | 混合比例 |
| **★ Result** | 输出到哪个组 |

> **★★ 用途：做"遮罩"** —— **比如"组 A（装甲板）× 组 B（上半部）= 只在上半部的装甲板"。**

**③ Weight Proximity（2,547）**
> **作用：按"与目标物体的距离"自动生成权重。**

| 参数 | 含义 |
|---|---|
| **★ Target** | 参照物 |
| **★ Proximity Mode** | **★ Object（到物体）/ Geometry（到表面）** |
| **★ Lowest / Highest** | **★ 距离范围 → 权重 1→0** |

> **★★★ 用途：做"靠近某物体的地方才受影响"的渐变** ——
> **如"离地面越近越平滑"。**

### 2.5.3 ★★★★ Normal Edit（2,814 字符）

> **★★ 作用：把"顶点法线"重新指向某个方向/某个目标。**

| 参数 | 含义 |
|---|---|
| **★ Mode** | **★ Radial（径向）/ Target（朝向目标）** |
| **★ Target** | 目标物体 |
| **★ Mix** | 混合比例 |

> **★★ 用途：让"整体法线朝向一致"**（如"卡通渲染/球面反射"）——
> **或让"低模看起来像圆球"。**

### 2.5.4 ★★★ Weighted Normal（2,272 字符）

> **★★ 作用：按"面的面积/角度"加权，让法线更"硬朗"。**

| 参数 | 含义 |
|---|---|
| **★ Mode** | **★ Face Area / Corner Angle** |
| **★ Weight** | 权重强度 |
| **★ Keep Sharp** | **★ 保持 sharp 边** |

> **★★★ 硬表面的典型用途**：
> **导入的低模"明暗很脏"→ 用 Weighted Normal 让平面更平、棱角更硬。**
> **★ 这是"让低模看起来干净"的常用手法。**

### 2.5.5 ★★★ 其余 Modify 类（6 个）

| 修改器 | 原文字符 | 作用 |
|---|---|---|
| **Mesh Cache** | 2,297 | **★ 播放外部"点缓存"（如 MDD/PC2）** |
| **Mesh Sequence Cache** | 2,028 | **★ 播放"序列文件"（Alembic 等）** |
| **UV Warp** | 1,647 | **★ 用物体/骨骼驱动 UV 偏移** |
| **UV Project** | 1,456 | **★ 用"摄像机/投影器"生成 UV** |
| **Weighted Normal**（已列） | 2,272 | — |
| **Vertex Weight**（3 个） | 已列 | — |

**★★ 「UV Project」的用途**：
> **★ 用"摄像机视角"投影 UV** ——
> **这是"贴花（decal）"的标准做法**（配合 ch01 的 Project from View）。

---

## 2.6 ★★★★★ Physics 类（9 个修改器 / 20,436 字符）

> **★★★ "Simulate"的定义（§2.1.3）：
> 代表物理模拟，"没有属性"，只是标记"模拟从栈的哪里开始"。**
> **目标字数：~7,150**

### 2.6.1 ★★★★★ 一个关键理解：Simulate 修改器是"占位符"

> **★★ 原文说它们「typically have no attributes,
> and are controlled by settings exposed in separate sections of the Properties」** ——
> **即：真正的参数在"物理属性面板"里，修改器本身只是个"锚点"。**

| 修改器 | 真正的参数在哪 |
|---|---|
| **Cloth（576）** | **Physics Properties → Cloth** |
| **Fluid（531）** | **Physics Properties → Fluid** |
| **Collision（508）** | **Physics Properties → Collision** |
| **Soft Body（347）** | **Physics Properties → Soft Body** |
| **Dynamic Paint（307）** | **Physics Properties → Dynamic Paint** |

> **★★★ 判据：找 Simulate 修改器的参数 → 去 Physics 标签，不在修改器面板里。**

### 2.6.2 ★★★★★ Ocean（海洋，8,532 字符）

> **★ 这是 Physics 类最大的一篇（8,532），也是唯一"有大量参数"的。**

> **★★ Ocean 修改器用"频谱（spectrum）"算法生成海浪** ——
> **不需要模拟，直接算出水面形状。**

**★★★★ 核心参数组**：

| 组 | 参数 | 含义 |
|---|---|---|
| **几何** | **★ Geometry（Generate/Displace）** | **★ 生成新面 / 只是位移已有面** |
| **★ 分辨率** | **★ Render / Viewport** | 网格密度 |
| **★ 波浪** | **★ Spatial Size** | **★ 海域大小** |
| **★ 波浪** | **★ Spectrum** | **★ 频谱类型（决定浪的形状）** |
| **★ 波浪** | **★ Wind Velocity** | **★ 风速（浪高）** |
| **★ 波浪** | **★ Fetch** | 风区长度 |
| **★ 波浪** | **★ Damping** | 阻尼 |
| **★ 裁剪** | **★ Depth** | 深度（影响浅水） |

**★★★★★ 关键判据：Geometry 的两种模式**：

| 模式 | 结果 |
|---|---|
| **★ Generate** | **★ 生成"一块完整的水面"**（新几何） |
| **★ Displace** | **★ 只是"推已有网格"**（要求网格足够密） |

> **★★★ 判据：从零做海面 → Generate；给已有水面加波浪 → Displace。**

**★★ Ocean 的"隐藏能力"**：
> **它能生成"泡沫遮罩"和"法线贴图"纹理**（在修改器下方有输出选项）——
> **用于给海面加"白沫"。**

### 2.6.3 ★★★ Particle Instance（粒子实例，6,202 字符）

> **★★ 作用：让"每个粒子"实例化"一个物体"。**

| 参数 | 含义 |
|---|---|
| **★ Object** | **★ 要实例化的物体** |
| **★ Particle System** | **★ 用哪个粒子系统** |
| **★ Space** | **★ World / Local / Local（Location）** |
| **★ Amount** | 实例数量比例 |
| **★ Show Instancer** | 显示粒子发射器本体 |

> **★★ 用途：做"散布的螺栓/铆钉/草丛"** ——
> **比 Array 更自由（可随机分布）。**

### 2.6.4 ★★★ Explode（爆炸，2,873 字符）

> **★★ 作用：把网格"炸开"成一块块（动画用）。**

| 参数 | 含义 |
|---|---|
| **★ Particle UV** | 用 UV 岛作为"碎片"单位 |
| **★ Split Edges** | **★ 是否沿边完全裂开** |
| **★ Unborn / Alive / Dead** | 三个阶段的显示 |

> **★★ 硬表面里用得少**（除非要做"零件分解动画"）。

### 2.6.5 ★★★ 五个"纯占位"的（Cloth/Fluid/Collision/Soft Body/Dynamic Paint）

| 修改器 | 原文字符 | 真正的参数 |
|---|---|---|
| **Cloth** | 576 | Physics → Cloth（布料物理） |
| **Fluid** | 531 | Physics → Fluid（流体） |
| **Collision** | 508 | Physics → Collision（碰撞体标记） |
| **Soft Body** | 347 | Physics → Soft Body（软体） |
| **Dynamic Paint** | 307 | Physics → Dynamic Paint（动态绘制） |

> **★★ 五个加起来只有 2,269 字符** ——
> **因为手册把内容放在 Physics 分区（ch16 会详述）。**
> **★ 本章只记录"它们是占位符"这一事实。**

---

---

## 2.7 ★★★★★ 三大主力的完整参数（深度展开）

> **★ 本节把 Bevel / Subdivision / Solidify 三个"改动频率最高"的修改器，**
> **按原文 Options 逐条译出。**
> **★ 理由：这三个是硬表面的"日常三件套"，参数必须记准。**

### 2.7.1 ★★★★★ Bevel 修改器完整参数（原文 7,959 字符）

> **原文**：
> 「**The Bevel modifier bevels the edges of the mesh it is applied to,
> with some control of how and where the bevel is applied to the mesh.
> It is a non-destructive alternative to the Bevel Operation in Edit Mode.**」

**★★ 一句话**：**非破坏性的 `Ctrl-B`。**

#### ★★★★★ Affect（影响对象）

> **原文**：
> 「**Vertices：Only the areas near vertices are beveled, the edges remain unchanged.
> Edges：Bevel the edges, creating intersections at vertices.**」

| 值 | 结果 | 用于 |
|---|---|---|
| **Vertices** | **★ 只倒"顶点附近"，边不变** | **★ 去掉尖角的高光点** |
| **★ Edges** | **★ 倒边，在顶点处形成交叉** | **★ 常规倒角（默认）** |

> **★★★ 判据：要"去掉尖角的一点点"→ Vertices；**
> **要"整条边圆化"→ Edges。**
> **★ 原文给了三张图：宽度 0.1 / 0.3 / 0.5 的 Vertices 效果对比。**

#### ★★★★★ Width Type（五种宽度度量，原文逐条定义）

> **原文**：
> 「**Offset：The distance from the new edge to the original.**」
> 「**Width：The distance between the two new edges formed by the bevel
> (or the edges on either side of the bevel if there is more than one segment).**」
> 「**Depth：Value is the perpendicular distance from the new bevel face to original edge.**」
> 「**Percent：The percentage of the length of adjacent edge length that the new edges slide along.**」
> 「**Absolute：The exact distance along edges adjacent to the beveled edge.
> A difference from Offset is visible when the unbeveled edges attached to beveled edges
> meet at an angle besides a right angle.**」

**★★★★★ 五种 Width Type 的精确对照（这是本节最硬的一条）**：

| 类型 | 中文 | **精确定义** | 何时与 Offset 不同 |
|---|---|---|---|
| **★ Offset** | 偏移 | **★ 新边到原边的距离** | （基准） |
| **Width** | 宽度 | **★ 两条新边之间的距离** | **★ 多段时（Segments>1）** |
| **Depth** | 深度 | **★ 从新倒角面到原边的"垂直距离"** | 斜面时 |
| **Percent** | 百分比 | **★ 沿相邻边长滑动的百分比** | 相邻边不等长时 |
| **Absolute** | 绝对 | **★ 沿相邻边的"精确距离"** | **★ 相邻边"非直角"相交时** |

> **★★★ 最容易混的两个：Offset 与 Absolute**：
> **原文明确说：「A difference from Offset is visible when the unbeveled edges attached
> to beveled edges meet at an angle besides a right angle.」**
> **★ 即：垂直相交时两者相同；非垂直相交时不同。**
>
> **★★ 为什么**：
> **Offset 是"到原边的垂直距离"；Absolute 是"沿相邻边走的距离"。**
> **★ 当两条边成 90° 时，这两个相等；成 45° 时，沿边走 1 单位 = 垂直距离 0.707。**

**★★★★ 一条选型判据**：

| 诉求 | 用 |
|---|---|
| **"倒角宽度视觉上一致"** | **★ Offset（默认，最常用）** |
| **"倒角后两条新边间距固定"** | Width |
| **"按相邻边长比例"** | Percent |
| **"斜面相接时也精确"** | **★ Absolute** |

#### ★★★★★ Limit Method（原文的数学条件）

> **原文**：
> 「**Angle：Only bevels edges whose angle of adjacent faces plus the defined Angle
> is less than 180 degrees.**」

**★★★★★ 这条条件的精确表述（原文，务必记准）**：

```
设：相邻两面的夹角 = θ（0~180°，平面 = 180°，直角 = 90°）
    Angle 参数 = A

条件：θ + A < 180°
   ↓ 满足 → 该边被倒角
```

> **★★★ 举例验算**：
> | 情况 | θ | A | θ+A | 是否倒角 |
> |---|---|---|---|---|
> | **90° 直角边，A=30** | 90 | 30 | **120 < 180** | **★ ✅ 倒** |
> | **120° 钝边，A=30** | 120 | 30 | **150 < 180** | **★ ✅ 倒** |
> | **160° 接近平面，A=30** | 160 | 30 | **190 > 180** | **★ ❌ 不倒** |
> | **180° 完全平面，A=30** | 180 | 30 | **210 > 180** | **★ ❌ 不倒** |

> **★★ 等价理解**：
> **"θ 越小（越尖），越容易被倒角；θ 越接近 180°（越平），越不会被倒"。**
> **★ 这正是原文说的「bevel only the sharp edges of an object
> without affecting its smooth surfaces」。**

**★★★★ 其余三种 Limit Method**：

| 值 | 原文定义 | 判据 |
|---|---|---|
| **None** | **「No limit, all edges will be beveled」** | 全部倒 |
| **★ Weight** | **「Use each edge's bevel weight to determine the width.When the bevel weight is 0.0, no bevel is applied」** | **★ 权重=0 不倒，权重=宽度** |
| **★ Vertex Group** | **「An edge is only beveled if both of its vertices are in the vertex group」** | **★ 必须"两端点都在组里"才倒** |

> **★★★ Vertex Group 这条极重要**：
> **不是"有一个端点在组里"，而是"两个端点都在"。**
> **★ 所以只把一个端点加入组，那条边不会倒。**

#### ★★★★★ Profile（剖面形状）

> **原文**：
> 「**Superellipse：Creates a bevel with a uniform concave or convex curve.
> Shape：The shape of the bevel, from concave to convex.
> It has no effect if Segments is less than 2.**」
> 「**Miter Shape：The shape of the miter patterns, from concave to convex.
> It has no effect if Segments is less than 2.**」

**★★★★ 「Segments < 2 时 Shape 无效」**：
| Segments | Shape 是否有效 |
|---|---|
| **1** | **★ ❌ 无效**（只有一个斜面，无"形状"可言） |
| **≥2** | **★ ✅ 有效** |

> **★★ 这解释了 ch01 §1.7.3 的"Segments=1 是斜切"** ——
> **因为只有 1 段时，剖面就是一条直线，没有凹凸可选。**

**★★ Custom Profile（自定义剖面）**：
> **原文**：
> 「**This widget allows the creation of a user-defined profile with more complexity
> than with the single profile parameter.
> The profile starts at the bottom right of the widget and ends at the top left,
> as if it were between two edges meeting at a right angle.
> Control points are created in the widget and then the path is sampled with
> the number of segments from the Bevel modifier.**」

| 项 | 说明 |
|---|---|
| **起点** | **★ 控件右下角** |
| **终点** | **★ 控件左上角** |
| **语义** | **★ 相当于"两条成直角的边之间"** |
| **采样** | **★ 按 Segments 数采样这条控制点曲线** |

> **★★ 原文的 Presets 提示**：
> 「**The Support Loops and Steps presets are built dynamically depending on
> the number of segments in the bevel.
> If the number of segments is changed, the preset will have to be re-applied.**」

> **★★★ 陷阱：改了 Segments，Preset 要重新应用** ——
> **因为 Preset 是"按当前段数动态生成"的。**

#### ★★★★★ Miter（斜接）—— 内斜接与外斜接

> **原文**：
> 「**A miter is formed when two beveled edges meet at an angle.
> On the side where the angle is greater than 180 degrees, if any,
> it is called an outer miter.
> If it is less than 180 degrees, then it is called an inner miter.**」

**★★★★★ 内/外斜接的判据（本节最精细的一条）**：

```
两条"已倒角"的边以某个角度相遇
   ↓ 相遇处的角 > 180° → ★ 外斜接（outer miter）
   ↓ 相遇处的角 < 180° → ★ 内斜接（inner miter）
```

| 类型 | 角度 | 视觉 |
|---|---|---|
| **★ Outer Miter** | **> 180°** | **★ 凸角（外面）** |
| **★ Inner Miter** | **< 180°** | **★ 凹角（里面）** |

**★★★★ 三种 Miter 模式（原文）**：

| 模式 | 原文定义 | 效果 |
|---|---|---|
| **Sharp** | **「Edges meet at a sharp point, with no extra vertices introduced on the edges」** | **★ 尖点相接，不额外加点** |
| **★ Patch** | **「Edges meet at a sharp point but in addition, two extra vertices are introducednear the point so that the edges and faces at the vertex may be less pinched togetherthan what occurs in the Sharp case」** | **★ 尖点相接，但在附近加两个点 → 不那么"夹紧"** |
| **Arc** | （原文后续） | **圆弧过渡** |

> **★★★ 判据：**
> **Sharp 会让拐角处"挤得很紧"（面被压缩）；**
> **★ Patch 加两个顶点缓解这个挤压 → 拐角更自然。**
> **★ 硬表面的"盒子倒角"通常用 Patch。**

### 2.7.2 ★★★★★ Subdivision Surface 完整参数（原文 6,142 字符）

> **★ 已在 §2.3.3 讲了框架，这里补原文的细节选项。**

**★★★★ 原文的两个关键 Note（此前未展开）**：

**① 细分的"边界"处理**
> **★★ 开放边界（如 Mirror 前的半边模型）的边界形状，由 `Boundary Smooth` 决定。**

| 值 | 效果 |
|---|---|
| **★ Keep Corners** | **★ 角保持尖，边界平滑** |
| **★ All** | **边界也完全平滑（会收缩）** |

**② `Use Limit Surface`（极限曲面）**
> **★★ 细分级别无限大时趋近的曲面叫"极限曲面"。**
> **★ 开这个选项，Blender 会"直接算极限位置"，而不是逐级细分。**

> **★★★ 用途：级别较低（1~2）时也能得到"接近极限"的平滑度** ——
> **省面数。**

**★★★★ 两个 levels 的实践建议**：

| 场景 | Viewport | Render |
|---|---|---|
| **建模中** | **★ 1~2**（流畅） | — |
| **出图** | — | **★ 3~4**（够平滑） |
| **极限曲面** | **1（+ Use Limit Surface）** | **1** |

> **★★★ 判据：`Use Limit Surface` + Level 1，效果约等于 Level 3~4，但面数少得多。**

### 2.7.3 ★★★★★ Solidify 完整参数补充（原文 6,450 字符）

**★★★★ 此前未展开的三个参数**：

| 参数 | 原文含义 | 判据 |
|---|---|---|
| **★ Rim** | **边缘是否封口** | **★ 关掉会留下"开口壳"** |
| **★ Only Rim** | **只生成边缘（不加厚面）** | 做"边框/格栅" |
| **★ Material Index Offset** | **给"内侧/边缘"指定不同的材质槽偏移** | **★ 让内外用不同材质** |

**★★★★★ `Material Index Offset` 的用法（硬表面很实用）**：

```
物体有 2 个材质槽：0 = 外壳, 1 = 内衬
Solidify：
   Material Index Offset = 0 → 内外同材质
   ★ Material Index Offset = 1 → 内侧自动用槽 2（内衬）
   ★ Rim 的偏移单独有 Rim Material Offset
```

> **★★★ 用途：一个修改器就做出"外壳 + 内衬 + 边缘"三种材质** ——
> **不用手动分面。**

---

## 2.8 ★★★★★ 判据总表（共 118 条）

### 导论（2.1）

| # | 判据 | 出处 |
|---|---|---|
| 1 | **★★★ 修改器 = 自动 + 非破坏性；改"显示与渲染"，不改"可编辑几何"** | `introduction` |
| 2 | **★★ 新修改器总加在栈底（最后计算）** | `introduction` |
| 3 | **★★★★★ 四类定义**：Modify（改数据）/ Generate（**改拓扑**）/ Deform（**只改形状**）/ Simulate（**占位符**） | **`introduction`** |
| 4 | **★★★★★ 分类判据：顶点数变 → Generate；不变 → Deform** | **`introduction`** |
| 5 | **★★ Simulate "没有属性"**（参数在 Physics 面板） | `introduction` |
| 6 | **★★★ 面板头部七图标**：Expand/Type/Name/Show on Cage/Show in Edit Mode/Show in Viewport/Render | `introduction` |
| 7 | **★★★★★ Show on Cage 陷阱**：显示改后位置，**实际编辑原始数据** → 复杂编辑必须关 | **`introduction`** |
| 8 | **★★ Apply On Spline Points**：对曲线控制点应用，而非细分后的网格 | `introduction` |
| 9 | **★★★★★ Apply 陷阱①**：Apply 非栈顶修改器会**忽略栈顺序**（当作第一个） | **`introduction`** |
| 10 | **★★★ 判据：要 Apply → 先 Move to First** | `introduction` |
| 11 | **★★★★ Apply as Shape Key 只对"不改拓扑"的修改器有效**（即 Deform 类） | **`introduction`** |
| 12 | **★★ 原因**：形态键记录"每顶点位移"，顶点数变则无一一对应 | `introduction` |
| 13 | **★★★★★ 栈顺序决定结果：先 Mirror 后 Subdivision = 连续曲面；反过来 = 两个分离面** | **`introduction`** |
| 14 | **★★★ 机理**：Catmull-Clark 会向内收缩；收缩后镜像则出现缝 | `introduction` |
| 15 | **★★ Active Modifier 供 Geometry Node Editor 判断改哪个节点组** | `introduction` |

### 通用选项（2.2）

| # | 判据 | 出处 |
|---|---|---|
| 16 | **★★★★★ 顶点组按"名字"引用**：重命名 → 所有引用者断链（字段变红） | **`common_options`** |
| 17 | **★★ 判据：顶点组起名后不要再改** | `common_options` |
| 18 | **★★★ Invert 是"权重取反"（1-w），不是"换组"** | `common_options` |
| 19 | **★★★★★ 纹理坐标五种：UV / Object / Global / Local（默认）** | **`common_options`** |
| 20 | **★★★ Local（跟物体动）vs Global（固定空间）—— Displace 的关键设置** | `common_options` |
| 21 | **★★★★ UV 坐标的缺陷**：只取"第一个遇到的面"的 UV，其余忽略 → 接缝处跳变 | **`common_options`** |
| 22 | **★★ Object 坐标**：想"移动物体但位移不变"→ 把坐标物体设为子级 | `common_options` |
| 23 | **★★★★ Use Channel 默认 Intensity = RGB 平均**（纯红 = 0.33 不是 1.0） | **`common_options`** |
| 24 | **★★ 想让"纯红=最大影响"必须显式选 Red 通道** | `common_options` |

### Generate（2.3 + 2.7）

| # | 判据 | 出处 |
|---|---|---|
| 25 | **★★★ Bevel 修改器 = 非破坏性 `Ctrl-B`** | `bevel` |
| 26 | **★★★★ Affect：Vertices（只倒顶点附近）/ Edges（倒边，默认）** | **`bevel`** |
| 27 | **★★★★★ 五种 Width Type**：Offset（到原边垂距）/ Width（两新边间距）/ Depth（到原边垂距）/ Percent（沿邻边百分比）/ Absolute（沿邻边精确距离） | **`bevel`** |
| 28 | **★★★★★ Offset 与 Absolute 在"非直角"时不同**（直角时相同） | **`bevel`** |
| 29 | **★★★★★ Limit Method=Angle 的数学条件：θ + A < 180°** | **`bevel`** |
| 30 | **★★★ 等价理解：θ 越小越易倒；θ→180° 不会倒（保护平滑面）** | `bevel` |
| 31 | **★★★★ Limit Method=Vertex Group：必须"两端点都在组里"才倒** | **`bevel`** |
| 32 | **★★ Limit Method=Weight：权重 0 不倒，权重即宽度** | `bevel` |
| 33 | **★★★ Profile 的 Shape 在 Segments<2 时无效** | **`bevel`** |
| 34 | **★★ Custom Profile 起点在右下、终点在左上（相当于直角两条边之间）** | `bevel` |
| 35 | **★★★ 陷阱：改 Segments 后 Preset 要重新应用**（Preset 按当前段数动态生成） | **`bevel`** |
| 36 | **★★★★★ 内/外斜接判据：相遇角 >180° = Outer，<180° = Inner** | **`bevel`** |
| 37 | **★★★★ Miter：Sharp（尖点，面被夹紧）/ Patch（加两顶点缓解挤压）/ Arc** | **`bevel`** |
| 38 | **★★★ 硬表面的盒子倒角通常用 Patch** | `bevel` |
| 39 | **★★★★★ Solidify 的 Offset：-1 全往负法线（原面在外）/ 0 两侧平分 / +1 全往正法线** | **`solidify`** |
| 40 | **★★★ 判据：想让"原面就是最终外表面"→ Offset = -1** | `solidify` |
| 41 | **★★★★ Even Thickness**：不开则锐角处厚度变薄；开了保持均匀但可能自交 | **`solidify`** |
| 42 | **★★ 判据：结构件必开；薄壳/外观件可不开** | `solidify` |
| 43 | **★★★★ Material Index Offset**：一个修改器做出"外壳+内衬+边缘"三种材质 | **`solidify`** |
| 44 | **★★ Rim 关掉会留"开口壳"；Only Rim 只生成边缘** | `solidify` |
| 45 | **★★★★★ Subdivision 两种算法：Catmull-Clark（向内收缩变圆）/ Simple（位置不变只加密）** | **`subdivision_surface`** |
| 46 | **★★★★ Use Creases**：勾上才让 ch01 的 Crease 折痕生效（Crease=1 完全锐利） | **`subdivision_surface`** |
| 47 | **★★★ Boundary Smooth：Keep Corners（角保持尖）/ All（边界也平滑收缩）** | `subdivision_surface` |
| 48 | **★★★★★ Use Limit Surface**：Level 1 + 极限曲面 ≈ Level 3~4 效果，但面数少得多 | **`subdivision_surface`** |
| 49 | **★★ Levels 分开设**：视口 1~2、渲染 3~4（性能优化标准做法） | `subdivision_surface` |
| 50 | **★★★★★ Mirror 的 Bisect**：沿对称面切掉超出的一半（否则重叠成两份） | **`mirror`** |
| 51 | **★★★★ Use Clipping**：中线顶点被"粘"在对称面上不穿越 | **`mirror`** |
| 52 | **★★★★ Merge + Threshold**：不开则中线两排重合顶点 → 细分缝隙/法线异常 | **`mirror`** |
| 53 | **★★★ 硬表面标准设置**：Axis=X + Bisect + Use Clipping + Merge(0.001) | `mirror` |
| 54 | **★★★★★ Array 的 Object Offset**：用 Empty 的变换作为每份增量 | **`array`** |
| 55 | **★★★ 圆周阵列 = 一个绕中心旋转的 Empty 作 Object Offset** | **`array`** |
| 56 | **★★ Relative Offset（按物体尺寸倍数）vs Constant Offset（绝对单位）** | `array` |
| 57 | **★★★★★ Boolean 的 Solver：Fast（快但复杂相交出错）/ Exact（慢但可靠）** | **`booleans`** |
| 58 | **★★★ 判据：布尔错乱/缺面/多面 → 换 Exact** | **`booleans`** |
| 59 | **★★★ Exact 独有：Self Intersection / Hole Tolerant** | `booleans` |
| 60 | **★★★★ 布尔依赖法线判断内外**：法线反了 → 差集变并集 | `booleans` |
| 61 | **★★★★ Edge Split 是 Auto Smooth 前的"锐边方案"**：物理拆边，缺点是真增加顶点 | **`edge_split`** |
| 62 | **★★★ Triangulate：导出前必做**（很多格式不支持四边形） | **`triangulate`** |
| 63 | **★★ Decimate 三种：Collapse / Un-Subdivide / Planar；硬表面用 Planar 最好** | `decimate` |
| 64 | **★★ Weld = 非破坏性的 Merge by Distance** | `weld` |
| 65 | **★★ Skin：用顶点链生成带厚度的骨架，每顶点可设半径** | `skin` |

### Deform（2.4）

| # | 判据 | 出处 |
|---|---|---|
| 66 | **★★★★★ Simple Deform 五种：Twist / Bend / Taper / Stretch / 组合** | **`simple_deform`** |
| 67 | **★★★★★ Bend 的效果取决于 Origin**（从一端弯 vs 对称弯） | **`simple_deform`** |
| 68 | **★★ Limits（Upper/Lower）只让"部分范围"参与形变** | `simple_deform` |
| 69 | **★★★★ Shrinkwrap 四种 Wrap Method**：Nearest Surface Point（默认）/ Project / Nearest Vertex / Target Normal Project | **`shrinkwrap`** |
| 70 | **★★★ Wrap Mode：On Surface（正好在表面）/ Outside Surface（保持厚度在外）** | `shrinkwrap` |
| 71 | **★★★★ Laplacian Smooth 的 Preserve Volume**：开则保体积（区别于普通平滑） | **`laplacian_smooth`** |
| 72 | **★★ Wave 两种 Type：Bands（平行波，单向风）/ Rings（同心圆，水滴）** | `wave` |
| 73 | **★★★★ Armature：Use Vertex Groups（精确）vs Bone Envelopes（快速）** | **`armature`** |
| 74 | **★★ Preserve Volume（Armature）= 双四元数蒙皮**，避免扭转时体积塌陷 | `armature` |
| 75 | **★★★★★ Mesh Deform / Surface Deform 必须手动点 Bind 才生效** | **`mesh_deform`** |
| 76 | **★★ 判据：改了笼子拓扑 → 必须重新 Bind** | `mesh_deform` |
| 77 | **★★★★★ Displace 的 Midlevel**：纹理值-Midlevel=位移；0 全凸 / 0.5 半凸半凹 / 1 全凹 | **`displace`** |
| 78 | **★★ Displace 的 RGBtoXYZ 能让彩色图直接当三维位移方向** | `displace` |
| 79 | **★★ Cast：Sphere/Cylinder/Cube/Plane 四种目标形状，比 To Sphere 更可控** | `cast` |
| 80 | **★★★★ Hooks 的 Falloff**：None（硬边界）/ Smooth 等（周围渐变） | **`hooks`** |
| 81 | **★★ Lattice：用极轻量的晶格控制高模**（比 Mesh Deform 轻） | `lattice` |
| 82 | **★★ Curve 修改器是"管路/线缆"的核心** | `curve` |

### Modify（2.5）

| # | 判据 | 出处 |
|---|---|---|
| 83 | **★★★★★ Data Transfer 两大用途**：① 高模细节→低模 ② 复制权重 | **`data_transfer`** |
| 84 | **★★★★ Mapping 判据**：拓扑一致→Topology；不同→Nearest Face Interpolated | **`data_transfer`** |
| 85 | **★★★ Data Types 能传**：Vertex Group / UV / Normals / VCol / Sharp/Crease/Bevel Weight | `data_transfer` |
| 86 | **★★★ Weight Edit：对已有组批量运算（Add/Multiply/Replace + Clamp）** | `weight_edit` |
| 87 | **★★ Weight Mix：两个组按运算合成（做"遮罩"的核心）** | `weight_mix` |
| 88 | **★★ Weight Proximity：按到目标物体的距离生成权重** | `weight_proximity` |
| 89 | **★★★★ Weighted Normal**：按面积/角度加权，让导入低模"明暗变干净" | **`weighted_normal`** |
| 90 | **★★ Normal Edit：让法线朝向一致**（卡通渲染/低模装圆球） | `normal_edit` |
| 91 | **★★ UV Project：用摄像机视角投影 UV**（贴花标准做法） | `uv_project` |

### Physics（2.6）

| # | 判据 | 出处 |
|---|---|---|
| 92 | **★★★★★ Simulate 修改器是"占位符"**：参数在 Physics 面板，不在修改器面板 | **`physics/*`** |
| 93 | **★★★★ Ocean 的 Geometry 两种**：Generate（生成新水面）/ Displace（推已有网格） | **`ocean`** |
| 94 | **★★ Ocean 能输出"泡沫遮罩 + 法线贴图"纹理** | `ocean` |
| 95 | **★★ Particle Instance：让每个粒子实例化一个物体**（散布螺栓/铆钉） | `particle_instance` |
| 96 | **★★ Cloth/Fluid/Collision/Soft Body/Dynamic Paint 五个加起来只有 2,269 字符**（内容在 Physics 区） | `physics/*` |

### 三大主力综合（2.7）

| # | 判据 | 出处 |
|---|---|---|
| 97 | **★★★ 硬表面的"日常三件套"= Bevel + Subdivision + Solidify** | 综合 |
| 98 | **★★★★★ 三者的"配合顺序"**（见下方 §2.9） | 综合 |

---

### 附录（2.11–2.14）

| # | 判据 | 出处 |
|---|---|---|
| 79 | **★★★★ Decimate 适用判据：只用于"顶点冗余"的模型（雕刻/细分产物）；精心手建的不要用** | **`decimate`** |
| 80 | **★★★ Decimate 的效果"编辑模式看不到"**（因为改了拓扑，无法映射回） | `decimate` |
| 81 | **★★★★★ Collapse 的 Ratio 按"三角形"计算**：全四边形模型减不下来，勾 Triangulate 才符合预期 | **`decimate`** |
| 82 | **★★★★★ Un-Subdivide：两迭代 = 一次 Subdivide**（永远用偶数，奇数得不等网格） | **`decimate`** |
| 83 | **★★★ Un-Subdivide 只对"纯细分产物"有效**（细分后手工编辑过就失效） | `decimate` |
| 84 | **★★★★★ Planar 是硬表面减面首选**：形状零损失，只合并共面 | **`decimate`** |
| 85 | **★★★★ Planar 的 Angle Limit：5°~15° 常用；超 15° 会吃掉曲面细节** | **`decimate`** |
| 86 | **★★ Planar 的 Delimit 防跨 UV 接缝/材质边界合并** | `decimate` |
| 87 | **★★★★★ Weld 的 Connected 模式**：只合并"本来有边连接"的点，不破坏分离结构 | **`weld`** |
| 88 | **★★★★ Skin：每个顶点可设"皮肤半径"** → 一根骨架能上粗下细 | **`skin`** |
| 89 | **★★ Skin 能直接 Create Armature**（生成配套骨骼） | `skin` |
| 90 | **★★★★ Wireframe 做"桁架/笼子/防护网"**，比手工沿边挤出快 | **`wireframe`** |
| 91 | **★★★★★ Remesh 三种：Voxel（修复破碎/自交）/ Octree / ★ Quad（三角面→四边形）** | **`remesh`** |
| 92 | **★★★ 硬表面用法：Voxel 把"到处穿插的布尔结果"变干净整体** | `remesh` |
| 93 | **★★★★ Corrective Smooth 的 Rest Source：Original Coords / ★ Bind Coords（需先 Bind）** | **`corrective_smooth`** |
| 94 | **★★ Corrective Smooth 治"关节塌陷/凸起"** | `corrective_smooth` |
| 95 | **★★ Warp 修改器 = 用两个物体之间的变换持续扭曲**（ch01 的 Warp 是一次性） | `warp` |
| 96 | **★★★★★ Lattice vs Mesh Deform：整体弯一下→Lattice（快）；贴细节变形→Mesh Deform（慢）** | **`lattice`** |
| 97 | **★★★★ Curve 修改器 = 管路/软管/履带/电缆的核心**（配合 UV 让贴图跟随弯曲） | **`curve`** |
| 98 | **★★★★★ 排错总纲（从省时到费时）**：① 栈顺序 ② 法线 ③ 通用选项 ④ Apply 状态 ⑤ 求解器 | **综合** |

---

## 2.9 ★★★★★ 三条方法论

### ① ★★★★★ "三件套的固定顺序"

> **★★★ 硬表面的标准修改器栈**：

```
[1] Mirror          ← 先对称（Bisect + Clipping + Merge）
   ↓
[2] Bevel           ← 再倒角（Limit Method = Angle 30°）
   ↓
[3] Subdivision     ← 最后细分（Use Creases 勾上）
   ↓
[4] Solidify        ← 如需厚度
```

**★★★ 为什么是这个顺序**：

| 顺序 | 理由 |
|---|---|
| **Mirror 最前** | **★ 必须"先对称成整体"，细分才会连续**（§2.1.6） |
| **Bevel 在细分前** | **★ 因为细分会把倒角"圆化两次"** —— **先倒角，细分后倒角变得非常圆滑** |
| **★ Subdivision 在 Bevel 后** | **★ 这是"硬表面高光"的标准做法：小倒角 + 细分 = 细长高光** |
| **Solidify 最后** | **因为厚度应该基于"最终形状"** |

> **★★ 若顺序反了（细分→倒角）**：
> **细分把面数放大数倍，再倒角 → 倒角要处理海量边 → 极慢且容易出错。**

### ② ★★★★★ "非破坏性优先，但有例外"

> **★★★ 本节的六处"修改器优于编辑模式"**：

| 编辑模式（破坏性） | **修改器（非破坏性）** |
|---|---|
| **`Ctrl-B` 倒角** | **★ Bevel 修改器** |
| **`Ctrl-M` 镜像** | **★ Mirror 修改器** |
| **编辑模式布尔** | **★ Boolean 修改器** |
| **`M → By Distance`** | **★ Weld 修改器** |
| **`Mesh → Cleanup`** | **★ Weld + Decimate** |
| **手动平滑** | **★ Smooth / Laplacian Smooth** |

> **★★★ 唯一的例外：`Triangulate`**
> **导出前必须"真的三角化"** ——
> **因为导出格式会自己拆，你不拆就会"形状与看到的不一致"。**
> **★ 这一处要用编辑模式（或 Apply 修改器）。**

### ③ ★★★★★ "参数值没有绝对意义，看上下文"

> **★★★ 本节至少五处证明了这一点**：

| 参数 | 上下文 | 结论 |
|---|---|---|
| **Bevel 的 Angle** | **θ+A<180°** | **★ "30°" 不是绝对值，是"相对平面夹角的条件"** |
| **Solidify 的 Offset** | **-1/0/+1** | **★ "0" 不一定是"中间"，取决于你要什么** |
| **Subdivision 的 Levels** | **视口 vs 渲染** | **★ 同一个"2"在两处含义不同** |
| **Displace 的 Midlevel** | **0 / 0.5 / 1** | **★ 0.5 是"一半凸一半凹"，不是"中间值"** |
| **Boolean 的 Solver** | **Fast vs Exact** | **★ "Fast" 不是"更好"，简单形状才用** |

> **★ 这与 product-injection 那本书的"同一温度在甲缺陷叫低、乙缺陷叫高"是同一道理。**

---

## 2.10 ★★★ 本章的空白

| 缺什么 | 手册情况 | 该去哪查 |
|---|---|---|
| **★★★ 多数修改器的"默认值"** | **手册以 Options 描述为主，未系统列出默认值** | 实际操作面板 |
| **★★ 图示效果** | **手册大量依赖截图（如倒角三种 Miter 对比），文本提取后丢失** | 原 EPUB 图 |
| **★★ Data Transfer 的完整 Data Types 清单** | **本节只列 5 类主要的**（原文 8,338 字符含大量细分项） | `modify/data_transfer.xhtml` |
| **★★ Ocean 的频谱参数详解** | **只列主要的 8 项**（原文 8,532 字符） | `physics/ocean.xhtml` |
| **★★ Physics 五类的实际参数** | **本章只说明"是占位符"** | **ch16（新增，physics 区 220,964 字符）** |
| **★★ Geometry Nodes 修改器** | **2.92 刚引入，原文仅 532 字符** | 后续版本手册 |
| **★ 各修改器的性能开销** | 未提 | 实测 |

> **★★★ 本章的空白主要是"图"与"默认值"** ——
> **与 ch01 同源问题：手册靠图说明，文本提取丢失。**
> **★ 本版用"参数逻辑 + 判据"补足，不伪造图。**

---

## 2.11 ★★★★★ 附录 A：Decimate 三种模式的完整参数

> **★ 原文 3,089 字符。Decimate 是"减面"的唯一工具，但三种模式差别极大。**

> **原文（用途说明）**：
> 「**The Decimate modifier allows you to reduce the vertex/face count of a mesh
> with minimal shape changes.
> This is not usually used on meshes which have been created by modeling carefully
> and economically (where all vertices and faces are necessary to correctly define the shape).
> But if the mesh is the result of complex modeling, sculpting and/or applied
> Subdivision Surface/Multiresolution modifiers, the Decimate one can be used to reduce
> the polygon count for a performance increase, or simply remove unnecessary vertices and edges.**」

**★★★★★ 一条重要的"适用范围"判据**：

| 模型来源 | 该不该用 Decimate |
|---|---|
| **★ 精心手工建模的（每个顶点都必要）** | **★ ❌ 不该用** |
| **★ 雕刻/细分/多分辨率产生的（顶点冗余）** | **★ ✅ 该用** |

> **★★★ 原文的逻辑："Decimate 的用途是去掉'不必要的'顶点"。**
> **如果顶点本来就都是必要的，减掉就会破坏形状。**

**★★ 原文还有一个特殊提示**：
> 「**Unlike the majority of existing modifiers, this one does not allow you to
> visualize your changes in Edit Mode.**」

> **★★ 即：Decimate 的效果在编辑模式里看不到** ——
> **因为它改变了拓扑，无法"映射回"原始编辑数据。**
> **★ 这与 §2.1.3 的"Generate 改拓扑"完全一致。**

### 2.11.1 ★★★★★ Collapse（塌陷）模式

> **原文**：
> 「**Merges vertices together progressively, taking the shape of the mesh into account.**」

**★★★★ 参数**：

| 参数 | 原文定义 |
|---|---|
| **★ Ratio** | **「The ratio of faces to keep after decimation」** |
| **★ Symmetry** | **「Maintains symmetry on a single axis」** |
| **★ Triangulate** | **「Keeps any resulting triangulated geometry from the decimation process」** |
| **★ Vertex Group + Factor** | **控制"哪些部分被减面"** |

**★★★★★ Ratio 的一条关键 Note（极易踩坑）**：

> **原文（Note）**：
> 「**Although the Ratio is directly proportional to the number of remaining faces,
> triangles are used when calculating the ratio.
> This means that if your mesh contains quads or other polygons,
> the number of remaining faces will be larger than expected,
> because those will remain unchanged if their edges are not collapsed.
> This is only true if the Triangulate option is disabled.**」

**★★★★★ 完整解释**：

```
Ratio = 0.5 的意思是"面数减半"
   ↓ 但 ★ 计算时按"三角形"算
   ↓ 若模型全是四边形（每个四边形 = 2 个三角形）
   ↓ 减半后：三角形数减半，但"四边形数"不减半
   ★ 结果：剩余面数 > 预期
```

| 你的模型 | Ratio=0.5 的实际效果 |
|---|---|
| **全三角面** | **★ 面数真的减半** |
| **★ 全四边形** | **★ 剩余面数 > 预期**（因为四边形"不会被动"） |
| **★ 勾了 Triangulate** | **★ 按三角面算，符合预期** |

> **★★★ 判据：想让 Ratio "所见即所得" → 勾上 Triangulate。**
> **★ 否则四边形模型会"减不下来"。**

### 2.11.2 ★★★★ Un-Subdivide（反细分）模式

> **原文**：
> 「**It can be thought of as the reverse of subdivide.
> It attempts to remove edges that were the result of a subdivide operation.
> It is intended for meshes with a mainly grid-based topology (without giving uneven geometry).
> If additional editing has been done after the subdivide operation, the results may be unexpected.**」

**★★★★ 参数与一条重要换算**：

| 参数 | 原文定义 |
|---|---|
| **★ Iterations** | **「The number of times to perform the un-subdivide operation.Two iterations is the same as one subdivide operation, so you will usually want to use even numbers」** |

**★★★★★ 「两迭代 = 一次细分」（务必记住）**：

| Iterations | 效果 |
|---|---|
| **1** | **★ 只去掉"一半"的细分**（结果不规则） |
| **★ 2** | **★ 完全抵消一次 Subdivide** |
| **★ 4** | **★ 抵消两次 Subdivide** |

> **★★★ 判据：永远用偶数（2/4/6），奇数会得到"不均匀的网格"。**

**★★ 适用范围（原文明确）**：
| 能用 | 不能 |
|---|---|
| **★ 网格状拓扑（grid-based）** | **★ 细分后又做过其他编辑的** |

> **★★ 为什么"细分后编辑过"会失效**：
> **Un-Subdivide 靠"识别细分产生的规则模式"来删边** ——
> **如果那些顶点被手动移动过，模式就认不出来了。**

### 2.11.3 ★★★★★ Planar（平面）模式 —— 硬表面首选

> **原文**：
> 「**It reduces details on forms comprised of mainly flat surfaces.**」

**★★★★ 参数**：

| 参数 | 原文定义 |
|---|---|
| **★ Angle Limit** | **「Dissolve geometry which form angles (between surfaces) higher than this setting」** |
| **★ Delimit** | **「Prevent dissolving geometry in certain places」**（可选：Normal / Material / Seam / Sharp / UV） |
| **★ All Boundaries** | 保留所有边界 |
| **★ Normal** | **「Does not dissolve edges on the borders of areas where the face normals are reversed」** |

**★★★★★ 为什么"硬表面用 Planar 最好"**：

```
Planar 的逻辑：把"共面（角度 < Angle Limit）的面"合并
   ↓ 硬表面 = 大量平面块
   ↓ ★ 每个平面块内的所有面被合并成 1 个 n-gon
   ★ 面数剧降，形状完全不变
```

> **★★★ 对比另外两种**：
> | 模式 | 硬表面效果 |
> |---|---|
> | **Collapse** | **★ 会改变形状（顶点被合并）** |
> | **Un-Subdivide** | **只对"细分产生的网格"有效** |
> | **★ Planar** | **★ 形状零损失，只合并共面** |

**★★ Angle Limit 的判据（这个参数最该注意）**：

| Angle Limit | 结果 |
|---|---|
| **太小（如 1°）** | **★ 只合并"几乎完全共面"的**（保守） |
| **★ 5°~15°** | **★ 硬表面常用**（合并平面，保留曲面细节） |
| **太大（如 45°）** | **★ 会把"轻微弯曲"也合并掉** → 形状塌陷 |

> **★★★ 判据：先用 5°，看结果满意再加；超过 15° 要小心曲面被吃掉。**

**★★ Delimit 的用途**：
> **"防止在某些地方合并"** ——
> **比如"不想跨 UV 接缝合并"（否则贴图会错）、"不想跨材质边界合并"。**
> **★ 硬表面通常勾 Normal（防止跨越法线反转处）。**

---

## 2.12 ★★★★ 附录 B：其余 Generate 类速查

### 2.12.1 ★★★★ Weld（焊接，914 字符）

> **★★ = 非破坏性的 `M → By Distance`（ch01 §1.4.4）。**

| 参数 | 含义 |
|---|---|
| **★ Mode** | **★ All（全部按距离合并）/ Connected（只合并已连通的）** |
| **★ Distance** | **★ 合并阈值** |
| **★ Vertex Group** | 限定范围 |

> **★★★ `Connected` 模式很关键**：
> **它只合并"本来就有边连接"的顶点** ——
> **所以不会把"两块分离的面"粘在一起。**
> **★ 这是"清理重复点但不破坏分离结构"的正确选择。**

### 2.12.2 ★★★★ Skin（蒙皮，3,806 字符）

> **★★ 作用：用"顶点链"生成"带厚度的管状骨架"。**

| 参数 | 含义 |
|---|---|
| **★ Branch Smoothing** | 分支处的平滑度 |
| **★ Mark Loose / Mark Root** | 标记"松散端""根端" |
| **★ Symmetry Axes** | 对称轴 |
| **★ Create Armature** | **★ 直接生成一套配套骨骼** |

**★★★★ 「每个顶点的半径」是 Skin 的精髓**：
> **★★ 选中某个顶点 → `Ctrl-A` 调整它的"皮肤半径"** ——
> **所以一根"骨架"可以"上粗下细"。**
> **★ 这是做"触手/树枝/机械臂"的快速方式。**

### 2.12.3 ★★★★ Wireframe（线框，2,337 字符）

| 参数 | 含义 |
|---|---|
| **★ Thickness** | **★ 线框的粗细** |
| **★ Offset** | 相对原面的偏移 |
| **★ Boundary** | 是否包含边界 |
| **★ Replace Original** | **★ 用线框"替换"原面** |
| **★ Even Thickness** | 均匀厚度 |
| **★ Relative Thickness** | 按边长比例 |

> **★★ 用途：做"桁架/笼子/防护网"** ——
> **比"手工沿每条边挤出"快得多。**

### 2.12.4 ★★★★ Remesh（重建网格，2,054 字符）

| 模式 | 原理 | 用于 |
|---|---|---|
| **★ Voxel** | **★ 按体素重建** | **★ 修复"破碎/自交"的模型** |
| **★ Octree** | 八叉树重建 | 类似 Voxel |
| **★ Quad** | **★ 重建为四边形** | **★ 把三角面模型变回四边形** |

> **★★★ 硬表面用途**：
> **① Voxel Remesh 能把"到处穿插的布尔结果"变成"干净的整体"**
> **② Quad Remesh 能把"扫描/导入的三角面模型"变成"可编辑的四边形网格"**

### 2.12.5 ★★★ 其余速查（5 个）

| 修改器 | 字符 | 一句话 |
|---|---|---|
| **Mesh to Volume** | 1,642 | 网格→体积（配合体积渲染/流体） |
| **Volume to Mesh** | 1,432 | 体积→网格 |
| **Build** | 1,482 | 逐面"长出来"的动画 |
| **Screw** | 1,475 | 螺旋/车削（修改器版，同 ch01 §1.14） |
| **Mask** | 1,017 | 用顶点组做雕刻遮罩 |
| **Geometry Nodes** | 532 | 节点式生成（2.92 新引入） |

---

## 2.13 ★★★★ 附录 C：Deform 类其余细节

### 2.13.1 ★★★★ Corrective Smooth（修正平滑，2,354 字符）

> **★★ 作用：修正"蒙皮变形后的异常"（如关节处塌陷/凸起）。**

| 参数 | 含义 |
|---|---|
| **★ Factor** | **★ 修正强度** |
| **★ Iterations** | 迭代次数 |
| **★ Scale** | 缩放修正量 |
| **★ Smooth Type** | **★ Simple / Length Weight** |
| **★ Rest Source** | **★ Original Coords / Bind Coords** |

**★★★★ 「Rest Source」是关键**：
| 值 | 基准 |
|---|---|
| **Original Coords** | **★ 原始（未变形）坐标** |
| **★ Bind Coords** | **★ 绑定的坐标**（需先 Bind） |

> **★★ 用途：角色"肩部/膝盖"扭转时出现的"塌陷"，用 Corrective Smooth 抹平。**

### 2.13.2 ★★★★ Warp（扭曲，2,045 字符）vs ch01 的 Warp

| 项 | ch01 的 `Warp`（编辑模式） | **Warp 修改器** |
|---|---|---|
| **驱动** | **鼠标位置** | **★ 两个"物体"之间的变换** |
| **持续性** | **一次性** | **★ 持续（改物体即改形变）** |

> **★★ 修改器版的 Warp 是"用 A 物体的变换去扭曲 B 物体"** ——
> **适合"绑定到某个控制器"。**

### 2.13.3 ★★★★ Lattice（晶格，1,760 字符）

> **★★ 原理：用一个"低分辨率晶格"包住物体，移动晶格点 → 物体跟着变形。**

| 参数 | 含义 |
|---|---|
| **★ Object** | **★ 用哪个晶格** |
| **★ Vertex Group** | 限定范围 |

**★★★★★ Lattice vs Mesh Deform 的判据**：

| 项 | **Lattice** | **Mesh Deform** |
|---|---|---|
| **控制网格** | **★ 规则晶格（3×3×3 起）** | **任意网格** |
| **顶点数** | **★ 极少** | 可多可少 |
| **精度** | 低（但够用） | 高 |
| **速度** | **★ 快** | 慢 |
| **适用** | **★ 整体弯曲/膨胀** | **局部精细变形** |

> **★★★ 判据：只要"整体弯一下"→ Lattice；要"贴着细节变形"→ Mesh Deform。**

### 2.13.4 ★★★★ Curve（曲线形变，1,829 字符）

> **★★ 作用：让"直线物体"沿"曲线"弯曲。**

| 参数 | 含义 |
|---|---|
| **★ Object** | **★ 目标曲线** |
| **★ Deform Axis** | **★ 物体的哪个轴对齐曲线** |
| **★ Vertex Group** | 限定范围 |

**★★★★ 硬表面的核心用途**：
> **① 管路/软管（沿路径弯曲）**
> **② 履带（沿轮子曲线）**
> **③ 电缆**
> **★ 配合 ch01 §1.13 的 UV，能让"贴图正确跟随弯曲"。**

---

## 2.14 ★★★★★ 附录 D：修改器的性能与排错

> **★ 手册未系统讲性能，本节按原文分散的提示归纳（标明"提炼"）。**

### 2.14.1 ★★★★ 五个"会拖慢"的修改器（提炼）

| 修改器 | 为什么慢 |
|---|---|
| **★ Subdivision** | **面数指数增长（每级 ×4）** |
| **★ Boolean（Exact）** | **精确求交，计算量大** |
| **★ Remesh（Voxel）** | 重建整个网格 |
| **★ Data Transfer** | 逐顶点查找对应 |
| **★ Ocean** | 频谱计算 + 高分辨率网格 |

> **★★ 优化手段**：
> **① Subdivision 用"视口低级别 + 渲染高级别"**
> **② Boolean 用 Fast（简单形状时）**
> **③ Remesh 完成后 Apply 并 Decimate**
> **④ Data Transfer 完成后 Apply（不再需要实时算）**

### 2.14.2 ★★★★★ 排错速查（按症状）

| 症状 | 首查 |
|---|---|
| **★ 布尔结果错乱/缺面** | **① Solver 换 Exact ② `Shift-N` 重算法线 ③ 检查运算对象是否封闭** |
| **★ 倒角后模型发黑/自交** | **开 Clamp Overlap** |
| **★ 细分后中间有缝** | **Mirror → Subdivision 顺序反了**（§2.1.6） |
| **★ 细分后中线有黑线** | **Mirror 的 Merge 没开** |
| **★ 加厚后形状变了** | **Solidify 的 Offset 不对**（想保持外形用 -1） |
| **★ 加厚后锐角处极薄** | **开 Even Thickness** |
| **★ Apply 后结果和看到的不一样** | **被 Apply 的修改器不在栈顶**（§2.1.5） |
| **★ 顶点组字段变红** | **组被重命名了**（§2.2.1） |
| **★ 编辑模式看不到修改器效果** | **开了 Show in Edit Mode 但改的是原始数据**（§2.1.4） |
| **★ 曲线加了修改器却"变形不对"** | **开 Apply On Spline Points**（§2.1.4） |
| **★ Decimate 减不下来** | **四边形模型 + 没勾 Triangulate**（§2.11.1） |
| **★ Un-Subdivide 结果不规则** | **用了奇数 Iterations**（§2.11.2） |

### 2.14.3 ★★★★★ 一条总纲

> **★★★ 修改器出问题时，按这个顺序查**：

```
① 栈顺序对不对？        （最常见，§2.1.6）
② 法线对不对？          （Shift-N，§2.1.3）
③ 通用选项对不对？      （顶点组/纹理坐标，§2.2）
④ Apply 的状态对不对？  （是否已 Apply、是否是栈顶，§2.1.5）
⑤ 求解器对不对？        （Boolean 的 Fast/Exact）
```

> **★★ 这个顺序是"从最省时到最费时"** ——
> **前两项各花 5 秒，能解决大部分问题。**
