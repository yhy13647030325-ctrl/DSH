# 判据与参数速查（Cheatsheet）

> 出自《Blender 3D Incredible Models》。**参数值均为原文给出的实际取值**。

## 一、硬表面 vs 有机（ch01）

| 判据 | 硬表面 | 有机 |
|---|---|---|
| **边** | 锐利 + 薄倒角 | 平滑弯曲 |
| **面** | 大量平面 | 软弯 + 格栅状纹理 |
| **边循环** | **短、不连续** | 长、连续 |
| **松散部件** | **多个独立部件** | 多为单体 |

> **结论**：**看网格特征，不看物体品类。**

## 二、四步工作流（ch01）

| # | 步 | 判据 |
|---|---|---|
| 1 | **收集参考** | 简单件一张照片；复杂件找蓝图（正交投影） |
| 2 | **拆分部件** | 拆到"每件都值得单独建"，按位置与细节等级合并 |
| 3 | **建块面** | **从父件开始**（其他一切附着于它的那个） |
| 4 | **加细节** | **90% 工作量在此** |

**三个项目的父件**：

| 项目 | 父件 |
|---|---|
| FN SCAR 步枪 | **机身（body）** |
| 赛博飞船 | **驾驶舱（cockpit）** |
| T-72 坦克 | **车体（hull）** |

## 三、全部数值参数（原文给出的精确值，共 24 项）

> 全部经原文逐条核对。**这些是"照着做"最该抄下来的数。**

### 建模类

| 项 | 值 | 出处 |
|---|---|---|
| **Bevel 的 Shape 滑条** | **0.040 ～ 0.050**（得到圆形倒角） | ch03 |
| **Auto Smooth 角度** | **45°**（"most of the time the best angle"） | ch03 |
| **切孔用圆的顶点数** | **12** | ch03 |
| **轮子缩放因子** | **0.2**（Pivot = Individual Origins） | ch10 |
| **轮子 Array Count** | **6** | ch07 |
| **轮子 Array Constant Offset Y** | **1.41 m** | ch07 |
| **排气格栅 Relative Offset** | **±2.000** | ch08 |
| **炮管圆旋转** | **绕 Y 轴 90°** | ch02 |
| **侧导轨旋转** | **90°** | ch03 |
| **某部件绕游标旋转示例** | **R+Z 输入 180°** | ch03 |
| **圆环分段复制旋转** | **45°** | ch09、ch10 |

### 材质与烘焙类

| 项 | 值 | 出处 |
|---|---|---|
| **Bevel 节点 Samples** | **10** | ch04 |
| **Bevel 节点 Radius** | **0.07** | ch04 |
| **Edge Map 分辨率** | **2048 px** + 勾 **32-bit Float** | ch04 |
| **烘焙 Type（边缘/发光）** | **Emit** | ch04 |
| **烘焙 Type（法线）** | **Normal** | ch06 |
| **Math/Power 节点 Exponent** | **0.200**（让边缘变暗） | ch04 |
| **法线贴花基底 Hex** | **8080FF** | ch06 |
| **碳纤维图案图尺寸** | **512 px × 512 px** | ch06 |
| **法线贴花烘焙图尺寸** | **512 px × 512 px** | ch06 |
| **Metallic（金属件）** | **1.000** | ch04 |

### 渲染与绑定类

| 项 | 值 | 出处 |
|---|---|---|
| **Render Samples** | **512** + 勾 **Denoising → Render** | ch04 |
| **底部补光强度** | **30 W**（浅蓝色，朝上） | ch04 |
| **Transformation 约束 X Max** | **1 degree** | ch11 |
| **主动轮约束比例** | **每 1° 球旋转 → 主动轮转 100°** | ch11 |

### 修改器设置（非数值，但必须勾对）

| 项 | 设置 | 出处 |
|---|---|---|
| **Solidify** | 勾 **Even Thickness** | ch03、ch08 |
| **EdgeSplit** | **取消 Edge Angle**，勾 **Sharp Edges** | ch08 |
| **Shrinkwrap** | **Wrap Method = Target Normal Project** | ch09 |
| **Transformation 约束** | **Extrapolate ✓ / Owner = Local Space** | ch11 |
| **Transformation 映射** | **Map From = Rotation / Map To = Location** | ch11 |
| **渲染引擎（边缘遮罩）** | **Cycles**（Eevee 不工作） | ch04 |

## 四、修改器选用（8 个）

| 我要… | 修改器 | 关键参数 |
|---|---|---|
| 左右对称 | **Mirror** | Axis=X，勾 Clipping+Merge |
| 重复件 N 次 | **Array** | Count + Offset；格栅用 **Relative Offset ±2.000** |
| 挖孔 | **Boolean** | **Operation = Difference**；切前修法线 **Shift+N** |
| 面片加厚 | **Solidify** | **勾 Even Thickness** |
| 平滑曲面 | **Subdivision Surface** | + **Ctrl+R 支撑边** 保硬边 |
| 沿路径弯曲 | **Curve** | Curve Object = 目标曲线；**调 Deform Axis** |
| 细节贴曲面 | **Shrinkwrap** | **Target Normal Project** |
| 控制平滑组 | **Edge Split** | **取消 Edge Angle，勾 Sharp Edges** |

## 五、快捷键核心 12（按频次）

| 键 | 作用 | 频次 |
|---|---|---|
| **Alt + S** | **沿法线缩放/加厚**（每条边距离相等） | 14 |
| **Ctrl + B** | 倒角 | 10 |
| **Ctrl + R** | 环切 | 8 |
| **G** | 移动（**按两次 = 顶点滑移**） | 6 |
| **S** | 缩放（后可加 X/Y/Z 限轴） | 5 |
| **Shift + N** | **重算法线**（旧版 Shift+N） | 5 |
| **Shift + D** | 复制 | 5 |
| **Shift + W** | **弯曲（transform.bend）** —— 合并顶点走 `M` 菜单 | 4 |
| **Ctrl + L** | 关联数据 / **Copy Modifiers** | 4 |
| **L** | **选松散部件** | 3 |
| **Shift + S** | Snap 菜单（**Cursor to Selected**） | 3 |
| **Tab** | Object ↔ Edit Mode | 3 |

## 六、易混淆的五组

| 对比 | 区别 |
|---|---|
| **`S` vs `Alt+S`** | S = 整体等比；**Alt+S = 沿法线，每条边距离相等** |
| **`Shift+W`** | **弯曲（transform.bend）** —— 合并顶点不在这个键 |
| **`Shift+N`** | **重算法线朝外**（5.1.2 实测；`Ctrl+Shift+N` 是变体） |
| **`G` vs `G` 两次** | G = 自由移动；**G 两次 = 顶点滑移（沿原边）** |
| **`Ctrl+J` vs `Shift+J`** | Ctrl+J = 合并物体；**Shift+J = 合并选中的圆（桥接用）** |

## 七、贴图三件事（ch04、ch06）

### 边缘遮罩节点链（ch04）

```
Bevel(Samples=10, Radius=0.07) ─┐
                                 ├─▶ Vector Math(Dot Product) ─value─▶ Invert ─color─▶ Material Output
Geometry ───────normal──────────┘
```
**★ 必须 Cycles（Eevee 不工作）**

### 边缘磨损（ch04）

```
Edge Map(Image Texture) ──▶ Mix RGB ──color──▶ Principled BSDF.Base Color
                            Color1 = 主色
                            Color2 = 边棱色
```

### 烘焙法线贴图的三个用途（ch06）

| # | 用途 | 效果 |
|---|---|---|
| 1 | **模拟凹凸表面** | 中模表面看起来不平 |
| 2 | **在低模上放倒角** | 无需真几何就有倒角 |
| 3 | **绘制法线贴花** | 看起来像建模了舱盖 |

## 八、三种项目的技术取舍

| 项目 | 面数 | 细节来源 | 适用 |
|---|---|---|---|
| FN SCAR | 高模 | 真几何（倒角、螺钉、导轨） | 影视/静帧 |
| **赛博飞船** | **中模** | **法线贴图伪造** | **游戏/动画** |
| T-72 | 高模 | 真几何 + 绑定 | 影视/演示 |

> **判据（ch05 原文）**：「**高度细节的模型往往不适合游戏和动画，必须替换成不那么复杂的模型。**」

## 九、按"做类似产品"查

| 你要做… | 参考章 | 核心手法 |
|---|---|---|
| **枪械/手持工具** | ch02–ch04 | 参考图 → 五件拆分 → Mirror → 布尔开孔 → 阵列导轨 → 边缘磨损材质 |
| **载具/飞船** | ch05–ch06 | 父件（驾驶舱）→ 装甲板 → 中模 + 法线贴图伪造 |
| **坦克/履带车辆** | ch07–ch12 | Edge Length 精确尺寸 → 删半 Mirror → EdgeSplit 控制着色 → Array+Curve 履带 → 空物体约束绑定 |
| **任何有重复细节的机械件** | ch03、ch08 | **做一级 + Array** |
| **任何有曲面的细节件** | ch09 | **Shrinkwrap（Target Normal Project）** |
| **任何需要"边缘磨损"的金属** | ch04 | **Edge Mask + 烘焙 + Mix RGB** |
