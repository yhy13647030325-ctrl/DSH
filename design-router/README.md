# 设计技能自动路由机制

## 要解决的问题

本工作区装了 10 个产品设计领域知识库，但它们的 `description` 里**都含"产品设计/工业设计"**。
模型看到技能目录时无法判断该调哪个，导致三种失败：

1. 只调一个（通常是最先命中的），漏掉其他关键判据
2. 干脆不调，凭常识答——给不出书里的具体数值
3. 调错领域（问结构却调了造型）

---

## 技术约束：DSH 没有关键词硬触发

实测结论（2026-11-11，检查 DSH app.asar）：

| 检查项 | 结果 |
|---|---|
| `autoLoad` | 3 处，全是 UI 滚动加载，与技能无关 |
| `autoTrigger` / `triggerKeywords` | **0 处** |
| 技能进入模型的机制 | `agent/pre-step` 时把技能目录快照注入 system prompt |
| 模型如何选择技能 | 读 `description` 自行判断，调 `skill` 工具 |

**所以不存在"输入某个词就自动加载"的内置机制。** 能做的是让系统提示里明确写入路由约定。

---

## 三层实现

### 第一层：`design-router` 技能本体

路径：`D:\deepseek 工作\.dsh\skills\design-router\SKILL.md`

内容：
- **路由表**：10 个领域 × 触发词 × 对应技能
- **组合表**：5 个高频场景的多技能联动方案
- **边界**：明确排除 UI/海报/视频/法律，只管实体产品

`description` 里塞满了触发词，确保它排在目录前列且容易被命中：

```
当用户提到"产品设计""工业设计""造型""结构设计""外观设计""人机""注塑"
"设计一个产品""做产品""设计方法论""视觉动力""设计心理学""设计元素""设计史"
等任何设计相关词时，先调用本技能
```

### 第二层：`AGENTS.md` 项目约定

路径：`D:\deepseek 工作\.dsh\AGENTS.md`

追加了一节「设计类请求先走 design-router」，明确写：

> 只要用户提到产品设计、工业设计、造型、结构、外观、人机、注塑、设计方法、
> 视觉动力、设计心理学、设计元素、设计史等任何设计相关词，
> **先调用 `skill` 工具加载 `design-router`**，由它按问题性质分派到对应领域技能。

`AGENTS.md` 会随项目文件变更自动注入系统提示（已验证：修改后立即生效）。

### 第三层：补齐缺失的触发词

`product-injection-defects` 原本的 description 只有注塑缺陷词，**不含"产品设计"**。
已补为：

```
做产品设计、工业设计、注塑件结构设计、模具评审时调用；当注塑件出现...
```

---

## 验证结果

### 技能目录已刷新

```
- `design-router`: 产品设计 / 工业设计 请求的统一入口路由器...
```

排在 `design-elements-hannah` 之前。

### 路由目标全部存在

10 个目标技能逐一验证，缺失 **0** 个：

| 技能 | 大小 | 行数 |
|---|---|---|
| design-elements-hannah | 9.8 KB | 134 |
| design-methodology-liuguanzong | 14.2 KB | 199 |
| design-psychology-norman | 9.9 KB | 152 |
| ergonomics-ding-yulan | 11.2 KB | 153 |
| product-design-styling-dabbs | 12.1 KB | 195 |
| visual-dynamics-industrial-design | 15.6 KB | 178 |
| product-structure-liubaoshun | 8.9 KB | 152 |
| product-injection-defects | 8.6 KB | 141 |
| ori-ai-product-design | 19.5 KB | 522 |
| world-modern-design-history | 20 KB | 228 |

全部有实质内容，不是空壳。

### 路由器可正常加载

实测 `skill` 工具加载 `design-router` 返回完整内容，路由表、组合表、边界规则齐全。

---

## 使用效果

用户说"产品设计"这类词时，预期行为：

1. 模型读 `AGENTS.md` 看到约定 → 调用 `design-router`
2. 路由器判断问题实质 → 加载 1~3 个领域技能
3. 回答中标注依据来自哪本书

例如问"帮我设计一个宠物用品"：

```
design-methodology-liuguanzong  → 先定做什么（事理学、外部因素分析）
product-design-styling-dabbs    → 再定长什么样（视觉主题、比例、材质）
product-structure-liubaoshun    → 再定怎么造（壁厚、拔模、卡扣）
```

而不路由时，通常只覆盖 1 个领域，且给不出具体数值。

---

## 局限与说明

**这不是硬触发的。** 依赖模型的判断，会有偶然遗漏。

如果要**真正强制**，需要 DSH 支持 hook 拦截 `agent/pre-step` 并注入技能内容。
本机未安装 `@deepseek-ai/dsh-hooks-claude-code` 桥接插件，且该插件需要
Claude Code 的 `hooks.json` 格式。安装并配置它能做到强制注入，但那需要额外的
插件安装与格式适配，不在本次范围内。

**当前的可靠性来源**：`AGENTS.md` 会随文件变更自动重新注入系统提示（本次修改已被
系统确认"Updated instructions from: .dsh\AGENTS.md"），这比只靠技能目录的
description 更硬——因为它是明确的行为指令，不是候选列表。

---

## 维护

### 新增设计技能时

1. 在 `design-router/SKILL.md` 的路由表里加一行
2. 确保新技能的 `description` 含"产品设计"或"工业设计"

### 路由不准时

改 `design-router/SKILL.md` 的路由表，把触发词写得更贴近实际问法。
不需要重启，技能文件改动后目录会在下一轮 `agent/pre-step` 自动刷新
（本次实测：新建技能后目录立即出现）。

---

## 文件清单

| 文件 | 作用 |
|---|---|
| `.dsh/skills/design-router/SKILL.md` | 路由器本体 |
| `.dsh/AGENTS.md` | 项目约定（含设计路由约定） |
| `.dsh/skills/*/SKILL.md` | 13 个领域知识库 |

---

## 更新记录

### 2026-11-16：接入 SOLIDWORKS 三本（10 → 13）

**背景**：三本 SW 技能（实战 / 曲面 / 2025 版）此前未接入路由表，
用户问曲面或钣金时可能被引到错误的一本。

**新增内容**：

| 新增 | 位置 |
|---|---|
| **表 1.1 SOLIDWORKS 三本分工** | SKILL.md §1.1 |
| **三条硬判据**（曲面 3,993 / 钣金 555 / 认证 34 独占） | §1.1 |
| **两个容易查反的**（渲染 eDrawings → 实战；公差分析 → 实战 §6.4c + 2025 §14.1） | §1.1 |
| **表 2.1 SW 三本联动**（4 个场景） | §2.1 |
| **边界补充**：SW API 问题走 `solidworks-api-traps` | §4 |

**依据**：三本 SW 的重叠与缺口盘点（`references/OVERLAP-SOLIDWORKS-3-NEW.md`）实测词频。

**关键结论**：三本不是"三份重复资料"，是**三种组织逻辑**——
同主题章节的「完全相同的行 = 0 条」，各有独占内容。
所以路由表必须**按"你要什么"选，不是按"哪个更全"选**。

| 问题 | 唯一答案 | 实测依据 |
|---|---|---|
| 曲面怎么接顺 | `solidworks-surface-advanced` | 曲面 3,993 次（占三本 91%） |
| 钣金/焊件/Routing/公差分析 | `solidworks-2025-mechanical` | 钣金 555 次（占 81%） |
| 要考 CSWA/CSWP | `solidworks-practice` ch99 | 认证 34 次（另两本 0，100% 独占） |

