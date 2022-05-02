class Info():
    """вся информация (килы, жизни и тд)"""
    def __init__(self):
        self.remove_statistic()
        self.start_game = True
        with open('score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def remove_statistic(self):
        self.ship_death = 2
        self.score_now = 0
