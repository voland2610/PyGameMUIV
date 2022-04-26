import pygame
import sys
from shipGun import ShipGun


def start():
    # Базовые настройки экрана игры
    pygame.init()
    pygame.display.set_caption("Space war")
    backgroundImg = pygame.image.load("img/bg/Purple Nebula 8 - 1024x1024.png")
    display = pygame.display.set_mode((1920, 1000))
    shipGun = ShipGun(display)

    # Основной цикл игры
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
        display.blit(backgroundImg, (0, 0))
        display.blit(backgroundImg, (1020, 0))
        shipGun.product()
        pygame.display.flip()


start()
