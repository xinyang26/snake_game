#!/bin/bash

# Ubuntu/Debian 中文字体安装脚本

echo "🐍 贪吃蛇游戏 - Ubuntu 中文字体安装脚本"
echo "============================================"

# 检查是否为 Ubuntu/Debian 系统
if ! command -v apt-get &> /dev/null; then
    echo "❌ 此脚本仅适用于 Ubuntu/Debian 系统"
    exit 1
fi

echo "📦 安装中文字体包..."

# 更新包列表
sudo apt-get update

# 安装常见的中文字体包
echo "正在安装文泉驿字体..."
sudo apt-get install -y fonts-wqy-zenhei fonts-wqy-microhei

echo "正在安装文鼎字体..."
sudo apt-get install -y fonts-arphic-uming fonts-arphic-ukai

echo "正在安装 Noto 字体（Google开源字体）..."
sudo apt-get install -y fonts-noto-cjk fonts-noto-cjk-extra

echo "正在安装其他中文字体..."
sudo apt-get install -y fonts-droid-fallback ttf-wqy-zenhei ttf-wqy-microhei

# 刷新字体缓存
echo "🔄 刷新字体缓存..."
fc-cache -fv

echo "✅ 字体安装完成！"
echo ""
echo "已安装的中文字体："
echo "- 文泉驿正黑 (WenQuanYi Zen Hei)"
echo "- 文泉驿微米黑 (WenQuanYi Micro Hei)" 
echo "- 文鼎PL简报宋 (AR PL UMing)"
echo "- 文鼎PL简中楷 (AR PL UKai)"
echo "- Google Noto CJK 字体"
echo "- Droid Sans Fallback"
echo ""
echo "🎮 现在可以运行贪吃蛇游戏了："
echo "   ./run.sh"
echo ""

# 验证字体安装
echo "🔍 验证中文字体是否可用："
if fc-list :lang=zh | grep -q "wqy\|noto\|arphic\|droid"; then
    echo "✅ 中文字体验证成功！"
else
    echo "⚠️  中文字体可能未正确安装，请手动检查。"
    echo "   可以运行: fc-list :lang=zh 查看可用的中文字体"
fi
