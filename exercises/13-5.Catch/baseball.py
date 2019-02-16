import pygame
from pygame.sprite import Sprite
from random import randint


class Baseball(Sprite):
    def __init__(self, screen, settings):
        """Initialize the baseball"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load_extended('images/baseball.png')
        self.scale_aspect(settings.ball_size)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #self.rect.centerx = self.screen_rect.centerx
        self.rect.centerx = randint(self.image.get_width(), 
            settings.screen_width - self.image.get_width())

        self.rect.top = self.screen_rect.top
        self.center = float(self.rect.top)


    def scale_aspect(self, new_width):
        curr_height = self.image.get_height()
        curr_width = self.image.get_width()
        new_height = int((curr_height / curr_width) * new_width)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))


    def update(self, settings):
        """update the ball's position"""
        self.center += settings.ball_move_speed
        self.rect.top = self.center

    
