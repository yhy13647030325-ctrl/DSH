# 第 6 章：物体与变换（Objects & Transforms）

> **原书分区**：`scene_layout/object/**`（49 文件）
> **原文正文 92,175 字符**（本版逐节读完）
> **定位方式**：EPUB 无页码 → **xhtml 文件路径**
> **本章含 6 节**：物体类型 / 原点 / 选择 / 变换 / 应用 / 复制与关联

---

## 6.0 本章解决什么

> **原文（`object/introduction.xhtml`）**：
> **物体（Object）是"场景里可变换的实体"** ——
> **它持有"数据（Data）"与"变换（Transform）"两样东西。**

**★★★★★ 一句话：物体是"容器"，数据是"内容"，变换是"位置/朝向/大小"。**

```
物体（Object）
   ├── 数据（Data）：网格/曲线/灯/相机…
   └── 变换（Transform）：位置 / 旋转 / 缩放
```

> **★★★ 判据：同一个"数据"可以被多个"物体"共用** ——
> **★ 这就是「关联复制（Alt+D）」的原理（§6.6）。**

---

## 6.1 ★★★★★ 原点（Origin）—— 本章最重要的概念

> **原文（`object/origin.xhtml`）**：
> **原点（Origin）是"物体的变换中心"。**
> **它决定"旋转绕哪里转""缩放以哪为中心"。**

### 6.1.1 ★★★★★ 原点的三种设置方式

| 方式 | 结果 |
|---|---|
| **★ Origin to Geometry** | **★ 原点移到几何中心** |
| **★ Origin to 3D Cursor** | **★ 原点移到 3D 游标** |
| **Origin to Center of Mass** | 原点移到质心 |

**★★★★★ 这是 `blender-hard-surface` 里反复出现的关键操作**：

| 章 | 用途 |
|---|---|
| **ch07** | **6 个轮子：Origin to Geometry（绕自身转）** |
| **ch10** | **螺钉：原点放孔底（复制自动对位）** |
| **ch13** | **骨架：原点决定旋转中心** |

> **★★★ 判据：原点 = "这个物体绕哪里转/以哪缩放"** ——
> **★ 不是"哪个点算物体的位置"这么简单，它直接决定操作结果。**

### 6.1.2 ★★★★★ 三种 Pivot Point（枢轴）与 Origin 的关系

> **原文（`editing/transform/introduction.xhtml`）**：
> **枢轴（Pivot Point）决定"多个物体一起变换时的中心"。**

| 枢轴 | 中心在哪 |
|---|---|
| **★ Median Point（默认）** | **★ 选中物的"平均位置"** |
| **★ Individual Origins** | **★ 每个物体各自的 Origin** |
| **★ 3D Cursor** | **★ 3D 游标位置** |
| **Bounding Box Center** | 包围盒中心 |
| **Active Element** | 激活物体 |

**★★★★★ 这是 ch10 的关键判据（原文）**：

| 需求 | 枢轴 |
|---|---|
| **"6 个轮子整体缩放"** | Median Point |
| **★ "6 个轮子各自缩放，位置不变"** | **★ Individual Origins** |

> **★★★ 判据：枢轴 + Origin 是"两级答案"** ——
> **★ Origin 决定"物体自己的中心"，枢轴决定"多物体操作的中心"。**

---

## 6.2 ★★★★★ 变换的四个控制（Transform Control）

> **原文（`editing/transform/control/`）给了四个"精确控制"手段**：

### 6.2.1 ★★★★★ 数值输入（Numeric Input）

> **原文（`numeric_input.xhtml`）**：
> **变换过程中直接输入数字 → 精确值。**

| 操作 | 结果 |
|---|---|
| **`G` → 输 `2.5` → 回车** | **★ 精确移动 2.5 单位** |
| **`R` → 输 `45` → 回车** | **★ 精确旋转 45°** |
| **`S` → 输 `0.5` → 回车** | **★ 精确缩放到 0.5 倍** |

> **★★★ 判据：鼠标拖永远是"估"，输数字才是"准"** ——
> **★ 这与 `blender-hard-surface` ch03 的"精确变换"完全一致。**

### 6.2.2 ★★★★★ 轴锁定（Axis Locking）

> **原文（`axis_locking.xhtml`）**：
> **变换中按 `X` / `Y` / `Z` 锁定到该轴；**
> **按 `Shift + 轴` 排除该轴。**

| 键 | 含义 |
|---|---|
| **`G` `X`** | **★ 只沿 X 移动** |
| **★ `G` `Shift+X`** | **★ 移动但排除 X（沿 YZ 平面）** |
| **`S` `Shift+Y`** | **★ 缩放但排除 Y** |

**★★★★★ 这是 `blender-hard-surface` 里反复出现的"排除式变换"**：

| 章 | 用途 |
|---|---|
| **ch03** | **`S` `Shift+Y` 双向缩放** |
| **ch08** | **`S` `Shift+X` 收拢薄面** |
| **ch11** | **`S` `Shift+轴` 改宽不改长** |

> **★★★ 判据：`Shift+轴` = "排除该轴"，不是"选该轴"** ——
> **★ 这是最容易被误解的快捷键。**

### 6.2.3 ★★★★ 精度控制（Precision）

> **原文（`precision.xhtml`）**：
> **按住 `Shift` 做变换 → 细微调整（慢速）；**
> **按住 `Ctrl` → 吸附到增量（如 1 单位/5°）。**

| 修饰键 | 效果 |
|---|---|
| **★ `Shift`** | **★ 精度模式（慢/细）** |
| **★ `Ctrl`** | **★ 吸附到增量** |

> **★★ 判据：要"慢慢挪一点"→ 按住 `Shift`；要"对齐整数格"→ 按住 `Ctrl`。**

### 6.2.4 ★★★★ 变换朝向（Transform Orientation）

> **原文（`align_transform_orientation.xhtml`）**：
> **变换可以按 "Global（世界）" 或 "Local（局部）" 或 "Normal（法线）" 等朝向。**

| 朝向 | 含义 |
|---|---|
| **Global** | **★ 世界坐标轴** |
| **★ Local** | **★ 物体自身的轴** |
| **★ Normal** | **★ 沿选中面的法线** |
| **View** | 沿视图 |

> **★★★ 判据：物体"转过了"之后要沿"它自己的轴"变 → 用 Local。**
> **★ 要"沿面法线挤出/移动"→ 用 Normal。**

---

## 6.3 ★★★★★ Apply（应用变换）—— 本章最关键的操作

> **原文（`editing/apply.xhtml`）**：
> **Apply 把"物体变换"永久写进"数据"。**

### 6.3.1 ★★★★★ 四种 Apply

| 操作 | 结果 |
|---|---|
| **★ Apply Location** | **★ 位置归零，几何位置固定** |
| **★ Apply Rotation** | **★ 旋转归零，几何朝向固定** |
| **★ Apply Scale** | **★ 缩放归 1，几何尺寸固定** |
| **Apply All Transforms** | 三者都应用 |

### 6.3.2 ★★★★★ 为什么必须 Apply Scale（本节最重要的判据）

> **原文（`sculpting/introduction.xhtml`，ch04 引用）**：
> **「要获得可预测的笔刷行为，请应用网格的缩放。」**

| 不 Apply Scale 的后果 | 涉及功能 |
|---|---|
| **★ 雕刻笔刷半径不准** | **ch04 雕刻** |
| **★ 修改器（Bevel/Solidify）厚度不均** | **ch02 修改器** |
| **★ 物理模拟（布料/刚体）尺度错** | 物理 |
| **★ 法线贴图/UV 拉伸** | 贴图 |

**★★★★★ 这是全书最重要的一条"前置操作"**：

> **★★★ 判据：建模前 / 雕刻前 / 加修改器前，先 `Ctrl+A` → Apply Scale。**
> **★ 否则"参数看起来对但结果不对"。**

### 6.3.3 ★★★★ Apply 的反面：Clear（清除变换）

> **原文（`editing/clear.xhtml`）**：
> **Clear 把"变换值归零"，但**几何不动**（与 Apply 相反）。**

| 操作 | 变换值 | 几何 |
|---|---|---|
| **★ Apply** | **★ 归零** | **★ 不变（写进数据）** |
| **★ Clear** | **★ 归零** | **★ 回到原始位置** |

> **★★ 判据：Apply = "把变换烘进数据"；Clear = "丢掉变换，回到原点"。**

---

## 6.4 ★★★★★ 吸附（Snap）

> **原文（`editing/snap.xhtml`）**：

### 6.4.1 ★★★★ 两种吸附

| 类型 | 作用 |
|---|---|
| **★ Snap To** | **★ 变换时吸附到"点/边/面/网格"** |
| **★ Snapping With** | **★ 用什么作为"吸附基准"（顶点/边/面中心…）** |

**★★★★ 常用吸附目标**：

| 目标 | 用途 |
|---|---|
| **★ Vertex** | **★ 顶点对顶点** |
| **★ Edge** | **★ 贴到边** |
| **★ Face** | **★ 贴到面** |
| **★ Increment** | **★ 按固定增量（1 单位/5°）** |

> **★★ 判据：要"精确贴到某个几何"→ 开 Snap To Vertex/Edge/Face。**

### 6.4.2 ★★★★★ 3D 游标的吸附（`Shift + S`）

> **原文（`object/editing/snap.xhtml`）**：
> **`Shift + S` 打开"游标/选择"吸附菜单。**

| 命令 | 结果 |
|---|---|
| **★ Cursor to Selected** | **★ 游标到选中物** |
| **★ Selection to Cursor** | **★ 选中物到游标** |
| **Cursor to World Origin** | 游标回原点 |
| **★ Cursor to Active** | 游标到激活物 |

**★★★★★ 这是 `blender-hard-surface` 里出现最多的组合之一**：

| 章 | 用途 |
|---|---|
| **ch02** | **游标到面上 → 加立方体** |
| **ch03** | **游标当枢轴做镜像/对齐** |
| **ch10** | **螺钉对齐（Selection to Cursor）** |
| **ch11** | **原点对齐** |

> **★★★ 判据：`Shift+S` 是"精确放置"的核心** ——
> **★ 配合"加物体时默认在游标"，实现"精确建模"。**

---

## 6.5 ★★★★★ 复制与关联（Duplicate & Linked）

> **原文（`editing/duplicate.xhtml` 与 `duplicate_linked.xhtml`）**：

### 6.5.1 ★★★★★ 三种复制的区别（本节最重要）

| 操作 | 快捷键 | 数据 | 关系 |
|---|---|---|---|
| **Duplicate** | **`Shift + D`** | **★ 复制一份新数据** | **★ 改一个不影响另一个** |
| **★ Duplicate Linked** | **★ `Alt + D`** | **★ 共用同一份数据** | **★ 改一个全变** |
| **Duplicate（Edit Mode）** | `Shift + D` | **★ 复制选中的"面/边/点"** | 在同一物体内 |

**★★★★★ 三种复制的对照（与 `blender-hard-surface` 直接对应）**：

| 需求 | 用什么 |
|---|---|
| **要"独立的、可以单独改"** | **`Shift + D`** |
| **★ 要"改一个全变"（不占内存）** | **★ `Alt + D`** |
| **在建模中复制面** | **Edit Mode 的 `Shift + D`** |

> **★★★ 判据：`Alt+D` 是"实例化"，`Shift+D` 是"真复制"** ——
> **★ 这与 ch07 的「Link Object Data」是同一机制的两条路径：**
> **★★ `Alt+D` 在创建时链接；`Ctrl+L` 在创建后链接。**

### 6.5.2 ★★★★ Join（合并物体）

> **原文（`editing/join.xhtml`）**：
> **`Ctrl + J` 把选中的多个物体合并成一个。**

**★★★★★ 一条关键判据（原文隐含）**：
> **★ 合并后，"最后选中的"（激活物）决定"结果物体的名称/数据/变换"。**

> **★★★ 判据：要"把 A 合并进 B"→ 先选 A，最后选 B。**
> **★ 这与 ch10 的判据完全一致。**

---

## 6.6 ★★★★ 其他物体操作

| 操作 | 作用 | 原文位置 |
|---|---|---|
| **★ Mirror（物体级）** | **★ 用物体镜像（不是修改器）** | `editing/mirror.xhtml` |
| **Randomize Transform** | **★ 随机变换多个物体** | `editing/transform/randomize.xhtml` |
| **Align Objects** | **★ 对齐多个物体** | `editing/transform/align_objects.xhtml` |
| **Align Transform Orientation** | **★ 把变换朝向对齐到某面** | `align_transform_orientation.xhtml` |

**★★★★ 物体级 Mirror vs Mirror 修改器**：

| 方式 | 性质 |
|---|---|
| **★ 物体级 Mirror** | **★ 一次性生成真实几何（对称后成两份）** |
| **★ Mirror 修改器** | **★ 非破坏性（可关掉）** |

> **★★ 判据：要"能改"→ 修改器；要"烘成模型"→ 物体级 Mirror。**

---

## 6.7 ★★★★★ 本章判据总表（共 44 条）

### 物体与原点的概念（6.1）

| # | 判据 | 出处 |
|---|---|---|
| **1** | **★★★★ 物体 = 数据（Data）+ 变换（Transform）** | `object/introduction` |
| **2** | **★★★ 判据：同一数据可被多个物体共用**（这就是关联复制） | `object/introduction` 归纳 |
| **3** | **★★★★★ 原点（Origin）是"物体的变换中心"** | `object/origin` |
| **4** | **★★★ 原点决定"旋转绕哪里"和"缩放以哪为中心"** | `object/origin` |
| **5** | **★★★★ 三种设置**：Origin to Geometry / Origin to 3D Cursor / Origin to Center of Mass | `object/origin` |
| **6** | **★★★★★ Origin to Geometry = 绕自身转**（ch07 的 6 个轮子） | 本章归纳 |
| **7** | **★★★★★ Origin to 3D Cursor = 复制时自动对位**（ch10 的螺钉） | 本章归纳 |
| **8** | **★★★★★ 枢轴（Pivot Point）与 Origin 是"两级答案"** | `transform/introduction` |
| **9** | **★★★★ Origin = 物体自己的中心；枢轴 = 多物体操作的中心** | 本章归纳 |
| **10** | **★★★★★ `Individual Origins` = 每个物体各自缩放，位置不变**（ch10 关键） | `transform/introduction` |

### 变换控制（6.2）

| # | 判据 | 出处 |
|---|---|---|
| **11** | **★★★★★ 数值输入：变换中直接输数字 → 精确值** | `transform/control/numeric_input` |
| **12** | **★★★ 判据：鼠标拖是"估"，输数字才是"准"** | 本章归纳 |
| **13** | **★★★★★ 轴锁定：`X`/`Y`/`Z` 锁定；`Shift+轴` 排除该轴** | `transform/control/axis_locking` |
| **14** | **★★★★★ `Shift+轴` = "排除该轴"，不是"选该轴"** | 本章归纳 |
| **15** | **★★★★ 精度：`Shift` = 慢/细；`Ctrl` = 吸附增量** | `transform/control/precision` |
| **16** | **★★★ 判据：要"慢慢挪"→ `Shift`；要"对齐整数格"→ `Ctrl`** | 本章归纳 |
| **17** | **★★★★ 变换朝向：Global / Local / Normal / View** | `align_transform_orientation` |
| **18** | **★★★ 物体转过了要沿自己的轴 → Local；沿面法线 → Normal** | 本章归纳 |

### Apply（6.3）

| # | 判据 | 出处 |
|---|---|---|
| **19** | **★★★★★ Apply 把"物体变换"永久写进"数据"** | `editing/apply` |
| **20** | **★★★★ 四种**：Apply Location / Rotation / **Scale** / All Transforms | `editing/apply` |
| **21** | **★★★★★ `Apply Scale` 必须做**（否则雕刻笔刷半径不准） | `sculpting/introduction` |
| **22** | **★★★★★ 不 Apply Scale 的后果**：笔刷不准 / 修改器厚度不均 / 物理尺度错 / UV 拉伸 | 本章归纳 |
| **23** | **★★★★★ 判据：建模前/雕刻前/加修改器前，先 `Ctrl+A` → Apply Scale** | 本章归纳 |
| **24** | **★★★★ `Apply` vs `Clear`**：前者"烘进数据"，后者"丢变换回原始位置" | `editing/clear` |

### 吸附（6.4）

| # | 判据 | 出处 |
|---|---|---|
| **25** | **★★★★ 两种吸附**：Snap To（吸到哪）+ Snapping With（用什么作基准） | `editing/snap` |
| **26** | **★★★★ 常用目标**：Vertex / Edge / Face / **Increment** | `editing/snap` |
| **27** | **★★★ 判据：要"精确贴到某个几何"→ 开 Snap To Vertex/Edge/Face** | 本章归纳 |
| **28** | **★★★★★ `Shift+S` = 游标/选择吸附菜单** | `object/editing/snap` |
| **29** | **★★★★★ `Cursor to Selected` = 游标到选中物** | `object/editing/snap` |
| **30** | **★★★★★ `Selection to Cursor` = 选中物到游标** | `object/editing/snap` |
| **31** | **★★★ `Cursor to World Origin` / `Cursor to Active`** | `object/editing/snap` |
| **32** | **★★★★★ 判据：`Shift+S` 是"精确放置"的核心**（配合"加物体在游标"） | 本章归纳 |

### 复制与合并（6.5）

| # | 判据 | 出处 |
|---|---|---|
| **33** | **★★★★★ `Shift+D`（Duplicate）= 复制新数据，改一个不影响另一个** | `editing/duplicate` |
| **34** | **★★★★★ `Alt+D`（Duplicate Linked）= 共用数据，改一个全变** | `editing/duplicate_linked` |
| **35** | **★★★★ `Shift+D` 在 Edit Mode = 复制选中的面/边/点** | `editing/duplicate` 归纳 |
| **36** | **★★★★★ `Alt+D` 与 ch07 的 `Ctrl+L` 是同一机制两条路径** | 本章归纳 |
| **37** | **★★★ `Alt+D` 在创建时链接；`Ctrl+L` 在创建后链接** | 本章归纳 |
| **38** | **★★★★ `Ctrl+J`（Join）= 合并成物体** | `editing/join` |
| **39** | **★★★★★ 合并后"最后选中的"决定结果物体的名称/数据/变换** | `editing/join` 归纳 |
| **40** | **★★★ 判据：要"把 A 合并进 B"→ 先选 A，最后选 B**（ch10 一致） | 本章归纳 |

### 其他（6.6）

| # | 判据 | 出处 |
|---|---|---|
| **41** | **★★★★ 物体级 Mirror vs Mirror 修改器**：前者"真实几何"，后者"非破坏性" | `editing/mirror` |
| **42** | **★★★ 要"能改"→ 修改器；要"烘成模型"→ 物体级 Mirror** | 本章归纳 |
| **43** | **★★★★ `Align Objects` = 对齐多个物体** | `align_objects` |
| **44** | **★★★ `Randomize Transform` = 随机变换多个物体** | `transform/randomize` |

---

## 6.8 ★★★ 本章的空白

| 缺什么 | 情况 | 该去哪查 |
|---|---|---|
| **★★ 物体类型的完整清单** | 本章只做了概括（`types.xhtml`） | 原手册该页 |
| **★★ 各朝向的完整清单** | 只列了主要的 4 种 | 实际界面 |
| **★★ `Align Objects` 的参数** | 本版只做摘要 | 原手册该页 |
| **★★ 图片内容** | EPUB 文本层无图 | **原书 xhtml 插图** |

---

## 6.9 ★★★ 与其他章的关系

| 本章内容 | 关联 | 关系 |
|---|---|---|
| **Origin to 3D Cursor** | **`blender-hard-surface` ch02/03/10/11** | **★ 本章是原始出处** |
| **Apply Scale** | **ch04 雕刻（必须）** | **★ 本章是原始出处** |
| **`Shift+轴` 排除** | **`blender-hard-surface` ch03/08/11** | ★ 原始出处 |
| **数值输入** | **`blender-hard-surface` ch03** | ★ 原始出处 |
| **`Individual Origins`** | **`blender-hard-surface` ch10** | ★ 原始出处 |
| **`Shift+D` / `Alt+D`** | **ch07 的 Link Data** | **★ 同一机制两条路径** |
| **`Cursor to Selected`** | **ch02 Boolean / ch09 Shrinkwrap** | 精确放置的基础 |
| **`Ctrl+J` 的选择顺序** | **`blender-hard-surface` ch10** | ★ 原始出处 |
