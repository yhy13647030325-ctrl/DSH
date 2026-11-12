# 第 2 章：修改器（57 个）

> 出自《Blender 2.92 Manual》建模区。

## 本章内容

**完整的 57 个修改器索引在 [references/modifier-index.md](../references/modifier-index.md)**，含：
- 每个修改器的**官方定义**
- **关键选项**（Mirror 的 Topology Mirror、Array 的 Fit Type 三种、Boolean 的 Manifold 警告等）
- **规模**（手册里该条的字符数，可判断详略）
- 按需求的**反查表**

## 与 blender-hard-surface 的关系

| | hard-surface | 本章 |
|---|---|---|
| 覆盖 | **8 个**（项目用到的） | **57 个**（全部） |
| 深度 | 实战参数（±2.000、Count 6/1.41m） | **官方定义与限制** |
| 用途 | 知道"该怎么用" | 知道"还有什么能用、边界在哪" |

## 三个项目书没讲的官方要点

### ① Boolean 的 Manifold 警告

> 「**只有流形（Manifold）网格才保证正确结果**。其他情况（**尤其"开放的"网格、非流形但无自相交的**）通常也工作良好，
> **但在某些情况下可能产生奇怪的故障与瑕疵**。」

### ② Mirror 的 Topology Mirror

> 「它**不仅看顶点位置，还看这些顶点与其他顶点的关系**，看整体拓扑来判断哪些顶点会被当作镜像顶点。
> **效果是：镜像顶点可以是非对称的，却仍被当作镜像。**」
> 「**Topology Mirror 在更精细的网格上更可靠。如果几何很简单（如立方体或 UV 球），常常不生效。**」

### ③ Array 的 Fit Type 三种

| 类型 | 说明 |
|---|---|
| **Fit Curve** | 按曲线上指定的**曲线长度**生成足够多副本 |
| **Fit Length** | 按 **Length** 给的长度生成足够多副本 |
| **Fixed Count** | 按 **Count** 指定的数量 |

> **★ 官方 Note**：「**Fit Curve 与 Fit Length 都使用基础物体的局部坐标系尺寸**，
> 这意味着在 Object Mode 下缩放基础物体会……（不改变阵列结果）」
