#!/usr/bin/env python3
"""
HTML 信息图截图工具
使用 Playwright 进行高质量全页面截图，支持多种设备分辨率
"""

import asyncio
import argparse
from pathlib import Path
from datetime import datetime
from playwright.async_api import async_playwright

# 预设设备分辨率
DEVICE_PRESETS = {
    "mobile": {"width": 390, "height": 844, "device_scale_factor": 3.0, "name": "iPhone 15 Pro"},
    "mobile-max": {"width": 430, "height": 932, "device_scale_factor": 3.0, "name": "iPhone 15 Pro Max"},
    "tablet": {"width": 834, "height": 1194, "device_scale_factor": 2.0, "name": "iPad Pro 11"},
    "tablet-large": {"width": 1024, "height": 1366, "device_scale_factor": 2.0, "name": "iPad Pro 12.9"},
    "desktop": {"width": 1920, "height": 1080, "device_scale_factor": 1.0, "name": "Desktop Full HD"},
    "desktop-2k": {"width": 2560, "height": 1440, "device_scale_factor": 1.0, "name": "Desktop 2K"},
    "desktop-4k": {"width": 3840, "height": 2160, "device_scale_factor": 1.0, "name": "Desktop 4K"},
    # 竖屏模式（适合信息图）
    "mobile-portrait": {"width": 390, "height": 1200, "device_scale_factor": 3.0, "name": "Mobile Portrait"},
    "tablet-portrait": {"width": 834, "height": 1600, "device_scale_factor": 2.0, "name": "Tablet Portrait"},
}


async def capture_screenshot(
    html_path: str,
    output_path: str,
    width: int = 1920,
    height: int = 1080,
    device_scale_factor: float = 1.0,
    full_page: bool = True,
    format: str = "png",
    quality: int = 90,
):
    """
    捕获网页截图
    
    Args:
        html_path: HTML 文件路径或 URL
        output_path: 输出截图路径
        width: 视口宽度
        height: 视口高度
        device_scale_factor: 设备缩放因子（Retina 屏幕用 2.0 或 3.0）
        full_page: 是否捕获完整页面（自动滚动拼接）
        format: 输出格式（png/jpeg）
        quality: JPEG 质量（1-100）
    """
    async with async_playwright() as p:
        # 启动浏览器（无头模式）
        browser = await p.chromium.launch(headless=True)
        
        # 创建页面
        page = await browser.new_page(
            viewport={"width": width, "height": height},
            device_scale_factor=device_scale_factor,
        )
        
        # 加载 HTML 文件
        file_url = f"file://{Path(html_path).resolve()}"
        await page.goto(file_url, wait_until="networkidle")
        
        # 等待页面完全渲染
        await page.wait_for_timeout(1000)
        
        # 截图
        screenshot_options = {
            "path": output_path,
            "full_page": full_page,
            "type": format,
        }
        
        if format == "jpeg":
            screenshot_options["quality"] = quality
        
        await page.screenshot(**screenshot_options)
        
        # 获取截图尺寸
        dimensions = await page.evaluate("""() => {
            return {
                width: document.documentElement.scrollWidth,
                height: document.documentElement.scrollHeight
            }
        }""")
        
        await browser.close()
        
        return dimensions


async def capture_multiple_devices(
    html_path: str,
    output_dir: str,
    devices: list,
    base_name: str = None,
):
    """
    一次性生成多个设备分辨率的截图
    
    Args:
        html_path: HTML 文件路径
        output_dir: 输出目录
        devices: 设备预设列表
        base_name: 输出文件基础名
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if base_name is None:
        base_name = Path(html_path).stem
    
    results = []
    
    for device_name in devices:
        if device_name not in DEVICE_PRESETS:
            print(f"⚠️  未知设备预设：{device_name}")
            continue
        
        preset = DEVICE_PRESETS[device_name]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{base_name}_{device_name}_{timestamp}.png"
        output_path = output_dir / output_filename
        
        print(f"📸 正在生成 {preset['name']} 截图...")
        
        dimensions = await capture_screenshot(
            html_path=html_path,
            output_path=str(output_path),
            width=preset["width"],
            height=preset["height"],
            device_scale_factor=preset["device_scale_factor"],
        )
        
        file_size = output_path.stat().st_size / 1024  # KB
        
        results.append({
            "device": device_name,
            "name": preset["name"],
            "resolution": f"{preset['width']}x{preset['height']}",
            "scale": preset["device_scale_factor"],
            "output": str(output_path),
            "size_kb": round(file_size, 1),
            "content_dimensions": f"{dimensions['width']}x{dimensions['height']}",
        })
        
        print(f"✅ {preset['name']}: {output_filename} ({file_size:.1f} KB)")
    
    return results


def print_results_table(results: list):
    """打印结果表格"""
    print("\n" + "=" * 100)
    print("📊 截图生成完成")
    print("=" * 100)
    print(f"{'设备':<20} {'分辨率':<20} {'缩放':<8} {'文件大小':<12} {'内容尺寸':<25} {'输出路径'}")
    print("-" * 100)
    
    for r in results:
        print(f"{r['name']:<20} {r['resolution']:<20} {r['scale']:<8} {r['size_kb']:<12} {r['content_dimensions']:<25} {r['output']}")
    
    print("=" * 100)
    print(f"✅ 共生成 {len(results)} 张截图\n")


async def main():
    parser = argparse.ArgumentParser(
        description="HTML 信息图截图工具 - 高质量全页面截图",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
设备预设:
  mobile              iPhone 15 Pro (390x844, 3x)
  mobile-max          iPhone 15 Pro Max (430x932, 3x)
  mobile-portrait     手机竖屏 (390x1200, 3x)
  tablet              iPad Pro 11 (834x1194, 2x)
  tablet-large        iPad Pro 12.9 (1024x1366, 2x)
  tablet-portrait     平板竖屏 (834x1600, 2x)
  desktop             桌面 Full HD (1920x1080, 1x)
  desktop-2k          桌面 2K (2560x1440, 1x)
  desktop-4k          桌面 4K (3840x2160, 1x)

示例:
  # 生成单张截图（桌面分辨率）
  python3 screenshot.py index.html
  
  # 生成手机和平板截图
  python3 screenshot.py index.html --device mobile --device tablet
  
  # 生成所有竖屏设备截图
  python3 screenshot.py index.html --device mobile-portrait --device tablet-portrait --device desktop
  
  # 自定义分辨率
  python3 screenshot.py index.html --width 1080 --height 1920 --scale 2.0
  
  # 批量生成多种设备
  python3 screenshot.py index.html --all-portrait
  
  # JPEG 格式（更小文件）
  python3 screenshot.py index.html --format jpeg --quality 85
        """,
    )
    
    parser.add_argument("html_path", help="HTML 文件路径")
    parser.add_argument("-o", "--output", help="输出目录（默认：screenshots/）")
    parser.add_argument("-n", "--name", help="输出文件基础名（默认：HTML 文件名）")
    parser.add_argument("-d", "--device", action="append", help="设备预设（可多次指定）")
    parser.add_argument("-w", "--width", type=int, default=1920, help="自定义宽度（像素）")
    parser.add_argument("-H", "--height", type=int, default=1080, help="自定义高度（像素）")
    parser.add_argument("-s", "--scale", type=float, default=1.0, help="设备缩放因子（Retina 用 2.0 或 3.0）")
    parser.add_argument("--format", choices=["png", "jpeg"], default="png", help="输出格式")
    parser.add_argument("--quality", type=int, default=90, help="JPEG 质量（1-100）")
    parser.add_argument("--no-full-page", action="store_true", help="仅截取可见区域（非全页面）")
    parser.add_argument("--all-portrait", action="store_true", help="生成所有竖屏设备截图")
    parser.add_argument("--all", action="store_true", help="生成所有设备预设截图")
    
    args = parser.parse_args()
    
    # 验证输入文件
    if not Path(args.html_path).exists():
        print(f"❌ 文件不存在：{args.html_path}")
        return 1
    
    # 确定设备列表
    devices = args.device or []
    
    if args.all_portrait:
        devices.extend(["mobile-portrait", "tablet-portrait", "desktop"])
    
    if args.all:
        devices = list(DEVICE_PRESETS.keys())
    
    if not devices:
        # 默认使用桌面分辨率
        devices = ["desktop"]
    
    # 输出目录
    output_dir = args.output or "screenshots"
    
    print(f"🎯 HTML 文件：{args.html_path}")
    print(f"📁 输出目录：{output_dir}")
    print(f"📱 设备预设：{', '.join(devices)}")
    print()
    
    # 执行截图
    if len(devices) == 1 and not args.device:
        # 单张截图（自定义分辨率）
        preset = DEVICE_PRESETS.get(devices[0], {})
        width = args.width or preset.get("width", 1920)
        height = preset.get("height", args.height)
        scale = args.scale or preset.get("device_scale_factor", 1.0)
        
        output_path = Path(output_dir) / f"{args.name or 'screenshot'}.png"
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        print(f"📸 正在生成截图（{width}x{height}, {scale}x 缩放）...")
        
        dimensions = await capture_screenshot(
            html_path=args.html_path,
            output_path=str(output_path),
            width=width,
            height=height,
            device_scale_factor=scale,
            full_page=not args.no_full_page,
            format=args.format,
            quality=args.quality,
        )
        
        file_size = output_path.stat().st_size / 1024
        print(f"✅ 截图完成：{output_path} ({file_size:.1f} KB)")
        print(f"   内容尺寸：{dimensions['width']}x{dimensions['height']}")
    else:
        # 多设备截图
        results = await capture_multiple_devices(
            html_path=args.html_path,
            output_dir=output_dir,
            devices=devices,
            base_name=args.name,
        )
        print_results_table(results)
    
    return 0


if __name__ == "__main__":
    exit(asyncio.run(main()))
