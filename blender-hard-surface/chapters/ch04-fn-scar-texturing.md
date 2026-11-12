# 第 4 章：FN SCAR 贴图与渲染

> 原书 Chapter 4: Texturing and Rendering the FN SCAR。
> 本章技术含量最高：**程序化材质 + 边缘遮罩 + 烘焙 + 边缘磨损 + 灯光渲染**。

## 本章解决什么

**给无色的模型上材质**，并做出一套"**边缘自动磨损**"的效果——**这是全书反复使用的核心技术**。

> 原文：「这个技术会**显著提升模型外观**，**我们会在本书其他模型上继续用它**。」

**五个主题（原文）**：
1. Creating materials
2. Understanding Material Nodes
3. Combining nodes
4. **Generating an Edge Mask**
5. **Creating Edge Wear**
6. Rendering the Scene

---

## 4.1 材质节点基础（原文 p 图 4.1–4.6）

### 进入着色工作区

| 步 | 操作 |
|---|---|
| 1 | 点屏幕顶部 **Shading** 按钮，进入 **Shading Workspace** |
| 2 | 鼠标悬停在窗口顶部**向上拖**，展开 **Shader Editor** |
| 3 | 在 Shader Editor 里点 **New**，为物体新建材质 |

### 材质的两个基础节点（原文）

> 「新材质由**两个节点**组成：**Principled BSDF** 和 **Material Output**。
> 这是几乎每个材质都有的两个最基础节点。
> 简单说，**Principled BSDF 像一个汇合点，我们把所有材质设置放在这里；
> Material Output 就是我们把一切插进去、显示到物体上的地方。**
> **默认每个材质都是纯白色**，模型上和 Principled BSDF 的 Base Color 部分都显示如此。」

### 设颜色与金属度

| 步 | 操作 | 要点 |
|---|---|---|
| 4 | 点 **Principled BSDF** 的 **Base Color** | 「这个菜单里有多种控制颜色的方式。**我偏好用 HSV（色相、饱和度、明度）控制**，因为在 HSV 里**更容易直接调饱和度和明度**」 |
| | 要米色 → 拖动色轮到图 4.5 位置，**右侧黑白条往下拉**降明度 | — |
| 5 | 把 **Metallic** 拖到 **1.000** | 「Metallic 是 Principled BSDF 里可控制的另一个属性。**Roughness 也常改，它决定材质有多亮（多光滑）**」 |

> **原文的关键补充**：
> 「这些属性**不只可以用 Principled BSDF 里的滑杆控制，也可以用其他节点控制**。」

---

## 4.2 组合节点：从"纯色"到"贴图"

**最基础的组合（图 4.7）**：
> 「**Image Texture 节点**用于从文件加载图像或纹理，
> **把它的 color 输出插到 Principled BSDF 的 Base Color 插口**。
> 这样我们就能**把任意图像应用到模型表面**，而不只是一个基础色。」

**节点插口的逻辑（提炼）**：
```
Image Texture ──color──▶ Principled BSDF.Base Color ──▶ Material Output.Surface
（数据源）              （汇合点，调属性）              （输出到物体）
```

---

## 4.3 边缘遮罩（Edge Mask）★ 本章核心技术

### 这一步在做什么（原文）

> 「这一节我们要用 Blender 的 **Cycles 渲染引擎**来生成一个 **Edge Mask**。
> 换句话说，我们要**让 Blender 检测锐利的边，并在那些区域周围创建边缘磨损效果**。」

> 「本质上，这是**一组节点的组合，会在 FN SCAR 的边周围产生白色区域**。
> 稍后我们**把这些白边变成基础材质上的边缘磨损**。」

### 完整节点链（10 步，原文 p 图 4.15–4.23）

| 步 | 操作 | 关键参数 |
|---|---|---|
| **1** | 选中 FN SCAR 所有面，Edit Mode 下按 **`U`** 打开 UV 映射菜单 → 选 **Smart UV Project** | 之前先 **Shift + N** 修法线，「确保整把枪是一个物体」 |
| **2** | Object Mode 下**复制整个 FN SCAR**，向上移开原体 | **Shift + D** |
| **3** | 给复制的模型**新建材质并赋给它**；在新材质里**删掉 Principled BSDF 节点** | 「结果应该是一个**全黑的物体**」 |
| **4** | Render Properties 标签 → **Render Engine 设为 Cycles** | **★ 边缘遮罩在 Eevee 里不工作** |
| **5** | Shader Editor 里 **Shift + A** 打开 Add 菜单 → 点 Search 栏 → **搜 `bevel` 加 Bevel 节点** | — |
| **6** | Bevel 节点里设 **Samples = 10**、**Radius = 0.07**；再在下方加 **Geometry** 节点 | **Samples 10 / Radius 0.07** |
| **7** | Add 菜单搜并加 **Vector Math** 节点，按图 4.21 放置 | 「刚添加时**默认是 Add**」 |
| **8** | 把 Vector Math 的 **Add 改成 `Dot Product`**；把前两个节点的 **Normal 输出**插进 Vector Math | — |
| **9** | 在 Vector Math 后加一个 **Invert** 节点 | — |
| **10** | Vector Math 的 **Value** 输出 → Invert 的 **Color** 输入；Invert 的 **Color** 输出 → Material Output 的 **Surface** | — |

**验证**：
> 「切换到 **Rendered View**（3D 视口右上角），模型的**边应该显示为白色，其余全黑**。」

### 节点链总结（可照抄）

```
Bevel ──normal──┐
                ├──▶ Vector Math(Dot Product) ──value──▶ Invert ──color──▶ Material Output
Geometry ─normal┘        [Samples=10, Radius=0.07]
```

> **★ 三个必须记住的点**：
> ① **必须用 Cycles**（Eevee 不工作）
> ② **Bevel 节点 Samples=10、Radius=0.07**
> ③ **Vector Math 要改成 Dot Product**（默认是 Add）

### 一个实用小技巧（本章 TIP）

> 「**可以在视口设置里移除背景图像**。点图 4.16 右上角的箭头，**把 World Opacity 滑杆拉低**。」

---

## 4.4 烘焙边缘贴图（Baking an edge map）

**目的（原文）**：
> 「把刚做的**用于突出边缘的材质变成一张图像纹理**。
> 然后我们就能**用这张图像纹理去控制之前创建的基础材质的底色**。」

| 步 | 操作 | 关键参数 |
|---|---|---|
| **1** | 在 Shading Workspace **左下角找到 Image Editor**，点顶部 **New** 新建图像 | — |
| **2** | **名字设 `Edge Map`，分辨率 2048 px，勾 `32-bit Float`**，点 OK | 「这会创建一张**纯黑图像**」 |
| **3** | 在 Edge Mask 节点旁搜并加 **Image Texture 节点**；在节点里打开图像浏览器，**载入步骤 2 生成的 edge map** | — |
| **4** | **把模型掰开**：把一些重叠部件移开 | 「比如**枪托上部通常盖住枪托其余部分，这会导致 edge map 出问题**」；**只掰开复制出来的那个模型** |
| **5** | 选中复制的 FN SCAR → Render Properties → 打开 **Bake 菜单** → **Bake Type 设为 `Emit`** → 点 **Bake** | **Bake Type = Emit** |

**结果**：
> 「几分钟后，我们生成的黑图会变成**烘焙好的 edge map**。」

> **★ 步骤 4 的判据值得记住**：
> **重叠/遮挡的几何会让烘焙结果出错**——所以**烘焙前把盖住的部件挪开**。

---

## 4.5 边缘磨损（Creating Edge Wear）★ 最实用的效果

**思路（原文）**：
> 「把 **edge map 与各种节点组合**，产生**高度可定制的效果**，帮助做出更真实的模型。」

### 把边缘贴图接进材质（原文步骤）

| 步 | 操作 | 说明 |
|---|---|---|
| **1** | 选要应用的第一种材质，**加 Image Texture 节点，载入 edge map** | 「把它插进 Principled BSDF 的 Base Color 会**让该材质变成 edge map 贴图**」 |
| **2** | 搜并加 **Mix RGB 节点**，**放在 Image Texture 与 Principled BSDF 之间** | 「这个节点**混合颜色**，我们用它和 Image Texture 一起**控制哪里显示哪个颜色**」 |
| **3** | **Color1 设米色**（物体主色），**Color2 设黑色**（边棱颜色） | — |

**节点链**：
```
Edge Map(Image Texture) ──▶ Mix RGB ──color──▶ Principled BSDF.Base Color
                             ▲
                    Color1=米色（主体）
                    Color2=黑色（边棱）
```

> **★ 逻辑**：edge map 是**黑白图**——**白=边棱，黑=平面**。
> 用 Mix RGB 把**白的地方换成一个颜色、黑的地方换成另一个颜色**，就得到**边缘磨损**。

---

## 4.6 多材质与复制节点（本章的两个效率技巧）

**Adding multiple materials（原文）**：
- 一个模型可以有多个材质，按面分配。

**Copying nodes to other materials（原文）**：
> 做好一套节点后，**复制到其他材质**，不用重搭。

**★ 批量操作：Link Object Data（本章 Ctrl+L 的用法）**
> 「完成时，**选中所有灯，最后选中间那盏**，用 **`Ctrl + L` 应用 Link Object Data**。」

---

## 4.7 灯光与渲染

**Lighting the scene / Rendering the scene**：

| 项 | 要点 |
|---|---|
| **灯光** | 可加多个灯，**用 Ctrl+L → Link Object Data 让它们共用数据** |
| **渲染引擎** | 边缘遮罩需要 **Cycles**；最终渲染可用 Cycles 或 Eevee |
| **渲染输出** | Render → Render Image（**F12**）|

> **（书中未展开）**：本章**没有给出具体的灯光强度、角度数值**，只说"给场景打光"并配图。
> 灯光的量化参数**本书未提供**，需按图 4.5x 目测。

---

## 本章操作速查（按顺序）

| 步 | 操作 |
|---|---|
| 1 | 顶部 **Shading** → 进 Shading Workspace |
| 2 | Shader Editor 点 **New** 建材质 |
| 3 | Principled BSDF 的 **Base Color** 设颜色（HSV 调） |
| 4 | **Metallic = 1.000**，Roughness 按需 |
| 5 | **边缘遮罩**：复制模型 → 新材质删 BSDF → **Render Engine = Cycles** → 加 **Bevel(Samples 10, Radius 0.07)** + **Geometry** → **Vector Math 改 Dot Product** → **Invert** → 接 Surface |
| 6 | **烘焙**：Image Editor 新建 **Edge Map 2048px 32-bit Float** → 加 Image Texture 载入它 → **掰开重叠部件** → Bake Type **Emit** → Bake |
| 7 | **边缘磨损**：材质里加 Image Texture（载 edge map）→ 加 **Mix RGB** → Color1 米色 / Color2 黑色 |
| 8 | 复制节点到其他材质 |
| 9 | 打灯 + 渲染 |

---

## 失败模式（F-B4）

| 编号 | 现象 | 根因 | 处置 |
|---|---|---|---|
| **F-B4-01** | 边缘遮罩做出来一片黑/一片白 | **用了 Eevee** | 原文：**Render Engine 必须设 Cycles** |
| **F-B4-02** | 边缘没有白色出现 | Vector Math 还是 **Add** | 改成 **Dot Product** |
| **F-B4-03** | 边缘太粗/太细 | Bevel 参数不对 | **Samples = 10**、**Radius = 0.07**（原文取值） |
| **F-B4-04** | 烘焙出来是纯黑 | **Bake Type 不是 Emit** | 设 **Bake Type = Emit** |
| **F-B4-05** | **烘焙结果在遮挡处出错** | **部件重叠遮挡** | 原文：**烘焙前把盖住的部件挪开**（只挪复制的那个模型） |
| **F-B4-06** | edge map 分辨率低、边缘糊 | 图像太小 | 新建图像时设 **2048 px**、勾 **32-bit Float** |
| **F-B4-07** | 边缘磨损颜色反了（平面变黑、边变米色） | Mix RGB 的 Color1/2 接反 | **Color1 = 主色（米色）**、**Color2 = 边棱色（黑）** |
| **F-B4-08** | 材质是纯白，改不了 | 没在 Shader Editor 里点 New | 点 **New** 建材质后再改 |
| **F-B4-09** | 调颜色很难调准 | 没用 HSV | 原文推荐 **HSV 模式**调饱和度与明度 |
| **F-B4-10** | 多个灯要一个个设 | 没复制数据 | **Ctrl + L → Link Object Data**（最后选中间那盏） |
| **F-B4-11** | 视口背景图干扰观察 | 背景不透明 | 视口设置里 **World Opacity 拉低** |
| **F-B4-12** | 多个材质要重搭节点 | 手工重做 | 复制节点到其他材质 |

## 与其他部分的关系

- **边缘磨损 → ch12 坦克**（同样的技术复用）
- **Cycles vs Eevee → 全书渲染选择**：需要真实效果用 Cycles
- **UV 展开（Smart UV Project）→ ch06 烘焙法线贴图**
- **本章做完，步枪项目结束 → ch05 换项目**

### 三个此前遗漏的精确参数（已核对原文）

| 项 | 值 | 原文 |
|---|---|---|
| **Math/Power 节点 Exponent** | **0.200** | 「把 **Exponent 值降到 0.200**，让边缘着色变暗」 |
| **Render Samples** | **512** + 勾 **Denoising → Render** | 「把 **Render 数量设为 512**。你可能还想**勾上 Denoising 菜单里的 Render 框**，防止渲染噪点」 |
| **底部补光** | **30 W，浅蓝色，朝上** | 「在模型下方加最后一盏面光，**朝上**。同时**把颜色设为浅蓝、功率设为 30 W**」 |
