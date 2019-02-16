import pygame

class Ship():
    def __init__(self, screen, settings):
        """Intiailze the ship and sets its starting position"""
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load_extended('images/ship.png')
        self.width, self.height = self.image.get_size()
        self.resize_aspect(self.settings.ship_size)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 270)

        self.center_ship()
        self.move_float = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        self.rect.centery = self.screen.get_rect().centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def update(self, settings):
        if self.moving_up == True and self.rect.top > 0:
            self.move_float -= settings.ship_speed

        if (self.moving_down == True and self.rect.bottom <
            self.screen.get_rect().bottom):
                self.move_float += settings.ship_speed
        
        self.rect.centery = self.move_float
    
    def resize_aspect(self, new_width):
        """Change the size of image while keeping aspect ratio"""
        # (original height / original width) x new width = new height
        new_height = int(self.height / self.width) * new_width
        self.image = pygame.transform.scale(self.image, (new_width, 
            new_height))

