
class Score():
    """A Class to keep track of score and modify settings"""
    def __init__(self, settings):
        self.score = 0
        self.high_score = 0
        self.settings = settings

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.settings.ball_move_speed += 0.25
        # self.settings.glove_move_speed += 0.25
        self.settings.glove_move_speed += 0.25
        print(self.score)
    
    def decrease_score(self):
        if self.score >= 1:
            self.score -= 1
            self.settings.ball_move_speed -= 0.25
            self.settings.glove_move_speed -= 0.25
            print(self.score)
