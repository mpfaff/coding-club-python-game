import sys
import pygame

windowSize = (800, 600)

pygame.init()
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

image = pygame.image.load("chicken.jpg")
image = pygame.transform.scale(image, (80, 80))

deltaTime = 0
x = 0
y = 0
vx = 0
vy = 0

chickenX = 140
chickenY = 140

isMoving = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.pos[0] > chickenX and event.pos[1] > chickenY and event.pos[0] < chickenX + image.get_width() and event.pos[1] < chickenY + image.get_height():
                isMoving = True
                vx = 0.1
                vy = -0.3
                x = chickenX + image.get_width() / 2
                y = chickenY + image.get_height()

    if isMoving:
        x += vx * deltaTime
        y += vy * deltaTime
        vy += 0.05

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        chickenX -= 0.5 * deltaTime
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        chickenX += 0.5 * deltaTime

    screen.fill(0x000000)

    # https://colorpicker.me
    pygame.draw.circle(screen, 0x37e50e, (x, y), 20)

    screen.blit(image, (chickenX, chickenY))
    
    pygame.display.flip()

    deltaTime = clock.tick(60)

