# 13 个 walkthrough（项目型章节）原文可用性核对表

> **核对日期**：2026-11-16
> **核对范围**：工作区内所有含 `chapters/` 的技能（13 个）
> **用途**：确认每个 walkthrough 的**原文是否可用**，以及**已蒸馏体量与原文的覆盖关系**

---

## 一、总表（13 个技能 / 141 章）

| # | 技能 | 章 | 现有字符 | 判据 | **原文可用性** | **源文字符** | 覆盖/转化 |
|---|---|---|---|---|---|---|---|
| **1** | **solidworks-practice** | 13 | **302,189** | **629** | **✅ 有文本层** | 306,983 | **98%** |
| **2** | **solidworks-surface-advanced** | 7 | **405,789** | **495** | **✅ 有文本层** | 330,578 | **123%** |
| **3** | **solidworks-2025-mechanical** | 14 | **475,272** | **544** | **✅ 有文本层** | 446,509 | **106%** |
| **4** | **blender-hard-surface** | 12 | **178,832** | **516** | **✅ MOBI 自解密** | 212,134 | 84% |
| **5** | **blender-manual-reference** | 18 | **257,918** | **795** | **✅ EPUB 文本层** | **3,408,863** | 7.6% |
| **6** | **product-injection-defects** | 7 | **203,946** | **357** | **✅ 视觉读图**（228 页纯扫描） | — | — |
| **7** | **world-modern-design-history** | 11 | **179,847** | **485** | **✅ EPUB 文本层** | 833,939 | 22% |
| **8** | **ergonomics-ding-yulan** | 12 | **55,956** | **0** | **✅ 有文本层** | 198,970 | 28% |
| **9** | **product-design-styling-dabbs** | 12 | **37,488** | **0** | **⚠ 自带 OCR 质量差** | 62,629（不可用） | — |
| **10** | **design-elements-hannah** | 6 | **19,380** | **0** | **✅ 已 OCR**（165 页） | 72,801 | 27% |
| **11** | **design-psychology-norman** | 7 | **24,097** | **0** | **✅ OCR 进行中 130/244 页** | 89,619（部分） | 27% |
| **12** | **product-structure-liubaoshun** | 8 | **208,343** | **0** | **❌ 纯扫描，待 OCR** | 0 | — |
| **13** | **visual-dynamics-industrial-design** | 14 | **57,527** | **0** | **❌ 纯扫描，待 OCR** | 0 | — |
| **合计** | — | **141** | **2,406,584** | **3,821** | — | — | — |

---

## 二、按"原文可用性"分类

### 2.1 ✅ 完全可用（7 个）

| 技能 | 原文形态 | 说明 |
|---|---|---|
| **solidworks-practice** | PDF 文本层 | `_re2/txt/sw-practice.txt` 306,983 字符 |
| **solidworks-surface-advanced** | PDF 文本层 | `sw-surface.txt` 330,578 |
| **solidworks-2025-mechanical** | PDF 文本层 | `sw-2025.txt` 446,509 |
| **blender-hard-surface** | **MOBI（自解密）** | PalmDB + PalmDOC LZ77 → 212,134 |
| **blender-manual-reference** | **EPUB 文本层** | 3,408,863 字符（**全书最大源文**） |
| **world-modern-design-history** | **EPUB 文本层** | 833,939 字符 / 530,850 汉字 |
| **ergonomics-ding-yulan** | PDF 文本层 | 198,970 字符 / 147,141 汉字 |

### 2.2 ✅ 已 OCR 可用（2 个）

| 技能 | OCR 状态 | 产出 |
|---|---|---|
| **design-elements-hannah** | **✅ 165/165 页完成** | 72,801 字符 / **55,045 汉字** |
| **design-psychology-norman** | **⏳ 130/244 页**（进行中） | 89,619 字符 / 73,629 汉字（部分） |

### 2.3 ⚠ 特殊处理（1 个）

| 技能 | 情况 | 处理 |
|---|---|---|
| **product-injection-defects** | **228 页纯扫描，无文本层** | **✅ 已用"逐页视觉读图"完成**（非 OCR 转写），7 章 / 203,946 字符 / 357 判据 |

### 2.4 ❌ 待处理（3 个）

| 技能 | 问题 | 原文量 |
|---|---|---|
| **product-design-styling-dabbs** | **自带 OCR 质量极差**（错字如"轮阶1和1.9廿甘证橄租眙地"），不能用于提炼判据 | 62,629 字符（不可用） |
| **product-structure-liubaoshun** | **纯扫描，无 OCR** | PDF 11,179,060 字节 / 139 页 |
| **visual-dynamics-industrial-design** | **纯扫描，无 OCR** | PDF 104,247,198 字节 / 194 页 |

---

## 三、按"是否已深度蒸馏"分类

### 3.1 ✅ 已深度蒸馏（10 章风格 + 判据表）

| 技能 | 章 | 判据 | 状态 |
|---|---|---|---|
| **solidworks-practice** | **13/13** | **629** | ✅ 完成 |
| **solidworks-surface-advanced** | **7/7** | **495** | ✅ 完成 |
| **solidworks-2025-mechanical** | **14/14** | **544** | ✅ 完成 |
| **blender-hard-surface** | **12/12** | **516** | ✅ 完成 |
| **blender-manual-reference** | **18/18** | **795** | ✅ 完成 |
| **product-injection-defects** | **7/7** | **357** | ✅ 完成 |
| **world-modern-design-history** | **7/11** | **485** | **⏳ 4 章待做**（ch08–ch11） |

**合计：78 章已深蒸 / 3,336 判据**（其中 history 贡献 7 章 / 485 条）

### 3.2 ⏳ 未深蒸（6 个，共 63 章）

| 技能 | 章 | 现判据 | 现状 |
|---|---|---|---|
| ergonomics-ding-yulan | 12 | 0 | **8 段模板**（已切分 12 章源文 188,454 字符） |
| product-design-styling-dabbs | 12 | 0 | 8 段模板（源文需重 OCR） |
| design-elements-hannah | 6 | 0 | 8 段模板（**源文已切分 6 章 56,911 字符**） |
| design-psychology-norman | 7 | 0 | 8 段模板（OCR 进行中） |
| product-structure-liubaoshun | 8 | 0 | 8 段模板（**源文缺失**） |
| visual-dynamics-industrial-design | 14 | 0 | 8 段模板（**源文缺失**） |

---

## 四、关键的"原文-技能"对应关系（可核查）

### 4.1 源文文件位置

| 技能 | 源文路径 | 大小 |
|---|---|---|
| solidworks-practice | `_re2/txt/sw-practice.txt` | 306,983 |
| solidworks-surface-advanced | `_re2/txt/sw-surface.txt` | 330,578 |
| solidworks-2025-mechanical | `_re2/txt/sw-2025.txt` | 446,509 |
| blender-hard-surface | `_re4/txt/blender-incredible.txt` | 212,134 |
| blender-manual-reference | `_re4/txt/blender-manual.txt` | 3,408,863 |
| world-modern-design-history | `_re4/txt/design/history.txt` + `history/` 11 章 | 833,939 / 732,952 |
| ergonomics-ding-yulan | `_re4/txt/design/ergonomics.txt` + `ergonomics/` 12 章 | 198,970 / 188,454 |
| design-elements-hannah | `_re4/txt/design/elements_ocr.txt` + `elements/` 6 章 | 72,801 / 56,911 |
| design-psychology-norman | `_re4/txt/design/psychology_ocr.txt`（进行中） | 89,619 |
| product-design-styling-dabbs | `_re4/txt/design/styling.txt`（**质量差**） | 62,629 |
| product-structure-liubaoshun | **无** | — |
| visual-dynamics-industrial-design | **无** | — |
| product-injection-defects | **无 txt**（视觉读图直接产出） | — |

### 4.2 原始文件位置（`下载/`）

| 技能 | 原始文件 | 大小 |
|---|---|---|
| solidworks-practice | `SolidWorks实战教程….pdf` | 88,633,895 |
| solidworks-surface-advanced | `SOLIDWORKS®高级曲面教程（2017版）….pdf` | 82,082,145 |
| solidworks-2025-mechanical | `SOLIDWORKS 2025中文版机械设计…pdf` | 53,461,002 |
| blender-hard-surface | `Blender 3D Incredible Models….mobi` | 47,072,356 |
| blender-manual-reference | `Blender 2.92 Manual….epub` | 170,302,416 |
| world-modern-design-history | `世界现代设计史（第二版）-王受之.epub` | 1,154,353 |
| ergonomics-ding-yulan | `人机工程学 (丁玉兰)….pdf` | 28,252,867 |
| design-elements-hannah | `设计元素 罗伊娜…pdf` | 33,063,340 |
| design-psychology-norman | `[设计心理学].(美)唐纳德·A·诺曼.扫描版.pdf` | 11,657,561 |
| product-design-styling-dabbs | `产品设计造型…pdf` | 36,912,985 |
| product-structure-liubaoshun | `…产品结构设计…pdf` | 11,179,060 |
| visual-dynamics-industrial-design | `工业产品设计中的视觉动力 第2版…pdf` | 104,247,198 |
| product-injection-defects | `精密注塑工艺与产品缺陷解决方案100例…pdf` | 15,123,421 |

> **★★★★★ 结论：13 个技能的原始文件全部在 `下载/` 里，一个都不缺。**
> **★ 问题只在"文本提取"环节（扫描件需 OCR）。**

---

## 五、待办清单（按优先级）

### P0：源文已就绪，可直接深蒸

| # | 技能 | 章 | 源文 |
|---|---|---|---|
| **1** | **world-modern-design-history** | **4**（ch08–ch11） | **✅ 已切分 732,952 字符** |
| **2** | **ergonomics-ding-yulan** | **12** | **✅ 已切分 188,454 字符** |
| **3** | **design-elements-hannah** | **6** | **✅ 已切分 56,911 字符** |

**合计 22 章源文完全就绪。**

### P1：等 OCR 完成

| # | 技能 | 章 | 状态 |
|---|---|---|---|
| **4** | **design-psychology-norman** | 7 | **⏳ 130/244 页** |
| **5** | **product-design-styling-dabbs** | 12 | **❌ 需重 OCR**（153 页） |
| **6** | **product-structure-liubaoshun** | 8 | **❌ 未 OCR**（139 页） |
| **7** | **visual-dynamics-industrial-design** | 14 | **❌ 未 OCR**（194 页） |

**剩余 OCR：约 486 页**（按 4.2 秒/页 ≈ 34 分钟）。

---

## 六、一个重要的核对结论

> **★★★★★ 13 个 walkthrough 的原文可用性：**
>
> | 状态 | 数量 | 技能 |
> |---|---|---|
> | **✅ 完全可用** | **7** | 3 本 SOLIDWORKS + 2 本 Blender + history + ergonomics |
> | **✅ 已 OCR 可用** | **2** | elements（完成）、psychology（进行中） |
> | **✅ 特殊处理完成** | **1** | injection（视觉读图） |
> | **❌ 待 OCR** | **3** | styling（需重做）、structure、dynamics |
>
> **★ 即：10/13 已有可用的原文，3/13 待 OCR。**
> **★ 且 13 个技能的原始 PDF/EPUB/MOBI 文件全部存在（在 `下载/`），无一项丢失。**

---

## 七、数据自洽性

| 校验项 | 结果 |
|---|---|
| 13 个技能章数合计 | **141 ✓** |
| 13 个技能字符合计 | **2,406,584 ✓** |
| 13 个技能判据合计 | **3,821 ✓** |
| 已深蒸章节 | **78**（SOLIDWORKS 34 + Blender 30 + injection 7 + history 7） |
| 未深蒸章节 | **63**（ergonomics 12 + styling 12 + elements 6 + psychology 7 + structure 8 + dynamics 14 + history 4） |
| 78 + 63 | **141 ✓** |
| 原始文件齐备率 | **13/13 = 100%** |
