import pygame
from pygame.sprite import Sprite

class Target(Sprite):
    """A Class to create the rectangle target"""

    def __init__(self, screen, settings):
        """Create a target object at the right side of screen"""
        super().__init__()
        self.screen = screen
        self.color = settings.target_color
        self.settings = settings
        # 1 means up, 0 means down
        self.moving_up = True
        self.moving_down = False


        self.screen_rect = screen.get_rect()

        # Create a rectangle at right-hand side of screen
        self.rect = pygame.Rect(0,0, settings.target_width,
            settings.target_height)
        
        self.float_move = float(self.screen_rect.centery)
        self.rect.centery = self.float_move
        self.rect.x = self.screen_rect.right - settings.target_width

    def draw_target(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    
    def check_top_bottom(self):
        if self.rect.top <= 0:
            self.moving_up = False
            self.moving_down = True
        if self.rect.bottom >= self.screen_rect.bottom:
            self.moving_up = True
            self.moving_down = False

    def update(self):
        self.check_top_bottom()
        if self.moving_up:
            self.float_move -= self.settings.target_speed
        if self.moving_down:
            self.float_move += self.settings.target_speed
        self.rect.centery = self.float_move
