import pygame
import sys


def start():
    # Базовые настройки экрана игры
    pygame.init()
    pygame.display.set_caption("Space war")
    backgroundColor = (0, 0, 0)
    display = pygame.display.set_mode((1200, 800))
    # Основной цикл игры
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
        display.fill(backgroundColor)
        pygame.display.flip()


start()
