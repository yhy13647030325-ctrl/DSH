# 第 8 章：材质与节点

> 出自《Blender 2.92 Manual》Render 区（478,435 字符 / 271 页）。

## 8.1 材质相关的官方条目

| 条目 |
|---|
| **AOV Output Node** |
| **Add Shader** |
| **Anisotropic BSDF** |
| **Attribute Node** |
| **Bevel Node** |
| **Blackbody Node** |
| **Brick Texture Node** |
| **Bump Node** |
| **Camera Data Node** |
| **Checker Texture Node** |
| **Clamp Node** |
| **Color Ramp Node** |
| **Diffuse BSDF** |
| **Displacement Node** |
| **Environment Texture Node** |
| **Fresnel Node** |
| **Gamma Node** |
| **Geometry Node** |
| **Glass BSDF** |
| **Glossy BSDF** |
| **Gradient Texture Node** |
| **Hair BSDF** |
| **Hair Info Node** |
| **Hue Saturation Value Node** |
| **IES Texture Node** |
| **Image Texture Node** |
| **Invert Node** |
| **Layer Weight Node** |
| **Legacy Textures** |
| **Light Falloff Node** |
| **Light Node** |
| **Light Path Node** |
| **Magic Texture Node** |
| **Map Range Node** |
| **Mapping Node** |
| **Material** |
| **Material Node** |
| **Material Properties** |
| **Material Settings** |
| **Materials** |

## 8.2 Principled BSDF 的官方参数（硬表面最常用）

| 参数 | 官方含义 |
|---|---|
| **Base Color** | 基础色 |
| **Metallic** | 金属度（0=绝缘体，1=金属） |
| **Roughness** | 粗糙度，**决定材质有多亮/多光滑** |
| **IOR** | 折射率 |
| **Alpha** | 透明度 |
| **Normal** | 法线输入（接法线贴图/Bevel 节点） |
| **Subsurface** | 次表面散射 |
| **Specular** | 高光强度 |
| **Sheen** | 光泽（布料类） |
| **Clearcoat** | 清漆层 |
| **Emission** | 自发光 |

> **⚠ 2.92 与 4.x 的差异**：4.x 把 `Specular` 改成 `Specular IOR Level`、`Transmission` 改成 `Transmission Weight`、`Clearcoat` 拆成两项等。**参数含义延续，名字有变。**

## 8.3 与 blender-hard-surface 的关系

| | hard-surface | 本章 |
|---|---|---|
| 材质做法 | **边缘遮罩→烘焙→Mix RGB 边缘磨损**（ch04） | **节点与参数的官方定义** |
| 深度 | 给完整流程与精确取值（Samples 10 / Radius 0.07） | 给每个参数是什么 |

---

## 与其他部分的关系

- **边缘磨损完整流程** → `blender-hard-surface` ch04
- **法线贴图与贴花** → `blender-hard-surface` ch06

