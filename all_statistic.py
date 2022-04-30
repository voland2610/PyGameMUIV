import pygame


class Info():
    """вся информация (килы, жизни и тд)"""
    def __init__(self):
        self.remove_statistic()

    def remove_statistic(self):
        self.ship_death = 2