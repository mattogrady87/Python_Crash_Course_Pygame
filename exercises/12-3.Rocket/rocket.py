import pygame


class Rocket():
    def __init__(self, screen, ai_settings):
        """Initialize the rocket and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the rocket image and get its rect.
        self.image = pygame.image.load_extended('images/rocket.png')
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag"""
        # Update the ships center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.centery += self.ai_settings.ship_speed_factor

        # update the rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)
