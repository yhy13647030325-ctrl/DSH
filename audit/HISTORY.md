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

---

## 八、第二批迁入：4 个专项校验器（2026-11-17 同日）

第一批迁了 5 个通用检查脚本（见 §一~§五）。同日把剩下 4 个项目专用校验器也迁了。

| 脚本 | 它校验什么 | 特殊依赖 |
|---|---|---|
| `check_xref.js` | 技能名交叉引用是否都指向真实技能 | 无 |
| `verify_router.js` | `design-router` 路由表结构与 19 口径 | 无 |
| `check_chapter_structure.js` | 章节六段结构齐全率 | 无 |
| `audit_cn.js` | `web-accessibility-cn` 专项（含 953 条引文回源） | **需要原文语料** `jianji-tianxia.txt` |

### 8.1 改造要点

与第一批同一套方法：

| 项 | 原版 | 现行版 |
|---|---|---|
| 仓库根 | `D:\deepseek 工作\.dsh\skills` | `path.resolve(__dirname, '..')` |
| 子技能目录 | 绝对路径 | `path.join(ROOT, 'web-accessibility-cn')` |
| 外部语料 | 写死 `_zl/txt/jianji-tianxia.txt` | `DSH_AUDIT_CORPUS` 环境变量 → 否则猜 `../../../_zl/txt/` → 都没有则跳过并退出 0 |

### 8.2 迁移中修掉的 3 个错误

| # | 错误 | 现象 | 根因 |
|---|---|---|---|
| 1 | `audit_cn.js` 引用了未定义的 `ROOT` | `ReferenceError: ROOT is not defined` | 我把 `const DIR = '<abs>/web-accessibility-cn'` 改成了 `path.join(ROOT, ...)`，但没补 `ROOT` 的定义 |
| 2 | 语料默认路径少一级 | 提示找不到 `D:\deepseek 工作\.dsh\_zl\txt\...` | `audit/` 的上一级是仓库根，再上一级是 `.dsh`，**工作区还得再上一级** —— 应为 `../../../_zl` |
| 3 | `check_xref.js` 把包名当技能名 | 报 `REPO-HYGIENE.md → archify-repository` 悬空 | `archify-repository` 是描述 npm 包改写时的字符串，不是技能引用 |

> **★ 第 3 个是典型的"检查器误报"**，修法是在匹配后加**上下文排除**：
> 若同一行含 `package.json` / `name:` / `version` / `安装改写` / `repository` 等元信息词，
> 或名字以 `-repository` 结尾，则不计为技能引用。

### 8.3 验证

9 个脚本从**仓库内新位置**逐个实跑，全部 `exit=0`：

```
full_acceptance.js           ★ ALL PASS
encoding_audit.js            BOM/U+FEFF/invalid/MIXED 全 0
check_links.js               ★ 无断链
check_numbering.js           不一致 0 处
check_fences.js              ★ 所有围栏均正常闭合
check_xref.js                ★ 交叉引用全部有效（本地 + 外部两类均已核对）
verify_router.js             ALL PASS
check_chapter_structure.js   ★ 全部 195 章结构齐全
audit_cn.js                  ★ ALL PASS ★（953/953 引文可回源，100.00%）
```

> **★ `audit_cn.js` 的语料是自动找到的**（未设环境变量，靠 `../../../_zl/txt/` 猜中）。
> 说明默认路径猜得对；换机器若猜不到，会打印提示并退出 0，不崩溃。

### 8.4 现在 audit/ 的完整构成

```
audit/
├── README.md                      用途、运行、依赖与降级
├── HISTORY.md                     本文档
├── full_acceptance.js             全库总览
├── encoding_audit.js              编码健康
├── check_links.js                 相对链接断链
├── check_numbering.js             判据编号 + 声明一致性
├── check_fences.js                代码围栏闭合
├── check_xref.js                  技能名交叉引用
├── verify_router.js               路由表结构
├── check_chapter_structure.js     章节六段结构
└── audit_cn.js                    web-accessibility-cn 专项
```

**9 个脚本，全部便携化，全部从仓库路径实跑通过。**

### 8.5 仍未迁移的

`_zl/` 下还有 **260+ 个**脚本，均为一次性过程工具（数据生成、单次排查、下载抓取），
**不建议迁移**：它们只对当时那次操作有效，无复用价值。

> **★ 数量是动态的**（迁移时会向 `_zl/_portable*/` 写中间产物），
> 想查当前值直接数目录，不要在文档里记具体数字。
