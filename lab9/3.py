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

# Функции для рисования фигур

# Функция для рисования квадрата
def draw_square(x, y, size):
    pygame.draw.rect(screen, current_color, (x, y, size, size))

# Функция для рисования прямоугольного треугольника
def draw_right_triangle(x, y, base, height):
    points = [(x, y), (x + base, y), (x, y - height)]
    pygame.draw.polygon(screen, current_color, points)

# Функция для рисования равностороннего треугольника
def draw_equilateral_triangle(x, y, size):
    height = (size * (3 ** 0.5)) / 2  # Высота равностороннего треугольника
    points = [(x, y), (x + size, y), (x + size / 2, y - height)]
    pygame.draw.polygon(screen, current_color, points)

# Функция для рисования ромба
def draw_rhombus(x, y, size):
    points = [
        (x, y - size),  # Верхняя точка
        (x + size, y),  # Правая точка
        (x, y + size),  # Нижняя точка
        (x - size, y),  # Левая точка
    ]
    pygame.draw.polygon(screen, current_color, points)

# Основной цикл игры
running = True
while running:
    screen.fill(WHITE)  # Очищаем экран каждый кадр

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

        # Клавиши для рисования фигур
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_3:  # Квадрат
                draw_square(100, 100, 50)  # Рисуем квадрат в (100, 100)
            if event.key == pygame.K_4:  # Прямоугольный треугольник
                draw_right_triangle(200, 300, 100, 80)  # Рисуем треугольник
            if event.key == pygame.K_5:  # Равносторонний треугольник
                draw_equilateral_triangle(300, 300, 100)  # Рисуем равносторонний треугольник
            if event.key == pygame.K_6:  # Ромб
                draw_rhombus(400, 100, 50)  # Рисуем ромб

    pygame.display.flip()  # Обновляем экран

pygame.quit()
