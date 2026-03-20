# 🎨 图解 - 3 分钟上手指南

> 从零到生成第一张信息图，只需 3 分钟

---

## 第 1 步：安装依赖（1 分钟）

```bash
# 安装 Python 依赖
pip install markdown click playwright --break-system-packages

# 安装浏览器（用于截图）
playwright install chromium
```

✅ 完成！

---

## 第 2 步：准备内容（30 秒）

创建一个 Markdown 文件 `test.md`：

```markdown
# 2026 年法律科技趋势

人工智能正在重塑法律行业。

## 核心数据
增长率：35%
市场规模：500 亿
用户数：1000 万+

## 三大趋势

### 1. AI 法律助手
智能问答、文书起草、法律检索

### 2. 合同审查自动化
风险识别、条款比对、合规检查

### 3. 虚拟法庭
在线庭审、证据展示、语音识别
```

✅ 完成！

---

## 第 3 步：生成信息图（30 秒）

```bash
# 进入技能目录
cd ~/.agents/skills/html-infographic

# 生成信息图
python3 scripts/generate.py test.md
```

**输出**:
```
🎨 生成配置:
   色系：紫蓝渐变 (科技、数据、商务报告)
   风格：现代简约 (圆角卡片、柔和阴影、留白充足)
   终端：responsive (自适应，默认方案)

✅ 信息图生成成功！
📁 项目路径：projects/2026 年法律科技趋势_20260321_062200/
📄 HTML 文件：projects/.../index.html
```

✅ 完成！

---

## 第 4 步：查看结果（30 秒）

### 方式 1: 直接打开

```bash
# macOS
open projects/你的项目/index.html

# Linux
xdg-open projects/你的项目/index.html

# Windows
start projects/你的项目/index.html
```

### 方式 2: 双击文件

在文件管理器中找到 `index.html`，双击打开。

### 方式 3: 拖入浏览器

将 `index.html` 文件拖到浏览器窗口。

✅ 完成！你看到了什么？

---

## 🎉 恭喜！你已经生成了第一张信息图！

---

## 下一步：尝试不同风格

### 换色系

```bash
# 深蓝专业（适合政府/法律）
python3 scripts/generate.py test.md --color "深蓝专业"

# 青绿清新（适合环保/教育）
python3 scripts/generate.py test.md --color "青绿清新"

# 橙红活力（适合营销/活动）
python3 scripts/generate.py test.md --color "橙红活力"
```

### 换风格

```bash
# 商务正式
python3 scripts/generate.py test.md --style "商务正式"

# 科技感
python3 scripts/generate.py test.md --style "科技感"

# 创意活泼
python3 scripts/generate.py test.md --style "创意活泼"
```

### 生成截图

```bash
# 生成手机 + 平板 + 桌面截图
cd projects/你的项目/
python3 ../../scripts/screenshot.py index.html --all-portrait

# 截图保存在 screenshots/ 目录
ls screenshots/
```

---

## 常用命令速查

```bash
# 最简单
python3 scripts/generate.py content.md

# 指定色系 + 风格
python3 scripts/generate.py content.md \
  --color "深蓝专业" \
  --style "商务正式"

# 生成截图
python3 scripts/screenshot.py projects/你的项目/index.html

# 启动本地服务（手机扫码查看）
python3 scripts/generate.py content.md --serve
```

---

## 色系选择

| 色系 | 适用场景 |
|------|----------|
| 紫蓝渐变 | 科技、数据、商务 ⭐ |
| 青绿清新 | 环保、健康、教育 |
| 橙红活力 | 营销、活动、创意 |
| 深蓝专业 | 政府、金融、法律 ⭐ |
| 极简黑白 | 高端、艺术、极简 |

---

## 风格选择

| 风格 | 特点 |
|------|------|
| 现代简约 | 圆角卡片、柔和阴影 ⭐ |
| 科技感 | 发光效果、未来感 |
| 商务正式 | 小圆角、专业稳重 ⭐ |
| 创意活泼 | 大圆角、倾斜动画 |
| 高端奢华 | 金色点缀、深度阴影 |

---

## 遇到问题？

### Q: 找不到 Python？
A: 确保已安装 Python 3.8+，运行 `python3 --version` 检查

### Q: 缺少依赖？
A: 运行 `pip install markdown click playwright --break-system-packages`

### Q: 截图失败？
A: 确保运行了 `playwright install chromium`

### Q: 如何在手机查看？
A: 使用 `--serve` 参数启动服务，然后扫码

---

## 更多文档

- **完整文档**: `SKILL.md` - 技术细节、API、模板开发
- **截图工具**: `SCREENSHOT.md` - 截图功能详解
- **GitHub**: https://github.com/seasky7/html-infographic

---

**就这么简单！开始创作你的信息图吧！** 🎨
