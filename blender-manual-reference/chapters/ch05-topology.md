# 第 5 章：拓扑与清理

> 出自《Blender 2.92 Manual》建模区。

## 5.1 相关修改器与工具

| 名称 | 作用 |
|---|---|
| **Remesh 修改器** | 生成新拓扑，输出遵循表面曲率 |
| **Decimate 修改器** | 以最小形状变化减面 |
| **Triangulate 修改器** | 所有面转三角面 |
| **Weld 修改器** | 阈值内合并顶点 |
| **Clean Up 一组** | Decimate Geometry / Fill Holes / Make Planar Faces / Split Non-Planar / Split Concave / Delete Loose / Degenerate Dissolve / Merge by Distance |
| **Normals 一组** | Flip / Recalculate / Set from Faces |

## 5.2 硬表面的拓扑要求（提炼）

| 要求 | 为什么 |
|---|---|
| **避免 n 边形（>4 边）** | 细分/布尔会出问题 |
| **面尽量为四边形** | 细分曲面假设四边面 |
| **避免狭长三角形** | 着色出错 |
| **保持流形（Manifold）** | Boolean 才保证正确（见 ch02） |

