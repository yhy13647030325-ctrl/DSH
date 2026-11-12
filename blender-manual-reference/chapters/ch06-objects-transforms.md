# 第 6 章：物体与变换

> 出自《Blender 2.92 Manual》Scenes & Objects 区（110,306 字符 / 59 页）。

## 6.1 官方条目

| 条目 |
|---|
| **Align Objects** |
| **Align to Transform Orientation** |
| **Apply** |
| **Axis Locking** |
| **Clean Up** |
| **Clear** |
| **Collection** |
| **Collections** |
| **Convert To** |
| **Delete** |
| **Duplicate** |
| **Duplicate Linked** |
| **Editing** |
| **Faces** |
| **Instancing** |
| **Introduction** |
| **Join** |
| **Make Links** |
| **Make Single User** |
| **Mirror** |
| **Move** |
| **Numeric Input** |
| **Object Origin** |
| **Object Types** |
| **Objects** |
| **Parenting Objects** |
| **Precision** |
| **Properties** |
| **Randomize** |
| **Relations** |
| **Rotate** |
| **Scale** |
| **Scale Cage** |
| **Scene Properties** |
| **Scenes** |
| **Selecting** |
| **Shading** |
| **Snap** |
| **Tool Settings** |
| **Toolbar** |
| **Tools** |
| **Transfer Mesh Data** |
| **Transfer Mesh Data Layout** |
| **Transform** |
| **Transform Control** |
| **Vertices** |
| **View Layers** |
| **Viewport Display** |
| **Visibility** |

## 6.2 四个必须掌握的概念

### ① 物体原点（Object Origin）

> 物体**变换绕其原点**。**原点的位置决定旋转/缩放的支点。**
> 硬表面的用法：**把原点设到 3D 游标**（`blender-hard-surface` ch03 螺钉做法）

### ② 父子关系（Parenting）

> 官方条目：Parenting Objects。**子级跟随父级变换。**
> **★ 操作顺序**：**先选子级，再选父级**，按 `Ctrl-P`（`blender-hard-surface` ch11 强调）

### ③ Apply（应用变换）

> 官方条目：Apply。**把变换烘进网格数据**（Location/Rotation/Scale → 0/0/1）。
> **为什么要 apply**：**缩放没应用时，修改器会受影响**（如 Array 的 Fit Length 用局部坐标尺寸）

### ④ 精度与轴锁定（Precision / Axis Locking）

| 操作 | 效果 |
|---|---|
| **按住 Ctrl 拖动** | 吸附到整数/刻度 |
| **按住 Shift 拖动** | 精细微调 |
| **按 X/Y/Z** | 锁定单轴 |
| **按两次同轴（如 X X）** | 切到局部轴 |

---

## 与其他部分的关系

- **3D 游标** → `blender-hard-surface` ch03
- **父子关系的实战** → `blender-hard-surface` ch11

