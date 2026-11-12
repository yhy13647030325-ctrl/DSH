# 第 4 章：雕刻与绘制

> 出自《Blender 2.92 Manual》Sculpting & Painting 区（142,778 字符 / 93 页）。

> **⚠ 本技能只做索引**：雕刻与硬表面建模关系较远，未深度提取。

## 4.1 主要条目（官方标题）

| 条目 |
|---|
| **Adaptive Sculpting** |
| **Blob** |
| **Boundary** |
| **Box Face Set** |
| **Box Mask** |
| **Box Trim** |
| **Brush** |
| **Brush Settings** |
| **Brushes** |
| **Clay** |
| **Clay Strips** |
| **Clay Thumb** |
| **Cloth** |
| **Cloth Filter** |
| **Crease** |
| **Cursor** |
| **Draw** |
| **Draw Face Sets** |
| **Draw Sharp** |
| **Dyntopo** |
| **Edit Face Set** |
| **Editing** |
| **Elastic Deform** |
| **Face Sets** |
| **Falloff** |
| **Fill** |
| **Flatten** |
| **Grab** |
| **Inflate** |
| **Introduction** |
| **Lasso Face Set** |
| **Lasso Mask** |
| **Lasso Trim** |
| **Layer** |
| **Line Mask** |

## 4.2 何时需要本章

| 场景 | 说明 |
|---|---|
| 要给硬表面加**细微凹凸/磨损** | 雕刻比建模快（但注意面数） |
| 要做**有机造型**再转硬表面 | 雕刻起形 |
| 要**顶点色/纹理绘制** | 见 Painting 部分 |

> **替代方案**：硬表面的表面细节**通常用贴图伪造**（`blender-hard-surface` ch06 法线贴图/贴花），比雕刻省面数。

