# 无障碍标准术语表（中英对照）

> 全部英文术语与定义**均取自本地原文**，抓取 **2026-11-17**。
> 中文译名为本技能所加，仅用于检索；**判定以英文原文为准**。
> 出处缩写：`W2.x` = WCAG 2.x 原文；`EN` = EN 301 549 v3.2.1。

---

## 一、WCAG 核心术语

| 英文（原文） | 中文 | 原文定义要点 | 出处 |
|---|---|---|---|
| **success criterion** | 成功准则 | WCAG 的可测试要求单元，编号形如 `1.4.10` | W2.1 §5.1 |
| **conformance level** | 一致性级别 | A / AA / AAA 三级，**累积**（AA 含全部 A） | W2.1 §5.2.1 |
| **Level A** | A 级 | 最低一致性级别 | W2.1 §5.2.1 |
| **Level AA** | AA 级 | 全部 A + 全部 AA 条目 | W2.1 §5.2.1 |
| **Level AAA** | AAA 级 | 全部 A + AA + AAA；**不得作为整站通用政策** | W2.1 §5.2.1 |
| **normative** | 规范性 | 「required for conformance」，构成要求 | W2.1 §6 Glossary |
| **informative** | 资料性 | 「for information purposes and not required for conformance」 | W2.1 §6 Glossary |
| **NOTE** | 注 | 属**非规范**（informative），不构成要求 | W2.1 §5.1 |
| **conforming alternate version** | 合规替代版本 | 在同一语言下提供等价的全部信息与功能 | W2.1 §6 Glossary |
| **full pages** | 整页 | 一致性只针对整页；**含响应式的每个变体** | W2.1 §5.2.2 |
| **complete processes** | 完整流程 | 流程内所有页都要达到该级别 | W2.1 §5.2.3 |
| **accessibility supported** | 可访问性支持 | 经辅助技术实测互通 + 有可获取的支持该技术的用户代理 | W2.1 §6 Glossary |
| **non-interference** | 非干扰 | 四条目（1.4.2/2.1.2/2.3.1/2.2.2）对全页含第三方内容生效 | W2.1 §5.2.5 |
| **Statement of Partial Conformance** | 部分符合声明 | 仅限『第三方内容』与『语言支持缺失』两种名义 | W2.1 §5.4 / §5.5 |
| **programmatically determined** | 可程序判定的 | 由软件从作者提供的数据中确定，供不同用户代理与辅助技术呈现 | W2.1 §6 Glossary |
| **programmatically set** | 可程序设置的 | 由软件用受用户代理支持的方法设置 | W2.1 §6 Glossary |
| **assistive technology (AT)** | 辅助技术 | 与主流用户代理共同或代替其提供超出其范围的功能的软硬件 | W2.1 §6 Glossary |
| **user agent** | 用户代理 | 检索并呈现网页内容的软件（浏览器/播放器等） | W2.1 §6 Glossary |
| **essential** | 必要的 | 去掉就会根本改变信息或功能，且无法用其他合规方式达成 | W2.1 §6 Glossary |
| **mechanism** | 机制 | 达成结果的流程或技术；须满足所声称级别的全部准则 | W2.1 §6 Glossary |
| **relied upon** | 所依赖的 | 用于满足准则的技术用法；不依赖的用法须不造成干扰 | W2.1 §5.2.4/5.2.5 |
| **conformance claim** | 符合性声明 | 可选；若声明则必含五项（日期/名称版本URI/级别/范围/技术清单） | W2.1 §5.3.1 |

---

## 二、WCAG 感知与交互术语

| 英文（原文） | 中文 | 原文要点 | 出处 |
|---|---|---|---|
| **contrast ratio** | 对比度 | `(L1+0.05)/(L2+0.05)`，范围 1:1–21:1 | W2.1 §6 |
| **relative luminance** | 相对亮度 | sRGB：`L = 0.2126R + 0.7152G + 0.0722B` | W2.1 §6 |
| **large scale (text)** | 大字 | ≥18pt，或 ≥14pt 粗体，或等效 CJK 尺寸 | W2.1 §6 |
| **CSS pixel** | CSS 像素 | 「visual angle of about 0.0213 degrees」，密度无关单位 | W2.1 §6 |
| **reflow** | 重排 | 320×256 CSS px 下不需二维滚动 | W2.1 1.4.10 |
| **text spacing** | 文本间距 | 行高1.5×/段后2×/字距0.12×/词距0.16× | W2.1 1.4.12 |
| **target size** | 目标尺寸 | 指针目标的尺寸下限（24 或 44 CSS px，分两档） | W2.1 2.5.5；W2.2 2.5.8 |
| **pointer input** | 指针输入 | 可定位屏幕上特定坐标的输入（鼠标/笔/触摸） | W2.1 §6 |
| **pointer gestures** | 指针手势 | 多点或基于路径的手势 | W2.1 2.5.1 |
| **down-event / up-event** | 按下事件/抬起事件 | 指针触发刺激被按下/释放时的平台事件 | W2.1 §6 |
| **single pointer** | 单指针 | 单点触控/单击，不需多指或划路径 | W2.1 2.5.2 |
| **dragging movements** | 拖拽动作 | 需按住并移动的操作 | W2.2 2.5.7 |
| **motion actuation** | 动作致动 | 由设备运动或用户动作触发的操作 | W2.1 2.5.4 |
| **motion animation** | 动态动画 | 在状态间插入步骤以产生运动感 | W2.1 §6 |
| **character key shortcut** | 字符键快捷键 | 仅用字母/标点/数字/符号实现的快捷键 | W2.1 2.1.4 |
| **status message** | 状态消息 | 不需接收焦点即可被辅助技术呈现的变化信息 | W2.1 4.1.3 |
| **focus not obscured** | 焦点未被遮挡 | 焦点控件不被作者创建的内容整个/部分盖住 | W2.2 2.4.11 / 2.4.12 |
| **focus appearance** | 焦点外观 | ≥2 CSS px 周界面积 + ≥3:1 对比 | W2.2 2.4.13 |
| **cognitive function test** | 认知功能测试 | 如记密码、解谜题等对认知能力的要求 | W2.2 3.3.8 |
| **redundant entry** | 重复录入 | 同流程内再次要求填写已提供的信息 | W2.2 3.3.7 |
| **consistent help** | 一致的帮助 | 帮助机制在多页间保持相对顺序一致 | W2.2 3.2.6 |

---

## 三、EN 301 549 术语

| 英文（原文） | 中文 | 原文要点 | 出处 |
|---|---|---|---|
| **ICT** | 信息通信技术 | 产品与服务的总称，含硬件、软件、web 与非 web | EN §1 |
| **functional performance statement** | 功能性能陈述 | 第 4.2 章的 11 条，用『使用者的能力』描述产品应达到什么 | EN §4.2 |
| **self-scoping** | 自作用式 | 条款以 `Where ICT <pre condition>` 开头，前置条件不成则不适用 | EN §14 |
| **closed functionality** | 封闭功能 | 用户不能自行安装软件/外设以访问该功能 | EN §5.1 |
| **operable parts** | 操作件 | 需被操作以实现功能的部件 | EN §5.5 |
| **tactilely discernible** | 可触知区分 | 不看即可分辨的做法（标准给出的一种实现方式） | EN §5.5.2 NOTE |
| **locking or toggle control** | 锁定/切换控制 | 只有 2–3 个状态且使用时保持状态的控件 | EN §5.6 |
| **stationary ICT** | 固定式 ICT | 可置于建成环境中的 ICT（自助机、信息亭、机舱等） | EN §8.3.0 |
| **forward reach** | 向前触及 | 无遮挡时操作件的高度上下限 | EN §8.3.2 |
| **side reach** | 侧向触及 | 侧向接近时的可达范围 | EN §8.3.3 |
| **magnetic coupling** | 磁耦合 | 助听器 T 线圈用的感应耦合（T-coil） | EN §8.2.2 |
| **presumption of conformity** | 推定符合 | 符合协调标准即推定符合指令基本要求 | EN Annex A |
| **harmonised standard** | 协调标准 | 由标准化请求授权制定、可推定符合指令的标准 | EN Annex A |
| **conformance** | 一致性/符合性 | 满足全部适用要求（含 `shall` 的条款） | EN §14 |
| **not applicable** | 不适用 | 前置条件为假时的测试结果（≠失败） | EN §14 |
| **not testable** | 不可测 | 例外情形下的第四种测试结果 | EN §14 |

---

## 四、各标准与机构缩写

| 缩写 | 全称 | 说明 |
|---|---|---|
| **WCAG** | Web Content Accessibility Guidelines | W3C 发布的网页内容无障碍指南 |
| **W3C** | World Wide Web Consortium | 万维网联盟，WCAG 的发布方 |
| **WAI** | Web Accessibility Initiative | W3C 的无障碍倡议（Understanding/Techniques 文档的出处） |
| **AGWG** | Accessibility Guidelines Working Group | W3C 中负责 WCAG 的工作组 |
| **EN 301 549** | — | 欧洲 ICT 无障碍采购协调标准（ETSI 牵头） |
| **ETSI** | European Telecommunications Standards Institute | 欧洲电信标准化协会 |
| **CEN** | Comité Européen de Normalisation | 欧洲标准化委员会 |
| **CENELEC** | Comité Européen de Normalisation Électrotechnique | 欧洲电工标准化委员会 |
| **EN 17161** | — | 欧洲 Design for All 标准（CEN 牵头）；**本技能未取得原文** |
| **ISO 21542** | — | 建成环境无障碍与可用性（2011 版）；**本技能未取得原文** |
| **ISO/IEC 40500** | — | **与 WCAG 2.0 相同**的国际标准编号（原文明确等价） |
| **ISO/IEC Guide 71** | — | 标准中处理无障碍的指南（2014）；**未取得原文** |
| **ISO/IEC 17007** | — | 测试程序编写规范（EN 301 549 声明其测试描述符合该标准） |
| **EN 301 549 内的引用** | | |
| `[i.34]` | ISO 21542:2011 | EN 301 549 文献表中的编号 |
| `[i.35]` | ISO/IEC Guide 71:2014 | 同上 |
| `[4]` | WCAG 2.0 / ISO/IEC 40500:2012 | 规范性引用 |
| `[5]` | WCAG 2.1 (2018-06) | 规范性引用（第 9 章据此逐条转写） |
| **Section 508** | — | 美国康复法 508 条款（2017-01 修订版），尺寸与 EN 8.3.2/8.3.3 相同 |
| **Directive 2016/2102** | — | 欧盟公共部门网站与移动应用无障碍指令 |
| **GB/T 37668-2019** | — | 中国《信息技术 互联网内容无障碍可访问性技术要求与测试方法》，**推荐性、现行**；本技能只有题录 |

---

## 五、一致性级别的中文表述规范

写文档时建议用以下表述，避免歧义：

| 场景 | 推荐表述 | 避免 |
|---|---|---|
| 声称级别 | 『符合 WCAG 2.2 **Level AA**』 | 『符合 AA 标准』（未说哪一版） |
| 条目引用 | 『WCAG 2.2 **2.5.8** Target Size (Minimum)，Level AA』 | 『触控尺寸要 24』（没说来源与级别） |
| 两档并存 | 『**2.5.8（24，AA）** 与 **2.5.5（44，AAA）** 同时有效』 | 『44 已经改成 24 了』 |
| 废止条目 | 『4.1.1 在 **2.2 起废止**；若引用 2.0/2.1 仍须测』 | 『4.1.1 废了』 |
| EN 条款 | 『EN 301 549 **8.3.2.1**（shall）』 | 『EN 301 549 要求 1220 mm』（漏了 shall 与条号） |
| 建议值 | 『EN 301 549 **8.3.0** 建议 800–1100 mm（recommended）』 | 『标准要求 800–1100 mm』 |
| 未获取的标准 | 『EN 17161 存在；本技能**未取得原文**』 | 『EN 17161 规定了……』 |
| 中国标准 | 『参照 **GB/T 37668-2019**（推荐性，现行）』 | 『符合 GB/T 37668 第 X 条』 |

---

## 六、容易混用的五对概念

| 对 | 区别 |
|---|---|
| **normative / informative** | 前者构成一致性要求；后者（含 NOTE、Example、附录）不构成 |
| **shall / should** | EN 301 549 中前者是要求，后者只是推荐 —— **直接决定能不能写进采购规格** |
| **not applicable / pass** | EN 301 549 中前置条件不成立时结果记为 not applicable；WCAG 说该条目『满足』——**两者都不等于失败** |
| **conforming alternate version / supplementary content** | 前者须提供全部等价信息与功能；后者只是补充、不能用于声称符合 |
| **accessibility supported / works in my browser** | 前者要求辅助技术实测互通 + 可获取的用户代理；后者不是标准判据 |
