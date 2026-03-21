# 🎨 图解 - HTML 信息图生成器

> 让数据更美观，让信息更直观

**图解**是一个专业的 HTML 信息图生成工具，支持多色系、多风格、多终端适配，可从 Markdown 内容一键生成精美的响应式信息图。

---

## ✨ 特性

- 🎨 **6 种色系** - 蓝色商务 (默认)/紫蓝/青绿/橙红/深蓝/极简，适配不同场景
- 🎭 **7 种风格** - 蓝色商务 (默认)/会议纪要/现代/科技/商务/创意/奢华，随心所欲
- 📱 **3 种终端** - 手机/平板/桌面，响应式适配
- 📸 **一键截图** - 自动生成多设备预览图
- 🚀 **即时部署** - 自动启动本地服务，返回可访问网址
- 📦 **独立项目** - 每个项目独立文件夹，便于管理
- 🎯 **大模型直出** - 支持大模型直接生成完整 HTML，无需脚本

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install markdown click playwright
playwright install chromium
```

### 2. 生成信息图

```bash
# 最简单 - 使用默认配置（蓝色商务风格 ⭐⭐⭐）
python3 scripts/generate.py content.md

# 指定色系和风格
python3 scripts/generate.py content.md \
  --color "蓝色商务风格" \
  --style "蓝色商务风格"

# 一键生成 + 截图 + 启动服务
python3 scripts/generate.py content.md --screenshot --serve
```

**大模型直接生成**（推荐）:

直接告诉大模型：
```
请使用蓝色商务风格生成 HTML 信息图
内容：[你的 Markdown 内容]
```

大模型会直接输出完整 HTML 代码，无需运行脚本！

### 3. 查看结果

生成的项目保存在 `projects/` 目录：

```
projects/
└── 项目名称_20260321_062200/
    ├── index.html       # 主页面
    ├── source.md        # 原始内容
    ├── config.json      # 配置信息
    └── screenshots/     # 截图（可选）
```

双击 `index.html` 或在浏览器打开即可预览。

---

## 🎨 色系选择

| 色系 | 预览 | 适用场景 |
|------|------|----------|
| 紫蓝渐变 | `#667eea` → `#764ba2` | 科技、数据、商务报告 ⭐ |
| 青绿清新 | `#11998e` → `#38ef7d` | 环保、健康、教育、成长 |
| 橙红活力 | `#f093fb` → `#f5576c` | 营销、活动、创意、年轻化 |
| 深蓝专业 | `#1e3c72` → `#2a5298` | 政府、金融、法律、正式报告 ⭐ |
| 极简黑白 | `#2d3748` → `#4a5568` | 极简主义、高端品牌、艺术 |

---

## 🎭 风格选择

| 风格 | 特点 | 适用场景 |
|------|------|----------|
| 会议纪要 | 专业简洁、浅灰背景、白色卡片 | 正式报告、会议记录 ⭐默认 |
| 现代简约 | 圆角卡片、柔和阴影 | 通用场景 |
| 科技感 | 发光效果、科技蓝 | 互联网、AI、科技产品 |
| 商务正式 | 小圆角、保守阴影 | 政府、企业、正式报告 |
| 创意活泼 | 大圆角、倾斜动画 | 营销、活动、创意展示 |
| 高端奢华 | 金色点缀、深度阴影 | 奢侈品、高端发布会 |

---

## 📱 终端适配

| 模式 | 说明 | 推荐场景 |
|------|------|----------|
| responsive | 响应式，自动适配 | 通用场景 ⭐ |
| mobile | 手机竖屏优先 | 朋友圈、小红书 |
| desktop | 桌面横屏优化 | 电脑展示、打印 |

---

## 💡 使用场景

### 场景 1: 会议纪要信息图

```bash
python3 scripts/generate.py meeting_notes.md \
  --color "深蓝专业" \
  --style "商务正式" \
  --screenshot
```

### 场景 2: 数据报告可视化

```bash
python3 scripts/generate.py data_report.md \
  --color "紫蓝渐变" \
  --style "现代简约" \
  --screenshot --serve
```

### 场景 3: 营销活动页

```bash
python3 scripts/generate.py campaign.md \
  --color "橙红活力" \
  --style "创意活泼" \
  --device mobile
```

### 场景 4: 快速分享

```bash
# 生成并启动本地服务
python3 scripts/generate.py content.md --serve

# 输出：
# 🌐 本地服务已启动：http://localhost:8080
# 📱 手机扫码查看：[二维码]
```

---

## 🔧 命令行参数

```bash
python3 scripts/generate.py content.md [选项]

选项:
  --color, -c     色系选择
                  可选：紫蓝渐变/青绿清新/橙红活力/深蓝专业/极简黑白
                  默认：紫蓝渐变
  
  --style, -s     风格选择
                  可选：会议纪要/现代简约/科技感/商务正式/创意活泼/高端奢华
                  默认：会议纪要 ⭐
  
  --device, -d    终端适配
                  可选：mobile/desktop/responsive
                  默认：responsive
  
  --output, -o    输出目录
                  默认：projects/
  
  --name, -n      项目名称
                  默认：从内容标题自动生成
  
  --screenshot    生成多设备截图
  
  --serve         启动本地 HTTP 服务
  
  --port, -p      服务端口
                  默认：8080
```

---

## 📸 截图工具

单独使用截图工具：

```bash
# 生成单张截图
python3 scripts/screenshot.py projects/你的项目/index.html

# 生成多设备截图（手机 + 平板 + 桌面）
python3 scripts/screenshot.py index.html --all-portrait

# 自定义分辨率
python3 scripts/screenshot.py index.html \
  --width 900 --height 1200 --scale 2.0
```

截图保存在 `screenshots/` 目录。

---

## 📁 项目结构

```
html-infographic/
├── README.md              # 本文件
├── SKILL.md               # 完整技术文档
├── QUICKSTART.md          # 3 分钟上手指南
├── SCREENSHOT.md          # 截图工具文档
├── requirements.txt       # Python 依赖
├── scripts/
│   ├── generate.py        # 主生成脚本
│   └── screenshot.py      # 截图工具
├── templates/             # 模板库（待扩展）
├── examples/              # 示例项目
└── projects/              # 生成的项目（.gitignore）
```

---

## 🌐 本地服务部署

使用 `--serve` 参数自动启动 HTTP 服务：

```bash
python3 scripts/generate.py content.md --serve
```

**输出示例**:
```
✅ 信息图生成成功！
📁 项目路径：projects/项目名称_20260321_062200/
🌐 本地服务已启动：http://localhost:8080
📱 手机扫码查看：
   [二维码图片]

按 Ctrl+C 停止服务
```

**功能**:
- ✅ 自动启动 HTTP 服务器
- ✅ 生成二维码供手机扫码
- ✅ 支持局域网访问
- ✅ 自动打开浏览器

---

## 📖 文档

- **快速上手**: `QUICKSTART.md` - 3 分钟上手
- **完整文档**: `SKILL.md` - 技术细节、API、模板开发
- **截图工具**: `SCREENSHOT.md` - 截图功能详解

---

## 🎯 典型工作流

```bash
# 1. 准备内容（Markdown 格式）
cat > content.md << EOF
# 2026 年法律科技趋势

## 核心指标
增长率：35%
市场规模：500 亿
用户数：1000 万+

## 主要趋势
1. AI 法律助手普及
2. 智能合同审查
3. 虚拟法庭应用
EOF

# 2. 生成信息图
python3 scripts/generate.py content.md \
  --color "深蓝专业" \
  --style "商务正式" \
  --screenshot --serve

# 3. 查看结果
# - 浏览器自动打开：http://localhost:8080
# - 手机扫码查看
# - 截图保存在 screenshots/

# 4. 分享
# - 发送截图到朋友圈/微信群
# - 分享局域网链接给同事
```

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

**作者**: 嘟嘟 (for seasky7)  
**版本**: 1.0.0  
**创建时间**: 2026-03-21  
**GitHub**: https://github.com/seasky7c/html-infographic
