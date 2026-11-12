---
name: video-creation
description: "视频创作总模块：把任意输入（一段话/一篇文章/一个 PDF/一张截图/一个前端项目/一段成品配音/一个已有视频）变成成片。统一调度七个专项技能：hyperframes、remotion、video-shotcraft、anything2explainer、video-talkcraft、voxlite、beatra，新增 probe 输入分析层（输入视频也能调：探针→拆解→复刻/改编/混剪）。Use when 用户说做视频、宣传片、口播、解说、科普、动画、动态图形、片子、成片、剪辑、改编、复刻、二创，或直接扔来一个视频文件要求处理。"
user-invocable: true
metadata:
  version: "1.0.0"
  kind: "orchestrator"
---

# video-creation 视频创作总模块

一个入口，七种生产能力，一条新的输入通道（视频进 → 视频出）。

```
                    ┌─────────────────────────┐
   一句话/文章/PDF ──┤                         ├──▶ 成片
   截图/前端项目  ──┤   video-creation 路由器  │
   成品配音      ──┤                         │
   已有视频      ──┤  probe 输入分析层        │
                    └─────────────────────────┘
```

## 调用方式

| 输入 | 路由目标 |
|---|---|
| 一个**视频文件**（.mp4/.mov/.mkv/.webm…） | **probe → 复刻/改编/混剪**（本模块新增能力，见下文） |
| 一句话主题 / 一篇文章 / 一个 PDF | `anything2explainer`（MG 风格科普）或 `video-talkcraft`（口播） |
| "做口播""把文案变成视频""给配音配画面" | `video-talkcraft` |
| 前端项目 / 网页 / 要产品宣传片 | `video-shotcraft` |
| "字幕什么时候出现""动画时间轴""批量出片" | `remotion` |
| 点名 Remotion 迁移 / HTML 声明式合成 | `hyperframes` |
| "Vox 风格""剪纸拼贴""数据可视化视频""一句话出片" | `voxlite` |
| "图片+视频+音乐+语音一起做""社交数据/竞品调研" | `beatra` |

**不确定路由到哪**：先跑 `probe`，它会给出输入画像 + 推荐目标技能。

---

## 🆕 输入视频即可调用（probe 通道）

这是本模块相对七个子技能的全新能力：**用户直接扔一个视频文件进来**。

```
视频文件
  │
  ▼
probe/probe.mjs 探针
  │  ffprobe 元数据 + ffmpeg 关键帧 + 音轨分离
  ▼
输入画像 probe.json
  │  时长/分辨率/帧率/码率/场景切换点/语音转写/关键帧序列
  ▼
用户选意图
  ├─ 复刻（replicate）→ 按原片结构重制：节奏/镜头/字幕全部对齐
  ├─ 改编（adapt）     → 保留结构换内容：比如换成自己的产品/文案
  └─ 混剪（remix）     → 拆出可用片段 + 重新编排 + 加字幕/配音
```

### 用法

```bash
# 1) 探针（自动定位 ffmpeg/ffprobe，无需系统安装）
node {skill_dir}/probe/probe.mjs <视频文件> [--out 输出目录]

# 2) 读画像，向用户确认意图（复刻/改编/混剪）
# 3) 按意图分派：
#    复刻/改编 → video-shotcraft（镜头配方）或 remotion（帧级控制）
#    混剪      → hyperframes（HTML 合成）/ voxlite（关键帧再生）/ 本地 ffmpeg 直接裁切编排
```

### probe 输出什么

`probe.json` 含：
- `meta` — 时长、分辨率、帧率、码率、编码、容器
- `scenes` — 场景切换点（ffmpeg `select='gt(scene,0.4)'`）
- `keyframes` — 关键帧 JPEG 序列（每场景 1 张，供视觉分析）
- `audio` — 分离的音轨（wav），若有语音可转写
- `shots` — 推断的镜头表（起止时间 + 关键帧 + 场景分）

---

## 子技能索引（七个专项）

| 技能 | 一句话定位 | 资产规模 |
|---|---|---|
| [video-shotcraft](../video-shotcraft/SKILL.md) | 电影感产品宣传片：152 张镜头配方卡 + 已验收模板 + 2.5D 运镜 | 864 文件 |
| [video-talkcraft](../video-talkcraft/SKILL.md) | 终极口播：配音→字级时间戳→SHOTBOOK 层矩阵→Remotion 成片 | 924 文件 |
| [anything2explainer](../anything2explainer/SKILL.md) | 黑底 MG 风格科普讲解：主题→配音字幕进度条→Remotion 动画 | 209 文件 |
| [hyperframes](../hyperframes/SKILL.md) | HTML 渲染视频：合成即 HTML，`data-*` 声明时序，运行时可 seek | 3 文件 |
| [remotion](../remotion/SKILL.md) | React 视频框架逐帧精确控制：视频是帧号的函数 | 3 文件 |
| [voxlite](../voxlite/SKILL.md) | 一句话全自动出片：Vox 风格科普短视频，4 种画风可对比 | 14 文件 |
| [beatra](../beatra/SKILL.md) | 云端 AI 创作套件：图/视频/音乐/语音 + 社交数据 | 26 文件 |

**子技能怎么读**：确认路由目标后，直接读它的 `SKILL.md`（路径见上表），按它的流程走。本模块只负责"选对路"，不重复子技能的工艺细节。

---

## 运行时依赖

| 依赖 | 用途 | 状态 |
|---|---|---|
| node / npm | 全部子技能 | ✅ v24.9.0 |
| ffmpeg / ffprobe | probe 探针、混剪、voxlite 拼接/字幕/音效 | ✅ `probe/` 内自动定位（ffmpeg-static 6.0 优先） |
| libass（ffmpeg `subtitles` 滤镜） | voxlite 烧 ASS 字幕 | ✅ 随 ffmpeg-static 提供 |
| edge-tts（Python 包） | voxlite 带情绪风格自然配音 | ✅ 已装于 Python314（免 API Key） |
| 中文字体（msyhbd.ttc 等） | voxlite 中文渲染、字幕 | ✅ 系统 `C:/Windows/Fonts/` |
| Remotion | shotcraft / talkcraft / explainer / remotion | 子技能自带（`runtime/` 或模板内） |
| playwright | talkcraft 无头浏览器 | 子技能 `check-runtime.sh` 装 |
| Beatra 账号 + 积分 | beatra 云端生成（图/视频/音乐/语音/克隆） | ⚠️ 需登录；规划/查询类操作免费 |

**ffmpeg 定位顺序**：`FFMPEG_PATH` 环境变量 → `PATH` → 本机已知安装位置 → `~/.dsh/_work/ffmpeg-tool/node_modules`（ffmpeg-static 优先于 @ffmpeg-installer）。

**voxlite 自带 ffmpeg**：它默认走 `imageio-ffmpeg` 的精简构建（缺 `grain`/`vignette` 滤镜）；若要纹理层，让 voxlite 复用本模块的 ffmpeg-static 6.0 即可。

**beatra 计费边界**：创意规划、授权、上传准备、声音浏览、模型发现、公开社交搜索与查看、任务列表、积分余额/明细/估价——**全部免费**。消耗积分的只有：图片、视频、音乐、语音、声音克隆、视频提示词增强、公开社交 execute。

---

## 硬性原则

1. **先探针，后动手**——任何视频输入必须先过 probe，不要凭文件名猜内容。
2. **路由一次说清**——向用户确认"我准备用 X 技能做 Y"，再开工；不要同时开两条线。
3. **子技能权威**——工艺细节（镜头语言、动效规范、验收标准）以子技能 SKILL.md 为准，本模块不覆盖。
4. **不重复造资产**——七个子技能的模板/配方卡/图元库直接复用，不要在模块内复制一份。
5. **母版不混版本**——Remotion 工程一旦开做，中途不升级依赖（talkcraft 的教训）。

## 边界

- 不生成真人数字人（talkcraft 明确排除；人物素材是输入）。
- 不替代专业 NLE（剪映/Premiere）——本模块产出的是**代码可复现**的视频。
- 视频输入仅限本地文件；不处理流媒体 URL（probe 阶段拒绝）。
