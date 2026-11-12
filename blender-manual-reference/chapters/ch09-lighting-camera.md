# 第 9 章：光照与相机

> 出自《Blender 2.92 Manual》Render 区。

## 9.1 四类灯光（官方）

| 类型 | 特点 | 硬表面用途 |
|---|---|---|
| **Point（点光）** | 从一点向所有方向发光 | 局部补光 |
| **Sun（太阳光）** | 平行光，方向固定，距离无衰减 | 主光（模拟日光） |
| **Spot（聚光）** | 锥形，可调大小与柔和度 | 强调细节 |
| **Area（面光）** | 面积光源，**最柔和自然** | **产品/硬表面渲染最常用** |

> **★ `blender-hard-surface` ch04 用的就是面光**：主光 + 补光 + **底部 30W 浅蓝面光朝上**

## 9.2 相机（Cameras）

| 参数 | 含义 |
|---|---|
| **Focal Length（焦距）** | 单位 mm；数值越大越接近长焦，透视越弱 |
| **Sensor** | 传感器尺寸 |
| **Shift X/Y** | 镜头偏移（不移动相机就能调构图） |
| **Clip Start/End** | 裁剪范围 |
| **Depth of Field** | 景深（需勾选） |

> **★ 硬表面渲染的相机建议（提炼）**：**用较长焦距（如 50–85mm）**，**透视畸变小**，产品感更强。

## 9.3 官方条目

| 条目 |
|---|
| **Camera Data Node** |
| **Cameras** |
| **Distance from Camera** |
| **Environment Texture Node** |
| **Indirect Lighting** |
| **Light Falloff Node** |
| **Light Node** |
| **Light Objects** |
| **Light Path Node** |
| **Light Paths** |
| **Light Probes** |
| **Light Settings** |
| **Lighting** |
| **Lights** |
| **Shadows** |
| **World** |
| **World Environment** |
| **World Node** |
| **World Settings** |

---

## 与其他部分的关系

- **打光的完整流程** → `blender-hard-surface` ch04

