# 蓝色商务风格模板

**版本**: 1.0  
**创建时间**: 2026-03-21  
**来源**: 基于用户参考图提取设计参数  
**状态**: ⭐⭐⭐ 默认模板

---

## 🎨 设计参数

### 配色方案
```css
--primary-blue: #1E3A8A;      /* 深蓝主色 */
--primary-light: #3B82F6;     /* 亮蓝渐变 */
--accent-cyan: #06B6D4;       /* 青色强调 */
--bg-light: #F0F9FF;          /* 浅蓝背景 */
--card-white: #FFFFFF;        /* 白色卡片 */
--text-dark: #1E293B;         /* 深色文字 */
--text-gray: #64748B;         /* 灰色文字 */
```

### 渐变效果
```css
--gradient-header: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
--gradient-text: linear-gradient(135deg, #1E3A8A 0%, #06B6D4 100%);
--gradient-card-top: linear-gradient(90deg, #1E3A8A 0%, #06B6D4 100%);
--gradient-bg: linear-gradient(180deg, #F0F9FF 0%, #E0F2FE 100%);
```

### 样式参数
```css
--border-radius: 12px;
--shadow: 0 4px 12px rgba(30,58,138,0.15);
--shadow-hover: 0 8px 20px rgba(30,58,138,0.2);
--border: 1px solid #E2E8F0;
--transform-hover: translateY(-4px);
```

---

## 🏗️ 结构特点

### 头部
- 深蓝渐变背景 (#1E3A8A → #3B82F6)
- 圆形装饰元素（半透明白色）
- 白色文字 + 文字阴影
- 底部 1px 分隔线

### 指标卡片
- 白色背景，圆角 12px
- 顶部 4px 蓝色渐变条
- 悬停上浮 4px + 加深阴影
- 数值文字使用蓝色渐变

### 内容章节
- 左侧 4px 蓝色边框
- 悬停时向右移动 4px
- 背景浅蓝渐变

### 强调卡片
- 深蓝渐变背景
- 青色文字 (#67E8F9)
- 半透明白色背景子卡片

---

## 📱 响应式断点

```css
@media (max-width: 480px) {
    .header h1 { font-size: 1.7rem; }
    .metrics-grid { grid-template-columns: 1fr; }
    .metric-card .value { font-size: 36px; }
    .highlight-card .stats { grid-template-columns: 1fr; }
}
```

---

## 🎯 使用场景

- ✅ 政府工作报告
- ✅ 法律科技文档
- ✅ 商务数据报告
- ✅ 正式会议材料
- ✅ 数据图解

---

## 📄 参考文件

- **完整 HTML 示例**: `/home/seasky7/.openclaw/workspace/output/最高检工作报告图解_蓝色商务风格.html`
- **截图示例**: `/home/seasky7/.openclaw/workspace/output/最高检工作报告图解_蓝色商务风格.png`

---

## 🚀 使用方法

### 方式 1: 大模型直接生成（推荐）

告诉大模型：
```
请使用蓝色商务风格生成 HTML 信息图
```

大模型会直接输出完整 HTML 代码。

### 方式 2: 使用脚本（备用）

```bash
python3 scripts/generate.py content.md \
  --color "深蓝专业" \
  --style "会议纪要" \
  --device "responsive"
```

然后手动应用蓝色商务风格的 CSS 变量。

---

**更新时间**: 2026-03-21 08:20
