import pygame

pygame.init()
s = pygame.display.set_mode((500, 500))
x, y = 225, 225

run = True
while run:
    pygame.time.delay(100)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: y -= 20
    if keys[pygame.K_DOWN]: y += 20
    if keys[pygame.K_LEFT]: x -= 20
    if keys[pygame.K_RIGHT]: x += 20

    x = max(0, min(x, 450))
    y = max(0, min(y, 450))

    s.fill((255, 255, 255))
    pygame.draw.circle(s, (255, 0, 0), (x + 25, y + 25), 25)
    pygame.display.update()

pygame.quit()
