import pygame
import random

pygame.init()

# Настройки экрана
WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)

# Начальные данные
snake = [(100, 100), (90, 100), (80, 100)]
direction = (CELL_SIZE, 0)
score = 0
level = 1
speed = 10

# Еда с таймером и весом
food_x, food_y = 0, 0
food_weight = 1
food_timer = 0

# Функция для генерации еды
def new_food():
    global food_x, food_y, food_weight, food_timer
    food_x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    food_y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    food_weight = random.choice([1, 2, 3])  # Случайный вес еды
    food_timer = pygame.time.get_ticks()  # Засекаем время появления еды

new_food()  # Создаем первую еду

running = True
clock = pygame.time.Clock()

# Игровой цикл
while running:
    screen.fill(BLACK)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # Движение змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка границ
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
        running = False  # Выход за границы
        break

    # Проверка столкновения с собой
    if new_head in snake:
        running = False  # Врезались в себя
        break

    snake.insert(0, new_head)

    # Если съели еду
    if new_head[0] == food_x and new_head[1] == food_y:
        score += food_weight  # Увеличиваем счет на вес еды
        new_food()
    else:
        snake.pop()

    # Проверяем, прошло ли 5 секунд с появления еды
    if pygame.time.get_ticks() - food_timer > 5000:
        new_food()

    # Уровни и скорость
    if score % 4 == 0 and score > 0:
        level = score // 4 + 1
        speed = 10 + (level - 1) * 2

    # Отрисовка змейки
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # Отрисовка еды (размер зависит от веса)
    pygame.draw.rect(screen, RED, (food_x, food_y, CELL_SIZE, CELL_SIZE))

    # Отображение счета
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
