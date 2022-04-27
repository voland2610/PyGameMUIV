import pygame
import sys


def events(shipGun):
    """получения и обработка какого либо события"""
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_d:
                shipGun.moveR = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_d:
                shipGun.moveR = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT or events.key == pygame.K_a:
                shipGun.moveL = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_a:
                shipGun.moveL = False


def display_update(backgroundImg, display, shipGun):
    """обнавление нашего экрана"""
    display.blit(backgroundImg, (0, 0))
    display.blit(backgroundImg, (1020, 0))
    shipGun.product()
    pygame.display.flip()