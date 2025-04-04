import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Класс игрока (машина)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 90))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 50:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 50:
            self.rect.x += 5

# Класс врага (машина-препятствие)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 90))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), -50))
        self.speed = 5  # Начальная скорость врага

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(50, WIDTH - 50), -50)

# Класс монеты (разный вес)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.weight = random.randint(1, 3)  # Вес монеты (1, 2 или 3 очка)
        self.image = pygame.Surface((20, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(-100, -20)))

    def update(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(50, WIDTH - 50), random.randint(-100, -20))

# Группы спрайтов
player = Player()
enemy = Enemy()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

coins = pygame.sprite.Group()
for _ in range(5):
    coin = Coin()
    all_sprites.add(coin)
    coins.add(coin)

# Счетчик монет
score = 0
font = pygame.font.Font(None, 36)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление спрайтов
    all_sprites.update()

    # Проверка столкновений с монетами
    collected_coins = pygame.sprite.spritecollide(player, coins, True)
    for coin in collected_coins:
        score += coin.weight  # Учитываем вес монеты
    
    # Добавляем новые монеты вместо собранных
    for _ in range(len(collected_coins)):
        new_coin = Coin()
        all_sprites.add(new_coin)
        coins.add(new_coin)

    # Увеличение скорости врага при достижении N очков
    if score >= 10:
        enemy.speed = 7
    if score >= 20:
        enemy.speed = 9

    # Отрисовка объектов
    all_sprites.draw(screen)

    # Отображение количества очков
    score_text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH - 120, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
