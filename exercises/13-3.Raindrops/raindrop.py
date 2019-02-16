import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop(Sprite):
    """A class to represent a single raindrop in the grid"""

    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load_extended('images/raindrop.png')
        self.randomize_size()
        self.randomize_rain_drop_rate()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.right
        print(self.rect)
        self.y = self.rect.y
        
    
    def randomize_rain_drop_rate(self):
        self.random_rain_drop_rate = randint(1, 5)

    def randomize_size(self):
        # original is 511,750
        # WE want to change width between 14 and 27 and keep height
        randWidth = randint(14, 27)
        randHeight = int(((750/511) * randWidth))
        self.image = pygame.transform.scale(self.image, 
            (randWidth, randHeight))
    
    def update(self):
        """Move the raindrops down the screen"""
        self.y += (self.random_rain_drop_rate)
        self.rect.y = self.y