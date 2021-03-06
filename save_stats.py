import pygame.font
from shipGun import ShipGun


class Stats():
    """показ жизней, килов"""
    def __init__(self, display, info):
        self.display = display
        self.display_rect = display.get_rect()
        self.info = info
        self.color_txt = (255, 235,  59)
        self.font = pygame.font.Font('Retro.ttf', 60)
        self.draw_stats()
        self.draw_high_score()
        self.img_ship()

    def draw_stats(self):
        """логика расположения счета"""
        self.stat_image = self.font.render(str(self.info.score_now), True, self.color_txt)
        self.stat_rect = self.stat_image.get_rect()
        self.stat_rect.right = self.display_rect.right - 40
        self.stat_rect.top = 20

    def show_stat(self):
        """отрисовка счета"""
        self.display.blit(self.stat_image, self.stat_rect)
        self.display.blit(self.number_score_hg, self.score_hg_rect)
        self.ship.draw(self.display)

    def img_ship(self):
        """отрисовка жизней слева в углу"""
        self.ship = pygame.sprite.Group()
        for ships in range(self.info.ship_death):
            ship = ShipGun(self.display)
            ship.rect.x = 15 + ships * ship.rect.width
            ship.rect.y = 20
            self.ship.add(ship)

    def draw_high_score(self):
        """Вводит по центру экрана рекорд"""
        self.number_score_hg = self.font.render(str(self.info.high_score), True, self.color_txt)
        self.score_hg_rect = self.number_score_hg.get_rect()
        self.score_hg_rect.centerx = self.display_rect.centerx
        self.score_hg_rect.top = self.display_rect.top + 20