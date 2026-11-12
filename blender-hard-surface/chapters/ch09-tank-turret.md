# 第 9 章：T-72 炮塔

> 原书 Chapter 9: Modeling the T-72 Tank Turret。
> 本章引入 **Shrinkwrap 修改器**——把细节贴合到炮塔曲面上。

## 本章解决什么

把 ch07 的开放造型炮塔做成**高模炮塔**，并完成主炮。

**三个小节（原文）**：
1. **Modeling the commander's hatch**（车长舱盖）
2. **Creating more turret details**（更多炮塔细节）
3. **Finishing the gun**（完成主炮）

---

## 9.1 车长舱盖：Shrinkwrap 的标准用法 ★ 本章核心

**原文的完整链条（7 步）**：

| 步 | 操作 | 快捷键 | 原文 |
|---|---|---|---|
| **1** | **加一个空心的圆（empty circle）** | — | — |
| **2** | **选中炮塔按 `F2` 重命名成可识别的名字** | **F2** | 「把炮塔重命名成可识别的名字」 |
| **3** | **给步骤 1 加的空心圆加 Shrinkwrap 修改器** | Shrinkwrap | — |
| **4** | **在 Shrinkwrap 里把 `Wrap Method` 设为 `Target Normal Project`**；**把 `Target` object 设为炮塔** | — | 「把 Wrap Method 设成 **Target Normal Project**，并把 Target 设为 **Turret**」 |
| **5** | **应用修改器，再向上挤出这个圆** | 应用 + **E** | 「圆**现在有了炮塔表面的形状**」 |
| **6** | （续） | — | — |
| **7** | （续） | — | — |

> **★ 为什么先重命名炮塔（步骤 2）**：
> Shrinkwrap 的 **Target 字段是个下拉列表**，**炮塔若叫默认名（如 `Cube.003`）就找不着**。

> **★ 这个技法的通用性**：
> **在任何曲面上做细节**（舱盖、凸起、贴片）：
> ```
> ① 做一个平面形状（圆/方）
> ② Shrinkwrap → Target Normal Project → 目标曲面
> ③ 应用
> ④ 挤出
> ```
> **得到的形状天然贴合曲面**，不用自己对着曲面找位置。

---

## 9.2 更多炮塔细节（creating more turret details）

**本节的代表性技巧**：

| 技巧 | 说明 |
|---|---|
| **细分 + 支撑边** | 与 ch03 握把同法：**Subdivision Surface + Ctrl+R 支撑边 + Ctrl+B 倒角** |
| **Shrinkwrap 复用** | 把更多平面细节贴到炮塔曲面 |
| **马克锐边** | **Ctrl+E → Mark Sharp** + **EdgeSplit** |

> **原文**：「我们会创建一个**高模炮塔**」。

---

## 9.3 完成主炮（finishing the gun）

**主炮要点**：

| 步 | 操作 | 快捷键 |
|---|---|---|
| 1 | 建炮管（圆柱） | **Shift+A → Cylinder** |
| 2 | 加环切做炮口/抽气装置的分段 | **Ctrl+R** |
| 3 | 倒角 | **Ctrl+B** |
| 4 | 抽壳/挖孔（炮口） | **Boolean** 或挤出 |

**一个实用判据（ch03 的 TIP，本章通用）**：
> 「**假装你要透过瞄具瞄准，以此确保瞄具对齐正确。**」

---

## 9.4 炮塔的两个技术要点总结

**① Shrinkwrap 解决"在曲面上定位细节"**

| 不用 Shrinkwrap | 用 Shrinkwrap |
|---|---|
| 手动把平面挪到曲面附近，再猜着挤 | **自动投影吸附到曲面**，形状天然贴合 |

**② 炮塔是"硬表面物体 + 有机式表面"**（ch01 已说）
> ch01 原文：「图 1.7 的**坦克炮塔**是硬表面物体，**但网格呈现格栅状（有机式）表面**。
> **因此建模它时可以用通常用于有机建模的工具。**」

**所以炮塔用到**：
- **Subdivision Surface**（有机工具）
- **Proportional Editing**（有机工具）
- **Shrinkwrap**（贴合曲面）

---

## 本章操作速查

| 我要… | 操作 |
|---|---|
| 在曲面上做一个贴合细节 | 建平面形状 → **Shrinkwrap → Target Normal Project → 选目标** → **应用** → **E** 挤出 |
| 让修改器能找到目标 | **先 `F2` 重命名目标物体** |
| 炮塔做平滑又保硬边 | **Subdivision Surface + Ctrl+R 支撑边 + Ctrl+B 倒角** |
| 标锐边 | **Ctrl+E → Mark Sharp** |
| 建炮管 | Shift+A → Cylinder → **Ctrl+R** 分段 → **Ctrl+B** 倒角 |
| 验证瞄具对齐 | **假装瞄准看是否对齐** |

---

## 失败模式（F-B9）

| 编号 | 现象 | 根因 | 处置 |
|---|---|---|---|
| **F-B9-01** | Shrinkwrap 的 Target 下拉里找不到炮塔 | **没先重命名** | 先选炮塔 **F2** 改名 |
| **F-B9-02** | Shrinkwrap 贴上去形状乱 | Wrap Method 不对 | 用 **Target Normal Project** |
| **F-B9-03** | 忘记应用 Shrinkwrap 就挤出，形状变形 | 没 Apply | **先应用修改器，再挤出** |
| **F-B9-04** | 细分后炮塔硬边全变圆 | 没支撑边 | **Ctrl+R 加环切** + **Ctrl+B 倒角** |
| **F-B9-05** | 平滑着色过界 | 没标锐边 | **Ctrl+E → Mark Sharp** + **EdgeSplit** |
| **F-B9-06** | 细节件飘在炮塔外面 | 没用 Shrinkwrap，手动摆 | 用 Shrinkwrap 自动贴合 |
| **F-B9-07** | 瞄具装上后不通视 | 没做功能验证 | 原文：**假装瞄准验证对齐** |

## 与其他部分的关系

- **Shrinkwrap → 全书唯一用法**（ch09 是本修改器的主场）
- **细分+支撑边 → ch03 握把**（同法）
- **有机工具用于硬表面 → ch01 炮塔例子**（首尾呼应）
- **本章完成炮塔 → ch10 履带与轮子**
