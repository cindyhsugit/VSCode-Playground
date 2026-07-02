import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

mario_img = pygame.image.load("./gameExample/mario.png").convert_alpha()
mario_img = pygame.transform.scale(mario_img, (50, 60))

mario = pygame.Rect(100, 500, 50, 60)
vel_y = 0
jumping = False

GRAVITY = 1
JUMP_POWER = -15
GROUND = 500

running = True
while running:
    screen.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        vel_y = JUMP_POWER
        jumping = True

    vel_y += GRAVITY
    mario.y += vel_y

    if mario.y >= GROUND:
        mario.y = GROUND
        vel_y = 0
        jumping = False

    screen.blit(mario_img, mario.topleft)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()