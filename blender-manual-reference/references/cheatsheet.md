# 常用设置速查

> 两本技能的统一入口。

## 一、按任务查（跨两本）

| 任务 | 查哪里 |
|---|---|
| 做一个机械件，从哪开始 | `blender-hard-surface` workflow.md |
| 某个修改器全部选项 | 本技能 modifier-index.md（57 个） |
| 某快捷键官方定义 | 本技能 shortcuts-official.md（132 键） |
| 金属件参数该填多少 | `blender-hard-surface` cheatsheet.md（26 项数值） |
| 报错怎么修 | `blender-hard-surface` failure-modes.md（111 条） |
| 某术语什么意思 | 本技能 glossary.md（67 条） |
| 约束怎么配 | 本技能 ch12（28 种）+ hard-surface ch11（履带实例） |

## 二、Blender 版本差异（必知）

> **完整对照见 [version-differences.md](version-differences.md)**（含 2.92 原文核实 + 4.x 变化 + 实操影响）。
> 下面只列**最容易踩的四条**。

| # | 项 | 2.92（手册） | 3.x/4.x |
|---|---|---|---|
| 1 | **Auto Smooth** | **Object Data ‣ Normals** 里的复选框 + Angle | **4.0 起移除**，改用 **Shade Auto Smooth**（自动挂 Smooth by Angle 修改器） |
| 2 | **重算法线** | `Shift-N` | **`Ctrl-N`** |
| 3 | **默认 View Transform** | **Filmic** | **AgX**（4.0+，Filmic 保留但非默认） |
| 4 | **Principled 参数名** | Specular / Transmission / Clearcoat / Sheen | **Specular IOR Level / Transmission Weight / Coat Weight / Sheen Weight** |

> **找不到设置时的通用解法**：**F3 搜索功能名**。跨版本最可靠。

## 三、四个引擎/工具选择

| 要什么 | 选 |
|---|---|
| 快预览 | EEVEE |
| 真实产品图 | **Cycles** |
| 边缘遮罩/烘焙 | **Cycles（必须）** |
| 刚性机械绑定 | **空物体 + 约束**（不是骨骼） |

## 四、快捷键两写法对照

| 含义 | 官方（本技能） | 项目书 |
|---|---|---|
| 环切 | `Ctrl-R` | `Ctrl + R` |
| 倒角 | `Ctrl-B` | `Ctrl + B` |
| 沿法线缩放 | `Alt-S` | `Alt + S` |
| 选边循环 | `Alt-LMB` | `Alt + 左键` |
| 复制 | `Shift-D` | `Shift + D` |
| 父级 | `Ctrl-P` | `Ctrl + P` |

