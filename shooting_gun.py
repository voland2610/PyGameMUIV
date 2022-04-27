import pygame


class Shooting(pygame.sprite.Sprite):
    def __init__(self, display, shipGun):
        """логика стрелбы нашего корабля из пушки"""
        super(Shooting, self).__init__()
        self.display = display
        self.rectangel = pygame.Rect(0, 0, 3, 20)
        self.color_bullet = 255, 235,  59
        #скорость полета пули
        self.bullet_speed = 15.5
        self.rectangel.centerx = shipGun.rectangel.centerx
        self.rectangel.top = shipGun.rectangel.top
        self.y = float(self.rectangel.y)

    def update(self):
        """движение пули вверх"""
        self.y -= self.bullet_speed
        self.rectangel.y = self.y

    def sketch_bullet(self):
        """отрисовка нашего снаряда на экране"""
        pygame.draw.rect(self.display, self.color_bullet, self.rectangel)
