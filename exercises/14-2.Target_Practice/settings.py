class Settings():
    """A Class to store settings for the target_practice game"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)


        # Target settings
        self.target_height = 200
        self.target_width = 30
        self.target_color = (0, 230, 0)
        self.target_speed = 0

        # Ship settings
        self.ship_speed = 2
        self.ship_size = 250

        # Bullet Settings
        self.bullet_size = 90
        self.bullet_speed = 3
        self.bullet_reload = 1.5

        # Game Settings
        self.misses_allowed = 3