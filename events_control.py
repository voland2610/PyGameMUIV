import random
import pygame
import sys
import shooting_gun
from alien import Alian



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


def display_update(backgroundImg, display, info, stats, shipGun, aliens, container_bullet):
    """обнавление нашего экрана"""
    display.blit(backgroundImg, (0, 0))
    display.blit(backgroundImg, (1020, 0))
    stats.show_stat()
    for bullets in container_bullet.sprites():
        bullets.sketch_bullet()
    shipGun.product()
    aliens.draw(display)
    pygame.display.flip()


def remove_bullet(display, info, stats, aliens, container_bullet):
    """удаление пуль + коллизия пули"""
    container_bullet.update()
    for bullets in container_bullet.copy():
        if bullets.rect.bottom <= 0:
            container_bullet.remove(bullets)
    colis = pygame.sprite.groupcollide(container_bullet, aliens, True, True)
    if colis:
        for aliens in colis.values():
            info.score_now += 10 * len(aliens)
        stats.draw_stats()
    if len(aliens) == 0:
        container_bullet.empty()
        create_alian(display, aliens)


def ships_death(info, display, shipGun, aliens, container_bullet):
    """логика столкновения корбля с пришельцами"""
    if info.ship_death > 0:
        info.ship_death -= 1
        aliens.empty()
        container_bullet.empty()
        create_alian(display, aliens)
        shipGun.ship_gun_create()
    else:
        info.start_game = False
        sys.exit()


def update_pos_alian(info, display, shipGun, aliens, container_bullet):
    aliens.update()
    if pygame.sprite.spritecollideany(shipGun, aliens):
        ships_death(info, display, shipGun, aliens, container_bullet)
    alians_inspect(info, display, shipGun, aliens, container_bullet)


def alians_inspect(info, display, shipGun, aliens, container_bullet):
    display_rect = display.get_rect()
    for alian in aliens.sprites():
        if alian.rect.bottom > display_rect.bottom:
            ships_death(info, display, shipGun, aliens, container_bullet)
            break


def create_alian(display, alians):
    alien = Alian(display)
    alien_width = alien.rect.width
    number_alian_x = (100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1600, 1700, 1900)
    for alian_number in range(15):
        alian = Alian(display)
        #alian.x = alien_width + alien_width * alian_number
        #alian.rect.x = alian.x
        alian.rect.x = random.choice(number_alian_x)
        alians.add(alian)