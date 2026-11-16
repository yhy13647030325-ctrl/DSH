# 第 5 章：网格编辑与拓扑（Mesh Editing & Topology）

> **原书分区**：`modeling/meshes/editing/**`（92 文件）
> **原文正文 169,384 字符**（本版逐节读完，本分区最大）
> **定位方式**：EPUB 无页码 → **xhtml 文件路径**
> **本章含 6 节**：变换 / 挤出 / 合并与分离 / 边工具 / UV / 拓扑清理

---

## 5.0 本章解决什么

> **原文（`meshes/editing/introduction.xhtml`）**：
> 编辑模式（Edit Mode）是"逐个操作顶点/边/面"的模式 ——
> **与雕刻模式（ch04）的"笔刷改区域"相反。**

**★★★★★ 本章的定位：这是"精确编辑"的工具全集**：

| 需求 | 本章的节 |
|---|---|
| **改形状** | **★ 变换（§5.1）** |
| **加材料** | **★ 挤出（§5.2）** |
| **减材料/合并** | **★ 合并与分离（§5.3）** |
| **改边缘** | **★ 边工具（§5.4）** |
| **贴图准备** | **★ UV（§5.5）** |
| **清理拓扑** | **★ 拓扑清理（§5.6）** |

---

## 5.1 ★★★★★ 网格变换工具（Transform，9 种）

> **原文（`meshes/editing/mesh/transform/`）给了 9 个"网格变换"工具**：

| 工具 | 原文位置 | 作用 |
|---|---|---|
| **Basic（移动/旋转/缩放）** | `basic.xhtml` | 三大基础变换 |
| **★ To Sphere** | `to_sphere.xhtml` | **★ 向球形收拢** |
| **★ Shear** | `shear.xhtml` | **★ 错切** |
| **★ Bend** | `bend.xhtml` | **★ 弯曲** |
| **★ Push/Pull** | `push_pull.xhtml` | **★ 推/拉（沿法线）** |
| **★ Warp** | `warp.xhtml` | **★ 按两轴扭曲** |
| **★ Randomize** | `randomize.xhtml` | **★ 随机位移** |
| **★ Shrink/Fatten** | `shrink-fatten.xhtml` | **★ 沿法线缩放（`Alt+S`）** |
| **Skin Resize** | `skin_resize.xhtml` | Skin 修改器的半径 |

**★★★★★ 三个最常用的（与硬表面直接相关）**：

### 5.1.1 ★★★★★ Shrink/Fatten（`Alt+S`）

> **原文（`shrink-fatten.xhtml`）**：沿顶点法线方向"收缩/膨胀"。

**★★★★★ 这是全书出现频率最高的工具之一**：

| 章 | 用途 |
|---|---|
| **`blender-hard-surface` ch02** | **枪托橡胶垫加厚** |
| **ch05** | **飞船唇口外推** |
| **ch08** | **5 处：挡泥板/观察窗/灯罩/侧裙/车尾** |
| **ch09/ch10** | 炮塔/轮辋 |

> **★★★ 判据：`Alt+S` 是"薄壳件加厚"的标准工具** ——
> **★ 因为它"沿各自法线"，所以厚度均匀（`S` 会改变厚度）。**

### 5.1.2 ★★★★ To Sphere（向球形收拢）

> **★★ 把所有选中顶点"朝球心方向"移动，移动量由模拟的球形决定。**
> **★ 参数是 `Factor`（0 = 不动，1 = 完全成球）。**

> **★★ 判据：要把"不规则的一团面"变成"球状"→ To Sphere。**
> **★ 比手动调每个顶点快得多。**

### 5.1.3 ★★★★★ Randomize（随机位移）

> **★★ 每个顶点"随机方向 + 随机距离"位移。**

**★★★★★ 这正是 ch08「故意凌乱」的实现工具**：

| 场景 | 是否需要 Randomize |
|---|---|
| **机械件（螺栓底环）** | **★ 需要（做出锻造/焊接痕迹）** |
| **精密面** | **★ 不需要（要保持平）** |

> **★★★ 判据：要"真实工业感"，用 Randomize 加微小扰动。**
> **★ 但要注意：它会让模型"不对称"，所以对称件要慎用。**

---

## 5.2 ★★★★★ 挤出（Extrude，六种模式）

> **原文（`meshes/editing/mesh/extrude.xhtml`）**：
> 挤出有 **6 个变体** + **1 个重复挤出**。

### 5.2.1 ★★★★★ 六个变体的区别（本节核心）

| 变体 | 机制 |
|---|---|
| **Extrude Faces** | **★ 沿法线挤出选中的面** |
| **★ Extrude Faces Along Normals** | **★ 沿"各面各自法线"挤出（会分叉）** |
| **★ Extrude Individual Faces** | **★ 每个面独立挤出（不连接）** |
| **★ Extrude Manifold** | **★ 流形挤出（保持拓扑合法）** |
| **Extrude Edges** | **★ 挤出边（造新面/边循环）** |
| **Extrude Vertices** | **★ 挤出点（造新边）** |

**★★★★★ 三个容易混淆的区别**：

| 对比 | 结果 |
|---|---|
| **Faces vs Along Normals** | **★ 前者沿"平均法线"，后者沿"各面法线"** |
| **★ Along Normals vs Individual Faces** | **★ 前者"连着"，后者"各面独立分开"** |
| **★ Manifold** | **★ 保持"每个边只有两个面"的合法性** |

> **★★★ 判据：「挤出面后要分开」→ 用 Individual Faces；「挤出面后还连着但朝各自法线」→ Along Normals。**
> **★ 这是决定"挤出后拓扑是否连通"的关键选择。**

**★★★★ `Extrude Manifold` 的价值**：
> **★★ 普通挤出会"产生内部面/非流形边"；**
> **★ Manifold 会"自动处理这些"，保持拓扑合法。**
> **★ 判据：要后续做 Boolean/Subdivision 的地方，用 Manifold 挤。**

### 5.2.2 ★★★★★ Extrude Repeat（本节最实用）

> **原文（`extrude.xhtml`）**：
> 「**这个工具行为类似 Array 修改器，
> 通过沿视图的 Z 轴挤出来重复选择。
> 如果选择不是流形，就按指定次数挤出。**」
> **参数**：**`Offset X/Y/Z`（实例间距）、`Steps`（实例数）、`Scale Offset`（缩放乘数）**

**★★★★★ Extrude Repeat vs Array 修改器**：

| 维度 | **Extrude Repeat** | **Array 修改器** |
|---|---|---|
| **性质** | **★ 一次性生成真实几何** | **★ 非破坏性（可改可删）** |
| **能做** | **沿"视图 Z 轴"** | **沿任意轴/曲线** |
| **适合** | **★ 快速造"一组真实的面"** | **★ 参数化重复** |

> **★★★ 判据：要"一次性得到真实几何"→ Extrude Repeat；要"后面还能改参数"→ Array 修改器。**
> **★ 这与 ch03/ch10 的 Array 用法互补。**

---

## 5.3 ★★★★★ 合并、分离与切分

### 5.3.1 ★★★★★ Merge（合并）

> **原文（`meshes/editing/mesh/merge.xhtml`）**：

| 合并方式 | 机制 |
|---|---|
| **At Center** | **★ 全并到中点** |
| **At Cursor** | **★ 全并到 3D 游标** |
| **★ By Distance** | **★ 按距离阈值合并（`Shift+W`）** |
| **At First / At Last** | **★ 并到首/末顶点** |

**★★★★★ `By Distance` 是最重要的一个**：

| 章 | 用途 |
|---|---|
| **`blender-hard-surface` ch08** | **`G` 滑动后合并重复顶点** |
| **ch10** | **轮辋焊接** |
| **ch07** | **滑动后收尾** |

> **★★★ 判据：任何"滑动/复制/镜像"之后，都该 `Shift+W`（Merge by Distance）** ——
> **★ 否则会留下"看不见的重复顶点"，破坏后续操作。**

### 5.3.2 ★★★★★ Separate（分离）的四种

> **原文（`meshes/editing/mesh/separate.xhtml`）**：

| 方式 | 结果 |
|---|---|
| **Selection** | **★ 选中的分出去（一个新物体）** |
| **★ By Material** | **★ 按材质分（每个材质一个物体）** |
| **★ By Loose Parts** | **★ 按松散件分（一次拆成多个）** |
| **By Edges** | **按选中的边切开** |

> **★★★ 判据：区分 Selection / Loose Parts / By Material 三个用途** ——
> **★ 硬表面常用 Loose Parts（ch07 的 6 个轮子）。**

### 5.3.3 ★★★★ Split（切开但仍在同一物体）

> **原文（`split.xhtml`）**：
> **`Split` 与 `Separate` 不同 —— 它"切开"但留在同一物体内。**

| 操作 | 结果 |
|---|---|
| **Separate** | **★ 变成两个物体** |
| **★ Split** | **★ 同一物体内"断开"** |

> **★★ 判据：要"同一物体但拓扑断开"→ Split；要"分成两个物体"→ Separate。**

### 5.3.4 ★★★★★ Bisect（切割）

> **原文（`bisect.xhtml`）**：
> **用一个平面"切开"网格**，可选"填充切口"或"清空一侧"。

> **★★ 判据：Bisect = "用平面切一刀"** ——
> **★ 与 Knife（手画切线）不同：Bisect 是"平面"，Knife 是"任意线"。**

### 5.3.5 ★★★★ Knife Project（投影切）

> **原文（`knife_project.xhtml`）**：
> **用另一个物体的轮廓"投影"到当前网格上切。**

> **★★ 判据：要用"某个形状"去切另一个物体 → Knife Project** ——
> **★ 比 Boolean 轻量（不用建实体），但只切不挖。**

---

## 5.4 ★★★★★ 边工具（Edge Tools）

### 5.4.1 ★★★★★ Bevel（倒角，`Ctrl+B`）

> **原文（`editing/edge/bevel.xhtml`，10,555 字符，本分区最大文件）**：
> 「**Bevel 工具让你在几何上创建斜面或圆角。
> 倒角是一种"平滑边缘和角落"的效果。
> 现实世界的边很少是完全锐利的。
> 连刀刃都不能算完全锐利。
> 大多数边出于机械与实践原因是故意倒了角的。**」
> 「**倒角对于给"非有机模型"增加真实感也很有用。
> 在现实世界里，物体上的钝边会接住光线，改变边缘周围的着色。
> 这给人坚实、真实的外观，与未倒角的物体相反。**」

**★★★★★ 这段原文正是 `blender-hard-surface` ch01 引用的"倒角矛盾"**：

| 内容 | 出处 |
|---|---|
| **「现实没有绝对锐边」** | **`modeling/meshes/editing/edge/bevel`** |
| **「倒角改变边缘着色」** | **同上** |
| **「游戏里倒角被烘焙成法线贴图」** | **`blender-hard-surface` ch01 引申** |

> **★★★ 判据：倒角的两个理由（真实感 + 光照）在本手册里有原始出处。**

**★★★★ 顶点倒角的快捷键（原文明确）**：
> **原文**：「**`Ctrl-B`（边倒角）／`Shift-Ctrl-B`（顶点倒角）**」

> **★★ 注意：这与 `blender-hard-surface` ch05 说的 `Shift+B` 不同** ——
> **★ 那是**2.9x 之后**的改键；**2.92 手册写的是 `Shift-Ctrl-B`。**
> **★ 本版如实记录两个版本的差异。**

### 5.4.2 ★★★★ Screw（螺旋）

> **原文（`editing/edge/screw.xhtml`，19,100 字符，本分区最大文件）**：
> **沿一个轴"螺旋"复制选中的面。**

> **★★ 判据：Screw = "把截面绕轴螺旋成形体"** ——
> **★ 可做螺纹/弹簧/瓶口。**

---

## 5.5 ★★★★★ UV（`modeling/meshes/uv/`）

> **原文（`uv/editing.xhtml`、`meshes/editing/uv.xhtml`）**：

### 5.5.1 ★★★★★ UV 的核心操作

| 操作 | 作用 |
|---|---|
| **★ Unwrap（各种算法）** | **★ 展开成 2D** |
| **★ Mark Seam** | **★ 标记"剪开"的边** |
| **★ Pack Islands** | **★ 把所有 UV 岛打包进 0–1** |
| **★ Average Island Scale** | **★ 统一各岛比例** |
| **★ Smart UV Project** | **★ 自动展开** |
| **★ Project from View** | **★ 按当前视角投影** |

**★★★★★ 三个"自动"方法的区别**：

| 方法 | 特点 |
|---|---|
| **★ Smart UV Project** | **★ 自动分岛（硬表面常用）** |
| **★ Project from View** | **★ 按视角（适合"平面类"物体）** |
| **Unwrap（默认）** | **★ 按 Seam 展开（最可控）** |

> **★★★ 判据：**
> **自动省事 → Smart UV Project；**
> **精确控制 → 标 Seam + Unwrap；**
> **扁平物体 → Project from View。**

### 5.5.2 ★★★★★ `Average Island Scale` 的作用

> **★★ 让"所有 UV 岛"的"像素/单位"比例一致** ——
> **★ 否则不同岛上的贴图分辨率不同（一个岛清晰，一个岛模糊）。**

> **★★★ 判据：多岛 UV 必须做 Average Island Scale** ——
> **★ 这是"贴图密度一致"的前提。**

---

## 5.6 ★★★★★ 拓扑清理（本节最实用）

> **原文（`meshes/editing/mesh/` 下的多个工具）**：

### 5.6.1 ★★★★★ 五个清理工具

| 工具 | 作用 |
|---|---|
| **★ Dissolve** | **★ 溶解（删边保留面，合并成 N 边形）** |
| **★ Delete** | **★ 删除（留洞）** |
| **★ Merge by Distance** | **★ 按距离合并重复点** |
| **★ Convex Hull** | **★ 生成凸包** |
| **★ Limited Dissolve** | **★ 按角度溶解（批量合并共面区域）** |

**★★★★★ Dissolve vs Delete（`blender-hard-surface` ch02 讲过，这里是原始出处）**：

| 操作 | 结果 |
|---|---|
| **Delete（`X` → Vertices/Edges/Faces）** | **★ 删掉，留洞** |
| **★ Dissolve（`X` → Dissolve）** | **★ 删边但面保留（变 N 边形）** |

> **★★★ 判据：清理"多余的内部边"用 Dissolve，不用 Delete。**

**★★★★★ `Limited Dissolve` 是"批量版 Dissolve"**：
> **★★ 按"角度阈值"一次溶解所有近平共面的边。**
> **★ 判据：清理导入的高模/布尔结果时，Limited Dissolve 一次搞定。**

### 5.6.2 ★★★★ Convex Hull（凸包）

> **★★ 把选中的几何"包成凸多面体"。**

> **★★ 判据：要"快速得到一个凸形状"→ Convex Hull** ——
> **★ 用于碰撞体/简化轮廓。**

---

## 5.7 ★★★★★ 本章判据总表（共 46 条）

### 变换（5.1）

| # | 判据 | 出处 |
|---|---|---|
| **1** | **★★★★ 九个网格变换工具**：Basic / To Sphere / Shear / Bend / Push-Pull / Warp / Randomize / **Shrink-Fatten** / Skin Resize | `mesh/transform/` |
| **2** | **★★★★★ `Shrink/Fatten`（`Alt+S`）= 沿顶点法线收缩/膨胀** | `mesh/transform/shrink-fatten` |
| **3** | **★★★★★ 判据：`Alt+S` 是"薄壳件加厚"的标准工具**（厚度均匀） | 本章归纳 |
| **4** | **★★★ `S` 会改变厚度，`Alt+S` 不会** | 本章归纳 |
| **5** | **★★★★ `To Sphere` = 把选中顶点朝球心方向移动**（`Factor` 0→1） | `mesh/transform/to_sphere` |
| **6** | **★★★ 判据：要把"不规则一团面"变球状 → To Sphere** | 本章归纳 |
| **7** | **★★★★ `Randomize` = 每个顶点随机方向 + 随机距离位移** | `mesh/transform/randomize` |
| **8** | **★★★★★ `Randomize` 是"故意凌乱（锻造/焊接痕迹）"的实现工具** | 本章归纳 |
| **9** | **★★★ 但它会破坏对称，对称件要慎用** | 本章归纳 |
| **10** | **★★★ `Shear` = 错切；`Bend` = 弯曲；`Warp` = 按两轴扭曲** | `mesh/transform/` |

### 挤出（5.2）

| # | 判据 | 出处 |
|---|---|---|
| **11** | **★★★★★ 六个挤出变体**：Faces / **Along Normals** / **Individual Faces** / **Manifold** / Edges / Vertices | `mesh/extrude` |
| **12** | **★★★★★ Faces vs Along Normals**：前者沿"平均法线"，后者沿"各面法线（会分叉）" | `mesh/extrude` 归纳 |
| **13** | **★★★★★ Along Normals vs Individual Faces**：前者"连着"，后者"各面独立" | `mesh/extrude` 归纳 |
| **14** | **★★★★★ `Extrude Manifold` 保持"每边只有两面"的拓扑合法性** | `mesh/extrude` |
| **15** | **★★★ 判据：要后续做 Boolean/Subdivision 的地方，用 Manifold 挤** | 本章归纳 |
| **16** | **★★★★★ `Extrude Repeat` 行为类似 Array 修改器**（沿视图 Z 轴重复） | `mesh/extrude` |
| **17** | **★★★ 参数**：`Offset X/Y/Z`（间距）、`Steps`（实例数）、`Scale Offset`（缩放乘数） | `mesh/extrude` |
| **18** | **★★★★★ `Extrude Repeat` vs Array**：前者"一次性真实几何"，后者"非破坏性可改" | 本章归纳 |

### 合并与分离（5.3）

| # | 判据 | 出处 |
|---|---|---|
| **19** | **★★★★ 四种合并**：At Center / At Cursor / **By Distance** / At First / At Last | `mesh/merge` |
| **20** | **★★★★★ `Merge by Distance`（`Shift+W`）最重要** | `mesh/merge` |
| **21** | **★★★★★ 判据：任何"滑动/复制/镜像"后都该 `Shift+W`**（否则留重复顶点） | 本章归纳 |
| **22** | **★★★★ 四种分离**：Selection / **By Material** / **By Loose Parts** / By Edges | `mesh/separate` |
| **23** | **★★★ 硬表面常用 Loose Parts**（一次拆成多个独立件） | 本章归纳 |
| **24** | **★★★★★ `Split` vs `Separate`**：前者"同一物体内断开"，后者"分成两物体" | `mesh/split` |
| **25** | **★★★★ `Bisect` = 用平面切开**（可选填充切口/清空一侧） | `mesh/bisect` |
| **26** | **★★★ `Bisect`（平面）vs Knife（任意线）** | 本章归纳 |
| **27** | **★★★★ `Knife Project` = 用另一物体的轮廓投影切** | `mesh/knife_project` |
| **28** | **★★★ 比 Boolean 轻量（不用建实体），但只切不挖** | 本章归纳 |

### 边工具（5.4）

| # | 判据 | 出处 |
|---|---|---|
| **29** | **★★★★★ 倒角的两个理由**：① 现实没有绝对锐边 ② 改变边缘着色（接光） | `edge/bevel` |
| **30** | **★★★★★ 这是 `blender-hard-surface` ch01「倒角矛盾」的原始出处** | `edge/bevel` |
| **31** | **★★★★★ 快捷键**：`Ctrl-B`（边倒角）/ **`Shift-Ctrl-B`（顶点倒角）** | `edge/bevel` |
| **32** | **★★★ 注意：`blender-hard-surface` ch05 写的是 `Shift+B`** —— 那是 2.9x 后的改键 | 本章归纳 |
| **33** | **★★★★ `Screw` = 沿轴螺旋复制选中的面**（可做螺纹/弹簧/瓶口） | `edge/screw` |

### UV（5.5）

| # | 判据 | 出处 |
|---|---|---|
| **34** | **★★★★★ 三个"自动"方法的区别**：Smart UV Project（自动分岛）/ Project from View（按视角）/ Unwrap（按 Seam） | `meshes/uv/editing` |
| **35** | **★★★ 判据：自动省事 → Smart UV；精确 → Seam+Unwrap；扁平 → Project from View** | 本章归纳 |
| **36** | **★★★★★ `Average Island Scale` 让所有 UV 岛的"像素/单位"比例一致** | `meshes/uv/editing` |
| **37** | **★★★ 否则不同岛分辨率不同（一清晰一模糊）** | 本章归纳 |
| **38** | **★★★★★ 判据：多岛 UV 必须做 Average Island Scale** | 本章归纳 |
| **39** | **★★★ `Pack Islands` = 把所有 UV 岛打包进 0–1 空间** | `meshes/uv/editing` |

### 拓扑清理（5.6）

| # | 判据 | 出处 |
|---|---|---|
| **40** | **★★★★★ `Dissolve` vs `Delete`**：前者删边保留面（变 N 边形），后者留洞 | `mesh/` |
| **41** | **★★★★★ 判据：清理多余内部边用 Dissolve，不用 Delete** | 本章归纳 |
| **42** | **★★★★★ `Limited Dissolve` = 按角度批量溶解近平共面的边** | `mesh/` |
| **43** | **★★★ 判据：清理导入高模/布尔结果时，Limited Dissolve 一次搞定** | 本章归纳 |
| **44** | **★★★★ `Convex Hull` = 把选中几何包成凸多面体** | `mesh/convex_hull` |
| **45** | **★★★ 用于碰撞体/简化轮廓** | 本章归纳 |
| **46** | **★★★ 五个清理工具**：Dissolve / Delete / Merge by Distance / Convex Hull / Limited Dissolve | `mesh/` |

---

## 5.8 ★★★ 本章的空白

| 缺什么 | 情况 | 该去哪查 |
|---|---|---|
| **★★ Screw 的参数全解** | 19,100 字符但本版只做摘要 | 原手册该页 |
| **★★ UV 各 Unwrap 算法的差异** | 原文分列，本版合并 | 原手册 `uv/unwrap` |
| **★★ 各工具的默认阈值** | 原文未给统一默认值 | 实际界面 |
| **★★ 图片内容** | EPUB 文本层无图 | **原书 xhtml 插图** |

---

## 5.9 ★★★ 与其他章的关系

| 本章内容 | 关联 | 关系 |
|---|---|---|
| **`Alt+S`** | **`blender-hard-surface` 全书（出现最多）** | **★ 本章是原始出处** |
| **Bevel 的两理由** | **`blender-hard-surface` ch01** | **★ 本章是原始出处** |
| **Dissolve vs Delete** | **`blender-hard-surface` ch02** | **★ 本章是原始出处** |
| **Merge by Distance** | **`blender-hard-surface` ch08/ch10** | ★ 原始出处 |
| **UV（Smart/Average Island Scale）** | **`blender-hard-surface` ch06/ch12** | ★ 本章是"UV 的完整工具集" |
| **Extrude Manifold** | **ch02 Boolean** | 流形是 Boolean 的前提 |
| **Randomize** | **`blender-hard-surface` ch08** | 故意凌乱的工具 |
| **Screw** | **ch08 缆绳（另一种做法）** | 螺旋 vs 沿曲线 |
