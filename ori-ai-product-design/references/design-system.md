# Design System 完整规范

> 从实际生产级产品原型提炼的设计系统，覆盖色彩、排版、布局、组件四大层面。
> 所有值均基于实际交付产品验证，可直接复用。

---

## 1. 色彩 Token 体系

### 1.1 基础色阶（以 Tech Blue 为例）

```css
:root {
  /* 主色阶（9级） */
  --c-primary-900: #0F172A;
  --c-primary-700: #1E40AF;
  --c-primary-500: #3B82F6;  /* 主色 */
  --c-primary-400: #60A5FA;
  --c-primary-300: #93C5FD;
  --c-primary-200: #BFDBFE;
  --c-primary-100: #DBEAFE;
  --c-primary-50:  #F0F9FF;

  /* 中性色阶（10级） */
  --c-neutral-900: #0F172A;
  --c-neutral-800: #1E293B;
  --c-neutral-700: #334155;
  --c-neutral-600: #475569;
  --c-neutral-500: #64748B;
  --c-neutral-400: #94A3B8;
  --c-neutral-300: #CBD5E1;
  --c-neutral-200: #E2E8F0;
  --c-neutral-100: #F1F5F9;
  --c-neutral-50:  #F8FAFC;

  /* 功能色 */
  --c-success: #22C55E;
  --c-error:   #EF4444;
  --c-warning: #F59E0B;
  --c-info:    #3B82F6;
}
```

### 1.2 语义映射（Light / Dark 双主题）

```css
:root {
  /* Light 主题 */
  --bg-page:       #EFF4FB;
  --bg-card:       rgba(255,255,255,0.72);
  --bg-card-hover: rgba(255,255,255,0.85);
  --bg-header:     rgba(15,23,42,0.88);
  --bg-sidebar:    rgba(255,255,255,0.6);
  --bg-input:      rgba(255,255,255,0.8);
  --bg-tag:        rgba(219,234,254,0.7);
  --bg-tag-active: var(--c-primary-500);

  --text-primary:   var(--c-neutral-900);
  --text-secondary: var(--c-neutral-600);
  --text-tertiary:  var(--c-neutral-400);
  --text-inverse:   #FFFFFF;

  --border-default: rgba(255,255,255,0.5);
  --border-focus:   var(--c-primary-500);

  --shadow-sm: 0 1px 3px rgba(15,23,42,0.04);
  --shadow-md: 0 4px 16px rgba(15,23,42,0.06);
  --shadow-lg: 0 8px 32px rgba(15,23,42,0.08);
}

[data-theme="dark"] {
  --bg-page:       #060D1B;
  --bg-card:       rgba(15,23,42,0.65);
  --bg-card-hover: rgba(30,41,59,0.8);
  --bg-header:     rgba(6,13,27,0.9);
  --bg-sidebar:    rgba(15,23,42,0.6);
  --bg-input:      rgba(30,41,59,0.7);
  --bg-tag:        rgba(59,130,246,0.12);

  --text-primary:   var(--c-neutral-100);
  --text-secondary: var(--c-neutral-400);
  --text-tertiary:  var(--c-neutral-500);

  --border-default: rgba(255,255,255,0.08);

  --shadow-sm: 0 1px 3px rgba(0,0,0,0.2);
  --shadow-md: 0 4px 16px rgba(0,0,0,0.3);
  --shadow-lg: 0 8px 32px rgba(0,0,0,0.4);
}
```

### 1.3 Glassmorphism Token

```css
:root {
  --glass-blur:    16px;
  --glass-bg:      rgba(255,255,255,0.72);
  --glass-border:  rgba(255,255,255,0.5);
  --glass-shine:   linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0) 50%);
  --glass-shadow:  0 8px 32px rgba(15,23,42,0.06), 0 1px 2px rgba(15,23,42,0.04);
}

[data-theme="dark"] {
  --glass-blur:    20px;
  --glass-bg:      rgba(15,23,42,0.65);
  --glass-border:  rgba(255,255,255,0.08);
  --glass-shine:   linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0) 50%);
  --glass-shadow:  0 8px 32px rgba(0,0,0,0.3), 0 1px 2px rgba(0,0,0,0.2);
}
```

### 1.4 可选配色方案（共6套）

| ID | 名称 | 主色 | 适用场景 | 圆角风格 |
|----|------|------|---------|---------|
| `blue` | 科技冷蓝 | #3B82F6 | 数据平台/监控 | 标准(8/10/14px) |
| `coral` | 清新珊瑚 | #FF7F6E | 情感/生活方式 | 圆润(12/14/16px) |
| `morandi` | 莫兰迪柔雾 | #9B8E8A | 高端/文化 | 标准 |
| `muji` | 日系无印 | #C4B5A5 | 极简/文档 | 紧凑(4/6/8px) |
| `red` | 中国红传统 | #DC2626 | 节庆/国潮 | 标准 |
| `report` | 商务报告 | #C4652A | 汇报/方案 | 标准 |

实现方式：`<html data-theme="light" data-palette="coral">`

---

## 2. 排版系统

### 2.1 字体栈

```css
--font-sans: -apple-system, "SF Pro Text", "PingFang SC", "Microsoft YaHei", sans-serif;
--font-mono: "SF Mono", "JetBrains Mono", "Fira Code", monospace;
```

### 2.2 字号层级

| 用途 | 字号 | 字重 | 行高 | 颜色 |
|------|------|------|------|------|
| 页面标题 | 24px | 700 | 1.3 | --text-primary |
| 卡片标题 | 16px | 600 | 1.4 | --text-primary |
| 正文 | 14px | 400 | 1.6 | --text-primary |
| 辅助文字 | 13px | 500 | 1.5 | --text-secondary |
| 标签/注释 | 12px | 500 | 1.4 | --text-tertiary |
| 微型文字 | 11px | 600 | 1.3 | --text-tertiary |
| 大数字 | 28px | 700 | 1.2 | --text-primary |
| 紧凑数字 | 22px | 700 | 1.2 | --text-primary |

### 2.3 数字排版

```css
.stat-value {
  font-variant-numeric: tabular-nums;  /* 表格对齐 */
}
```

格式化规则：
- `≥10000` → 显示"X.X万"（如 `68万`，整数时不带小数）
- `<10000` → 显示原始数字，逗号分隔（如 `8,200`）
- 百分比 → 保留一位小数（如 `+12.3%`）
- 货币 → ¥符号 + 逗号分隔（如 `¥1,200`）

---

## 3. 布局系统

### 3.1 全局布局变量

```css
--header-h: 56px;
--sidebar-w: 240px;
--radius-sm: 8px;
--radius-md: 10px;
--radius-lg: 14px;
--radius-xl: 18px;
```

### 3.2 响应式断点

| 断点 | 变化 |
|------|------|
| `>1440px` | 标准三栏 |
| `≤1200px` | 双栏网格降为单栏 |
| `≤1024px` | Sidebar隐藏，Main全宽 |
| `≤768px` | 控件纵排，图表高度缩减，卡片2列→2列保持 |

### 3.3 间距节奏（8px 栅格）

- 组件内间距：`16px` / `20px` / `24px`
- 组件间距：`12px`（紧凑）/ `16px`（标准）/ `24px`（宽松）
- 区域间距：`24px` / `32px`
- 页面边距：`32px`（桌面）/ `16px`（移动端）

---

## 4. 组件规范

### 4.1 按钮体系

| 类型 | 用途 | 样式 |
|------|------|------|
| `btn-primary` | 主操作（查询/提交/添加） | 主色填充 + 白字 + 阴影 |
| `btn-outline` | 次要操作（查看详情/追踪/导出） | 主色边框 + 主色文字 + 透明底 |
| `btn-ghost` | 三级操作（取消/更多/辅助） | 半透明底 + 玻璃边框 + 次要文字色 |

### 4.2 Tabs选中态

```css
/* 容器：白底 + 细灰边框 */
.metric-tabs {
  padding: 2px 4px;
  background: var(--bg-input);
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-default);
}

/* 选中态：文字变色 + 底部下划线指示条（不用背景填充） */
.metric-tab.active {
  color: var(--c-primary-600);
}
.metric-tab.active::after {
  content: '';
  position: absolute;
  bottom: 1px;
  left: 50%; transform: translateX(-50%);
  width: 16px; height: 2px;
  border-radius: 1px;
  background: var(--c-primary-500);
}
```

### 4.3 数据卡片

两种规格：
- **标准卡片**：`stat-card`（padding: 20px，数字28px）
- **紧凑卡片**：`stat-card-compact`（padding: 16px，数字22px，可点击切换指标）

选中态：`border-color: var(--c-primary-500); box-shadow: 0 0 0 2px rgba(59,130,246,0.12);`

### 4.4 玻璃卡片

```css
.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(var(--glass-blur));
  -webkit-backdrop-filter: blur(var(--glass-blur));
  border: 1px solid var(--glass-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--glass-shadow);
}

/* 顶部高光线（增强玻璃质感） */
.glass-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: var(--glass-shine);
  pointer-events: none;
}
```

### 4.5 表格

```css
.content-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 13px;
}
.content-table th {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  border-bottom: 1px solid var(--border-default);
}
.content-table tr:hover td {
  background: var(--bg-card-hover);
}
```

排序：列头可点击，CSS `::after` 双箭头指示器（▴▾）。

### 4.6 标签体系（语义配色）

```css
/* 按业务语义分配颜色，不用主色 */
.tag-hot    { background: rgba(239,68,68,0.1);  color: #DC2626; }  /* 高热 */
.tag-warn   { background: rgba(249,115,22,0.1); color: #EA580C; }  /* 警告 */
.tag-info   { background: rgba(59,130,246,0.1);  color: #2563EB; } /* 信息 */
.tag-muted  { background: rgba(148,163,184,0.1); color: #64748B; } /* 低优 */
.tag-purple { background: rgba(139,92,246,0.1);  color: #7C3AED; } /* 特殊 */
.tag-green  { background: rgba(34,197,94,0.1);   color: #16A34A; } /* 正向 */
.tag-pink   { background: rgba(236,72,153,0.1);  color: #DB2777; } /* 次特殊 */
```

### 4.7 涨跌色（中国市场惯例）

```css
.stat-change.up   { color: var(--c-error);   background: rgba(239,68,68,0.08); }   /* 涨=红 */
.stat-change.down { color: var(--c-success);  background: rgba(34,197,94,0.08); }   /* 跌=绿 */
```

### 4.8 动效

```css
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
--duration-fast: 150ms;
--duration-normal: 300ms;

/* 入场动画 */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* 卡片错峰入场 */
.stat-card:nth-child(2) { animation-delay: 0.05s; }
.stat-card:nth-child(3) { animation-delay: 0.1s; }
```

---

## 5. 图标规范

**绝对不使用 emoji**。全部使用 SVG inline 图标。

标准属性：
```html
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" 
     stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
```

尺寸规范：
- Header图标：20px
- Sidebar图标：18px
- 按钮内图标：14-16px
- 卡片装饰图标：48px

推荐图标源：Lucide / Feather（线性风格统一）

---

## 6. 页面背景增强

微妙的径向渐变球增强玻璃层次感：

```css
body::before {
  content: '';
  position: fixed;
  top: -20%; right: -10%;
  width: 600px; height: 600px;
  background: radial-gradient(circle, rgba(59,130,246,0.08) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
  z-index: 0;
}
```

每套配色方案的渐变球使用对应主色，透明度 5-8%。
