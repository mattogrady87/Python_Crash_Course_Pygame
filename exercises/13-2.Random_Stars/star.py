import pygame
from pygame.sprite import Sprite 

class Star(Sprite):
    """ A class to represent a single star in the grid."""

    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load_extended('images/star.png')
        self.rect = self.image.get_rect()
        self.rect.size = 100,100


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        def blitme(self):
            self.screen.blit(self.image, self.rect)