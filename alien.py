import pygame


class Alian(pygame.sprite.Sprite):

    def __init__(self, display, ):
        super(Alian, self).__init__()
        self.display = display
        self.img = pygame.image.load("img/game_texture/imgonline-com-ua-Resize-LpnyxuW5qMVCLO.png")
        self.rect = self.img.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def sketch_alian(self):
        self.display.blit(self.img, self.rect)