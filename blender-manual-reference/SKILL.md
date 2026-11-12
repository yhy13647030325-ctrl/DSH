---
name: blender-manual-reference
description: Blender 2.92 官方参考手册知识库（蒸馏自 Blender Documentation Team 的《Blender 2.92 Manual》，1653 页 / 343.9 万字符）。当需要查 Blender 某个具体功能、某个修改器/约束/节点的全部选项含义、某个编辑器的操作、某类物理模拟参数、渲染与色彩管理设置、或遇到报错要排查时调用。与 blender-hard-surface（实战项目书）互补：那本讲"怎么做一个成品"，本技能讲"这个功能到底怎么用、每个选项什么含义"。
---

# Blender 2.92 官方参考手册

> 来源：Blender Documentation Team《Blender 2.92 Manual》，2021。
> **1653 个页面、343.9 万字符、19 个顶层分区**。
> **这是官方权威参考**——定义准确、选项完整、边界条件写清。

## 这本书与 blender-hard-surface 的分工（关键）

两本都讲 Blender，但**性质完全不同**：

| | **blender-hard-surface**（项目书） | **本技能（官方手册）** |
|---|---|---|
| 类型 | **实战教程**，3 个完整项目 | **参考手册**，功能字典 |
| 回答 | "**怎么做一个 FN SCAR / 飞船 / 坦克**" | "**这个选项到底干什么**" |
| 组织 | 按**项目流程**（四步工作流） | 按**功能模块**（19 分区） |
| 强项 | 工作流、判据、失败模式、参数取值 | **选项完整性、定义准确、边界条件** |
| 弱项 | 只覆盖三个项目用到的功能 | **不给完整项目流程** |
| 体量 | 9.7 万字 | **343.9 万字**（全量） |

**调用决策**：

| 你的问题 | 用哪个 |
|---|---|
| "我要做一个机械件，从哪开始" | **hard-surface**（四步工作流） |
| "Mirror 修改器的 Topology Mirror 是什么" | **本技能**（modeling 区） |
| "为什么我的布尔切不出孔" | **hard-surface**（F-B3-01）+ 本技能查限制 |
| "Principled BSDF 的 Sheen 参数含义" | **本技能**（render 区） |
| "履带怎么绑" | **hard-surface** ch11 |
| "Cloth 模拟的 Pressure 参数范围" | **本技能**（physics 区） |
| "快捷键 Ctrl-L 是干什么的" | **两本都有**，本技能更准（官方定义） |

> **一句话**：**"做东西"看 hard-surface，"查功能"看本技能。**

---

## 一、19 个分区（按体量排序）

| # | 分区 | 字符 | 页面 | 内容 |
|---|---|---|---|---|
| 1 | **Modeling** | 619,233 | 290 | 网格编辑、修改器（Mirror/Array/Boolean/Solidify/Subsurf 等全部） |
| 2 | **Render** | 478,435 | 271 | 相机、色彩管理、Cycles/EEVEE、光照、材质节点、输出 |
| 3 | **Add-ons** | 342,813 | 130 | 官方与第三方插件（含 3D Navigation、BlenderKit 等） |
| 4 | **Editors** | 339,869 | 155 | 各类编辑器（合成器、驱动、文件浏览器、图像、NLA…） |
| 5 | **Animation & Rigging** | 270,324 | 117 | 动作、骨骼、约束、关键帧、驱动器 |
| 6 | **Physics** | 238,512 | 119 | 刚体、布料、流体、烟雾、软体、碰撞、烘焙 |
| 7 | **Compositing** | 147,811 | 95 | 合成节点、通道、输出 |
| 8 | **Grease Pencil** | 144,825 | 102 | 二维动画工具 |
| 9 | **Sculpting & Painting** | 142,778 | 93 | 雕刻、顶点绘制、纹理绘制、权重绘制 |
| 10 | **Scenes & Objects** | 110,306 | 59 | 场景、集合、物体、变换、父子关系 |
| 11 | **User Interface** | 100,850 | 38 | 界面、选择、面板、工具栏 |
| 12 | **Video Editing** | 85,330 | 44 | 序列编辑器 |
| 13 | **Files & Data System** | 80,058 | 19 | 数据块、导入导出、路径 |
| 14 | **Motion Tracking & Masking** | 71,894 | 35 | 追踪、遮罩 |
| 15 | **Advanced** | 69,419 | 20 | 应用模板、目录结构、命令行、脚本 |
| 16 | **Troubleshooting** | 53,063 | 23 | **各类报错与故障排查** |
| 17 | **About** | 49,775 | 20 | 贡献文档、许可 |
| 18 | **Getting Started** | 49,156 | 16 | 帮助系统、社区、安装 |
| 19 | **Glossary** | 33,789 | 1 | **术语表（33.8 万字？实为 3.4 万字）** |

---

## 二、本技能收录策略（为什么不是全量搬入）

**343.9 万字不可能全塞进一个技能**——加载一次就爆上下文。

**策略：按"硬表面建模者最需要查的内容"做深度提取，其余留索引。**

| 分区 | 收录程度 | 理由 |
|---|---|---|
| **Modeling** | **深度**（完整章节） | 硬表面建模的核心 |
| **Render** | **深度**（材质/光照/渲染设置） | 上材质与出图 |
| **Scenes & Objects** | **深度**（变换/父子/集合） | 所有建模的地基 |
| **Interface** | **中等**（选择/快捷键原则） | 通用操作 |
| **Animation & Rigging** | **中等**（约束部分，对应履带绑定） | 机械绑定的参考 |
| **Physics** | **索引为主** | 硬表面用得少，但布料/刚体可能用到 |
| **Add-ons** | **索引为主** | 只列常用插件 |
| **Troubleshooting** | **深度**（报错排查） | 直接有用 |
| **Glossary** | **深度**（术语表） | 查词 |
| Compositing / Grease Pencil / Video Editing / Motion Tracking | **仅索引** | 与硬表面建模无关 |
| About / Getting Started | 跳过 | 无技术价值 |

---

## 三、快捷键写法说明（与 hard-surface 的差异）

**本手册用连字符**：`Ctrl-L`、`Shift-Alt`、`Shift-LMB`
**项目书用加号**：`Ctrl + L`、`Shift + Alt`

> **两者含义相同**，只是写法不同。本技能统一采用**手册原写法**（便于对照官方文档），
> 在 [references/shortcuts-official.md](references/shortcuts-official.md) 中给出**两种写法的对照表**。

**鼠标键缩写**（手册专用）：

| 缩写 | 含义 |
|---|---|
| **LMB** | 鼠标左键（Left Mouse Button） |
| **RMB** | 鼠标右键 |
| **MMB** | 鼠标中键（滚轮按下） |
| **Numpad** | 小键盘 |

---

## 四、主题索引（按"要查什么"找）

### 建模（modeling 区）

| 要查 | 章节 |
|---|---|
| 网格选择与编辑 | [ch01-mesh-editing](chapters/ch01-mesh-editing.md) |
| **修改器总览与逐项参数** | [ch02-modifiers](chapters/ch02-modifiers.md) |
| 曲线与曲面建模 | [ch03-curve-surface](chapters/ch03-curve-surface.md) |
| 雕刻 | [ch04-sculpting](chapters/ch04-sculpting.md) |
| 拓扑与重网格 | [ch05-topology](chapters/ch05-topology.md) |

### 物体与场景

| 要查 | 章节 |
|---|---|
| 物体变换、原点、父子 | [ch06-objects-transforms](chapters/ch06-objects-transforms.md) |
| 集合与场景管理 | [ch07-collections-scenes](chapters/ch07-collections-scenes.md) |

### 渲染与材质

| 要查 | 章节 |
|---|---|
| 材质与节点 | [ch08-materials-nodes](chapters/ch08-materials-nodes.md) |
| 光照与相机 | [ch09-lighting-camera](chapters/ch09-lighting-camera.md) |
| 渲染引擎与设置 | [ch10-render-engines](chapters/ch10-render-engines.md) |
| 色彩管理 | [ch11-color-management](chapters/ch11-color-management.md) |

### 绑定与动画

| 要查 | 章节 |
|---|---|
| 约束（含 Transformation） | [ch12-constraints](chapters/ch12-constraints.md) |
| 骨骼与绑定 | [ch13-armature-rigging](chapters/ch13-armature-rigging.md) |

### 排查与术语

| 要查 | 章节 |
|---|---|
| **报错排查** | [ch14-troubleshooting](chapters/ch14-troubleshooting.md) |
| **术语表** | [references/glossary.md](references/glossary.md) |

## 五、配套文件

- [references/BEFORE-AFTER.md](references/BEFORE-AFTER.md) — **蒸馏前后对照表**（两本总览、逐章数据、关键增量、实测纠错记录、覆盖缺口）

- [references/shortcuts-official.md](references/shortcuts-official.md) — 官方手册快捷键全表（**218 条分区记录 / 105 个唯一键位**，同一键在不同编辑器含义不同，故按分区列出；含两种写法对照）
- [references/modifier-index.md](references/modifier-index.md) — **全部修改器索引（57 个）**（含冷门修改器）
- [references/node-index.md](references/node-index.md) — 材质/合成节点索引
- [references/glossary.md](references/glossary.md) — 术语表（67 条）
- [references/version-differences.md](references/version-differences.md) — **2.92 ↔ 3.x/4.x 完整版本差异**（7 小节：View Transform / Principled 参数 / Auto Smooth / 重算法线 / EEVEE / 其他 / 实操建议）
- [references/cheatsheet.md](references/cheatsheet.md) — 常用设置速查 + 版本差异四条摘要
- [references/STANDARD.md](references/STANDARD.md) — **两个 Blender 技能的统筹规范**（分工、调用决策表、覆盖缺口）
- [templates/feature-lookup.md](templates/feature-lookup.md) — "查一个功能"的检索模板

## 相关技能

- **`blender-hard-surface`（互补，必看）**：三个完整项目的实战流程、四步工作流、111 条失败模式、精确参数取值
- `design-elements-hannah` / `product-design-styling-dabbs`（形态从哪来）
- `design-methodology-liuguanzong/references/skill-index.md`（总索引）

## 限制

- **版本 2.92（2021）**：Blender 现为 4.x。
  **完整差异对照见 [references/version-differences.md](references/version-differences.md)**，其中最影响照着做的四条：
  - **Auto Smooth**：2.92 是 Object Data 里的复选框；**4.0 起移除**，改用 **Shade Auto Smooth**
  - **重算法线**：2.92 是 `Shift-N`；**3.x/4.x 是 `Ctrl-N`**
  - **默认 View Transform**：2.92 是 **Filmic**；**4.0 起为 AgX**
  - **Principled 参数名**：Specular → **Specular IOR Level**、Transmission → **Transmission Weight** 等
- **不含项目流程**：手册是功能参考，**不给"从零做一个东西"的完整路径**——那在 hard-surface。
- **不含数值调参建议**：手册给**参数范围与含义**，但不给"做金属件该填多少"这类经验值（那在 hard-surface）。
- **Add-ons 区涵盖大量第三方插件**，多数与硬表面建模无关。
