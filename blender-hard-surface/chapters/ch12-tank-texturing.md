# 第 12 章：坦克贴图

> 原书 Chapter 12: Texturing the Tank。
> **全书最后一章**：用**程序化材质**给坦克上色，并把前面所有技术收束。

## 本章解决什么

> 原文：「我们会**创建材质，并用程序化技术给坦克贴图**。」

**三个小节（原文）**：
1. **Texturing the turret**（炮塔贴图）
2. **Combining nodes**（组合节点）
3. **Texturing the tracks**（履带贴图）

---

## 12.1 程序化材质（Procedural Texturing）是什么

**与"贴图绘制"的区别**：

| 方式 | 做法 | 章 |
|---|---|---|
| **纹理绘制（Texture Painting）** | 用手在图上画 | ch06 |
| **程序化（Procedural）** | **用节点程序生成纹理**，不画 | **ch12** |

> **原文对本章的定位**：「**uses procedural texturing to finalize the tank**」

**程序化的优点**（提炼）：
- **不用 UV 展开就能上纹理**
- **可无限缩放，不糊**
- **改参数即改外观**

**代价**：控制不如手绘精确。

---

## 12.2 炮塔材质（Texturing the turret）

**本章的炮塔材质要做的事**：

| 要素 | 手段 |
|---|---|
| **基础色（军绿/沙色）** | Principled BSDF 的 Base Color |
| **金属度** | Metallic（坦克装甲是金属 → 接近 1.000） |
| **粗糙度** | Roughness（装甲通常较粗糙） |
| **表面凹凸/噪点** | **程序化节点**（噪波 Noise Texture 等） |
| **边缘磨损** | **可复用 ch04 的 Edge Mask 技术** |

> **★ 与 ch04 的衔接**：
> ch04 的边缘磨损流程（**Edge Mask → 烘焙 → Mix RGB**）在坦克上同样适用。
> 原文说 ch04 的技术「**we will apply it to the other models we create in this book**」——**坦克就是其中之一。**

---

## 12.3 组合节点（Combining nodes）

**本节做的事**：把多个节点组合成复杂材质。

**节点组合的基本逻辑（承接 ch04）**：
```
程序化纹理（Noise / Musgrave 等）──▶ 颜色/粗糙度
Edge Map（烘焙）──────────────────▶ 边缘磨损
                    ↓
              Mix RGB / Mix Shader
                    ↓
            Principled BSDF → Material Output
```

**可复用的组合模式（全书出现过的）**：

| 组合 | 出处 | 作用 |
|---|---|---|
| **Image Texture → Base Color** | ch04 | 用贴图上色 |
| **Edge Map → Mix RGB(Color1/Color2) → Base Color** | ch04 | 边缘磨损 |
| **Bevel + Geometry → Vector Math(Dot Product) → Invert** | ch04 | 边缘遮罩生成 |
| **程序化节点 → 粗糙度/凹凸** | ch12 | 表面质感 |
| **节点复制到其他材质** | ch04 | 批量套用 |

---

## 12.4 履带材质（Texturing the tracks）

**履带材质的特点**：

| 项 | 要点 |
|---|---|
| **金属 + 泥污** | 履带是**重磨损件**，与车体材质不同 |
| **重复图案** | 履带是 Array 出来的，**每块一样** |
| **粗糙度更高** | 履带比装甲更糙 |

> **（书中本节以图推进，未给具体节点参数）**

---

## 12.5 全书技术收束（最后一章的总结意义）

**原文总结**：
> 「下一章我们会开始**第三个、也是最后一个、最高级的项目**——**用一个高模 T-72 坦克，把目前学过的所有技术都用上**。」

> 即 ch12 是**全书技术的总检验**：

| 来自 | 技术 | 在坦克上的应用 |
|---|---|---|
| ch01 | 四步工作流、判据 | 拆件、找父件（车体） |
| ch02 | 基础工具、Mirror | 车体对称 |
| ch03 | 细分+支撑边、Boolean、Array、Solidify | 各处细节 |
| ch04 | 材质节点、边缘遮罩、边缘磨损 | **坦克材质复用** |
| ch05 | 中模思路、装甲板 | 车体装甲 |
| ch06 | 烘焙法线、倒角贴图、纹理绘制 | 表面细节 |
| ch07 | Edge Length 精确尺寸 | 车体尺寸 |
| ch08 | EdgeSplit、格栅 Array | 排气格栅 |
| ch09 | Shrinkwrap | 炮塔细节 |
| ch10 | Array + Curve | 履带绕轮 |
| ch11 | 空物体 + 约束 | 履带绑定 |
| **ch12** | **程序化材质** | **本章** |

---

## 本章操作速查

| 我要… | 操作 |
|---|---|
| 进着色工作区 | 顶部 **Shading** |
| 新建材质 | Shader Editor 点 **New** |
| 调基础色 | Principled BSDF 的 **Base Color**（HSV 模式更好调） |
| 设金属度 | **Metallic**（装甲接近 1.000） |
| 设粗糙度 | **Roughness** |
| 加程序化纹理 | **Shift+A** → 搜 **Noise Texture** 等 |
| 做边缘磨损 | **复用 ch04 的 Edge Mask → Mix RGB 流程** |
| 复制节点到其他材质 | 复制粘贴节点 |

---

## 失败模式（F-B12）

| 编号 | 现象 | 根因 | 处置 |
|---|---|---|---|
| **F-B12-01** | 程序化纹理不明显 | 节点参数范围太小 | 调 Noise 的 Scale/Detail |
| **F-B12-02** | 车体和履带材质一样，不真实 | 没有分开做 | 履带应**更粗糙、更脏** |
| **F-B12-03** | 边缘磨损在坦克上没用 | 没有重做 Edge Mask | **复用 ch04 流程**：复制模型 → Cycles → Bevel+Geometry → Dot Product → Invert → Bake → Mix RGB |
| **F-B12-04** | 想手绘但画不细 | 用错了方法 | 程序化**不画**，调参数；要手绘走 ch06 的纹理绘制 |
| **F-B12-05** | 材质是纯白改不了 | 没点 New | Shader Editor 点 **New** |
| **F-B12-06** | 每个材质都重搭节点 | 手工重做 | **复制节点**到其他材质 |

## 与全书的关系

- **本章是全书终点**，把 ch01–ch11 的技术全部用上
- **ch04 的边缘磨损技术 → 本章坦克复用**（原文明确说会用于其他模型）
- **ch06 的烘焙 → 本章表面细节**
- **ch11 的绑定 → 本章材质完成后可渲染动画**
