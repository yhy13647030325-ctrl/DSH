# Blender 双技能统筹规范

> **本文件是 `blender-hard-surface` 与 `blender-manual-reference` 两个技能的联合总纲**。
> 两个技能**不是重复**，而是"**做**"与"**查**"的分工。
> 任何涉及 Blender 的任务，先看这里决定调哪个。

---

## 一、两个技能的分工

| | **blender-hard-surface** | **blender-manual-reference** |
|---|---|---|
| **性质** | 实战项目书（Arijan Belec，Packt 2022） | 官方参考手册（Blender 2.92 Documentation） |
| **回答** | "**怎么把一个东西做出来**" | "**这个功能到底怎么用**" |
| **组织** | 按**项目流程** | 按**功能模块** |
| **体量** | 9.7 万字 / 12 章 / 3 个项目 | 343.9 万字 / 1653 页 / 19 分区（**本技能深度提取**） |
| **强项** | 四步工作流、判据、**精确参数取值**、111 条失败模式 | **57 个修改器的完整选项**、官方定义、**边界条件与警告** |
| **弱项** | 只覆盖三个项目用到的功能（8 个修改器） | **不给项目流程**、不给经验取值 |
| **版本** | Blender 3.x 时代 | **Blender 2.92** |

### 一句话决策

> **"做东西" → hard-surface；"查功能" → manual-reference。**

---

## 二、调用决策表（按你的问题类型）

| 你的问题 | 调哪个 | 具体位置 |
|---|---|---|
| **我要做一个机械件，从哪开始？** | hard-surface | `workflow.md` 四步工作流 |
| 该拆成几个部件？父件是哪个？ | hard-surface | `workflow.md` ②③ |
| **建一个类似 FN SCAR 的枪械** | hard-surface | ch02–ch04 |
| 建载具/飞船 | hard-surface | ch05–ch06 |
| **建坦克/履带车** | hard-surface | ch07–ch12 |
| 重复细节怎么高效做？ | hard-surface | "做一级 + Array" |
| **某个修改器的全部选项含义** | **manual-reference** | `modifier-index.md` |
| **Mirror 的 Topology Mirror 是什么** | **manual-reference** | `modifier-index.md` Mirror 条目 |
| **Boolean 为什么切不出孔 / 有什么限制** | **两本都要** | hard-surface F-B3-01（处置）+ manual（Manifold 警告） |
| **Array 的 Fit Type 三种区别** | **manual-reference** | `modifier-index.md` Array 条目 |
| **57 个修改器里还有哪些能用** | **manual-reference** | `modifier-index.md` |
| **某个快捷键官方定义** | **manual-reference** | `shortcuts-official.md` |
| 同一个键在不同编辑器含义不同？ | **manual-reference** | `shortcuts-official.md`（按分区） |
| **做金属件的参数该填多少** | hard-surface | `cheatsheet.md` 26 项数值 |
| **某个术语什么意思** | **manual-reference** | `glossary.md` |
| 报错了怎么办 | **两本都要** | hard-surface `failure-modes.md` 111 条 + manual troubleshooting |
| **约束（Transformation）怎么配** | **两本都要** | hard-surface ch11（履带实例）+ manual `constraints` |

---

## 三、两本的"重叠但角度不同"清单

> 这些主题两本都有，**但一个给"怎么用"，一个给"全貌"**。

| 主题 | hard-surface 给什么 | manual-reference 给什么 |
|---|---|---|
| **Mirror** | 三个项目的用法（步枪/飞船/坦克都对半分）+ 勾 Clipping/Merge | **Topology Mirror 的原理与限制**、Bisect、Flip、Merge Threshold |
| **Array** | 导轨/格栅/履带的实际参数（±2.000、Count 6/Offset 1.41m） | **Fit Type 三种**、多 Array 叠加、局部坐标系的坑 |
| **Boolean** | 挖孔 6 步流程 + "先修法线" | **Manifold 警告**、Wireframe/X-Ray 实时看拓扑 |
| **Solidify** | 必勾 Even Thickness | 完整选项（Offset/Rim/Only Rim/材质索引） |
| **Subdivision** | 配支撑边 + 倒角的实战组合 | Levels Viewport/Render、Type（Catmull-Clark/Simple） |
| **Edge Split** | 取消 Edge Angle、勾 Sharp Edges | 完整定义与 Split Angle |
| **Shrinkwrap** | 炮塔细节 7 步 + Target Normal Project | **Wrap Method 五种全列** |
| **Curve** | 履带绕轮流程 + 调 Deform Axis | 完整定义 |
| **快捷键** | 按"做项目"的高频 12 个（加号写法） | **132 键按分区**（连字符写法） |

> **结论**：**先用 hard-surface 知道该干什么，要深挖某功能时翻 manual。**

---

## 四、统一规范（两本共同遵守）

### R1 命令/操作写全路径
```
✅ 右侧 Modifier Properties 标签 → Add Modifier → Generate → Mirror
❌ 加个 Mirror
```

### R2 参数给"官方定义 + 经验取值"两层
- **官方定义**（数值范围、含义、限制）→ **manual-reference**
- **经验取值**（做金属件该填多少）→ **hard-surface** 的 26 项数值表
- **两者都标出处**

### R3 快捷键双写法对照
| 含义 | hard-surface | manual-reference |
|---|---|---|
| 环切 | `Ctrl + R` | `Ctrl-R` |
| 沿法线缩放 | `Alt + S` | `Alt-S` |

**引用时在自己技能内保持一致**，跨技能引用时**注明写法差异**。

### R4 版本差异必须标注
- hard-surface：Blender 3.x 时代
- manual-reference：**Blender 2.92**
- **已知差异要写明**（如法线重算：2.92 手册 `Shift-N`，3.x 起 `Ctrl-N`）

### R5 不臆造
- 两本都**不给**的内容 → 标 **（书中未展开）**
- 示意图是关键载体 → 标 **（需对照原书图 N）**

---

## 五、覆盖度对照（两本合起来够不够用）

| 能力 | hard-surface | manual-reference | 合计 |
|---|---|---|---|
| **建模工作流** | ★★★ 三个项目 | ✗ | 够 |
| **修改器** | ★★ 8 个深度 | **★★★ 57 个全览** | **够** |
| **快捷键** | ★★ 12 个高频 | **★★★ 132 个按分区** | **够** |
| **材质节点** | ★★★ 边缘磨损/法线贴花 | ★★ 节点索引 | 够 |
| **渲染设置** | ★★ EEVEE + Cycles 基础 | ★★★ 完整 | 够 |
| **绑定** | ★★ 履带约束实例 | ★★★ 约束/骨骼全览 | 够 |
| **雕刻** | ✗ | ★★（未深度提取） | **partial** |
| **物理模拟** | ✗ | ★（仅索引） | **partial** |
| **合成/合成器** | ✗ | ✗ | **缺** |
| **蜡笔/视频剪辑** | ✗ | ✗（仅索引） | **缺** |
| **动画关键帧** | ✗ | ★（仅索引） | **partial** |

> **明确的缺口**：**雕刻、物理模拟细节、合成、蜡笔、视频剪辑、关键帧动画**。
> 这些**与硬表面建模关系较远**，所以本技能没深度提取；
> **若要做这些，需另找资料或查手册原文对应分区。**

---

## 六、执行顺序（接到 Blender 任务时）

```
① 判断任务类型
   ├ 建模一个机械/载具/武器 → hard-surface 四步工作流
   ├ 只查某个功能/参数 → manual-reference 直接查
   └ 混合（多数情况） → 见下

② 用 hard-surface 定"做什么、怎么拆分、走什么流程"
      ↓
③ 卡在某个功能不会用 → 翻 manual-reference 对应条目
      ↓
④ 参数不知道填多少 → 翻 hard-surface 的 26 项数值表
      ↓
⑤ 报错 → hard-surface 的 111 条失败模式 + manual 的限制说明
      ↓
⑥ 交付前 → hard-surface 的 project-plan.md 检查清单
```

---

## 七、两本的维护约定

| 规则 | 说明 |
|---|---|
| **新增知识点先判断归属** | "怎么用" → hard-surface；"是什么/全部选项" → manual-reference |
| **不重复搬** | 同一条内容只在一本里详写，另一本**引用技能名** |
| **交叉引用只写技能名** | 写 `` `blender-manual-reference` ``，**不写相对路径** |
| **manual 的深度提取范围** | 只提取与建模/材质/渲染/绑定相关的；其余留索引 |
