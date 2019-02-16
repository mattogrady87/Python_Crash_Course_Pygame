class Settings():
    """A class to store the settings for sideways shooter"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 230, 0)

        # Sideways Rocket Settings
        self.ship_speed_factor = 1.5


        # Bullet Settings
        self.bullet_speed_factor = 2
        self.bullet_width = 40
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3