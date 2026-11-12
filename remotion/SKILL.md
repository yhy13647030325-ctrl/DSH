---
name: remotion
description: 用 Remotion（React 视频框架）精确控制字幕时机、画面切换与动画进场。视频是"帧号的函数"，逐帧可复现、可参数化批量渲染。当用户说"字幕什么时候出现""动画时间轴""批量出片""用代码做视频""Remotion"时启用。
version: 1.0.0
slug: remotion
displayName: Remotion · 字幕与动画时间轴
summary: 视频生产线第4环：用 React 写代码控制视频。字幕何时出现、画面何时切、动画何时进场，全部精确到帧。逐帧可复现、可参数化批量渲染。含 Compose 结构、useCurrentFrame、序列偏移等核心用法。
tags: [Remotion, 字幕, 动画, 时间轴, React视频]
license: MIT
---

# remotion · 时间与动画控制

> 工具：Remotion —— 用 React 组件生成真实 MP4 的框架。
> 定位：视频生产线的**第 4 环**。这一步决定视频是"能用"还是"好看"。

## 核心模型

**视频 = 帧号的函数。**

```
frame（帧号） → React 组件 → 画面 → 视频
```

时间轴动画的本质是 `f(t) → frame` 的纯函数，而 React 组件恰好是 `props → JSX` 的声明式映射。把 frame 作为 props 注入，组件就在每一帧自动重渲染出该时刻的画面。

## 关键 API

| API | 作用 |
|---|---|
| `Composition` | 定义一个视频：尺寸、fps、时长（帧数） |
| `Sequence` | 时间轴上的一段移位区间 |
| `useCurrentFrame()` | 当前帧号（0 起） |
| `useVideoConfig()` | `{ fps, width, height, durationInFrames }` |
| `interpolate()` | 把帧区间映射到输出值（淡入、位移、缩放） |
| `spring()` | 物理缓动（阻尼/刚度/质量可调） |

```tsx
import { AbsoluteFill, useCurrentFrame, interpolate } from 'remotion';

export const MyVideo = () => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 30], [0, 1], { extrapolateRight: 'clamp' });
  return <AbsoluteFill style={{ opacity }}>字幕内容</AbsoluteFill>;
};
```

## 渲染原理（决定了它的适用边界）

```
启动 Chrome Headless → 逐帧 React.render() + 截图 → 全部帧 + 音轨 → FFmpeg 编码
```

**推论 1**：整个 Web 平台都是你的工具箱（CSS / SVG / Canvas / WebGL / Three.js / Lottie / Tailwind 全部可用）。
**推论 2**：逐帧走浏览器渲染流水线，**渲染较慢**，适合几十秒到几分钟的短视频，**不适合实时直播**。
**推论 3**：**Remotion 底层依赖 FFmpeg** —— 第 4 环与第 5 环是硬关联，不是各自独立。

## ⚠️ 授权（最大的坑，必须先读）

**Remotion 不是开源**，是 source-available，用的不是 MIT/Apache。

| 场景 | 是否需要付费 |
|---|---|
| 个人 | 免费（可商用） |
| 非营利 | 免费 |
| **盈利公司 ≤ 3 人** | 免费 |
| **盈利公司 > 3 人** | **必须买 Company License** |

- Remotion for Creators：**$25/月/席位**
- Remotion for Automators：**$0.01/次渲染，最低 $100/月**（SaaS / 批量渲染场景）
- Enterprise：$500/月起

**常见翻车**：看到 GitHub 仓库就以为随便商用——不是。5 人公司拿它给客户出片，需要付费许可。**先算清这笔账再上。**

## 为什么用它而不是剪辑软件

| 维度 | 传统剪辑 | Remotion |
|---|---|---|
| 改一个变量 | 手动改每条 | **改一次，批量渲染 100 条** |
| 数据源变了 | 手动更新图表 | 图表自动更新 |
| 协作 | 工程文件锁死 | Git 里是 React 组件，可 PR 评审 |
| 版本管理 | 难 | 天然可版本化 |

**甜点场景**：文字动画、数据可视化、产品演示、终端录屏、功能发布、社交短片、字幕渲染。
**不擅长**：元素大量叠加、时序极复杂的场景，可能渲染不完美。

## 上手

```bash
npx create-video@latest my-video
cd my-video
npm start              # Remotion Studio 预览
npx remotion render src/index.ts MyComp out.mp4
```

Remotion 会自动管理 Chrome Headless Shell 与 FFmpeg，通常无需手动安装。

## 硬约束

1. **先确认授权** —— 商用团队 > 3 人必须先解决 License，否则违法风险。
2. **时长与帧率必须来自第 1 环的分镜** —— 时间码不得凭感觉填。
3. **复杂叠加场景要预判渲染风险** —— 先小样验证再批量。
4. **不适合实时场景** —— 逐帧渲染的本质限制。
5. 渲染结果与 FFmpeg 强耦合，环境需保证 FFmpeg 可用。

## 边界

- 本 Skill 管时间轴与动画，**不生成画面素材本身**（数字人画面来自第 3 环）。
- 不做视频主题与美术风格的决策。
- 授权与计费的最终判断以官方为准，本 Skill 只提示风险。

## 关联

- 第 1 环：`video-use`（分镜时长是时间码的唯一来源）
- 第 3 环：`heygen`
- 第 5 环：`ffmpeg`（Remotion 的编码底层）
