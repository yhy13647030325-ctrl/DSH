# 第 13 章：骨骼与绑定

> 出自《Blender 2.92 Manual》Animation & Rigging 区（270,324 字符 / 117 页）。

## 13.1 Armature 是什么（官方术语）

> 「**Armature**：由 **Bone（骨骼）** 组成的物体，用于**绑定（Rig）角色、道具等**。」
> 「**Bone**：Armature 的**构建单元**，由 **Head（头）、Tail（尾）** 组成。」

## 13.2 何时需要真正的骨骼绑定

| 场景 | 用骨骼？ | 用什么 |
|---|---|---|
| **角色/生物** | ✓ | Armature + 权重 + IK |
| **机械件（刚体运动）** | **通常不用** | **空物体 + 约束**（`blender-hard-surface` ch11） |
| **机械件需要变形**（如履带弯曲） | 可用 | Armature 或 Curve |

> **★ 关键判断**：**刚性块的运动用约束，会变形的用骨骼。**
> `blender-hard-surface` 的坦克履带**用的是约束**（空球 + Transformation），**不是骨骼**。

## 13.3 官方条目

| 条目 |
|---|
| **Armature Constraint** |
| **Armature Deform Parent** |
| **Armatures** |
| **Bendy Bones** |
| **Bone Constraints** |
| **Bone Groups** |
| **Bone Roll** |
| **Bones** |
| **Pose Library** |
| **Separate Bones** |
| **Skinning** |

## 13.4 与硬表面相关的三个概念

| 概念 | 说明 |
|---|---|
| **Bone Envelope** | 骨骼的影响范围（球形/胶囊形），**不用权重也能变形** |
| **Vertex Group** | 顶点组；**权重绑定的载体** |
| **Pose Mode** | 摆姿势模式（区别于 Edit Mode 改骨骼形状） |

---

## 与其他部分的关系

- **约束全览** → [ch12-constraints](ch12-constraints.md)
- **履带的约束绑定实操** → `blender-hard-surface` ch11

