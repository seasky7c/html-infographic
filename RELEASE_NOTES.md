# 🎨 HTML Infographic Generator v1.0

**发布日期**: 2026-03-21

---

## ✨ 核心功能

- 🎨 **5 种色系** - 紫蓝/青绿/橙红/深蓝/极简，适配不同场景
- 🎭 **5 种风格** - 现代/科技/商务/创意/奢华，随心所欲
- 📱 **3 种终端** - 手机/平板/桌面，响应式适配
- 📸 **一键截图** - 自动生成多设备预览图
- 🚀 **即时部署** - 自动启动本地服务，返回可访问网址
- 📦 **独立项目** - 每个项目独立文件夹，便于管理

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. 生成信息图

```bash
# 最简单
python3 scripts/generate.py content.md

# 指定色系和风格
python3 scripts/generate.py content.md \
  --color "深蓝专业" \
  --style "商务正式"

# 一键生成 + 截图 + 启动服务
python3 scripts/generate.py content.md --screenshot --serve
```

### 3. 查看结果

生成的项目保存在 `projects/` 目录，双击 `index.html` 即可预览。

---

## 🎨 色系选择

| 色系 | 适用场景 |
|------|----------|
| 紫蓝渐变 | 科技、数据、商务 ⭐ |
| 青绿清新 | 环保、健康、教育 |
| 橙红活力 | 营销、活动、创意 |
| 深蓝专业 | 政府、金融、法律 ⭐ |
| 极简黑白 | 高端、艺术、极简 |

---

## 🎭 风格选择

| 风格 | 特点 |
|------|------|
| 现代简约 | 圆角卡片、柔和阴影 ⭐ |
| 科技感 | 发光效果、未来感 |
| 商务正式 | 小圆角、专业稳重 ⭐ |
| 创意活泼 | 大圆角、倾斜动画 |
| 高端奢华 | 金色点缀、深度阴影 |

---

## 📸 截图功能

```bash
# 生成多设备截图（手机 + 平板 + 桌面）
python3 scripts/screenshot.py projects/你的项目/index.html --all-portrait
```

---

## 🌐 本地服务

```bash
# 启动服务（自动生成二维码）
python3 scripts/generate.py content.md --serve

# 输出:
# 🌐 本地访问：http://localhost:8080
# 📱 局域网访问：http://192.168.1.100:8080
# 📱 手机扫码查看：qrcode.png
```

---

## 📚 文档

- **README.md** - 主文档
- **QUICKSTART.md** - 3 分钟上手指南
- **SKILL.md** - 完整技术文档
- **SCREENSHOT.md** - 截图工具详解

---

## 📝 示例

```bash
# 法律科技趋势示例
python3 scripts/generate.py examples/legal-tech-trends.md

# 会议纪要示例
python3 scripts/generate.py examples/meeting-notes.md --screenshot
```

---

## 🔧 技术栈

- Python 3.8+
- markdown, click, playwright, qrcode
- MIT License

---

## 🎯 使用场景

- 📊 数据报告可视化
- 📝 会议纪要信息图
- 📱 社交媒体配图
- 💼 商务演示文稿
- 📈 运营数据看板

---

## 📖 完整文档

https://github.com/seasky7c/html-infographic#readme

---

**作者**: seasky7  
**许可**: MIT
