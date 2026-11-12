# 第 11 章：色彩管理

> 出自《Blender 2.92 Manual》Render 区。

## 11.1 为什么重要

> 色彩管理决定**渲染出来的颜色看起来对不对**。
> 同一个材质，**不同 View Transform 出来的观感差别很大**。

## 11.2 View Transform（视图变换）

| 类型 | 特点 |
|---|---|
| **Standard** | 不做色调映射，**颜色直出**（可能与预期不符） |
| **Filmic** | **电影感的色调映射**，高光不易过曝，**但会降低对比度与饱和度** |
| **False Color** | 假色，**用于检查曝光** |

> **★ 2.92 时代默认是 Filmic。**
> **4.x 起默认改为 AgX**，并保留 Standard / Filmic。

## 11.3 三个关键概念（官方术语表）

| 术语 | 官方定义 |
|---|---|
| **Aliasing** | 渲染伪影，表现为**锯齿状线条** |
| **Anti-Aliasing** | **每像素多次采样**来最小化锯齿的技术 |
| **Straight vs Premultiplied Alpha** | **画图软件/网页输出用 Straight；渲染/合成中间文件用 Premultiplied。** 两者转换**不是简单运算** |

## 11.4 硬表面的实用建议（提炼）

| 你要 | 用 |
|---|---|
| 产品图，颜色要准 | **Standard** + 手动控制曝光 |
| 影视感，高光柔 | **Filmic**（2.92）/ **AgX**（4.x） |
| 检查哪里过曝 | **False Color** |

---

## 与其他部分的关系

- **术语** → [references/glossary.md](../references/glossary.md)

