import pygame

class Glove():
    def __init__(self, screen, settings):
        """Intialize a baseball glove to move to catch the ball"""
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load_extended('images/glove.png')

        self.scale_aspect(settings.glove_size)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Center glove based on screen's rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Make self.center a float that can take decimals
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False


    def scale_aspect(self, new_width):
        curr_height = self.image.get_height()
        curr_width = self.image.get_width()
        new_height = int((curr_height / curr_width) * new_width)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))


    def update(self):
        """update the gloves position based on movement flags"""
        if (self.moving_right and self.rect.right < 
                self.screen_rect.right):
            self.center += self.settings.glove_move_speed

        if (self.moving_left and self.rect.left > 0):
            self.center -= self.settings.glove_move_speed

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
