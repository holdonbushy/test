import pygame
import random

# 初始化 Pygame
pygame.init()

# 游戏窗口大小
window_width = 800
window_height = 600

# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("飞机大战")

# 加载图像资源
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")

# 玩家飞机类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = window_width // 2
        self.rect.bottom = window_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > window_width:
            self.rect.right = window_width

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

# 敌机类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, window_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > window_height + 10:
            self.rect.x = random.randrange(0, window_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 4)

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

# 创建精灵组
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
 
# 创建玩家飞机实例
player = Player()
all_sprites.add(player)

# 创建敌机实例
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 游戏主循环
running = True
clock = pygame.time.Clock()
score = 0

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
            elif event.key == pygame.K_SPACE:
                player.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    # 更新游戏状态
    all_sprites.update()

    # 检测玩家飞机和敌机的碰撞
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # 检测子弹和敌机的碰撞
    bullet_hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for _ in bullet_hits:
        score += 10
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # 绘制游戏窗口
    window.fill(black)
    all_sprites.draw(window)

    # 绘制得分
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))

    # 刷新游戏窗口
    pygame.display.flip()
    clock.tick(60)

# 退出游戏
pygame.quit()
