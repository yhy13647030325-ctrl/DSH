# 第 10 章：渲染引擎与设置

> 出自《Blender 2.92 Manual》Render 区（478,435 字符 / 271 页）。

## 10.1 两个引擎的选择

| | **EEVEE** | **Cycles** |
|---|---|---|
| 原理 | **实时栅格化** | **路径追踪** |
| 速度 | **快** | 慢 |
| 真实度 | 近似 | **物理准确** |
| 适合 | 预览、动画、风格化 | **产品渲染、真实效果** |
| **边缘遮罩/烘焙** | ✗ **不支持** | ✓

> **★ `blender-hard-surface` ch04 明确**：「**边缘遮罩在 Eevee 里不工作**」——所以做边缘磨损**必须切 Cycles**。

## 10.2 Render Samples

| 引擎 | 采样含义 | 实战取值 |
|---|---|---|
| **Cycles** | 每像素光线数 | `blender-hard-surface` 用 **512** + 勾 **Denoising** |
| **EEVEE** | TAA 采样数 | 预览 16–32，最终 64–128 |

## 10.3 Denoising（降噪）

> **官方机制**：**用算法消除低采样产生的噪点**，使低采样也能出干净图。
> **`blender-hard-surface` ch04 明确要勾 Denoising 的 Render 框。**

## 10.4 输出设置

| 参数 | 说明 |
|---|---|
| **Resolution** | 分辨率（1920×1080 等） |
| **Resolution %** | 分辨率百分比（预览用 50%） |
| **File Format** | PNG（默认）/ JPEG / OpenEXR |
| **Color Depth** | 8 bit / 16 bit / 32 bit |
| **Color Management** | 见 [ch11](ch11-color-management.md) |

---

## 与其他部分的关系

- **渲染实操** → `blender-hard-surface` ch04
- **色彩管理** → [ch11-color-management](ch11-color-management.md)

