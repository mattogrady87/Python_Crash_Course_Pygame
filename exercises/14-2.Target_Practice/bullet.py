import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, screen, settings, ship):
        """Create a bullet object at the ship's current location"""
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        # Load image of bullet
        self.image = pygame.image.load_extended('images/bullet.png')
        self.width, self.height = self.image.get_size()
        self.resize_aspect(self.settings.bullet_size)
        self.rect = self.image.get_rect()
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right - self.rect.width
        self.need_reload = True
        self.float_x = float(self.rect.left)
        self.shooting_bullet = False

    def new_bullet(self):
        pass
        
    def load_bullet(self, ship, settings):
        if self.need_reload == True and (self.rect.left < 
                ship.rect.right):
            self.float_x += settings.bullet_reload
            self.rect.left = int(self.float_x)
        else:
            self.need_reload = False
    
    def shoot_bullet(self, ship, bullets, settings):
        if self.need_reload == False and self.shooting_bullet:
            if self.rect.left < self.screen_rect.right:
                self.rect.x += settings.bullet_speed
            elif self.rect.left >= self.screen_rect.right:
                 bullets.empty()


            
    def update(self, ship):
        if self.shooting_bullet == False:
            self.rect.centery = ship.rect.centery


    def blitme(self):
        """Draw teh bullet at its current location"""
        self.screen.blit(self.image, self.rect)

    def resize_aspect(self, new_width):
        """Change the size of image while keeping aspect ratio"""
        # (original height / original width) x new width = new height
        new_height = int(self.height / self.width) * new_width
        self.image = pygame.transform.scale(self.image, (new_width, 
            new_height))