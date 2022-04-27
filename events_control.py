import pygame
import sys
import shooting_gun


def events(display, shipGun, container_bullet):
    """получения и обработка какого либо события"""
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_d:
                shipGun.moveR = True
            if events.key == pygame.K_SPACE:
                bullets = shooting_gun.Shooting(display, shipGun)
                container_bullet.add(bullets)
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_d:
                shipGun.moveR = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT or events.key == pygame.K_a:
                shipGun.moveL = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_a:
                shipGun.moveL = False


def display_update(backgroundImg, display, shipGun, container_bullet):
    """обнавление нашего экрана"""
    display.blit(backgroundImg, (0, 0))
    display.blit(backgroundImg, (1020, 0))
    for bullets in container_bullet.sprites():
        bullets.sketch_bullet()
    shipGun.product()
    pygame.display.flip()
