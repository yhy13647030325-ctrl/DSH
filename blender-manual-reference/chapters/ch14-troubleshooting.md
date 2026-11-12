# 第 14 章：故障排查

> 出自《Blender 2.92 Manual》Troubleshooting 区（53,063 字符 / 23 页）。

## 14.1 官方排查条目

| 条目 |
|---|
| **Common Problems** |
| **Crashes** |
| **Drivers** |
| **Graphics Hardware** |
| **Information** |
| **Laptops** |
| **Python Errors** |
| **Recovering Data** |
| **Startup** |
| **Troubleshooting** |

## 14.2 硬表面建模的十类常见故障

> **先查 `blender-hard-surface` 的 111 条失败模式**（带编号、带处置），
> 本章只在**那 111 条都没覆盖**时查官方排查。

| 现象 | 先去哪查 |
|---|---|
| Boolean 切不出孔 | hard-surface F-B3-01（修法线） |
| 烘焙结果怪异 | hard-surface F-B4-05（挪开遮挡件）+ 查本章 |
| 修改器不生效 | 查本章 + 确认物体缩放是否 apply |
| 平滑着色难看 | hard-surface F-B8-01/02 + Weighted Normal |
| 履带绑定不动 | hard-surface F-B11-02/04/05 |
| 渲染有噪点 | 提高 Samples + 开 Denoising（[ch10](ch10-render-engines.md)） |
| 颜色不对 | 查 Color Management（[ch11](ch11-color-management.md)） |
| 崩溃 | 查本章 Crashes 条目 |
| 视图卡顿 | 查本章 3D Viewport 条目 |
| 找不到某功能 | 查 [shortcuts-official](../references/shortcuts-official.md) |

---

## 与其他部分的关系

- **111 条失败模式** → `blender-hard-surface` `references/failure-modes.md`

