import pygame
import sys


def start():
    # Базовые настройки экрана игры
    pygame.init()
    pygame.display.set_caption("Space war")
    backgroundimg = pygame.image.load("img/Purple Nebula 8 - 1024x1024.png")
    display = pygame.display.set_mode((1024, 1024))
    # Основной цикл игры
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
        display.blit(backgroundimg, (0, 0))
        pygame.display.flip()


start()
