# 技能库分类总览

> 扫描时间：2026-11-10（**已执行停用**）| 技能总数 **24** 个
> **停用 2 个**：`hyperframes`、`beatra` → 已移至 `.dsh/skills-backup/`，可随时恢复
> 数据来源：逐个读取 `SKILL.md` 与统计全部 `.md` 字符数，非凭记忆。

---

## 一、按来源分两大类

| 类别 | 数量 | 体量 | 说明 |
|---|---|---|---|
| **A. 我们蒸馏的** | **14** | **111.7 万字 / 235 文件** | 按统一模板（chapter + references + templates）从书中提炼 |
| **B. 预装/第三方** | **10**（原 12，停用 2） | 124.8 MB | 视频、法律、Office 等，非我们制作 |

> **判据**：A 类都有 `chapters/` + `references/` + `templates/` 三件套，且 `description` 含大量中文（我们写的触发词）。
> B 类多为单文件或自带 `bin/scripts/runtime` 等运行时目录。

---

## 二、A 类：我们蒸馏的 14 个（按职能分五组）

### 第 1 组：设计思维与历史（4 个，27.9 万字）

| 技能 | 来源 | 体量 | 章数 | 回答什么 |
|---|---|---|---|---|
| `design-methodology-liuguanzong` | 柳冠中《设计方法论》 | **7.2 万**（含总索引+本总览） | — | **该不该做**、事理学、内外因、五品生命周期 |
| `world-modern-design-history` | 王受之《世界现代设计史》 | **9.8 万** | 11 | 这类产品**历史上怎么来的** |
| `design-psychology-norman` | 诺曼《设计心理学》 | 3.8 万 | 7 | 用户**怎么用、怎么用错** |
| `ergonomics-ding-yulan` | 丁玉兰《人机工程学》 | 7.1 万 | 12 | 这个**尺寸**合适吗 |

> **特点**：`design-methodology-liuguanzong` 里放着**总索引**（`references/skill-index.md`，6868 字），
> 是 14 个设计技能的路由入口。

### 第 2 组：形态与造型（3 个，16.7 万字）

| 技能 | 来源 | 体量 | 章数 | 回答什么 |
|---|---|---|---|---|
| `design-elements-hannah` | 汉娜《设计元素》 | 3.2 万 | 6 | 形体**怎么统一**（主次从属、三比例、相贯楔入） |
| `product-design-styling-dabbs` | 戴布斯《产品设计造型》 | 5.5 万 | 12 | 造型**语言**对不对（轮廓、配置图、形状四步） |
| `visual-dynamics-industrial-design` | 李想《视觉动力》 | 8.0 万 | 14 | 形态**有动感吗**（视觉动力 F、施力者/受力者） |

### 第 3 组：结构与工艺（2 个，8.7 万字）

| 技能 | 来源 | 体量 | 章数 | 回答什么 |
|---|---|---|---|---|
| `product-structure-liubaoshun` | 刘宝顺《产品结构设计》 | 15.3 万 | 6 | 结构**怎么成立**、四大工艺、密封、安全 |
| `product-injection-defects` | 李忠文《注塑缺陷 100 例》 | 3.4 万 | 1 + 索引 | 做出来**会不会有缺陷**（100 例） |

> **注意**：`product-injection-defects` 的 `chapters/` 只有 1 个（ch00-overview），
> 主体在 `references/case-index.md`（100 例索引）——**结构与其他技能不同，是刻意的**（案例型知识用索引更好查）。

### 第 4 组：SOLIDWORKS 工程 CAD（3 个，39.4 万字）

| 技能 | 来源 | 体量 | 章数 | 强项 |
|---|---|---|---|---|
| **`solidworks-practice`** | 《SolidWorks 实战教程》（三泽） | **21.1 万** | 13 | **逐步操作 + 182 条失败模式 + CSWA/CSWP** |
| `solidworks-surface-advanced` | DS 官方《高级曲面教程 2017》 | 9.7 万 | 7 | 曲面原理（C0/C1/C2、复杂接合、破面修补、主模型） |
| `solidworks-2025-mechanical` | 赵罘《2025 机械设计》 | 8.6 万 | 14 | **2025 版全模块** + 钣金/焊件/线路/公差 |

> **这本是最大的单体技能**（21.1 万字，36 文件）。
> 三者有统筹文档：`solidworks-practice/references/STANDARD.md`（含蒸馏前后对照表、口径定义、重叠矩阵）。

### 第 5 组：Blender 视觉建模（2 个，19.0 万字）

| 技能 | 来源 | 体量 | 章数 | 定位 |
|---|---|---|---|---|
| `blender-hard-surface` | Belec《Blender 3D Incredible Models》 | 9.8 万 | 12 | **怎么做一个成品**（3 个项目：步枪/飞船/坦克） |
| `blender-manual-reference` | Blender 2.92 官方手册 | 9.2 万 | 14 | **这个功能怎么用**（57 修改器 / 132 键 / 术语） |

> **两者也是互补关系**，统筹文档在 `blender-manual-reference/references/STANDARD.md`。
> 含 `version-differences.md`（2.92 ↔ 5.1 实测）与 `BEFORE-AFTER.md`（蒸馏前后对照表）。

---

## 三、B 类：预装/第三方 10 个（含依赖与适用场景）

> **已停用 2 个**（`hyperframes`、`beatra`），下表保留它们的信息以备恢复参考，但**标注为已停用**。

> **依赖列含义**：`bin`/`scripts`/`runtime` = 技能自带的执行资产（**必需**）；
> 外部工具 = 机器上需另装（ffmpeg/node/python 等）；密钥 = 需配置 API Key。

### 3.1 视频创作链（原 8 个 → 现实 6 个）

| 技能 | 用途 | 文件 | 自带依赖 | 外部依赖 | 需密钥 |
|---|---|---|---|---|---|
| **`video-creation`** | **总调度器**（`kind: orchestrator`）：路由到下面各技能之一，含 **probe 视频探针**通道。**⚠ 它的路由表仍写着已停用的 2 个**（见下） | 3 | `probe/`、`references/` | ffmpeg / node / python / playwright / npm | 有 |
| `video-talkcraft` | **口播视频**：配音 → 字级时间戳 → SHOTBOOK 分镜 → Remotion 成片 | **924** | `scripts/`、`runtime/`、`package.json` | ffmpeg / node / python / playwright / chrome / git / npm / fish | 有 |
| `video-shotcraft` | **产品宣传片**：152 张镜头配方卡 + 2.5D 运镜 + 卡点剪辑 | **864** | `scripts/` | ffmpeg / node / python / git / npm | 有 |
| `anything2explainer` | **黑底 MG 科普**：主题 → 配音字幕进度条 → Remotion 动画 | 209 | `template/`、`reference/`、`examples/` | python / npm / edge-tts | 无 |
| `voxlite` | **Vox 风格短片**：一句话 → 搜数据 → 图生视频 → ffmpeg 拼接 → 配音字幕 | 14 | `scripts/`、`references/` | ffmpeg / python / git / edge-tts / fish | 有 |
| ~~`beatra`~~ **【已停用】** | **图片/视频/音乐/语音综合创作** + 社交数据查证 | 35 | `scripts/`、`agents/`、`references/` | python | 有 |
| ~~`hyperframes`~~ **【已停用】** | **HTML 渲染视频**：合成即 HTML，`data-*` 声明时序，运行时可 seek | 3 | — | chrome / git | 有 |
| `remotion` | **React 视频框架**：视频是帧号的函数，逐帧可复现 | 3 | — | ffmpeg / chrome / git / npm | 无 |

> **★ 这 8 个不能合并**：`video-creation` 是**路由层**（不含生产能力），
> 其余 7 个是**各自独立的生产管线**，喂的输入与产出物都不同（口播/宣传片/科普/Vox/综合/HTML/React）。
> **但 7 个里有重度重叠的外部依赖**（ffmpeg、node、python、chrome 几乎每个都要）。

> **★ 停用后的连带影响（必须知道）**：
> `video-creation` 的 description 里仍列着"统一调度七个专项技能：hyperframes、remotion、video-shotcraft、anything2explainer、video-talkcraft、voxlite、beatra"。
> **其中 hyperframes 与 beatra 已停用** —— 意味着该路由表的 2 个分支现在指向不存在的技能。
>
> **影响评估**：`video-creation` 本身仍可用（其余 5 个分支正常），
> **只是用户若点名"Vox/口播/宣传片"等仍能路由；若路由到那 2 个会失败**。
> **处置决定（已与用户确认）：保持原样，不修改 `video-creation`。**
> 理由：那 2 个分支只有在被**显式点名**时才会走到，概率低；
> 而改它的 `description` 会改变触发语义（那段文字参与技能匹配），**风险大于收益**。
> **故本条为"已知且接受"的遗留项，不是遗漏。**

### 3.2 知识与工具（3 个）

| 技能 | 用途 | 文件 | 自带依赖 | 外部依赖 | 需密钥 |
|---|---|---|---|---|---|
| `book-to-skill` | **书 → 技能**：PDF/EPUB/MOBI 转结构化技能（**我们蒸馏方法的上游工具**） | 113 | `book_to_skill/`、`scripts/`、`pyproject.toml` | python / git | 有 |
| `archify` | **图表**：架构/流程/时序/ERD/类图/时间线，输出可交互 HTML | 203 | `bin/`、`scripts/`、`package.json` | node | 无 |
| `ori-ai-product-design` | **AI 产品设计**：需求 → 原型 / 数据看板 / PPT 方案 | 5 | `references/` | 无 | 无 |

### 3.3 领域知识（1 个）

| 技能 | 用途 | 文件 | 自带依赖 | 外部依赖 | 需密钥 |
|---|---|---|---|---|---|
| `civil-code-china` | **民法典**：合同效力、物权、侵权、婚姻、继承、诉讼时效等 | 14 | `scripts/`、`assets/`、`references/` | 无 | 无 |

---

## 四、处置结论与动手清单

> **先说一句重要的**：我尝试用实际调用数据支撑判断，但**取不到**——
> - `tool_stats_summary` 只有 `skill` 工具的总次数（20 次 / 30 天），**不按技能拆分**
> - 会话存档（56 个 `.zstd`，解压 372.9M 字符）**只存 text/chunk/reasoning，不存工具调用结构**
> - `dsh-skills-manager.log` 只记来源启停，不记调用
>
> **所以下面是基于"结构事实"的判断**：文件规模、跨技能引用、外部依赖、是否自包含。
> **不是基于使用频率。** 如果你有调用记录，请以记录为准。

### 4.1 明确结论：分四档

| 档 | 处置 | 技能 | 依据 |
|---|---|---|---|
| **① 必须保留** | **不动** | `remotion`、`video-creation`、`book-to-skill`、`anything2explainer`、`civil-code-china`、`ori-ai-product-design` | **被其他技能依赖**或**零成本** |
| **② 保留但瘦身** | 合并重复工具层 | `video-talkcraft`、`video-shotcraft`、`voxlite` | 三个都自带 ffmpeg+TTS 脚本，**重复** |
| **③ 可考虑停用** | 从技能库移除（可恢复） | `hyperframes`、`beatra` | 见 4.2 的逐项理由 |
| **④ 不动（B 类核心）** | — | `archify`、`video-shotcraft`、`video-talkcraft` | 唯一能产出图/片的工具 |

### 4.2 逐项理由（关键是不能删的）

**❌ 不能删 `remotion`（3 文件 / 2.8K 字符，看着最该删）**

`video-shotcraft`、`video-talkcraft`、`hyperframes` **三个技能都引用它**。
删掉会让三个技能的核心渲染路径断掉。**它小，但它是底座。**

**❌ 不能删 `video-creation`（3 文件 / 4.2K 字符）**

它是 `kind: orchestrator` 的路由层，**引用全部 7 个视频技能**。
删了就没有统一入口，用户得自己记 7 个技能名。

**❌ 不能删 `book-to-skill`（113 文件）**

**我们 14 个蒸馏技能的方法论来源**。下次蒸馏新书还要用它。

**❌ 不建议删 `anything2explainer`（209 文件）**

自包含、无跨技能依赖、无密钥需求（只用 edge-tts），**是 8 个视频技能里"最干净"的一个**。

**⚠ `hyperframes` —— 可以停用（我的推荐）**

| 事实 | 数据 |
|---|---|
| 规模 | **3 文件 / 11.3K 字符** |
| 依赖 | chrome + git + **需要 API key** |
| 功能重叠 | 与 `video-creation` 的 probe/混剪路由**功能重合** |
| 独有能力 | HTML 声明式合成，**但 `remotion` 能做同类事** |
| **注意** | **它只有 0.02 MB，停用不省空间** —— 理由是**功能已被覆盖，少一个路由分叉** |

> **代价**：如果你以后要"用 HTML 做视频"，需要重新启用。**属于可恢复操作。**

**⚠ `beatra` —— 可以停用（我的推荐）**

| 事实 | 数据 |
|---|---|
| 规模 | 35 文件 / 10.7 万字符 |
| 依赖 | python + **需要 token** |
| 独有能力 | 社交数据查证（抖音/小红书/YouTube）+ 音乐/语音生成 |
| **问题** | **完全偏离你的主业务**（设计建模 + 视频）；且依赖外部 API |
| **注意** | **它只有 0.44 MB，停用不省空间** —— 停它的理由是**减少技能位干扰**，不是省磁盘 |

> **例外**：如果你要做社交平台竞品调研，它有用。**否则是纯负担。**

**⚠ `voxlite` —— 保留，但有重复**

它和 `video-talkcraft`、`anything2explainer` 都在做"文案→成片"，**三套 ffmpeg+TTS 脚本各写一遍**。
如果三选一，**优先保 `video-talkcraft`**（能力最全，924 文件），`voxlite` 次之（风格独特）。

### 4.3 动手清单（可直接执行）

#### 第一步：停用两个（推荐，可恢复）

```powershell
# 从技能库移出（不删除，移到备份）
$B = "D:\deepseek 工作\.dsh\skills"
$BK = "D:\deepseek 工作\.dsh\skills-backup"
New-Item -ItemType Directory -Force -Path $BK | Out-Null

# 停用 hyperframes（功能已被 remotion / video-creation 覆盖）
Move-Item "$B\hyperframes" "$BK\hyperframes" -Force

# 停用 beatra（偏离主业务，依赖外部 API）
Move-Item "$B\beatra" "$BK\beatra" -Force
```

**恢复方式**：`Move-Item "$BK\hyperframes" "$B\hyperframes"`

> **注意**：`skill-catalog.md` 和 `SKILL.md` 里对这两个的引用**不需要改**——
> 它们只是说明文档，技能不在时自然无法加载。

#### 第二步：合并重复工具层（可选，工作量大）

**现状**：`video-talkcraft`、`video-shotcraft`、`voxlite` 各自带 ffmpeg 调用脚本与 TTS 逻辑。

```
建议：抽出公共层
skills/_shared/video-tools/
  ├── ffmpeg-helper.sh     ← 三处重复的拼接/转码
  ├── tts-helper.sh        ← edge-tts 调用
  └── probe-helper.sh      ← 关键帧/音轨提取
```

**但这属于"改第三方技能"，风险高**：
- 三个技能的脚本接口未必一致
- 改完要逐个回归测试
- **收益是省重复代码，不是省磁盘**（脚本只占几 KB）

> **我的建议：不做。** 除非你确实要维护这套视频链。**投入产出比不划算。**

#### 第三步：不动 A 类 14 个

理由：
- 体量小（111.7 万字全部是 markdown，**总共几百 KB**）
- **零外部依赖**（不装 ffmpeg/node，纯文本）
- 有总索引 + 总览维护，**查找成本已降到最低**
- **它们是我们真正的资产**

### 4.4 磁盘占用实测

| 技能 | 文件 | 大小 |
|---|---|---|
| `video-shotcraft` | 864 | **48.31 MB** |
| `video-talkcraft` | 924 | **34.99 MB** |
| `anything2explainer` | 209 | 22.53 MB |
| `archify` | 203 | 17.00 MB |
| `book-to-skill` | 113 | 1.73 MB |
| `beatra` | 35 | **0.44 MB** |
| `voxlite` | 14 | 0.11 MB |
| `civil-code-china` | 14 | 0.05 MB |
| `ori-ai-product-design` | 5 | 0.04 MB |
| `video-creation` | 3 | 0.03 MB |
| `hyperframes` | 3 | **0.02 MB** |
| `remotion` | 3 | 0.01 MB |
| **预装小计** | **2,390** | **125.3 MB** |
| **我们蒸馏 14 个小计** | **235** | **2.21 MB** |
| **总计** | **2,625** | **127.5 MB** |

> **★ 这张表推翻了"清小文件能省空间"的直觉**：
> - 我原本推荐停用的 `hyperframes` 只有 **0.02 MB**、`beatra` 只有 **0.44 MB**
> - **停用它们几乎不省空间**（合计 0.46 MB，占 0.4%）
> - 真正占空间的是 **`video-shotcraft` 48 MB + `video-talkcraft` 35 MB + `anything2explainer` 22 MB + `archify` 17 MB = 122 MB（96%）**
>
> **所以"清理"这件事要分清两个目的**：
> | 目的 | 该动谁 |
> |---|---|
> | **省磁盘** | 只能动那四个大户（shotcraft/talkcraft/explainer/archify），但它们是**唯一能出片/出图的工具**，删了就没了 |
> | **降心智负担**（少几个技能名干扰路由） | 动 `hyperframes` / `beatra`——**它们小，但它们是"用不上却占一个技能位"** |

## 五、按"产业流程"看 A 类 14 个的位置

```
┌─ 第 1 层：为什么做 ─────────────────────────┐
│  柳冠中（事理学）      王受之（设计史）      │
└────────────────────────────────────────────┘
                 ↓
┌─ 第 2 层：做成什么样 ───────────────────────┐
│  诺曼（可用性）        丁玉兰（人机尺寸）    │
│  汉娜（构成）  戴布斯（造型）  李想（动感）  │
└────────────────────────────────────────────┘
                 ↓
┌─ 第 3 层：怎么造出来 ───────────────────────┐
│  刘宝顺（结构）        李忠文（注塑缺陷）    │
│  ─────────────────────────────────────────  │
│  solidworks-practice      实体建模·操作      │
│  solidworks-surface-advanced  曲面·原理      │
│  solidworks-2025-mechanical   2025·全模块    │
└────────────────────────────────────────────┘
                 ↓
┌─ 第 4 层：视觉呈现（可选）──────────────────┐
│  blender-hard-surface      Blender·实战      │
│  blender-manual-reference  Blender·官方手册  │
└────────────────────────────────────────────┘
```

> **注意第 3 层与第 4 层的分野**：
> **SOLIDWORKS = 工程 CAD（要能真的造出来）；Blender = 视觉建模（要好看、用于游戏/影视/宣传）。**
> 同一个产品，两条路线都要走。

---

## 六、成熟度分级（我们的自评）

| 等级 | 技能 | 判据 |
|---|---|---|
| **A：可直接照做** | `solidworks-practice`、`blender-hard-surface`、`blender-manual-reference`、`solidworks-2025-mechanical` | 有编号步骤 + 菜单路径 + 对话框默认值 + 失败模式 |
| **B：原理清楚，操作需配 CAD** | `solidworks-surface-advanced`、`product-structure-liubaoshun` | 判据完整，部分参数依赖原书图 |
| **C：判据型，不给步骤** | 设计思维 4 个 + 形态 3 个 | 本来就是**判断工具**，不该给操作步骤 |
| **D：案例索引型** | `product-injection-defects` | 100 例靠索引查，不做线性阅读 |

> **C 级不是缺陷**：柳冠中/诺曼/汉娜这些书**本质是判断框架**，写成操作步骤反而失真。

---

## 七、已知短板（诚实标注）

| 短板 | 涉及技能 | 说明 |
|---|---|---|
| **依赖原书图** | 三个 SOLIDWORKS + 两个 Blender | 大量以图给参数处标"（需对照原书图 N）"，未臆造 |
| **依赖配套素材** | `solidworks-practice`、`blender-hard-surface` | 需随书 Lesson/项目文件才能逐像素对拍 |
| **版本滞后** | `blender-manual-reference`（2.92）、`solidworks-practice`（2014 前后） | 均有版本差异标注 |
| **覆盖缺口** | `blender-manual-reference` | 雕刻/物理/合成/蜡笔/视频剪辑**仅索引**（刻意取舍） |
| **未互联** | `product-injection-defects` 以外 13 个已进总索引 | 注塑缺陷技能未挂进总索引路由表 |

---

## 七、预装技能与我们蒸馏技能的分工

> **这两类不是"多与少"的关系，而是"手"与"脑"的关系。**

| 维度 | 预装 12 个（B 类） | 我们蒸馏的 14 个（A 类） |
|---|---|---|
| **性质** | **执行工具**——调 ffmpeg/Remotion/API 真正产出文件 | **判断框架 + 操作知识**——回答"该做什么、怎么做对" |
| **输入** | 一句话、一篇文章、一个视频文件、一张截图 | 一个决策、一个尺寸、一处接缝、一个报错 |
| **产出** | **成片 / 图表 / 文档**（可见的交付物） | **判断 + 参数 + 步骤**（喂给工具或喂给人） |
| **失效方式** | 缺 ffmpeg/密钥就跑不动 | 版本变了会过时（已有版本差异标注） |
| **维护成本** | 高（依赖环境） | 低（纯 markdown） |

### 实操分工（一句话说清）

> **先用 A 类想清楚"做成什么样、用什么参数"，再用 B 类把它变成成片。**

具体到三条常见链路：

| 你要做的事 | A 类负责（脑） | B 类负责（手） |
|---|---|---|
| **做产品宣传片** | 戴布斯定造型语言 → 李想查动势 → 刘宝顺确认能造 | **`video-shotcraft`** 出片（镜头配方 + 2.5D 运镜） |
| **做口播讲解** | 柳冠中理清"讲什么"→ 诺曼检查"是否易懂" | **`video-talkcraft`** 出片（配音→时间戳→成片） |
| **做技术图表** | 无对应（A 类不含图表法） | **`archify`**（架构/流程/时序图） |

### 不重叠的部分（各自独有）

| 只有 A 类能做 | 只有 B 类能做 |
|---|---|
| 判断"这个产品该不该做" | 真正渲染出一帧视频 |
| 给出拔模斜度 15′/30′ | 调 ffmpeg 拼接 100 个片段 |
| 从 100 个注塑案例定位缺陷 | 从一句话生成 MG 动画 |
| 判断曲面 C0/C1/C2 是否达标 | 查民法典条文 |

> **⚠ 一条容易踩的坑**：
> **B 类技能里也有"知识"**（如 `video-talkcraft` 含 108 张动效配方卡、`video-shotcraft` 含 152 张镜头卡），
> 那些是**它自己的方法论**。所以不是"B 类全是工具、A 类全是知识"——
> **准确说法是：B 类的知识服务于它自己的产出，A 类的知识服务于跨工具的设计判断。**

## 八、一句话总结

> **A 类 14 个 = 一条"从想清楚 → 做出来 → 好看"的完整产业流程知识链**（111.7 万字 / 235 文件）。
> **B 类 12 个 = 视频与办公工具链**，与设计建模知识库是两条独立线。
