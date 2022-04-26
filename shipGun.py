import pygame


class ShipGun:
    def __init__(self, display):
        """логика корабля"""
        self.display = display
        self.img = pygame.image.load("img/game_texture/imgonline-com-ua-Resize-RqwzkcxljVEeDCsd.png")
        self.rectangel = self.img.get_rect()
        self.display_rectangel = display.get_rect()
        self.rectangel.centerx = self.display_rectangel.centerx
        self.rectangel.bottom = self.display_rectangel.bottom

    def product(self):
        """прорисовка нашего корабля"""
        self.display.blit(self.img, self.rectangel)

