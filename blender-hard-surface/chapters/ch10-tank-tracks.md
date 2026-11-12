# 第 10 章：坦克履带与轮子

> 原书 Chapter 10: Modeling Tank Tracks。
> **本章是全书建模技术最密集的一章**：履带片建模 + Array + Curve 弯曲。

## 本章解决什么

把坦克的行走机构（轮子 + 履带）建出来，并**用曲线把履带绕到轮子上**。

**七个小节（原文）**：
1. Creating the suspension and wheels
2. **Modeling the wheels**
3. **Modeling the rear sprocket**
4. **Modeling the front sprocket**
5. **Creating the tracks**
6. **Finishing the tracks**
7. （承 ch11 绑定）

---

## 10.1 履带片建模（Creating the tracks）— 7 步完整

**原文总述**：
> 「本节我们**建一块履带片，用 Array 修改器复制它，再用曲线把履带绕到轮子上**。」

| 步 | 操作 | 快捷键 | 原文细节 |
|---|---|---|---|
| **1** | **加一块薄板，长度刚好能放进主动轮的齿之间** | — | 「**just long enough to fit in between the teeth of the sprocket**」 |
| **2** | **沿这块形状的侧面加一个圆柱，并在圆柱上做四条环切** | **Shift+A → Cylinder** + **Ctrl+R** | 「**这将作为连接履带的铰链**」 |
| **3** | **复制其中两个面循环，用 3D 游标镜像到履带的另一侧** | **Shift+D** + **S -1**（枢轴=3D Cursor） | 「用 3D 游标把两个面循环镜像到另一侧」 |
| **4** | **删掉一些面循环，做出一个"中断的圆柱"** | **X** | 「**这就是履带的基础形状**」 |
| **5** | **用一个平面在这形状周围做一些边框**；**实体化后，这就是坦克履带版的"轮胎花纹"** | Plane + Solidify | 「solidified 后，这就是**汽车轮子上胎面花纹的坦克对应物**」 |
| **6** | **实体化（Solidify）并给它的边倒角** | Solidify + **Ctrl+B** | — |
| **7** | **用更多横条把两侧连接起来** | **F** / **E** | 「连接两侧」 |

**验证**：
> 「**给履带加 Array 修改器会显示多块履带可以完美接合。**」

---

## 10.2 用曲线绕轮（Finishing the tracks）★ Curve 修改器主场

**原文总述**：
> 「本节我们**用一条曲线配合 Curve 修改器，把履带绕到轮子和主动轮上**。」

| 步 | 操作 | 快捷键 | 原文 |
|---|---|---|---|
| **1** | **在轮子下方加一条 Path 曲线** | **Shift+A → Curve → Path** | 「加上一条 Path 曲线」 |
| **2** | （在曲线上调整控制点，使其绕过所有轮子） | **G** / 编辑模式 | — |
| **3** | **给履带（已加 Array）加 Curve 修改器** | Curve modifier | — |
| **4** | **在 `Curve Object` 字段选刚建的曲线** | — | — |
| **5** | **可能需要调整 `Deform Axis` 因子直到贴合正确** | — | 「You may need to adjust the Deform Axis factor until it fits correctly」 |
| **6** | **之后应用 Curve 修改器** | 应用 | 「Afterward, apply the Curve modifier」 |

**★ 履带绕轮的完整链条**：
```
① 建一块履带片
② Array 复制成链（完美接合）
③ 建一条 Path 曲线（绕所有轮子的路径）
④ 履带加 Curve 修改器 → Curve Object = 那条 Path
⑤ 调 Deform Axis 直到贴合
⑥ 应用 Curve 修改器
```

> **★ `Deform Axis` 必须试**：原文明确「**may need to adjust**」。轴不对，履带会翻到错误方向。

---

## 10.3 轮子（Modeling the wheels）

**三类轮子**：

| 轮子 | 章 | 特点 |
|---|---|---|
| **负重轮（road wheels）** | ch10 | 数量多，同款重复 |
| **后主动轮（rear sprocket）** | ch10 | **带齿**（履带片要卡进齿间） |
| **前主动轮（front sprocket）** | ch10 | 带齿/惰轮 |

**★ 主动轮的齿距决定履带片长度**（原文步骤 1 已明确）：
> 「薄板**长度刚好能放进主动轮的齿之间**」

> **即：先建主动轮，再按齿距做履带片；或者反过来——但两者必须匹配。**

**悬挂（suspension）**：
> 原文「Creating the suspension and wheels」——**悬挂是连接轮子与车体的结构**。

### 一个省时技巧：复制修改器到所有轮子（原文）

> 「**选所有轮子和悬挂，最后选前面那个。然后按 `Ctrl + L` 再选 `Copy Modifiers`。**
> **这会把 Edge Split 修改器复制到其他所有物体上，产生更好的着色。**」

> **★ 这是 `Ctrl+L → Copy Modifiers` 的用法**——**注意先选目标，最后选源**。

---

## 10.4 本章技术总结

| 技术 | 用在哪 |
|---|---|
| **薄板 + 圆柱做铰链** | 履带片结构 |
| **3D 游标 + S -1 镜像** | 履带片左右对称 |
| **删面循环做中断圆柱** | 履带片铰链造型 |
| **Plane + Solidify** | 履带花纹 |
| **Array** | 履带片复制成链 |
| **Curve 修改器** | 履带绕轮 |
| **Ctrl+L → Copy Modifiers** | 批量给轮子统一着色 |

---

## 本章操作速查

| 我要… | 操作 |
|---|---|
| 做履带片铰链 | 圆柱 + **Ctrl+R** 四条环切 |
| 镜像面循环 | 枢轴设 3D Cursor → **Shift+D** → **S -1** |
| 做出"中断的圆柱" | 删部分面循环 **X** |
| 做履带花纹 | **Plane + Solidify** |
| 履带实体化倒角 | **Solidify** + **Ctrl+B** |
| 连接两侧 | **F** 填面 / **E** 挤出 |
| 履带复制 | **Array** |
| 履带绕轮 | **Path 曲线** + **Curve 修改器**（调 Deform Axis）|
| 批量复制修改器 | 选全部 → 最后选源 → **Ctrl+L → Copy Modifiers** |

---

## 失败模式（F-B10）

| 编号 | 现象 | 根因 | 处置 |
|---|---|---|---|
| **F-B10-01** | 履带片卡不进主动轮齿间 | 薄板长度不对 | 原文：**长度刚好放进齿之间**（先看齿距） |
| **F-B10-02** | Array 后履带块之间有大缝/重叠 | Array 的 Offset 不对 | 调 **Relative Offset**（履带应**完美接合**） |
| **F-B10-03** | 履带绕轮时方向反了/翻面 | **Deform Axis 不对** | 原文：**需要调整 Deform Axis 直到贴合正确** |
| **F-B10-04** | 履带绕完形状奇怪 | 曲线路径不对 | 曲线的控制点要**绕过所有轮子** |
| **F-B10-05** | 忘记应用 Curve 就做后续操作，出错 | 没 Apply | 原文：**Afterward, apply the Curve modifier** |
| **F-B10-06** | 每个轮子都要重设一遍着色 | 手工逐个加 | **选全部 → 最后选源 → Ctrl+L → Copy Modifiers** |
| **F-B10-07** | 镜像的铰链位置不对 | 枢轴不是 3D 游标 | 枢轴设 **3D Cursor**，再 **S -1** |
| **F-B10-08** | 履带片花纹做不出来 | 直接挤实心 | 用 **Plane + Solidify** 做薄花纹 |

## 与其他部分的关系

- **Array → ch03 导轨、ch08 格栅**（同类）
- **Curve 修改器 → ch08 线缆**（同法：Array + Curve）
- **Ctrl+L Copy Modifiers → ch04 Link Object Data**（同键，不同目标）
- **本章完成几何 → ch11 绑定让履带动起来**
