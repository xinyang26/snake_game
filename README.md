# 🐍 贪吃蛇游戏

一个使用 Python 和 pygame 开发的经典贪吃蛇游戏。

## 📸 游戏截图

游戏窗口大小：640x480 像素
- 绿色方块：蛇身
- 红色方块：食物
- 黑色背景：游戏区域

## 🎮 游戏特性

- **经典玩法**：控制蛇移动，吃食物长大
- **碰撞检测**：撞墙或撞到自己就会游戏结束
- **计分系统**：每个食物得10分
- **游戏重启**：游戏结束后可重新开始
- **流畅操作**：响应式键盘控制

## 🕹️ 控制方式

| 按键 | 功能 |
|------|------|
| ↑ ↓ ← → | 控制蛇的移动方向 |
| `ESC` | 退出游戏 |
| `R` | 游戏结束后重新开始 |

## 📟 系统要求

- Python 3.7+
- macOS / Linux / Windows
- 至少50MB 可用空间

### Ubuntu/Linux 用户注意：

为了正常显示中文界面，请先安装中文字体：

```bash
# 使用自动安装脚本（推荐）
./install_fonts_ubuntu.sh

# 或手动安装
sudo apt-get update
sudo apt-get install -y fonts-wqy-zenhei fonts-noto-cjk
```

## 🚀 快速开始

### 方法一：使用运行脚本（推荐）

```bash
# 克隆或下载项目后
cd snake_game
./run.sh
```

### 方法二：手动运行

1. **创建虚拟环境**：
   ```bash
   python3 -m venv snake_game_env
   source snake_game_env/bin/activate  # macOS/Linux
   # 或 snake_game_env\Scripts\activate  # Windows
   ```

2. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

3. **运行游戏**：
   ```bash
   python snake_game.py
   ```

## 🔧️ 项目结构

```
snake_game/
├── snake_game.py           # 主游戏文件
├── requirements.txt        # Python依赖
├── run.sh                 # 运行脚本
├── install_fonts_ubuntu.sh # Ubuntu中文字体安装脚本
├── .gitignore             # Git忽略文件
├── README.md              # 项目说明
└── snake_game_env/        # 虚拟环境（被git忽略）
```

## 🎯 游戏规则

1. **目标**：控制蛇吃到尽可能多的食物
2. **移动**：蛇会持续向当前方向移动
3. **生长**：吃到食物后蛇身会增长一节
4. **得分**：每吃到一个食物得10分
5. **游戏结束**：
   - 撞到边界墙壁
   - 蛇头撞到自己的身体

## 🔧 自定义配置

你可以在 `snake_game.py` 中修改以下参数：

```python
# 游戏配置
WINDOW_WIDTH = 640      # 窗口宽度
WINDOW_HEIGHT = 480     # 窗口高度
GRID_SIZE = 20          # 网格大小
FPS = 10               # 游戏速度（帧率）

# 颜色配置
BLACK = (0, 0, 0)      # 背景色
GREEN = (0, 255, 0)    # 蛇身颜色
RED = (255, 0, 0)      # 食物颜色
WHITE = (255, 255, 255) # 文字颜色
```

## 🐛 常见问题

### Q: 游戏运行时出现 "No module named 'pygame'" 错误
**A:** 确保已经激活虚拟环境并安装了pygame：
```bash
source snake_game_env/bin/activate
pip install pygame
```

### Q: 在 macOS 上提示外部管理环境错误
**A:** 使用虚拟环境可以避免这个问题，项目已经配置好了虚拟环境。

### Q: 游戏窗口无法显示
**A:** 确保你的系统支持图形界面，并且pygame能够访问显示器。

### Q: Ubuntu 上中文显示为方块或乱码
**A:** 这是因为缺少中文字体，请安装中文字体：
```bash
# 使用项目提供的脚本
./install_fonts_ubuntu.sh

# 或手动安装最基本的中文字体
sudo apt install fonts-wqy-zenhei
sudo fc-cache -fv

# 验证字体安装
fc-list :lang=zh
```

### Q: 在虚拟机中运行游戏卡顿
**A:** 在虚拟机中可能需要启用3D加速或调低游戏帧率：
```python
# 在 snake_game.py 中修改这一行
self.clock.tick(5)  # 降低到5FPS
```

## 🚧 未来改进计划

- [ ] 添加音效
- [ ] 增加难度等级
- [ ] 添加最高分记录
- [ ] 实现暂停功能
- [ ] 添加更多视觉效果
- [ ] 支持自定义皮肤

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 👨‍💻 开发者

由 AI Assistant 使用 Python 和 pygame 开发。

---

**享受游戏！🎉**
