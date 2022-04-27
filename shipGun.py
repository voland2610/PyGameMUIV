import pygame


class ShipGun:
    def __init__(self, display):
        """логика корабля"""
        self.right_side = 1770
        self.left_side = 150
        self.display = display
        self.img = pygame.image.load("img/game_texture/imgonline-com-ua-Resize-RqwzkcxljVEeDCsd.png")
        self.rectangel = self.img.get_rect()
        self.display_rectangel = display.get_rect()
        self.rectangel.centerx = self.display_rectangel.centerx
        self.rectangel.bottom = self.display_rectangel.bottom
        self.moveR = False
        self.moveL = False

    def product(self):
        """прорисовка нашего корабля"""
        self.display.blit(self.img, self.rectangel)

    def pos_update(self):
        # проверка на нажатие клавиши и выхода за правый край
        if self.moveR == True and self.rectangel.centerx < self.right_side:
            self.rectangel.centerx += 10
        # проверка на нажатие клавиши и выхода за левый край
        if self.moveL == True and self.rectangel.centerx > self.left_side:
            self.rectangel.centerx -= 10