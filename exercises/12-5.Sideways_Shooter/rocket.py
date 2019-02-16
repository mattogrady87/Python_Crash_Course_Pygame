import pygame

class Rocket():
    def __init__(self, screen, ai_settings):
        """Initialize the rocket and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect
        self.image = pygame.image.load_extended('images/rocket.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the left/middle of the screen
        self.rect.centery = self.screen_rect.centery
        #self.rect.left = self.screen_rect.left

        # Store a decimal value for the ships center
        self.center = float(self.rect.centery)


        # Movement flag
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect
        if self.moving_up and self.rect.top > (self.screen_rect.top-45):
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < (self.screen_rect.bottom+50):
            self.center += self.ai_settings.ship_speed_factor

        # Update the rect object from self.center
        self.rect.centery = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)