---
name: html-infographic
description: |
  HTML 信息图自动生成技能。支持多色系、多风格、多终端适配，可从参考图提取设计参数。
  内置模板：
- **蓝色商务风格**（默认）⭐⭐⭐ - 深蓝渐变头部、卡片顶部渐变条、文字渐变效果、悬停动画
- 会议纪要信息图（专业简洁，正式报告）
- 其他风格：现代简约/科技感/商务正式/创意活泼/高端奢华
  
  TRIGGERS - 使用此技能当用户：
  - "生成信息图" / "创建信息图"
  - "把这个做成可视化页面" / "生成 HTML 信息图"
  - "制作数据看板" / "生成报告页面"
  - 提供内容并要求生成可视化 HTML
  - "参考这张图生成" / "按这个风格做"
  - "用蓝色商务风格生成"
  
  参数：--color 色系 --device 终端 --style 风格 --template 模板名/参考图
  输出：完整 HTML 代码 + 独立项目文件夹保存
  
  **默认行为**: 当用户未指定风格时，使用蓝色商务风格（基于 2026-03-21 用户参考图设计）
---

# HTML Infographic - 专业信息图生成技能

**核心理念**: 由大模型直接生成完整 HTML，支持色系/风格/终端定制，可从参考图提取设计参数。

---

## 🎨 五大色系（--color）

### 1. 紫蓝渐变 (default)
```css
--primary: #667eea
--primary-light: #764ba2
--accent: #4facfe
--gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
```
**适用**: 科技、数据、商务报告

### 2. 青绿清新
```css
--primary: #11998e
--primary-light: #38ef7d
--accent: #0ba360
--gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%)
```
**适用**: 环保、健康、教育、成长主题

### 3. 橙红活力
```css
--primary: #f093fb
--primary-light: #f5576c
--accent: #fa709a
--gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%)
```
**适用**: 营销、活动、创意、年轻化内容

### 4. 深蓝专业
```css
--primary: #1e3c72
--primary-light: #2a5298
--accent: #4facfe
--gradient: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)
```
**适用**: 政府、金融、法律、正式报告

### 5. 极简黑白
```css
--primary: #2d3748
--primary-light: #4a5568
--accent: #718096
--gradient: linear-gradient(135deg, #2d3748 0%, #4a5568 100%)
```
**适用**: 极简主义、高端品牌、艺术展示

---

## 📱 终端适配（--device）

### mobile (手机端)
```css
/* 竖屏优先，单列布局 */
.container { max-width: 100%; padding: 20px 15px; }
.metrics-grid { grid-template-columns: 1fr; gap: 15px; }
.metric-card { padding: 20px; }
.metric-value { font-size: 2rem; }
.header h1 { font-size: 1.8rem; }
```
**特点**: 单列卡片、大字体、触摸友好

### desktop (电脑端)
```css
/* 横屏优化，多列网格 */
.container { max-width: 1200px; margin: 0 auto; }
.metrics-grid { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
.metric-card { padding: 30px; }
.metric-value { font-size: 2.5rem; }
.header h1 { font-size: 2.5rem; }
```
**特点**: 多列布局、信息密度高、鼠标交互

### responsive (响应式，default)
```css
/* 自适应，默认方案 */
.container { max-width: 1200px; margin: 0 auto; padding: 40px 20px; }
.metrics-grid { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
@media (max-width: 768px) {
  .metrics-grid { grid-template-columns: 1fr; }
  .header h1 { font-size: 1.8rem; }
}
```
**特点**: 一套代码适配所有设备

---

## 🎭 六大风格（--style）

### 0. 蓝色商务风格 (default) ⭐⭐⭐ NEW
```css
--primary-blue: #1E3A8A (深蓝主色)
--primary-light: #3B82F6 (亮蓝渐变)
--accent-cyan: #06B6D4 (青色强调)
--bg-light: #F0F9FF (浅蓝背景)
--card-white: #FFFFFF (白色卡片)
--text-dark: #1E293B (深色文字)
--text-gray: #64748B (灰色文字)
--border-radius: 12px (圆角)
--shadow: 0 4px 12px rgba(30,58,138,0.15) (阴影)
--gradient-header: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%)
--gradient-text: linear-gradient(135deg, #1E3A8A 0%, #06B6D4 100%)
--gradient-card-top: linear-gradient(90deg, #1E3A8A 0%, #06B6D4 100%)
```
**特点**: 
- 深蓝渐变头部 + 圆形装饰元素
- 卡片顶部蓝色渐变条
- 文字使用渐变色效果
- 圆角 12px，柔和阴影
- 数据卡片悬停上浮动画
- 强调卡片深蓝背景 + 青色文字
- 浅蓝渐变背景 (#F0F9FF → #E0F2FE)

**适用**: 政府报告、法律科技、商务文档、正式报告、数据图解 ⭐默认推荐  
**来源**: 基于用户参考图提取设计参数 (2026-03-21)

### 1. 会议纪要 ⭐
```css
--primary: #1E40AF (深蓝)
--secondary: #3B82F6 (亮蓝)
--accent: #F59E0B (琥珀)
.background: #F3F4F6 (浅灰页面) + #FFFFFF (白色卡片)
.border-radius: 12px
.box-shadow: 0 1px 3px rgba(0,0,0,0.1)
.header: 左对齐，底部边框分隔
.metrics: 蓝紫渐变背景卡片，白色文字
```
**特点**: 专业简洁、正式报告风格、浅灰背景 + 白色卡片、指标卡片渐变背景  
**适用**: 会议纪要、正式报告、政府/企业文档

### 2. 现代简约
```css
.border-radius: 16px
.box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1)
.font-weight: 400-700
.spacing: generous
```
**特点**: 圆角卡片、柔和阴影、留白充足、清晰易读  
**适用**: 通用场景

### 3. 科技感
```css
.border-radius: 8px
.box-shadow: 0 0 20px rgba(102,126,234,0.3)
.border: 1px solid rgba(255,255,255,0.1)
.effects: glow, gradient-border
```
**特点**: 发光效果、科技蓝、未来感、动态渐变  
**适用**: 互联网、AI、科技产品

### 4. 商务正式
```css
.border-radius: 4px
.box-shadow: 0 2px 4px rgba(0,0,0,0.1)
.border: 1px solid #e2e8f0
.font: serif/sans-serif mix
```
**特点**: 小圆角、保守阴影、边框清晰、专业稳重  
**适用**: 政府、企业、正式报告

### 5. 创意活泼
```css
.border-radius: 24px
.box-shadow: 8px 8px 0px rgba(0,0,0,0.1)
.transform: rotate(-2deg) hover
.colors: vibrant, multi-color
```
**特点**: 大圆角、硬阴影、倾斜动画、多彩配色  
**适用**: 营销、活动、创意展示

### 6. 高端奢华
```css
.border-radius: 12px
.box-shadow: 0 20px 40px rgba(0,0,0,0.2)
.border: 1px solid rgba(255,215,0,0.3)
.gradient: gold accents
```
**特点**: 金色点缀、深度阴影、精致细节、奢华感  
**适用**: 奢侈品、高端发布会

---

## 🖼️ 参考图提取（--template）

### 从图片提取设计参数

当用户提供参考图时，自动提取：

```yaml
提取参数:
  - 主色调：从背景/主视觉提取
  - 辅助色：从强调元素提取
  - 圆角大小：从卡片/按钮提取
  - 阴影强度：从投影效果提取
  - 字体风格：从文字样式推断
  - 布局结构：从元素排布分析
  - 间距比例：从元素间隔推断
```

### 提取流程

1. **分析图片** → 识别主色、辅色、强调色
2. **检测布局** → 网格类型、卡片数量、间距
3. **识别风格** → 圆角、阴影、边框、字体
4. **生成模板** → 创建 CSS 变量和样式规则
5. **应用模板** → 将提取参数应用到新 HTML

### 示例命令

```bash
# 从参考图生成
python3 scripts/generate.py content.md --template reference.png

# 指定色系 + 风格
python3 scripts/generate.py content.md --color "青绿清新" --style "现代简约"

# 指定终端
python3 scripts/generate.py content.md --device mobile
```

---

## 📋 HTML 生成模板

### 蓝色商务风格模板（默认）⭐⭐⭐

当用户选择或默认使用蓝色商务风格时，直接生成以下完整 HTML：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{标题}</title>
    <style>
        :root {
            --primary-blue: #1E3A8A;
            --primary-light: #3B82F6;
            --accent-cyan: #06B6D4;
            --bg-light: #F0F9FF;
            --card-white: #FFFFFF;
            --text-dark: #1E293B;
            --text-gray: #64748B;
            --border-radius: 12px;
            --shadow: 0 4px 12px rgba(30,58,138,0.15);
        }
        
        body {
            font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
            background: linear-gradient(180deg, #F0F9FF 0%, #E0F2FE 100%);
            padding: 20px 15px;
        }
        
        .header {
            background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
            color: white;
            padding: 45px 30px;
            text-align: center;
        }
        
        .metric-card .value {
            background: linear-gradient(135deg, #1E3A8A 0%, #06B6D4 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        @media (max-width: 768px) {
            .metrics-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>{标题}</h1>
        </header>
        <section class="metrics-grid">{指标卡片}</section>
        <main class="content">{内容章节}</main>
    </div>
</body>
</html>
```

**完整示例**: 参考 `/home/seasky7/.openclaw/workspace/output/最高检工作报告图解_蓝色商务风格.html`

### 基础结构（其他风格使用）

---

## 🎯 参数组合示例

### 示例 1: 蓝色商务风格（默认）⭐⭐⭐ NEW
```
--style "蓝色商务风格"
--device "responsive"
```
**效果**: 深蓝渐变头部 + 圆形装饰、卡片顶部渐变条、文字渐变效果、悬停动画，适合政府/法律/商务报告 ⭐默认推荐

### 示例 2: 法律科技报告
```
--color "深蓝专业"
--device "responsive"
--style "商务正式"
```
**效果**: 专业稳重，适合政府/法律场景

### 示例 3: 营销活动页
```
--color "橙红活力"
--device "mobile"
--style "创意活泼"
```
**效果**: 年轻活力，适合社交媒体传播

### 示例 4: 环保主题
```
--color "青绿清新"
--device "desktop"
--style "现代简约"
```
**效果**: 清新自然，适合教育/公益

### 示例 5: 高端发布会
```
--color "极简黑白"
--device "desktop"
--style "高端奢华"
```
**效果**: 简约奢华，适合产品发布

### 示例 6: 参考图复刻
```
--template "reference.png"
--device "responsive"
```
**效果**: 自动提取参考图设计参数

---

## ✅ 质量检查清单

生成前必须确认：

- [ ] 色系选择（5 选 1，默认紫蓝）
- [ ] 终端适配（mobile/desktop/responsive，默认 responsive）
- [ ] 风格选择（5 选 1，默认现代简约）
- [ ] 参考图提取（如有，优先使用提取参数）
- [ ] 响应式 meta 标签
- [ ] CSS 全部内联
- [ ] 无外部依赖（可选 CDN）
- [ ] 代码可直浏览器打开

---

## 📁 项目保存规范

```
projects/
└── 项目名称_YYYYMMDD_HHMMSS/
    ├── index.html        # 主页面
    ├── source.md         # 原始内容
    ├── config.json       # 配置参数（色系/风格/终端）
    └── reference.png     # 参考图（如有）
```

### config.json 示例
```json
{
  "color": "紫蓝渐变",
  "device": "responsive",
  "style": "现代简约",
  "template": null,
  "generated_at": "2026-03-20T19:15:00+08:00"
}
```

---

## 🚀 使用方法

### 方式 1: 对话生成（推荐）

**用户**:
```
请生成 HTML 信息图：
内容：[标题 + 数据 + 章节]
色系：深蓝专业
风格：商务正式
终端：响应式
```

**模型**: 直接输出完整 HTML

### 方式 2: 脚本生成（批量）

```bash
python3 scripts/generate.py content.md \
  --color "深蓝专业" \
  --style "商务正式" \
  --device "responsive" \
  --name "项目名称"
```

### 方式 3: 参考图生成

**用户**: [发送图片] + "按这个风格生成信息图"

**模型**: 
1. 分析图片提取设计参数
2. 应用参数生成 HTML
3. 保存配置到 config.json

---

## 🔧 脚本参数（备用）

```bash
usage: generate.py [-h] [--color COLOR] [--device DEVICE] [--style STYLE]
                   [--template TEMPLATE] [--output OUTPUT] [--name NAME]
                   content_or_file

参数:
  content_or_file    Markdown 内容或文件路径
  
选项:
  --color, -c        色系选择
                     可选：紫蓝渐变/青绿清新/橙红活力/深蓝专业/极简黑白
                     默认：紫蓝渐变
  
  --device, -d       终端适配
                     可选：mobile/desktop/responsive
                     默认：responsive
  
  --style, -s        风格选择
                     可选：蓝色商务风格/会议纪要/现代简约/科技感/商务正式/创意活泼/高端奢华
                     默认：蓝色商务风格 ⭐⭐⭐
  
  --template, -t     参考图路径（自动提取设计参数）
  
  --output, -o       输出目录
  
  --name, -n         项目名称
```

---

**版本**: 3.1 (蓝色商务风格默认版)  
**创建时间**: 2026-03-20  
**更新时间**: 2026-03-21 (新增蓝色商务风格为默认模板)  
**作者**: 嘟嘟 (for seasky7)
