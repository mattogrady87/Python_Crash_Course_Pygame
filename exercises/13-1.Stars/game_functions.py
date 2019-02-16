import sys
import pygame
from star import Star

def check_keydown_events(event):
    if event.key == pygame.K_q:
        sys.exit()

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)

def create_star(settings, screen, stars, star_row, star_number):
    """Create a star and place it"""
    star = Star(settings, screen)
    star.rect.left = 0 + (star.rect.width * star_number)
    star.rect.top = 0 + (star.rect.height * star_row)

    stars.add(star)

def create_grid(settings, screen, stars):
    star = Star(settings, screen)
    star_cols = int(settings.screen_width / star.rect.width) - 1
    star_rows = int(settings.screen_height / star.rect.height) - 1
    for star_row in range(star_rows):
        for star_number in range(star_cols):
            create_star(settings, screen, stars, star_row, star_number)


def update_screen(settings, screen, stars):
    screen.fill(settings.bg_color)
    stars.draw(screen)

    pygame.display.flip()