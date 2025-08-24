#!/bin/bash

# 贪吃蛇游戏运行脚本

echo "🐍 启动贪吃蛇游戏..."

# 检查虚拟环境是否存在
if [ ! -d "snake_game_env" ]; then
    echo "创建虚拟环境..."
    python3 -m venv snake_game_env
    echo "安装依赖..."
    source snake_game_env/bin/activate
    pip install -r requirements.txt
else
    echo "激活虚拟环境..."
    source snake_game_env/bin/activate
fi

# 运行游戏
echo "启动游戏窗口..."
python snake_game.py
