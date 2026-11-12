# 功能查阅模板（Feature Lookup）

> 用法：要查 Blender 某个功能时，按此模板定位。

## 一、先分类

| 我要查的是 | 去 |
|---|---|
| 修改器（Mirror/Array/Boolean…） | `references/modifier-index.md`（57 个） |
| 快捷键 | `references/shortcuts-official.md`（132 键，按分区） |
| 节点 | `references/node-index.md` |
| 术语 | `references/glossary.md`（67 条） |
| 约束 | `chapters/ch12-constraints.md`（28 种） |
| 网格编辑工具 | `chapters/ch01-mesh-editing.md`（63 工具带菜单路径） |
| 渲染设置 | `chapters/ch10-render-engines.md` |
| 光照/相机 | `chapters/ch09-lighting-camera.md` |
| 材质参数 | `chapters/ch08-materials-nodes.md` |
| 报错 | `chapters/ch14-troubleshooting.md` + `blender-hard-surface` 111 条 |

## 二、查到之后还要问三个问题

| # | 问题 | 为什么 |
|---|---|---|
| 1 | **这个功能在哪个模式可用？**（Object / Edit / Pose） | 手册的 Reference 块有 Mode 字段 |
| 2 | **有没有限制或警告？** | 手册的 Note/Warning 往往是最有价值的部分（如 Boolean 的 Manifold 警告） |
| 3 | **项目书里有没有实际用法？** | `blender-hard-surface` 给的是在真实项目里怎么用 |

## 三、若两本都没有

| 情况 | 处理 |
|---|---|
| 与硬表面建模无关（雕刻/合成/蜡笔） | 本技能没深度提取，需查手册原文对应分区 |
| 版本差异导致 | 对照 `references/cheatsheet.md` 的版本差异表 |
| 手册也没写 | 标（书中未展开），不臆造 |

