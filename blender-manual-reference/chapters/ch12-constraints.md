# 第 12 章：约束（Constraints）

> 出自《Blender 2.92 Manual》Animation & Rigging 区（270,324 字符 / 117 页）。

## 12.1 全部 28 种约束

| # | 约束 | 用途 |
|---|---|---|
| 1 | **Action** | 动作 |
| 2 | **Armature** | 骨骼 |
| 3 | **Camera Solver** | 相机求解 |
| 4 | **Child Of** | 临时父子关系 |
| 5 | **Clamp To** | 约束到曲线 |
| 6 | **Copy Location** | 复制位置 |
| 7 | **Copy Rotation** | 复制旋转 |
| 8 | **Copy Scale** | 复制缩放 |
| 9 | **Copy Transforms** | 复制全部变换 |
| 10 | **Damped Track** | 阻尼跟随 |
| 11 | **Floor** | 地板约束 |
| 12 | **Follow Path** | 沿路径 |
| 13 | **Follow Track** | 跟随轨道 |
| 14 | **Inverse Kinematics** | 反向动力学 |
| 15 | **Limit Distance** | 限制距离 |
| 16 | **Limit Location** | 限制位置 |
| 17 | **Limit Rotation** | 限制旋转 |
| 18 | **Limit Scale** | 限制缩放 |
| 19 | **Locked Track** | 锁定跟随 |
| 20 | **Maintain Volume** | 保持体积 |
| 21 | **Object Solver** | 物体求解 |
| 22 | **Pivot** | 枢轴 |
| 23 | **Shrinkwrap** | 贴合表面 |
| 24 | **Spline IK** | 样条 IK |
| 25 | **Stretch To** | 拉伸朝向 |
| 26 | **Track To** | 指向目标 |
| 27 | **Transform Cache** | 变换缓存 |
| 28 | **Transformation** | ★ 把一种变换映射成另一种（履带绑定用） |

## 12.2 Transformation 约束（最重要，履带绑定关键）

> **官方定义**：
> 「这个约束比其他 transform 约束**更复杂、更通用**。
> 它允许你**把目标的一种变换属性（location / rotation / scale）映射到 owner 的同一种或另一种变换属性**，
> **在给定的值范围内**（每个目标与 owner 属性的范围可以不同）。
> **你还可以切换轴**，并**把范围值不当限制，而当「标记」** 来定义输入（target）与输出（owner）值之间的映射。」

> **官方举例**：
> 「例如你可以**用目标沿 X 轴的位置来控制 owner 绕 Z 轴的旋转**，
> 说**目标 X 轴 1 个单位对应 owner 绕 Z 轴 10 个单位**。
> **典型用途包括齿轮（见下方 Note），以及基于位置的旋转设置。**」

### 关键选项（官方）

| 选项 | 官方说明 |
|---|---|
| **Target** | 选择约束目标；**无目标时显示为红色（不可用）** |
| **Extrapolate** | **默认 Min/Max 限定输入输出值，范围外的值被裁剪到边界。** 启用后 **Min/Max 不再是严格限制，而是定义输入与输出之间成比例（线性）映射的「标记」** |
| **Target/Owner** | 空间转换（Standard 等） |
| **Influence** | 约束对物体的影响百分比 |
| **Map From** | 输入（来自 target）的设置 |
| **Map To** | 输出（到 owner）的设置 |

> **★ Extrapolate 的官方图解**（原文给了两张图）：
> 输入范围设 (1.0–4.0)，对应输出范围 (1.0–2.0)：
> - **Extrapolate 关闭**：输出值被**限定在 1.0–2.0 之内**
> - **Extrapolate 开启**：输出值**自由地按比例跟随输入**

> **这解释了 `blender-hard-surface` ch11 为什么必须勾 Extrapolate**：
> **不勾的话，空球转过一定角度后履带就不动了**（输出被夹在范围内）。

## 12.3 与 blender-hard-surface 的关系

| | hard-surface ch11 | 本章 |
|---|---|---|
| 覆盖 | **只讲 Transformation**（履带绑定） | **28 种全览** |
| 深度 | 履带的 9 步实操 + 精确取值（X Max 1°） | **Extrapolate 的原理与图解** |
| 用途 | 知道怎么做履带 | 知道还有哪些约束、为什么这样设 |

---

## 与其他部分的关系

- **履带绑定的实操** → `blender-hard-surface` ch11
- **骨骼与 Armature** → [ch13-armature-rigging](ch13-armature-rigging.md)
- **物体父子关系** → [ch06-objects-transforms](ch06-objects-transforms.md)
