import pygame

pygame.init()

# Устанавливаем размер экрана
WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
current_color = BLACK

# Флаги для рисования
drawing = False
last_pos = (0, 0)

# Основной цикл игры
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Начало рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos

        # Конец рисования
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Рисование линии
        if event.type == pygame.MOUSEMOTION and drawing:
            pygame.draw.line(screen, current_color, last_pos, event.pos, 2)
            last_pos = event.pos

        # Выбор цвета
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_color = BLACK
            if event.key == pygame.K_2:
                current_color = RED

    pygame.display.flip()

pygame.quit()
