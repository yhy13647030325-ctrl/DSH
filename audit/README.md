# audit/ — 全库审计脚本

> **本目录的脚本用于校验整个 skills 仓库的结构与内容一致性。**
> 从 `D:\deepseek 工作\_zl\` 迁入（2026-11-17），已做**便携化改造**：
> 原来写死的绝对路径全部改为 `path.resolve(__dirname, '..')`，
> 换机器、换目录都能直接跑。

## 四个脚本

| 脚本 | 检查什么 | 判定 |
|---|---|---|
| `full_acceptance.js` | 全库总览：技能数 / 章节数 / 字符数 / 页码引用 / 占位符 / 未索引章节 / 页码越界 | 逐技能 PASS/FAIL |
| `encoding_audit.js` | 编码健康：首部 BOM / 杂散 U+FEFF / 非法 UTF-8 / 混用行尾 | 四项均应为 0 |
| `check_links.js` | 相对链接断链（已屏蔽行内代码与围栏代码块） | 应为 0 |
| `check_numbering.js` | 判据编号连续性 + 「共 N 条」声明与实际行数是否一致 | 均应为 0 |
| `check_fences.js` | 代码围栏是否全部闭合（未闭合会吞掉后续正文） | 未闭合应为 0 |
| `check_xref.js` | 技能名交叉引用是否都指向真实技能 | 悬空应为 0 |
| `verify_router.js` | `design-router` 路由表结构与 19 口径 | ALL PASS |
| `check_chapter_structure.js` | 章节六段结构（章节头/总纲/逐节展开/内容表/本章空白/章间连接） | 齐全率应 100% |
| `audit_cn.js` | `web-accessibility-cn` 专项：章数/索引/页码/逐字引文回源/占位符 | ALL PASS |

## 运行

```bash
node audit/full_acceptance.js
node audit/encoding_audit.js
node audit/check_links.js
node audit/check_numbering.js
node audit/check_fences.js
node audit/check_xref.js
node audit/verify_router.js
node audit/check_chapter_structure.js
node audit/audit_cn.js
```

## 依赖与降级

**三个脚本零依赖**，只需 Node.js（≥18）与内置 `fs`/`path`。

`full_acceptance.js` 的**页码越界校验**需要一个外部语料目录
（各书的抽取文本，含 `===== PAGE N =====` 标记）：

- 位置：**不在本仓库内**（语料体积大、且有版权顾虑）
- 默认猜测：`../../_zl/txt`（即仓库上两级的 `_zl/txt`）
- 可用环境变量覆盖：

```bash
# Windows PowerShell
$env:DSH_AUDIT_TXT = "D:\deepseek 工作\_zl\txt"
node audit/full_acceptance.js
```

- **语料缺失时不会崩溃**，会打印提示并**跳过页码越界校验**（页码引用显示 0，其余照常）。

## 产出文件

| 脚本 | 产出 |
|---|---|
| `encoding_audit.js` | `encoding_audit.json` |
| `check_links.js` | `broken-links.json` |
| `check_numbering.js` | `numbering-final.json` |
| `full_acceptance.js` | （无，只打印） |

产出文件写在**本目录**下，不进版本控制（见 `.gitignore` 中的 `audit/*.json`）。

## 明确不审计的范围

以下 4 个**预装技能**被 `.gitignore` 排除、由上游维护、本仓库不修改，
因此 `check_links.js` / `encoding_audit.js` 会主动跳过它们：

```
video-talkcraft/  anything2explainer/  video-shotcraft/  archify/
```

`full_acceptance.js` 仍会统计它们的规模（技能数、字符数），但不做链接与编码审计。

## 背景

这些检查的发现、误报与教训记录在：

```
design-methodology-liuguanzong/references/REPO-HYGIENE.md
```

其中值得先读的几节：

- **§七 已知的校验脚本误报**（避免把内容误判成缺陷）
- **§十一 判据编号检查的 10 版迭代**（为什么"全连续"是错误目标）
- **§十三 页码覆盖率的三次口径修正**（大面积异常 = 规则错了）
- **§十五 预装技能不该审计**（一次越界修改与 52 文件还原）
