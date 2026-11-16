# 第 8 章：材质与着色节点（Materials & Shader Nodes）

> **原书分区**：`render/shader_nodes/**` + `render/materials/**`（119 文件）
> **原文正文 173,745 字符**（本版按主题逐节读完，本分区文件最多）
> **定位方式**：EPUB 无页码 → **xhtml 文件路径**
> **本章含 6 节**：着色器概念 / Principled BSDF / 材质槽 / 混合节点 / 贴图节点 / 节点组织

---

## 8.0 本章解决什么

> **原文（`shader_nodes/introduction.xhtml`）**：
> 「**材质、灯光和背景都是用"着色节点网络"定义的。
> 这些节点输出值、向量、颜色和着色器。**」

**★★★★★ 一句话：材质不是"填参数"，是"搭一个数据流网络"。**

| 层级 | 内容 |
|---|---|
| **★ 节点（Node）** | **★ 最小的计算单元** |
| **★ 节点网络（Node Tree）** | **★ 若干节点连线** |
| **★ 材质（Material）** | **★ 一个节点网络的数据块** |

> **★★★ 判据：理解材质 = 理解"数据从哪流到哪"** ——
> **★ 这与 ch06 的"节点式建模"是同一思维。**

---

## 8.1 ★★★★★ 着色器（Shader）—— 本章最核心的概念

> **原文（`shader_nodes/introduction.xhtml`）**：
> 「**搭建节点设置时要理解的一个重要概念是"着色器 socket"。
> 所有表面着色器与体积着色器的输出"是一个着色器"，
> 描述表面或体积处的光照交互，而不是表面的颜色。**」

**★★★★★ 「着色器 socket ≠ 颜色 socket」**：

| Socket 类型 | 传的是什么 |
|---|---|
| **★ Color** | **★ 颜色（RGB）** |
| **★ Vector** | **★ 向量（位置/方向/UV）** |
| **★ Value** | **★ 单个数值** |
| **★ Shader** | **★ "光照交互的描述"（不是颜色！）** |

> **★★★ 判据：Shader socket 插到 Color socket 上是错的** ——
> **★ 因为它不是"颜色"，是"BSDF 的计算结果"。**
> **★ 这是初学者最常见的连线错误。**

**★★★★★ 四种着色器（原文明确列举）**：

| 着色器 | 描述（原文） |
|---|---|
| **★ BSDF** | **★ 描述物体表面的光反射、折射与吸收** |
| **★ Emission** | **★ 描述物体表面或体积里的光发射** |
| **★ Volume** | **★ 描述体积内部的光散射** |
| **★ Background** | **★ 描述环境的光发射** |

**★★★★ 一个共同点（原文）**：
> **「每个着色器节点都有一个颜色输入，并输出……（着色器）」**
> **★ 所以"着色器 = 颜色 + 光照行为"的组合。**

---

## 8.2 ★★★★★ Principled BSDF（本章最重要的节点）

> **原文（`shader_nodes/shader/principled.xhtml`）**：
> 「**Principled BSDF 把多个层组合成一个易用的节点。
> 它基于 Disney 的 principled 模型，也叫 "PBR" 着色器，
> 这使它与其他软件兼容，如 Pixar 的 Renderman® 和 Unreal Engine®。
> 从 Substance Painter® 这类软件绘制或烘焙的图像贴图，
> 可以直接连到这个着色器对应的参数上。**」
> 「**这个 "Uber" 着色器包含多个层，能创建种类繁多的材质。
> 基础层是"漫反射、金属、次表面散射与透射"之间的用户可控混合。
> 在这之上还有一个高光层、光泽层（sheen）和清漆层（clearcoat）。**」

**★★★★★ Principled BSDF 的分层结构（本节的核心）**：

```
★ 清漆层（Clearcoat）
   ↓
★ 光泽层（Sheen）
   ↓
★ 高光层（Specular）
   ↓
★ 基础层（Base）：漫反射 / 金属 / 次表面散射 / 透射
```

**★★★★★ 这个"分层"是理解所有参数的地图**：

| 层 | 参数（典型） | 用于 |
|---|---|---|
| **基础层** | **Base Color / Metallic / Subsurface / Transmission** | **★ 决定"这是什么材质"** |
| **高光层** | **Specular / Roughness** | **★ 表面反射强度** |
| **光泽层** | **Sheen** | **★ 布料/天鹅绒** |
| **清漆层** | **Clearcoat** | **★ 车漆/上光** |

> **★★★ 判据：调材质时先问"这是哪一层的问题"** ——
> **★ 颜色不对 → 基础层；反光太强 → 高光层；布感不足 → 光泽层；不够亮 → 清漆层。**

**★★★★★ 三个最常用的参数（与 `blender-hard-surface` 对应）**：

| 参数 | 作用 | 硬表面用法 |
|---|---|---|
| **★ Base Color** | **★ 底色** | **军绿/米色/黑** |
| **★ Metallic** | **★ 金属度（0/1）** | **★ 枪械金属件 = 1.000** |
| **★ Roughness** | **★ 粗糙度（0 亮 / 1 糙）** | **★ 与 ch12 的粗糙度贴图联动** |

**★★★★★ 原文的一条重要说明（PBR 兼容性）**：
> **「强调与其他软件兼容，意味着它对某些输入参数的解释不同……」**
> **★★ 所以 Blender 的 Principled BSDF 与 Substance/Renderman 的"同名参数"可能"含义略有差异"。**
> **★ 判据：跨软件导贴图时要"验证一次"，不能假定完全等价。**

---

## 8.3 ★★★★★ 材质赋值（Material Assignment）

> **原文（`materials/assignment.xhtml`）**：
> 「**材质是数据块，可以创建后赋给一个或多个物体。
> 一个物体也可以在不同材质槽里赋多个材质，
> 它们对应物体的不同部分。
> 如果希望材质之间有平滑过渡，那么用 `Mix Shader` 混合着色节点是更好的方案。**」
> 「**材质槽把材质链接到物体与网格。
> 默认情况下物体只有一个材质槽，把材质赋给整个物体。
> 如果网格的不同部分需要不同材质，可以创建多个材质槽。**」

**★★★★★ 两条关键判据（本节最重要）**：

**① 多材质槽 = 硬边界；Mix Shader = 软过渡**

| 方式 | 效果 |
|---|---|
| **★ 多材质槽** | **★ 部件之间"硬边界"** |
| **★ Mix Shader** | **★ 材质之间"平滑过渡"** |

> **★★★ 判据：要"这块是金属、那块是漆"→ 多材质槽；**
> **★ 要"金属和漆渐变"→ Mix Shader。**
> **★ 这与 `blender-hard-surface` ch04 的"四个材质"完全对应（那里用的是多材质槽）。**

**② 材质槽"链接到物体与网格"**
> **★★ 所以同一材质可以"赋给多个物体"，改一次全变。**
> **★ 这与 ch06 的 `Alt+D`（链接数据）是同一思维。**

---

## 8.4 ★★★★★ 混合节点（Mix Node）

> **原文（`shader_nodes/color/mix.xhtml`）**：
> **Mix Node 把两个输入按一个系数混合。**

**★★★★★ Mix 的三种用途（本章最重要的实用知识）**：

| 用途 | 输入 A | 输入 B | 系数 |
|---|---|---|---|
| **★ 混色** | **★ 颜色 1** | **★ 颜色 2** | **★ 遮罩（灰度图）** |
| **★ 混材质** | **★ BSDF 1** | **★ BSDF 2** | **★ 遮罩** |
| **★ 混贴图** | 贴图 1 | 贴图 2 | 遮罩/UV |

**★★★★★ 这是 `blender-hard-surface` ch04/ch12 的核心手法**：

| 章 | 用法 |
|---|---|
| **ch04** | **Edge Mask 作系数 → 混"漆色"与"磨损色"** |
| **ch04** | **两张法线贴图用 MixRGB 混合** |
| **ch12** | **Noise 驱动系数 → 磨损强度随机** |

> **★★★ 判据：Mix 的"系数输入"是"遮罩"的入口** ——
> **★ 任何灰度图（Edge Mask / Noise / 渐变）都可以插进系数，控制"哪里显示哪个"。**
> **★ 这是"程序化材质"的万能结构。**

---

## 8.5 ★★★★★ 贴图节点（Texture Nodes）

> **原文（`shader_nodes/textures/` 与 `render/materials/legacy_textures/`）**：

### 8.5.1 ★★★★ 两大类贴图

| 类型 | 来源 |
|---|---|
| **★ Image Texture** | **★ 外部图像文件** |
| **★ Procedural Texture** | **★ 程序生成（Noise / Voronoi / Checker / Gradient…）** |

**★★★★★ 程序化 vs 图像（关键对照）**：

| 维度 | 图像贴图 | **程序化贴图** |
|---|---|---|
| **分辨率** | **★ 固定（会糊）** | **★ 无限（可任意放大）** |
| **文件大小** | 大 | **★ 无** |
| **可控性** | 有限（要重绘） | **★ 参数可调** |
| **真实度** | **★ 高（真实照片）** | 中（数学生成） |

> **★★★ 判据：`blender-hard-surface` ch12 用 `Bump` + `Noise` 而不用烘焙法线图** ——
> **★ 正是因为程序化的"无限分辨率"（放大不糊）。**

### 8.5.2 ★★★★★ 常用程序化纹理

| 纹理 | 特点 |
|---|---|
| **★ Noise Texture** | **★ 随机噪声（最常用）** |
| **★ Voronoi Texture** | **★ 细胞状（做裂纹/鳞片）** |
| **★ Checker Texture** | **★ 棋盘格（做校验）** |
| **★ Gradient Texture** | **★ 渐变** |
| **Wave Texture** | 波纹（木纹/水波） |
| **Magic Texture** | 迷幻图案 |

> **★★ 判据：`Noise` 是"万能起点"**（磨损/粗糙/凹凸都能用）。

### 8.5.3 ★★★★★ 法线贴图节点（`Normal Map`）

> **原文（`shader_nodes/converter/normal_map.xhtml`）**：
> **`Normal Map` 节点把"颜色编码的法线"转成"真实法线向量"。**

**★★★★★ 这是 `blender-hard-surface` ch06 的关键判据的原始出处**：

| 项 | 内容 |
|---|---|
| **必须用 `Normal Map` 节点** | **★ 不能把法线贴图直连 Normal 插口** |
| **★ 因为** | **★ 贴图是"颜色编码"，直连会被当颜色** |

**★★★★ 与 `Bump` 节点的区别**：

| 节点 | 输入 | 用途 |
|---|---|---|
| **★ `Normal Map`** | **★ 法线贴图（RGB）** | **★ 已烘焙的法线图** |
| **★ `Bump`** | **★ 灰度高度图** | **★ 程序化假凹凸** |

> **★★ 判据：`Normal Map` 读"法线数据"，`Bump` 从"灰度"生成法线。**

---

## 8.6 ★★★★ 坐标与映射（Texture Coordinate & Mapping）

> **原文（`shader_nodes/input/texture_coordinate.xhtml`）**：

**★★★★★ Texture Coordinate 的四种输出**：

| 输出 | 含义 |
|---|---|
| **★ Generated** | **★ 按物体包围盒（会随缩放变）** |
| **★ Object** | **★ 按物体的局部坐标** |
| **★ UV** | **★ 按 UV 展开（最可控）** |
| **Normal** | 按法线方向 |

**★★★★★ 这是 `blender-hard-surface` ch06/ch12 反复用到的**：

| 章 | 用法 |
|---|---|
| **ch06** | **Box Mapping 用 `Object` 输出** |
| **ch12** | **`Ctrl+T` 后选 `UV`（让噪声跟 UV 走）** |

> **★★★ 判据：**
> **要"贴图不随物体缩放变"→ 用 `UV`；**
> **要"按物体形状投射"→ 用 `Object`（Box Mapping）。**

---

## 8.7 ★★★★★ 本章判据总表（共 40 条）

### 着色器概念（8.1）

| # | 判据 | 出处 |
|---|---|---|
| **1** | **★★★★★ 材质、灯光、背景都由"着色节点网络"定义** | `shader_nodes/introduction` |
| **2** | **★★★★★ 着色器 socket 传的是"光照交互描述"，**不是颜色**** | `shader_nodes/introduction` |
| **3** | **★★★ 判据：Shader socket 插到 Color socket 上是错的** | 本章归纳 |
| **4** | **★★★★★ 四种着色器**：BSDF（反射/折射/吸收）/ Emission（发射）/ Volume（散射）/ Background（环境） | `shader_nodes/introduction` |
| **5** | **★★★ 每个着色器都有"颜色输入"和"着色器输出"** | `shader_nodes/introduction` |

### Principled BSDF（8.2）

| # | 判据 | 出处 |
|---|---|---|
| **6** | **★★★★★ Principled BSDF 基于 Disney principled 模型（PBR）** | `shader_nodes/shader/principled` |
| **7** | **★★★★ 与其他软件兼容**（Renderman / Unreal / Substance Painter） | `shader_nodes/shader/principled` |
| **8** | **★★★★★ 分层结构**：清漆（Clearcoat）→ 光泽（Sheen）→ 高光（Specular）→ **基础（Base）** | `shader_nodes/shader/principled` |
| **9** | **★★★★★ 基础层 = 漫反射/金属/次表面散射/透射的混合** | `shader_nodes/shader/principled` |
| **10** | **★★★★★ 判据：调材质先问"这是哪一层的问题"** | 本章归纳 |
| **11** | **★★★ 颜色不对→基础层；反光太强→高光层；布感不足→光泽层；不够亮→清漆层** | 本章归纳 |
| **12** | **★★★★★ 三个最常用参数**：Base Color / **Metallic（0/1）** / **Roughness（0 亮 / 1 糙）** | `shader_nodes/shader/principled` |
| **13** | **★★★ 硬表面金属件 Metallic = 1.000** | 本章归纳 |
| **14** | **★★★★ 原文强调"对某些输入参数的解释不同"**（跨软件不假定完全等价） | `shader_nodes/shader/principled` |
| **15** | **★★★ 判据：跨软件导贴图要验证一次** | 本章归纳 |

### 材质赋值（8.3）

| # | 判据 | 出处 |
|---|---|---|
| **16** | **★★★★ 材质是数据块，可赋给一个或多个物体** | `materials/assignment` |
| **17** | **★★★★★ 多材质槽 = 部件之间的"硬边界"** | `materials/assignment` |
| **18** | **★★★★★ `Mix Shader` = 材质之间的"平滑过渡"** | `materials/assignment` |
| **19** | **★★★★★ 判据：要"这块是金属那块是漆"→ 多材质槽；要渐变→ Mix Shader** | 本章归纳 |
| **20** | **★★★ 材质槽"链接到物体与网格"** → 同一材质改一次全变 | `materials/assignment` |
| **21** | **★★★ 与 ch06 的 `Alt+D`（链接数据）同一思维** | 本章归纳 |

### 混合节点（8.4）

| # | 判据 | 出处 |
|---|---|---|
| **22** | **★★★★★ Mix Node 把两个输入按"系数"混合** | `shader_nodes/color/mix` |
| **23** | **★★★★★ 三种用途**：混色 / 混材质（Mix Shader）/ 混贴图 | `shader_nodes/color/mix` |
| **24** | **★★★★★ 系数输入是"遮罩"的入口** | 本章归纳 |
| **25** | **★★★★★ 任何灰度图（Edge Mask / Noise / 渐变）都能插进系数** | 本章归纳 |
| **26** | **★★★ 这是"程序化材质"的万能结构** | 本章归纳 |
| **27** | **★★★★ 这是 `blender-hard-surface` ch04/ch12 的核心手法** | 本章归纳 |

### 贴图节点（8.5）

| # | 判据 | 出处 |
|---|---|---|
| **28** | **★★★★ 两大类**：Image Texture（外部图）/ Procedural Texture（程序生成） | `shader_nodes/textures/` |
| **29** | **★★★★★ 程序化 vs 图像**：前者无限分辨率、无文件体积、参数可调；后者真实度高 | 本章归纳 |
| **30** | **★★★ 判据：`blender-hard-surface` ch12 用 Bump+Noise 而不用烘焙法线图，正是因为无限分辨率** | 本章归纳 |
| **31** | **★★★★ 六个常用程序化纹理**：Noise / Voronoi / Checker / Gradient / Wave / Magic | `shader_nodes/textures/` |
| **32** | **★★★ 判据：`Noise` 是"万能起点"**（磨损/粗糙/凹凸都能用） | 本章归纳 |
| **33** | **★★★★★ `Normal Map` 节点把"颜色编码的法线"转成"真实法线向量"** | `shader_nodes/converter/normal_map` |
| **34** | **★★★★★ 法线贴图**不能直连 Normal 插口**（会被当颜色）** | `shader_nodes/converter/normal_map` |
| **35** | **★★★★★ 这是 `blender-hard-surface` ch06「必须过 Normal Map 节点」的原始出处** | 本章归纳 |
| **36** | **★★★★ `Normal Map` vs `Bump`**：前者读法线图（RGB），后者从灰度生成法线 | 本章归纳 |

### 坐标与映射（8.6）

| # | 判据 | 出处 |
|---|---|---|
| **37** | **★★★★★ Texture Coordinate 四输出**：**Generated**（包围盒）/ **Object**（局部）/ **UV**（最可控）/ Normal | `shader_nodes/input/texture_coordinate` |
| **38** | **★★★★★ 判据：要"贴图不随缩放变"→ `UV`** | 本章归纳 |
| **39** | **★★★★★ 要"按物体形状投射"→ `Object`（Box Mapping）** | 本章归纳 |
| **40** | **★★★ 这正是 `blender-hard-surface` ch06 的 Box Mapping 与 ch12 的 `Ctrl+T` 选 `UV` 的依据** | 本章归纳 |

---

## 8.8 ★★★ 本章的空白

| 缺什么 | 情况 | 该去哪查 |
|---|---|---|
| **★★ 各节点的完整参数** | 119 文件，本版按主题摘要 | 原手册 `shader_nodes/` |
| **★★ Principled BSDF 的全部参数值** | 只列了最常用的三个 | 原手册 `shader/principled` |
| **★★ 体积着色器的用法** | 只列了存在 | 原手册 `shader/volume` |
| **★★ 图片内容** | EPUB 文本层无图 | **原书 xhtml 插图** |

---

## 8.9 ★★★ 与其他章的关系

| 本章内容 | 关联 | 关系 |
|---|---|---|
| **Principled BSDF 三参数** | **`blender-hard-surface` ch04/ch12** | **★ 本章是原始出处** |
| **多材质槽 vs Mix Shader** | **`blender-hard-surface` ch04（四个材质）** | ★ 原始出处 |
| **Mix 的系数 = 遮罩** | **`blender-hard-surface` ch04/ch12** | **★ 本章是原始出处** |
| **`Normal Map` 必须过节点** | **`blender-hard-surface` ch06** | ★ 原始出处 |
| **`Bump`（灰度）** | **`blender-hard-surface` ch12** | ★ 原始出处 |
| **Texture Coordinate（UV/Object）** | **`blender-hard-surface` ch06/ch12** | ★ 原始出处 |
| **色彩管理（Non-Color）** | **ch11** | 法线贴图的色彩空间 |
| **渲染引擎（Cycles/Eevee）** | **ch10** | 材质在两引擎里的表现 |
