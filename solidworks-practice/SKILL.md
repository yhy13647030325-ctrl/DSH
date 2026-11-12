---
name: solidworks-practice
description: SOLIDWORKS 实战操作参考（蒸馏自《SolidWorks 实战教程》，上海三泽信息技术有限公司编著，机械工业出版社）。当需要建模、出图、装配、渲染、动画、仿真或准备 CSWA/CSWP 时调用，包括：零件建模与特征选型（拉伸/旋转/扫描/放样/抽壳/筋/阵列/拔模）、草图完全定义与设计意图、装配体（自底向上/自顶向下、配合、自由度、爆炸视图）、工程图（模板、标准三视图、派生视图、尺寸与注解、材料明细表）、PhotoView360 渲染（外观/布景/贴图/光源）、配置与参数化（系列零件设计表）、3D 草图与焊件、MotionManager 动画、eDrawings 发布批注、Simulation 静力分析与设计优化、CSWA/CSWP 样题套路。
---

# SOLIDWORKS 实战参考

> 来源：`D:\deepseek 工作\下载\SolidWorks实战教程 (SolidWorks实战教程.pdf)....pdf`（280 页，书内页 1–270 + 附录）。
> 边界：本技能只复述该书已写明的操作与判据。凡标 **（书中未展开）** 处，表示原书没有给规则，不得替它编；凡标 **（提炼）** 处，为从书中多个实例归纳出的通用做法，不是原书原句。

## 怎么用

| 你在做什么 | 读哪个文件 |
|---|---|
| **开工前想少踩坑** | **[walkthroughs/PRE-FLIGHT.md](references/walkthroughs/PRE-FLIGHT.md)**（七问 + 91 条功能自查，唯一该背的一页） |
| 刚接手一个零件任务，不知道从哪下手 | [walkthroughs/ch03.md](references/walkthroughs/ch03.md)（14 个例题的逐步清单，先看 X00"分析模型"） |
| 照书做但卡在某一步 | [walkthroughs/](references/walkthroughs/) 对应章文件——每步标了 `[原书]`/`[隐]`/`[判]` 和书内页码 |
| 遇到报错或结果不对 | [walkthroughs/F-INDEX.md](references/walkthroughs/F-INDEX.md)（182 条失败模式，按现象查） |
| 草图变蓝/变黄、改不动 | [walkthroughs/ch02.md](references/walkthroughs/ch02.md)（草图三色 + F-02 系列） |
| 该用拉伸还是旋转/扫描/放样 | 本文件"特征选型速查" + [walkthroughs/ch03.md](references/walkthroughs/ch03.md) |
| 装配装不上去、零件乱跑 | [walkthroughs/ch04.md](references/walkthroughs/ch04.md)（自由度与配合） |
| 出工程图、标注不规范 | [walkthroughs/ch06.md](references/walkthroughs/ch06.md) |
| 要渲染效果图 | [walkthroughs/ch07.md](references/walkthroughs/ch07.md)（含外观层级判断） |
| 一个模型要多规格 | [walkthroughs/ch08.md](references/walkthroughs/ch08.md) |
| 管路/框架/焊件 | [walkthroughs/ch09.md](references/walkthroughs/ch09.md) |
| 做装配动画 | [walkthroughs/ch10.md](references/walkthroughs/ch10.md) |
| 发给别人看模型 | [walkthroughs/ch11.md](references/walkthroughs/ch11.md) |
| 强度校核、减重优化 | [walkthroughs/ch12.md](references/walkthroughs/ch12.md) |
| 考 CSWA / CSWP | [walkthroughs/ch99.md](references/walkthroughs/ch99.md) |
| 只要知识点、不要步骤 | [chapters/](chapters/)（12 章主题式整理） |
| 查术语、查参数默认值 | [references/glossary.md](references/glossary.md)、[references/cheatsheet.md](references/cheatsheet.md) |

## 全书贯穿的"隐性规矩"

这些是书里每道例题都重复、但只在正文里散着出现的约定，先记住能少踩一半坑：

| 项 | 约定 |
|---|---|
| 单位系统 | **MMGS**（毫米、克、秒），全书例题默认 |
| 小数位数 | **2** |
| 零件模板 | `gb_part`（第 8 章写法）；第 9 章写作 `gd_part`，两处文字不一致，均为国标零件模板 |
| 图纸模板 | `gb_a3`（国标 A3） |
| 环境设置时机 | **画草图之前**设置单位与小数位，不是画完再改 |
| 尺寸名称格式 | `Dx@草图n`，默认隐藏，`视图 > 尺寸名称` 显示 |
| 材料 | 例题多为 1060 铝合金（2700 kg/m³）、ABS（1020）、6061 铝合金（2700）；附录用红铜 0.0089 g/mm³、黄铜 0.0085 g/mm³、铜 0.321 lb/in³ |
| 模型命名 | 一律按书中给定名称保存，练习要求"计算总质量、体积、质心"时材料必须指定 |

## 只背一页的话，背这页

**[references/walkthroughs/PRE-FLIGHT.md](references/walkthroughs/PRE-FLIGHT.md)** — 开工前 10 秒自查。

对 182 条失败模式逐条归类后，真实分布是：

| 类 | 根因 | 条数 | 占比 |
|---|---|---|---|
| **I** | **不知道有这功能/机制** | **91** | **50%** |
| P | 开关或设置状态不对 | 22 | 12% |
| L | 软件硬限制与语义 | 19 | 10% |
| V | 数值/资料/单位错 | 17 | 9% |
| K | 选错对象或够不着 | 16 | 9% |
| O | 顺序倒置 | 12 | 7% |
| Q | 状态未达成 | 5 | 3% |

**一半的坑不是做错，而是不知道软件能那么说。** 所以那页分两半：上半七问关口（拦 64 条可预防的错，实测零重叠），下半 91 条功能自查表（认出你不知道存在的功能）。

## 六个核心工作流（背下来就能开工）

**① 零件建模标准流程（每道例题都是这 7 步）**
```
分析模型 → 新建零件 → 环境设置（MMGS/小数位2）→ 绘制草图并完全定义
→ 创建特征 → 编辑材料 → 保存并关闭
```
第一步"分析模型"含两件事，书里明确要求：**模型的摆放**（决定二维视图方向、影响出图）+ **最佳轮廓的选择**（决定后续改型难易）。

**② 草图 = 轮廓 + 几何关系 + 尺寸，三件齐了才叫"完全定义"**
先画近似形状（尺寸驱动，不必画准），再加几何关系，最后标尺寸。颜色即状态：蓝=欠定义、黑=完全定义、黄=过定义。

**③ 内外因式的"先想清楚再画"（提炼）**
书里所有复杂例子（台灯、漏斗、篮球架、装载机）都是先看参照物/图片/工程图，再定基准面与路径，最后才落笔。**不要在没想清拓扑关系时开始画第一根线。**

**④ 装配 = 插入 + 配合（吃掉 6 个自由度）**
第一个插入的零件自动【固定】；其余零件 6 个自由度，靠【重合】【同轴心】【宽度】等逐步约束。装配前先想清连接关系，先把零件摆到大致位置再配。

**⑤ 出图 = 模板 + 视图 + 尺寸 + 注解**
`新建工程图选模板 → 模型视图/标准三视图 → 派生视图（剖面/局部/断开剖/断裂/交替位置）→ 导入模型尺寸 → 加注解与公差 → 保存`。

**⑥ 分析与优化 = 算例 → 网格 → 结果 → 改模型 → 再算**
网格越小精度越高但更慢；判据：网格加密一档后应力变化进入 **5%** 以内即可停。

## 特征选型速查（该用哪个）

| 几何特征 | 首选特征 | 关键点 |
|---|---|---|
| 等截面直线延伸 | 拉伸凸台/基体 | 终止条件：给定深度 / 两侧对称 / 成形到下一面 / 成形到一顶点 / 完全贯穿 / 到离指定面指定的距离 |
| 回转体 | 旋转凸台/基体 | 需中心线或构造线作轴 |
| 沿路径的等截面（弹簧、回形针、管路） | 扫描 | 轮廓 + 路径（+ 引导线） |
| 多截面过渡（漏斗、铸件） | 放样 | 轮廓 + 接头（+ 引导线）；接头不对齐会扭曲甚至失败 |
| 薄壁壳体 | 抽壳 | 可多厚度；先实体后抽壳 |
| 加强 | 筋 | 可带拔模、可选"在草图基准面处" |
| 重复特征 | 线性/圆周/镜像/草图驱动/表格驱动/曲线驱动/填充阵列 | 可"只阵列源"、可用【可跳过的实例】挖掉个别实例 |
| 脱模斜度 | 拔模（+ 拔模分析） | 拔模分析先分类面：正拔模/负拔模/需要拔模 |
| 文字/Logo | 包覆 | 需先草图文字 |

## 失败模式：182 条带编号、可回查

**完整索引见 [references/walkthroughs/F-INDEX.md](references/walkthroughs/F-INDEX.md)**，按"现象关键词 → 编号 → 处置 → 书内页码"组织。编号规则 `F-章-序`（如 `F-03-12` = 第 3 章第 12 条）。

按章分布：

| 章 | 条数 | 章 | 条数 |
|---|---|---|---|
| 01 界面环境 | 7 | 07 渲染 | 13 |
| 02 草图 | 15 | 08 配置 | 12 |
| 03 基本特征 | **26** | 09 3D草图/焊件 | 12 |
| 04 装配体 | 18 | 10 动画 | 14 |
| 05 标准件 | 11 | 11 eDrawings | 9 |
| 06 工程图 | 18 | 12 分析 | 15 |
|  |  | 附录 CSWA/CSWP | 12 |

**最高频的五个根因**（跨章重复出现，先改这五个能消掉大半）：

| 根因 | 典型编号 | 一句话 |
|---|---|---|
| **层级/作用域选错** | F-07-02、F-06-01、F-10-02、F-03-01 | 改到了错误的层（面/零件/文档层），或选错了作用范围 |
| **顺序倒置** | F-02-10、F-03-12、F-04-04、F-08-01 | 该"先定义/先摆位/先显示"的步骤被推到后面 |
| **前置开关没开** | F-05-01、F-07-06、F-08-05、F-10-01、F-03-08 | 功能存在但没启用（插件/自动键码/临时轴/Instant3D） |
| **默认值没清** | F-07-01、F-08-03、F-12-08、F-06-11 | 白色外观、Excel 文本格式、默认网格、默认比例 |
| **软件硬限制没记住** | F-06-06、F-06-07、F-10-03、F-09-01、F-03-12 | 剖视图禁忌、算例类型、Tab 切面、引导线定型 |

## 章节索引

| # | 标题 | 主要内容 |
|---|---|---|
| [ch01](chapters/ch01-interface-and-env.md) | 软件介绍与基本环境 | 界面构成、系统选项 vs 文档属性、鼠标三键、快捷键 |
| [ch02](chapters/ch02-sketch.md) | 草图 | 草图实体、草图工具、几何关系、完全定义、智能尺寸、4 个示例 |
| [ch03](chapters/ch03-basic-features.md) | 基本特征 | 拉伸三型、参考几何体、阵列四种、旋转、扫描三型、拔模、抽壳与筋、放样两型 |
| [ch04](chapters/ch04-assembly.md) | 装配体 | 自底向上、自顶向下、配合、子装配体刚性/柔性、爆炸视图与爆炸直线 |
| [ch05](chapters/ch05-toolbox-standard-parts.md) | 标准件库 | 设计库、Toolbox、异型孔向导、智能扣件、3DContentCentral |
| [ch06](chapters/ch06-drawing.md) | 工程图 | 术语、9 类派生视图、尺寸与注解、两个完整出图实例 |
| [ch07](chapters/ch07-render.md) | 渲染 | RealView、环境封闭、PhotoView360、外观/贴图/布景/光源、最终渲染 |
| [ch08](chapters/ch08-configuration-parametric.md) | 参数化设计基础 | 配置、手动添加、系列零件设计表（Excel）、显示特征尺寸 |
| [ch09](chapters/ch09-3d-sketch-weldment.md) | 3D 草图 | 空间控标、Tab 切基准面、3D 管道、焊件结构构件分组 |
| [ch10](chapters/ch10-animation.md) | 动画 | 三类算例、关键帧与插值、马达/引力/接触、动态剖切、动画渲染 |
| [ch11](chapters/ch11-edrawings.md) | eDrawings | 文件类型、测量/标注/戳记/横断面、批注、exe 发布 |
| [ch12](chapters/ch12-simulation.md) | 分析工具 | 静力分析假设、夹具与载荷、网格、结果图解、设计洞察、设计算例优化 |
| [ch99](chapters/ch99-certification-cswa-cswp.md) | CSWA / CSWP 样题 | 全局变量 + 链接数值 + 质量属性 的标准打法 |

## 主题索引

- **拔模 / 拔模分析** → ch03
- **爆炸视图 / 爆炸直线草图** → ch04
- **布局设计** → ch04（仅提及，未展开）
- **材料（编辑材料 / 自定义材料 / 密度）** → ch03、ch06
- **草图状态（欠定义/完全定义/过定义）** → ch02
- **草图图片（描摹参照）** → ch03（台灯实例）
- **尺寸名称 / 显示特征尺寸** → ch08
- **穿透（几何关系）** → ch03（扫描引导线）
- **动态剖切** → ch10
- **对称 / 两侧对称** → ch02、ch03
- **多厚度抽壳** → ch03
- **干涉检查（静态/动态）** → ch04
- **工程图模板 / 图纸格式** → ch06
- **关系（配合）** → ch04
- **焊件 / 结构构件** → ch09
- **基准面 / 基准轴** → ch03
- **几何关系** → ch02
- **间隙 / 可跳过的实例** → ch03
- **剪裁五法** → ch02
- **键码 / 关键帧 / 插值模式** → ch10
- **筋** → ch03（含拔模）
- **镜像（草图/特征/零部件）** → ch02、ch03、ch04
- **可变装配体特征** → ch10（动态剖切）
- **拉伸（拔模/薄壁/方向）** → ch03
- **零件序号 / 材料明细表** → ch06
- **配置 / ConfigurationManager** → ch08
- **剖面视图 vs 断开的剖视图（局部剖）** → ch06
- **柔性与刚性** → ch04
- **扫描** → ch03
- **设计库** → ch05
- **设计洞察图解** → ch12
- **视图调色板** → ch06
- **质量属性 / 质心** → 附录
- **智能扣件** → ch05
- **中心线 / 构造线** → ch02
- **装配体透明度 / 迫使透明** → ch04
- **自由拖动 / 物理动力学** → ch06（交替位置视图）
- **AutoCAD 文件（DXF/DWG）** → ch11（eDrawings 可直开）

## 三层资料结构

本技能分三层，按"你要多细"选入口：

| 层 | 目录 | 内容 | 何时用 |
|---|---|---|---|
| **L1 主题** | `chapters/` | 12 章按知识点重组（表格化、判据化），不含逐步操作 | 想快速理解某个概念/参数 |
| **L2 步骤** | `references/walkthroughs/` | **13 个章节文件的逐步清单**，共 **42 个主例题 + 12 个认证变体**；每步标 `[原书]`/`[隐]`/`[判]` + 书内页码 | 正在照书做，卡在某一步 |
| **L3 判据** | `references/patterns.md`、`cheatsheet.md`、`F-INDEX.md` | 8 个套路、17 组速查、182 条失败模式 | 做判断、查参数、排错 |

**`[隐]` 是本轮新增的核心价值**：标出原书**没写、但缺了就做不下去**的动作。例：
- 第 3 章每个例题都写"分析模型"却只有 1 处解释 → 其余 13 处按 `[隐]` 处理（F-03-02）
- 第 2 章 E2 直接从"画中心线"开始，省略了"新建/选基准面/正视于" → `[隐]` 标注（F-02-15）
- 第 9 章焊件"圆弧单独成组"从未被解释为什么 → `[隐]` 提炼为分组规律（F-09-07）

## 配套文件

- [references/walkthroughs/PRE-FLIGHT.md](references/walkthroughs/PRE-FLIGHT.md) — **开工前 10 秒自查**（七问关口 + 91 条功能自查表）
- [references/walkthroughs/](references/walkthroughs/) — **L2 逐步清单**：ch01–ch12、ch99、F-INDEX（14 个文件）
- [references/patterns.md](references/patterns.md) — 8 个可复用套路 + 11 条反模式
- [references/cheatsheet.md](references/cheatsheet.md) — 17 组速查（快捷键/终止条件/阵列/视图/配合/渲染/分析）
- [references/glossary.md](references/glossary.md) — 约 200 条术语
- [chapters/](chapters/) — L1 主题整理（12 章 + 认证）
- [templates/modeling-worksheet.md](templates/modeling-worksheet.md) — 建模前填写单
- [templates/config-matrix.md](templates/config-matrix.md) — 配置/系列零件设计表矩阵
- [templates/drawing-checklist.md](templates/drawing-checklist.md) — 出图自检清单

## 相关技能

> **总索引**：[design-methodology-liuguanzong/references/skill-index.md](../design-methodology-liuguanzong/references/skill-index.md) —— 12 个设计技能的分工、路由表与 6 个跨技能接缝。

### 三个 SOLIDWORKS 技能的分工

| 技能 | 定位 | 何时用 |
|---|---|---|
| **本技能** | **逐步操作 + 182 条失败模式 + CSWA/CSWP** | 照书做、卡住、报错 |
| `solidworks-surface-advanced` | **曲面原理与判据**（C0/C1/C2、复杂接合、破面修补、主模型） | 做自由曲面、判断质量 |
| `solidworks-2025-mechanical` | **2025 版全模块** + 曲面命令参数 + 钣金/焊件/线路/公差 | 查参数、用新模块 |

- `design-methodology-liuguanzong`（柳冠中《设计方法论》）：回答"该不该做这个产品"；本技能回答"这个产品怎么在 SOLIDWORKS 里造出来"。
- `ergonomics-ding-yulan`（丁玉兰《人机工程学》）：涉及人机尺寸与操作空间时配合使用；本技能只负责把它落成模型。
- `product-design-styling-dabbs` / `design-elements-hannah`：造型语言与形态推敲；本技能负责把造型落成可加工的特征树。
