import pygame


class Info():
    """вся информация (килы, жизни и тд)"""
    def __init__(self):
        self.remove_statistic()
        self.start_game = True

    def remove_statistic(self):
        self.ship_death = 2
        self.score_now = 0