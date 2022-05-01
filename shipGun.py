import pygame


class ShipGun:
    def __init__(self, display):
        """логика корабля"""
        self.right_side = 1770
        self.left_side = 150
        self.display = display
        self.img = pygame.image.load("img/game_texture/imgonline-com-ua-Resize-Pbxj43pH9Vf.png")
        self.rect = self.img.get_rect()
        self.display_rectangel = display.get_rect()
        self.rect.centerx = self.display_rectangel.centerx
        self.number_center = float(self.rect.centerx)
        self.rect.bottom = self.display_rectangel.bottom
        self.moveR = False
        self.moveL = False

    def product(self):
        """прорисовка нашего корабля"""
        self.display.blit(self.img, self.rect)

    def pos_update(self):
        # проверка на нажатие клавиши и выхода за правый край
        if self.moveR == True and self.rect.centerx < self.right_side:
            self.number_center += 12.5
        # проверка на нажатие клавиши и выхода за левый край
        if self.moveL == True and self.rect.centerx > self.left_side:
            self.number_center -= 12.5

        self.rect.centerx = self.number_center

    def ship_gun_create(self):
        """появление пушки после смерти"""
        self.number_center = self.display_rectangel.centerx
