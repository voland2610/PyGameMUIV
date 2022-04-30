import random
import pygame
import sys
import shooting_gun
from alien import Alian
import time


def events(display, shipGun, container_bullet):
    """получения и обработка какого либо события"""
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_d:
                shipGun.moveR = True
            if events.key == pygame.K_SPACE:
                bullets = shooting_gun.Shooting(display, shipGun)
                container_bullet.add(bullets)
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_RIGHT or events.key == pygame.K_d:
                shipGun.moveR = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT or events.key == pygame.K_a:
                shipGun.moveL = True
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_LEFT or events.key == pygame.K_a:
                shipGun.moveL = False


def display_update(backgroundImg, display, shipGun, aliens, container_bullet):
    """обнавление нашего экрана"""
    display.blit(backgroundImg, (0, 0))
    display.blit(backgroundImg, (1020, 0))
    for bullets in container_bullet.sprites():
        bullets.sketch_bullet()
    shipGun.product()
    aliens.draw(display)
    pygame.display.flip()


def remove_bullet(aliens, container_bullet):
    """удаление пуль + коллизия пули"""
    container_bullet.update()
    for bullets in container_bullet.copy():
        if bullets.rect.bottom <= 0:
            container_bullet.remove(bullets)
    colis = pygame.sprite.groupcollide(container_bullet, aliens, True, True)


def ships_death(info, display, shipGun, aliens, container_bullet):
    """логика столкновения корбля с пришельцами"""
    info.ship_death -= 1
    if info.ship_death == 0:
        aliens.empty()
        container_bullet.empty()
        create_alian(display, aliens)
        shipGun.ship_gun_create()


def update_pos_alian(info, display, shipGun, aliens, container_bullet):
    aliens.update()
    if pygame.sprite.spritecollideany(shipGun, aliens):
        ships_death(info, display, shipGun, aliens, container_bullet)

def create_alian(display, alians):
    alien = Alian(display)
    alien_width = alien.rect.width
    number_alian_x = int((1920 - 2 * alien_width) / alien_width)
    for alian_number in range(number_alian_x):
        alian = Alian(display)
        #alian.x = alien_width + alien_width * alian_number
        #alian.rect.x = alian.x
        alian.rect.x = random.randint(100, 1000)
        alians.add(alian)