import pygame
from shipGun import ShipGun
import events_control


def start():
    # Базовые настройки экрана игры
    pygame.init()
    pygame.display.set_caption("Space war")
    backgroundImg = pygame.image.load("img/bg/Purple Nebula 8 - 1024x1024.png")
    display = pygame.display.set_mode((1920, 1000))
    shipGun = ShipGun(display)
    container_bullet = pygame.sprite.Group()

    # Основной цикл игры
    while True:
        events_control.events(display, shipGun, container_bullet)
        shipGun.pos_update()
        container_bullet.update()
        events_control.display_update(backgroundImg, display, shipGun, container_bullet)





start()
