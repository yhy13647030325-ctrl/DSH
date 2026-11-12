# 节点索引

> 出自《Blender 2.92 Manual》Render 与 Compositing 区。

## 共 59 个节点（官方标题）

| 节点 |
|---|
| **AOV Output Node** |
| **Attribute Node** |
| **Bevel Node** |
| **Blackbody Node** |
| **Brick Texture Node** |
| **Bump Node** |
| **Camera Data Node** |
| **Checker Texture Node** |
| **Clamp Node** |
| **Color Ramp Node** |
| **Displacement Node** |
| **Environment Texture Node** |
| **Fresnel Node** |
| **Gamma Node** |
| **Geometry Node** |
| **Gradient Texture Node** |
| **Hair Info Node** |
| **Hue Saturation Value Node** |
| **IES Texture Node** |
| **Image Texture Node** |
| **Invert Node** |
| **Layer Weight Node** |
| **Light Falloff Node** |
| **Light Node** |
| **Light Path Node** |
| **Magic Texture Node** |
| **Map Range Node** |
| **Mapping Node** |
| **Material Node** |
| **Math Node** |
| **Mix Node** |
| **Musgrave Texture Node** |
| **Noise Texture Node** |
| **Normal Map Node** |
| **Normal Node** |
| **Object Info Node** |
| **Particle Info Node** |
| **Point Density Node** |
| **RGB Curves Node** |
| **RGB Node** |
| **RGB to BW Node** |
| **Sky Texture Node** |
| **Tangent Node** |
| **Texture Coordinate Node** |
| **UV Map Node** |
| **Value Node** |
| **Vector Curves Node** |
| **Vector Displacement Node** |
| **Vector Math Node** |
| **Vector Rotate Node** |
| **Vector Transform Node** |
| **Vertex Color Node** |
| **Volume Info Node** |
| **Voronoi Texture Node** |
| **Wave Texture Node** |
| **Wavelength Node** |
| **White Noise Texture Node** |
| **Wireframe Node** |
| **World Node** |

## 硬表面材质最常用的节点（提炼）

| 节点 | 用途 |
|---|---|
| **Principled BSDF** | 主着色器（几乎所有材质的汇合点） |
| **Image Texture** | 载入贴图 |
| **Mix RGB** | 混合两色（边缘磨损用） |
| **Bevel** | 生成边缘遮罩（Samples 10 / Radius 0.07） |
| **Geometry** | 取法线/位置等信息 |
| **Vector Math** | 向量运算（改 Dot Product 做边缘检测） |
| **Invert** | 反相（黑变白） |
| **Math** | 数学运算（可用 Power 调边缘强度，Exponent 0.200） |
| **Noise Texture** | 程序化噪波（做表面不规则） |
| **Color Ramp** | 颜色映射/渐变控制 |
| **Bump** | 法线凹凸（不做几何） |
| **Normal Map** | 法线贴图（接烘好的法线图） |
| **Mapping** | 变换纹理坐标 |
| **Texture Coordinate** | 取坐标来源（UV/Generated/Object） |

---

## 与其他部分的关系

- **边缘磨损的完整节点链** → `blender-hard-surface` ch04
- **法线贴花** → `blender-hard-surface` ch06

