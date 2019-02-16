class Settings():
    """A Class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 230, 0)

        # Ship Settings
        self.ship_speed_factor = 1.5
