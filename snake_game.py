import pygame
import random
import sys
import os

# 初始化pygame
pygame.init()

# 游戏配置
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def get_chinese_font(size=36):
    """获取支持中文的字体"""
    import platform
    
    system = platform.system().lower()
    
    # 根据操作系统定义字体路径
    chinese_fonts = []
    
    if system == 'darwin':  # macOS
        chinese_fonts = [
            '/System/Library/Fonts/PingFang.ttc',
            '/System/Library/Fonts/STHeiti Light.ttc', 
            '/System/Library/Fonts/Hiragino Sans GB.ttc',
            '/Library/Fonts/Arial Unicode MS.ttf',
        ]
    elif system == 'windows':
        chinese_fonts = [
            'C:/Windows/Fonts/simhei.ttf',  # 黑体
            'C:/Windows/Fonts/simsun.ttc',  # 宋体
            'C:/Windows/Fonts/msyh.ttc',    # 微软雅黑
            'C:/Windows/Fonts/msyhbd.ttc',  # 微软雅黑Bold
        ]
    else:  # Linux/Ubuntu
        chinese_fonts = [
            # Ubuntu/Debian 常见中文字体
            '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
            '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 
            '/usr/share/fonts/truetype/arphic/uming.ttc',
            '/usr/share/fonts/truetype/arphic/ukai.ttc',
            '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
            '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc',
            '/usr/share/fonts/truetype/noto/NotoSerifCJK-Regular.ttc',
            # 用户字体目录
            os.path.expanduser('~/.local/share/fonts/wqy-zenhei.ttc'),
            os.path.expanduser('~/.fonts/wqy-zenhei.ttc'),
            # Flatpak字体
            '/var/lib/flatpak/app/org.wqy.zenhei/current/active/files/share/fonts/wqy-zenhei.ttc',
        ]
    
    # 尝试加载指定的中文字体
    for font_path in chinese_fonts:
        if os.path.exists(font_path):
            try:
                font = pygame.font.Font(font_path, size)
                # 测试字体是否真的支持中文
                test_surface = font.render('测', True, (255, 255, 255))
                if test_surface.get_width() > 0:  # 如果能正常渲染中文
                    return font
            except Exception as e:
                continue
    
    # 如果上述都不行，尝试使用系统字体API
    if system == 'linux':
        try:
            # 尝试使用fontconfig查找中文字体
            import subprocess
            result = subprocess.run(['fc-match', ':lang=zh'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                font_info = result.stdout.strip()
                if font_info:
                    # 提取字体文件名
                    font_name = font_info.split(':')[0]
                    # 尝试在常见位置查找
                    for font_dir in ['/usr/share/fonts/', '/usr/local/share/fonts/', 
                                   os.path.expanduser('~/.local/share/fonts/'),
                                   os.path.expanduser('~/.fonts/')]:
                        for root, dirs, files in os.walk(font_dir):
                            for file in files:
                                if file.lower() == font_name.lower():
                                    font_path = os.path.join(root, file)
                                    try:
                                        return pygame.font.Font(font_path, size)
                                    except:
                                        continue
        except:
            pass
    
    # 最后的fallback选项
    fallback_fonts = [
        pygame.font.get_default_font(),
        None  # pygame内置字体
    ]
    
    for font_path in fallback_fonts:
        try:
            return pygame.font.Font(font_path, size)
        except:
            continue
    
    # 如果全部失败，返回一个基础字体
    return pygame.font.Font(None, size)

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]  # 蛇的初始位置
        self.direction = (1, 0)  # 初始方向向右
        self.grow = False  # 是否需要生长
    
    def move(self):
        head_x, head_y = self.positions[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # 检查是否撞墙
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            return False
        
        # 检查是否撞到自己
        if new_head in self.positions:
            return False
        
        self.positions.insert(0, new_head)
        
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False
        
        return True
    
    def change_direction(self, direction):
        # 防止反向移动
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction
    
    def grow_snake(self):
        self.grow = True
    
    def draw(self, surface):
        for position in self.positions:
            rect = pygame.Rect(position[0] * GRID_SIZE, position[1] * GRID_SIZE, 
                             GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GREEN, rect)
            pygame.draw.rect(surface, WHITE, rect, 1)

class Food:
    def __init__(self):
        self.position = self.generate_position()
    
    def generate_position(self):
        return (random.randint(0, GRID_WIDTH - 1), 
                random.randint(0, GRID_HEIGHT - 1))
    
    def respawn(self, snake_positions):
        # 确保食物不会生成在蛇身上
        while True:
            self.position = self.generate_position()
            if self.position not in snake_positions:
                break
    
    def draw(self, surface):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE,
                          GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("贪吃蛇")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        # 使用支持中文的字体
        self.font = get_chinese_font(28)
        self.large_font = get_chinese_font(36)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction((1, 0))
                elif event.key == pygame.K_ESCAPE:
                    return False
        return True
    
    def update(self):
        # 移动蛇
        if not self.snake.move():
            return False  # 游戏结束
        
        # 检查是否吃到食物
        if self.snake.positions[0] == self.food.position:
            self.snake.grow_snake()
            self.score += 10
            self.food.respawn(self.snake.positions)
        
        return True
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # 绘制蛇
        self.snake.draw(self.screen)
        
        # 绘制食物
        self.food.draw(self.screen)
        
        # 绘制分数
        score_text = self.font.render(f"分数: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # 绘制控制提示
        control_text = self.font.render("使用方向键控制，ESC退出", True, WHITE)
        self.screen.blit(control_text, (10, WINDOW_HEIGHT - 30))
        
        pygame.display.flip()
    
    def game_over_screen(self):
        # 游戏结束画面
        game_over_text = self.large_font.render("游戏结束!", True, RED)
        final_score_text = self.font.render(f"最终分数: {self.score}", True, WHITE)
        restart_text = self.font.render("按 R 重新开始，ESC 退出", True, WHITE)
        
        # 计算文本位置以居中显示
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True  # 重新开始游戏
                    elif event.key == pygame.K_ESCAPE:
                        return False  # 退出游戏
            
            self.screen.fill(BLACK)
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(final_score_text, score_rect)
            self.screen.blit(restart_text, restart_rect)
            pygame.display.flip()
            self.clock.tick(60)
    
    def run(self):
        running = True
        
        while running:
            # 处理事件
            if not self.handle_events():
                break
            
            # 更新游戏状态
            if not self.update():
                # 游戏结束
                if self.game_over_screen():
                    # 重新开始游戏
                    self.snake = Snake()
                    self.food = Food()
                    self.score = 0
                else:
                    # 退出游戏
                    break
            
            # 绘制画面
            self.draw()
            
            # 控制游戏速度
            self.clock.tick(10)  # 每秒10帧
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
