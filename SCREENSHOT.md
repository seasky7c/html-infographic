# 📸 HTML 信息图截图工具

高质量全页面截图工具，基于 Playwright 实现，支持多种设备分辨率。

## ✨ 特性

- ✅ **完整页面截图** - 自动滚动拼接，不是视口截图
- ✅ **多设备支持** - 手机/平板/桌面多种预设
- ✅ **Retina 高清** - 支持 2x/3x 缩放因子
- ✅ **批量生成** - 一次性生成多种分辨率
- ✅ **无头模式** - 无需打开浏览器窗口
- ✅ **高质量输出** - PNG/JPEG 格式可选

## 📦 安装依赖

```bash
# 安装 Playwright
pip install playwright --break-system-packages

# 安装 Chromium 浏览器
playwright install chromium
```

## 🚀 快速开始

### 单张截图（默认桌面分辨率）

```bash
cd ~/.agents/skills/html-infographic

# 最简单用法
python3 scripts/screenshot.py projects/你的项目/index.html

# 指定输出目录
python3 scripts/screenshot.py projects/你的项目/index.html -o screenshots/

# 自定义文件名
python3 scripts/screenshot.py projects/你的项目/index.html -n 我的信息图
```

### 指定设备分辨率

```bash
# 手机竖屏（适合小红书/朋友圈）
python3 scripts/screenshot.py index.html --device mobile-portrait

# 平板竖屏
python3 scripts/screenshot.py index.html --device tablet-portrait

# 桌面 Full HD
python3 scripts/screenshot.py index.html --device desktop

# 同时生成多种设备
python3 scripts/screenshot.py index.html \
  --device mobile-portrait \
  --device tablet-portrait \
  --device desktop
```

### 批量生成所有竖屏设备（推荐）

```bash
# 一键生成手机 + 平板 + 桌面（最适合信息图）
python3 scripts/screenshot.py index.html --all-portrait
```

### 自定义分辨率

```bash
# 自定义尺寸（适合特定平台）
python3 scripts/screenshot.py index.html \
  --width 1080 \
  --height 1920 \
  --scale 2.0

# 小红书封面（3:4）
python3 scripts/screenshot.py index.html \
  --width 900 \
  --height 1200 \
  --scale 2.0
```

### 输出格式

```bash
# PNG（默认，无损）
python3 scripts/screenshot.py index.html --format png

# JPEG（文件更小，适合网络传输）
python3 scripts/screenshot.py index.html \
  --format jpeg \
  --quality 85
```

## 📱 设备预设

| 预设名 | 分辨率 | 缩放 | 适用场景 |
|--------|--------|------|----------|
| `mobile` | 390x844 | 3.0x | iPhone 15 Pro |
| `mobile-max` | 430x932 | 3.0x | iPhone 15 Pro Max |
| `mobile-portrait` | 390x1200 | 3.0x | 手机竖屏（推荐） |
| `tablet` | 834x1194 | 2.0x | iPad Pro 11 |
| `tablet-large` | 1024x1366 | 2.0x | iPad Pro 12.9 |
| `tablet-portrait` | 834x1600 | 2.0x | 平板竖屏（推荐） |
| `desktop` | 1920x1080 | 1.0x | 桌面 Full HD |
| `desktop-2k` | 2560x1440 | 1.0x | 桌面 2K |
| `desktop-4k` | 3840x2160 | 1.0x | 桌面 4K |

## 💡 常用场景

### 场景 1：生成社交媒体配图

```bash
# 小红书（3:4 竖屏）
python3 scripts/screenshot.py index.html \
  --width 900 --height 1200 --scale 2.0 \
  -n xiaohongshu_cover

# 微信朋友圈（16:9）
python3 scripts/screenshot.py index.html \
  --width 1080 --height 608 --scale 2.0 \
  -n wechat_moments
```

### 场景 2：多设备预览

```bash
# 一键生成所有设备预览图
python3 scripts/screenshot.py index.html --all
```

### 场景 3：高质量打印

```bash
# 4K 分辨率 + PNG 无损格式
python3 scripts/screenshot.py index.html \
  --device desktop-4k \
  --format png \
  -o print_ready/
```

## 🔧 高级选项

```bash
python3 scripts/screenshot.py index.html \
  --device mobile-portrait \
  --output screenshots/ \
  --name 我的信息图 \
  --format png \
  --no-full-page  # 仅截取可见区域（默认是全页面）
```

## 📊 输出示例

```
📊 截图生成完成
====================================================================================================
设备                   分辨率                  缩放       文件大小         内容尺寸                      输出路径
----------------------------------------------------------------------------------------------------
Mobile Portrait      390x1200             3.0      2241.5 KB    390x6214     screenshots/index_mobile.png
Tablet Portrait      834x1600             2.0      1495.2 KB    834x4899     screenshots/index_tablet.png
Desktop Full HD      1920x1080            1.0      639.2 KB     1920x4313    screenshots/index_desktop.png
====================================================================================================
✅ 共生成 3 张截图
```

## ⚠️ 注意事项

1. **首次运行慢**：首次启动 Chromium 浏览器需要几秒钟
2. **文件大小**：PNG 格式质量高但文件较大，JPEG 更适合网络传输
3. **长页面**：全页面截图会自动滚动拼接，页面越长截图时间越长
4. **字体渲染**：确保 HTML 中使用的字体在系统中已安装

## 🎯 推荐工作流

```bash
# 1. 生成信息图
python3 scripts/generate.py content.md

# 2. 进入项目目录
cd projects/项目名称_时间戳/

# 3. 生成多设备截图
python3 ~/.agents/skills/html-infographic/scripts/screenshot.py index.html \
  --all-portrait \
  -o screenshots/

# 4. 查看生成的截图
ls -lh screenshots/
```

---

**工具位置**: `~/.agents/skills/html-infographic/scripts/screenshot.py`

**依赖**: Playwright (Chromium)
