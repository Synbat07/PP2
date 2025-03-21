import pygame
import sys
import math
import time

pygame.init()

# Настройки окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

# Загрузка изображений
clock_img = pygame.image.load("clock.png")
minute_hand = pygame.image.load("minute_hand.png")
second_hand = pygame.image.load("second_hand.png")

# Функция поворота стрелок
def rotate_hand(image, angle, pos):
    rotated_image = pygame.transform.rotate(image, angle)
    rect = rotated_image.get_rect(center=pos)
    return rotated_image, rect

# Основной цикл игры
running = True
while running:
    screen.fill((255, 255, 255))  # Белый фон
    screen.blit(clock_img, (0, 0))  # Отображаем часы
    
    # Получаем текущее время
    t = time.localtime()
    seconds = t.tm_sec
    minutes = t.tm_min
    
    # Углы поворота (секунды -6 градусов за каждую секунду, минуты -6 градусов за каждую минуту)
    sec_angle = -6 * seconds
    min_angle = -6 * minutes
    
    # Рисуем стрелки
    sec_rot, sec_rect = rotate_hand(second_hand, sec_angle, (250, 250))
    min_rot, min_rect = rotate_hand(minute_hand, min_angle, (250, 250))
    screen.blit(sec_rot, sec_rect)
    screen.blit(min_rot, min_rect)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
