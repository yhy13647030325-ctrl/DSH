# audit/ 的历史：4 个脚本的来源与改造

> **归档日期**：2026-11-17
> **本文档记录**：这些脚本原来在哪、为什么迁入仓库、迁入时改了什么、如何验证等价性。
> 原始版本归档在 `_zl/_archive/audit-originals-2026-11-17/`（**仅本机，不在版本控制内**）。

---

## 一、它们原来不在仓库里

这 4 个脚本最早写在 `D:\deepseek 工作\_zl\` 下 —— 那是一个**过程脚本目录**，
存放整个蒸馏工程中用过的一次性工具（240+ 个文件），不在版本控制内。

问题很直接：**换一台机器就没有了。**

2026-11-17 把其中 4 个长期复用的检查脚本迁入本仓库。

---

## 二、不能直接搬：原版写死了绝对路径

直接复制会带来三处硬依赖：

| 项 | 原版（`_zl/`） | 现行版（`audit/`） |
|---|---|---|
| **仓库根** | 写死 `D:\deepseek 工作\.dsh\skills` | `path.resolve(__dirname, '..')` |
| **语料目录** | 写死 `D:\deepseek 工作\_zl\txt` | 环境变量 `DSH_AUDIT_TXT`，其次猜 `../../_zl/txt` |
| **产出文件** | 写回 `_zl/`（外部） | 写回 `audit/`（本目录，已 gitignore） |

改造后：

- **换机器、换目录都能直接跑**（只要脚本仍在 `<repo>/audit/`）
- 语料缺失时**不崩溃**，打印提示并跳过页码越界校验
- 产出文件跟脚本待在一起，不再散落在外部目录

---

## 三、迁移中修掉的 4 个错误

这些错误都是改造过程自己引入的，记录在此以免后来者重犯：

| # | 错误 | 现象 | 根因 |
|---|---|---|---|
| 1 | 替换时吃掉了字符串引号 | `'path.join(__dirname,...)'` 变成语法错误 | 正则把含引号的整段替换掉，又把表达式塞回引号位置 |
| 2 | `_REPO` 定义被插到 `require('path')` 之前 | `ReferenceError: Cannot access 'path' before initialization` | `const` 的**暂时性死区**（TDZ） |
| 3 | `encoding_audit` 产出路径被错改到 `<repo>/_zl/` | `ENOENT` | 替换规则把所有 `_zl` 路径都当成了同一类 |
| 4 | `full_acceptance` 在无语料时直接崩溃 | 进程退出 | 缺少 `existsSync` 守卫 |

**教训**：批量正则替换路径时，"输入路径"与"输出路径"、"本仓库文件"与"外部语料"必须分开处理。

---

## 四、等价性验证（删除旧版前做的）

归档/删除原版之前，先确认现行版能**完整替代**。方法是对同一仓库分别运行两份，比对输出：

| 脚本 | 输出是否一致 |
|---|---|
| `check_links.js` | **一致** |
| `check_numbering.js` | **一致** |
| `encoding_audit.js` | **一致** |
| `full_acceptance.js` | **一致**（均带 `DSH_AUDIT_TXT` 语料） |

比对时已归一化两类无关差异：
- 绝对路径前缀
- `wrote xxx.json` 这类提示文字

> **★ 验证的是结果，不是代码。** 两份代码行数不同（65–111 vs 69–122），
> 但只要输出的诊断结论一致，就可以替代。

---

## 五、现行用法

```bash
node audit/check_links.js
node audit/encoding_audit.js
node audit/check_numbering.js

# 带页码越界校验（需要外部语料）
# Windows PowerShell
$env:DSH_AUDIT_TXT = "D:\deepseek 工作\_zl\txt"
node audit/full_acceptance.js
```

---

## 六、未迁移的部分

`_zl/` 下还有 240+ 个脚本，**绝大多数没有迁入**，因为它们是一次性的过程脚本：

| 类型 | 例子 | 为什么不迁 |
|---|---|---|
| 单次数据生成 | `add_ch08_tables.js`、`extend_criteria_space.js` | 只对某次内容补录有效，已执行完 |
| 一次性排查 | `diag_page_offset.js`、`prove_bold_hypothesis.js` | 记录的是当时的排查思路，无复用价值 |
| 下载/抓取 | `dlchunk.js`、`lgseq.js`、`zl101.js` | 依赖外部站点与配额，不可复现 |
| 专项校验 | `check_xref.js`、`verify_router.js`、`check_chapter_structure.js`、`audit_cn.js` | **仍在使用，但尚未便携化** |

> **★ 最后一行需要说明**：`check_xref.js` / `verify_router.js` / `check_chapter_structure.js` / `audit_cn.js`
> 这 4 个项目专用校验器**还在 `_zl/` 里，仍被仓库文档引用**
> （`REPO-HYGIENE.md` 与 `REPORT-5-ACTIONS.md` 里标了"未迁移"）。
> 若将来也需要跨机器可用，应按本文档同样的方法迁移。

---

## 七、相关文档

- `audit/README.md` —— 四个脚本各自检查什么、判定标准、降级行为
- `design-methodology-liuguanzong/references/REPO-HYGIENE.md` —— 全部检查项的
  发现、误报与教训（§七 校验器误报、§十一 编号检查 10 版迭代、§十三 页码口径三次修正、§十五 预装技能不该审计）
