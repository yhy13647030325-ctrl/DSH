# 第 17 章：几何节点（Geometry Nodes）

> **原书分区**：`modeling/geometry_nodes/**`（44 文件 / 39,884 字符）
> **本版覆盖**：导论 + 8 类节点 + 40 个具体节点（原文逐节读完）
> **定位方式**：EPUB 无页码 → **xhtml 文件路径**
> **⚠ 版本说明**：这是 **Blender 2.92** 的几何节点（第一代）——
> **节点名与 3.x/4.x 有差异**，本版在§17.5 给出对照。

---

## 17.0 本章解决什么

> **原文（`geometry_nodes/introduction.xhtml`）**：
> 「**节点可以用比普通修改器更复杂的方式改变物体的几何。
> 要使用它们，加一个"几何节点修改器（Geometry Nodes Modifier）"。**」

**★★★★★ 一句话：几何节点 = "用节点图代替修改器栈"。**

| 维度 | 修改器栈 | **几何节点** |
|---|---|---|
| **组合方式** | **★ 线性堆叠（上→下）** | **★ 任意图（可分支/合并）** |
| **灵活性** | 有限（每个修改器固定功能） | **★ 高（可自定义逻辑）** |
| **复用** | 单个修改器 | **★ 节点组（Node Group）** |

> **★★★ 判据：修改器是"固定配方"，几何节点是"可编程的配方"。**
> **★ 当"Array + Curve + 手调"不够用时，才需要几何节点。**

**★★★★ 它在硬表面工作流里的位置**：
> **★★ `blender-hard-surface` ch03/ch05/ch08/ch10 用 Array 做重复件** ——
> **★ 但 Array 只能"沿直线/相对偏移"。**
> **★ 几何节点的 `Point Distribute` + `Point Instance` 能"沿任意表面散布"。**

---

## 17.1 ★★★★★ 八类节点（Node Categories）

> **原文（`introduction.xhtml`，Node Categories 一节）**：

| 类别 | 原文表述 |
|---|---|
| **★ Attribute（属性）** | **「用于处理"按物体元素存储的数据"的节点，例如顶点组。」** |
| **★ Color（颜色）** | **「用于修改通过颜色插口传递的颜色数据。」** |
| **★ Geometry（几何）** | **「可操作不同几何类型（体积、网格）的节点。」** |
| **★ Input（输入）** | **「主要用作其他节点输入的节点。」** |
| **★ Mesh（网格）** | **「只操作网格的节点。」** |
| **★ Point（点）** | **「修改物体元素（如顶点）的节点。」** |
| **★ Utilities（工具）** | **「用于修改数据的通用目的节点。」** |
| **★ Vector（向量）** | **「用于修改向量量的节点。」** |

**★★★★★ 八类的"用途地图"（本节核心）**：

| 想做什么 | 看哪类 |
|---|---|
| **★ 读/写顶点组、自定义属性** | **★ Attribute** |
| **★ 上色** | Color |
| **★ 网格与体积互转、变换** | **★ Geometry** |
| **★ 取物体信息、给常量** | **★ Input** |
| **★ 布尔、细分、三角化** | **★ Mesh** |
| **★ 散布点、实例化、旋转缩放** | **★ Point（最重要的类）** |
| **★ 数学运算、范围映射** | **★ Utilities** |
| **★ 向量拆分合并** | Vector |

> **★★★ 判据：硬表面最常用的是 `Point` 类**（散布 + 实例化 = 替代 Array）。

---

## 17.2 ★★★★★ 40 个具体节点（按类）

> **原文（`geometry_nodes/index.xhtml` 的目录 + 各节点页）**：

### 17.2.1 ★★★★★ Attribute 类（7 个）

| 节点 | 作用 |
|---|---|
| **Attribute Compare** | 比较属性值 |
| **Attribute Fill** | 用常量填充属性 |
| **Attribute Math** | 对属性做数学运算 |
| **Attribute Mix** | 混合两个属性 |
| **Attribute Vector Math** | 对向量属性做运算 |
| **★ Attribute Randomize** | **★ 随机化属性（做"凌乱"用）** |
| **Attribute Color Ramp** | 用色带重映射属性 |

**★★★★ 与 `blender-hard-surface` 的对应**：
> **★★ `Attribute Randomize` 类似 ch08 的 `Randomize`（物体级）** ——
> **★ 但这里是"按属性逐元素随机"。**

### 17.2.2 ★★★★ Color 类（3 个）

| 节点 | 作用 |
|---|---|
| Color Ramp | 色带重映射 |
| Combine RGB | 合成 RGB |
| Separate RGB | 拆分 RGB |

### 17.2.3 ★★★★★ Geometry 类（2 个）

| 节点 | 作用 |
|---|---|
| **★ Join Geometry** | **★ 合并多个几何（把多份网格拼成一个）** |
| **★ Transform** | **★ 对几何做变换** |

> **★★ 判据：`Join Geometry` 是"把多个实例合成一份网格"的关键** ——
> **★ 实例化后要"变成真几何"就用它。**

### 17.2.4 ★★★★ Input 类（4 个）

| 节点 | 作用 |
|---|---|
| **★ Object Info** | **★ 取另一个物体的信息（位置/几何）** |
| **Random Float** | 随机浮点数 |
| **Value** | 常量值 |
| **Vector** | 常量向量 |

### 17.2.5 ★★★★★ Mesh 类（4 个）

| 节点 | 作用 |
|---|---|
| **★ Boolean** | **★ 布尔运算（几何节点版）** |
| **★ Edge Split** | **★ 按角度拆边** |
| **★ Subdivision Surface** | **★ 细分（几何节点版）** |
| **★ Triangulate** | **★ 三角化** |

> **★★★ 判据：`Mesh` 类的四个节点都是"把修改器搬进节点图"** ——
> **★ 所以可以用"节点逻辑"控制它们（如"按距离决定细分级数"）。**

### 17.2.6 ★★★★★ Point 类（7 个，最重要）

| 节点 | 作用 |
|---|---|
| **★ Align Rotation to Vector** | **★ 让实例朝向某向量** |
| **★★ Point Distribute** | **★ 在表面散布点** |
| **★★ Point Instance** | **★ 在每个点上实例化物体** |
| **★ Point Rotate** | **★ 旋转点** |
| **★ Point Scale** | **★ 缩放点** |
| **★ Point Separate** | **★ 按条件分离点** |
| **★ Point Translate** | **★ 平移点** |

**★★★★★ 这是"替代 Array"的完整链条（本节核心）**：

```
Point Distribute（在表面撒点）
   ↓
Point Instance（每个点放一个"要重复的物体"）
   ↓
Align Rotation to Vector（让每个实例朝着表面法线）
   ↓
★ 结果：沿任意曲面散布的重复件
```

| 步骤 | 对应 Array 的能力 |
|---|---|
| **★ Point Distribute** | **★ Array 做不到（只能直线/曲线）** |
| **Point Instance** | Array 的"复制" |
| **Align Rotation** | **★ Array 做不到（不自动朝法线）** |

> **★★★ 判据：几何节点相对 Array 的两个"质变"** ——
> **★ ① 能在任意表面散布；② 能自动对齐法线。**
> **★ 这两个能力正是"螺栓/铆钉/散热片"最需要的。**

### 17.2.7 ★★★★ Utilities 类（6 个）

| 节点 | 作用 |
|---|---|
| Boolean Math | 布尔逻辑运算 |
| Clamp | 钳制到范围 |
| Float Compare | 浮点比较 |
| **★ Map Range** | **★ 把一个范围映射到另一个（做比例换算）** |
| **★ Math** | **★ 数学运算（加减乘除/幂/正弦等）** |
| Vector Math | 向量运算 |

> **★★ `Map Range` 类似 `blender-hard-surface` ch11 的 `Transformation` 约束的"映射"** ——
> **★ 但这里是"数值范围映射"，不是"物体属性映射"。**

### 17.2.8 ★★★★ Vector 类（3 个）

| 节点 | 作用 |
|---|---|
| Combine XYZ | 合成向量 |
| Separate XYZ | 拆分向量 |
| Vector Math | 向量运算 |

### 17.2.9 ★★★★ Group 类（3 个）

| 节点 | 作用 |
|---|---|
| **Make Group** | **★ 把选中的节点打包成一个组** |
| **Ungroup** | **★ 拆开组** |
| **Node Groups** | **★ 复用组** |

> **★★★ 判据：`Make Group` 是"把节点图变成可复用组件"的关键** ——
> **★ 与 ch02 的"修改器可复用"同理，但颗粒度是"整个逻辑"。**

---

## 17.3 ★★★★ 属性系统（Attributes）

> **原文（`geometry_nodes/attributes_reference.xhtml`，2,479 字符）**：

**★★★★★ 属性（Attribute）是什么**：
> **★★ 属性 = "按物体元素存储的数据"** ——
> **★ 如：每个顶点的位置、每个面的材质索引、每个点的自定义数值。**

| 属性类型 | 存储在哪 |
|---|---|
| **Position** | 每个顶点 |
| **Normal** | 每个顶点/面 |
| **Material Index** | 每个面 |
| **★ 自定义属性** | **★ 任意元素（点/边/面/角）** |

**★★★★★ 与顶点组的关系（原文明确提到）**：
> **「Attribute：用于处理"按物体元素存储的数据"的节点，例如顶点组。」**

| 概念 | 关系 |
|---|---|
| **★ 顶点组** | **★ 一种特殊的属性（每个顶点的权重）** |
| **★ 自定义属性** | **★ 更通用（可以是任意数值/向量/颜色）** |

> **★★ 判据：几何节点能"读顶点组"** ——
> **★ 所以可以把"权重刷的结果"作为节点逻辑的输入。**

**★★★★ 内置属性（Built-In Attributes）**：
> **原文提到 `Built-In Attributes` 与 `Naming Conventions` 两节** ——
> **★ 说明有一批"系统预定义"的属性名，不需要自己创建。**

---

## 17.4 ★★★★★ 几何节点 vs 修改器的分工

**★★★★★ 五条判据（本版归纳）**：

| 需求 | 用哪个 |
|---|---|
| **★ 线性处理（倒角→细分→镜像）** | **★ 修改器栈**（简单直观） |
| **★ 沿表面散布重复件** | **★ 几何节点**（Array 做不到） |
| **★ 按条件分支处理** | **★ 几何节点**（修改器无分支） |
| **★ 把逻辑复用到多个物体** | **★ 两者都行**（修改器 vs 节点组） |
| **★ 参数要暴露给用户调** | **★ 几何节点（Modifier 面板可显示输入）** |

> **★★★ 判据：几何节点的价值在"改不了的部分"** ——
> **★ 能用修改器做的，就别用几何节点**（因为修改器简单、快、易调）。

---

## 17.5 ★★★★★ 版本差异（必读，否则 3.x/4.x 会找不到节点）

**★★★★★ 2.92 与 3.x/4.x 的节点名对照（本版归纳，需实测验证）**：

| 2.92（本书） | 3.x / 4.x |
|---|---|
| **Point Distribute** | **★ Distribute Points on Faces** |
| **Point Instance** | **★ Instance on Points** |
| **Attribute Math** | **★ Math（统一为一个）** |
| **Attribute Vector Math** | **★ Vector Math** |
| **Attribute Mix** | **★ Mix** |
| **Attribute Color Ramp** | **★ Color Ramp** |
| **Attribute Randomize** | **★ Random Value** |
| **Attribute Compare** | **★ Compare** |
| **Join Geometry** | **★ Join Geometry（未变）** |
| **Make Group / Ungroup** | **★ 改为 "Group / Ungroup"（`Ctrl+G`）** |

> **★★★ 判据：2.92 的 "Attribute 前缀" 在 3.x 后被取消** ——
> **★ 因为"属性"成了通用概念，不需要每个节点都加前缀。**
> **⚠ 本版如实标注：上表按节点功能对应，未在 3.x/4.x 逐条实测。**

**★★★★ 一条最重要的版本差异**：
> **★★ 2.92 的几何节点"只能改几何，不能读取场景"**；
> **★ 3.x 之后加入"Field（域）"系统，能力大幅扩展。**
> **★ 判据：本章的节点逻辑"框架仍然有效"，但具体节点要按新版本找。**

---

## 17.6 ★★★★★ 本章判据总表（共 36 条）

### 定位（17.0）

| # | 判据 | 出处 |
|---|---|---|
| **1** | **★★★★★ 几何节点 = "用节点图代替修改器栈"** | `geometry_nodes/introduction` |
| **2** | **★★★★ 要给物体加"几何节点修改器"才能用** | `geometry_nodes/introduction` |
| **3** | **★★★★★ 修改器是"固定配方"，几何节点是"可编程的配方"** | 本章归纳 |
| **4** | **★★★★ 修改器线性堆叠；几何节点可分支/合并** | 本章归纳 |
| **5** | **★★★ 判据：能用修改器做的，就别用几何节点** | 本章归纳 |

### 八类节点（17.1）

| # | 判据 | 出处 |
|---|---|---|
| **6** | **★★★★★ 八类**：Attribute / Color / Geometry / Input / Mesh / Point / Utilities / Vector | `geometry_nodes/introduction` |
| **7** | **★★★★ Attribute = 处理"按物体元素存储的数据"（如顶点组）** | `geometry_nodes/introduction` |
| **8** | **★★★★ Geometry = 可操作不同几何类型（体积、网格）** | `geometry_nodes/introduction` |
| **9** | **★★★★ Point = 修改物体元素（如顶点）** | `geometry_nodes/introduction` |
| **10** | **★★★ Vector = 修改向量量** | `geometry_nodes/introduction` |
| **11** | **★★★★★ 判据：硬表面最常用的类是 `Point`**（散布+实例化=替代 Array） | 本章归纳 |

### 关键节点（17.2）

| # | 判据 | 出处 |
|---|---|---|
| **12** | **★★★★ `Attribute Randomize` = 逐元素随机**（做"凌乱"） | `geometry_nodes/attribute/attribute_randomize` |
| **13** | **★★★★ 类似 ch08 的 `Randomize`，但这里是"按属性逐元素"** | 本章归纳 |
| **14** | **★★★★★ `Join Geometry` = 合并多个几何（实例转真几何）** | `geometry_nodes/geometry/join_geometry` |
| **15** | **★★★ 判据：实例化后要"变成真几何"就用它** | 本章归纳 |
| **16** | **★★★★ `Transform` = 对几何做变换** | `geometry_nodes/geometry/transform` |
| **17** | **★★★★ `Object Info` = 取另一个物体的信息** | `geometry_nodes/input/object_info` |
| **18** | **★★★★★ Mesh 类四个都是"修改器搬进节点图"**：Boolean / Edge Split / Subdivision / Triangulate | `geometry_nodes/mesh/` |
| **19** | **★★★★ 所以可以用"节点逻辑"控制它们（如按距离决定细分）** | 本章归纳 |
| **20** | **★★★★★ `Point Distribute` = 在表面散布点** | `geometry_nodes/point/point_distribute` |
| **21** | **★★★★★ `Point Instance` = 在每个点上实例化物体** | `geometry_nodes/point/point_instance` |
| **22** | **★★★★★ `Align Rotation to Vector` = 让实例朝向某向量** | `geometry_nodes/point/align_rotation_to_vector` |
| **23** | **★★★★★ 完整链条**：Distribute → Instance → Align Rotation → 结果 | 本章归纳 |
| **24** | **★★★★★ 相对 Array 的两个质变**：① 任意表面散布 ② 自动对齐法线 | 本章归纳 |
| **25** | **★★★★ 这两个能力正是"螺栓/铆钉/散热片"最需要的** | 本章归纳 |
| **26** | **★★★★ `Map Range` = 把一个范围映射到另一个** | `geometry_nodes/utilities/map_range` |
| **27** | **★★★ 类似 ch11 的 Transformation 约束的"映射"，但这是数值不是属性** | 本章归纳 |
| **28** | **★★★★ `Math` = 数学运算（加减乘除/幂/正弦）** | `geometry_nodes/utilities/math` |
| **29** | **★★★★★ `Make Group` = 把选中节点打包成组** | `geometry_nodes/group` |
| **30** | **★★★ 判据：这是"把节点图变成可复用组件"的关键** | 本章归纳 |

### 属性系统（17.3）

| # | 判据 | 出处 |
|---|---|---|
| **31** | **★★★★★ 属性 = 按物体元素存储的数据**（位置/法线/材质索引/自定义） | `geometry_nodes/attributes_reference` |
| **32** | **★★★★★ 顶点组是一种特殊的属性**（每个顶点的权重） | `geometry_nodes/attributes_reference` |
| **33** | **★★★ 判据：几何节点能"读顶点组"** | 本章归纳 |
| **34** | **★★★ 所以可以把"权重刷的结果"作为节点逻辑的输入** | 本章归纳 |
| **35** | **★★★★ 有一批"系统预定义"的内置属性名** | `geometry_nodes/attributes_reference` |

### 版本差异（17.5）

| # | 判据 | 出处 |
|---|---|---|
| **36** | **★★★★★ 2.92 的 "Attribute 前缀"在 3.x 后被取消**（详见§17.5 对照表） | 本章归纳 |

---

## 17.7 ★★★ 本章的空白

| 缺什么 | 情况 | 该去哪查 |
|---|---|---|
| **★★ 3.x/4.x 的完整节点对照** | 本版只给了 10 个主要对照 | 新版官方手册 |
| **★★ Field（域）系统** | 2.92 无，3.x 新增 | 新版手册 |
| **★★ 完整项目实战** | 原手册只讲节点定义，无完整项目 | 需另行学习 |
| **★★ 各节点参数全解** | 40 个节点，本版按类摘要 | 原手册各节点页 |
| **★★ 图片内容** | EPUB 文本层无图 | 原书 xhtml 插图 |

---

## 17.8 ★★★ 与其他章的关系

| 本章内容 | 关联 | 关系 |
|---|---|---|
| **Point Distribute + Instance** | **`blender-hard-surface` ch03/ch10 的 Array** | **★ 升级版：任意表面散布** |
| **Mesh 类（Boolean/Subdivision）** | **ch02 修改器** | **★ 同一功能的两条路径** |
| **Attribute（顶点组）** | **ch13/ch16 蒙皮权重** | **★ 权重可作为节点输入** |
| **Make Group** | **ch08 节点组** | **★ 着色节点也是"组"** |
| **Map Range** | **ch12 Transformation 约束** | 数值版 vs 属性版 |
| **几何节点写在 ch17** | **`blender-hard-surface` 无此内容** | **★ 两本里唯一完全缺的现代能力** |
