from shipGun import ShipGun
import events_control
import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
from typing import Tuple, Any

surface = create_example_window('Example - Simple', (600, 400))


def set_difficulty(selected: Tuple, value: Any):
    pass


def start_the_game():
    pygame.init()
    pygame.display.set_caption("Space war")
    backgroundImg = pygame.image.load("img/bg/Purple Nebula 8 - 1024x1024.png")
    display = pygame.display.set_mode((1920, 1000), pygame.RESIZABLE)
    shipGun = ShipGun(display)
    container_bullet = pygame.sprite.Group()

    # Основной цикл игры
    while True:
        events_control.events(display, shipGun, container_bullet)
        shipGun.pos_update()
        container_bullet.update()
        events_control.display_update(backgroundImg, display, shipGun, container_bullet)


menu_start_game = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=400
)

#menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu_start_game.add.button('Play', start_the_game)
menu_start_game.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu_start_game.mainloop(surface)