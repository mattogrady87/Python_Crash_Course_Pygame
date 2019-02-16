class Settings():
    """A class to store all settings for catch"""

    def __init__(self):
        """intialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 230, 0)

        # Glove Settings
        self.glove_move_speed = 0.25
        self.glove_size = 100

        # Ball Settings
        self.ball_move_speed = 0.25
        self.ball_size = 40