import sys
import pygame
from star import Star
from random import randint
import time

def check_keydown_events(event):
    if event.key == pygame.K_q:
        sys.exit()

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)

def create_star(settings, screen, stars, x, y):
    """Create a star and place it"""
    star = Star(settings, screen)
    star.rect.x = x
    star.rect.y = y

    stars.add(star)

def create_grid(settings, screen, stars):
    star = Star(settings, screen)
    for _ in range(100):
        x = randint(0, settings.screen_width - star.rect.right)
        y = randint(0, settings.screen_height - star.rect.bottom)
        create_star(settings, screen, stars, x, y)


def update_screen(settings, screen, stars):
    screen.fill(settings.bg_color)
    stars.draw(screen)
    stars.empty()
    create_grid(settings, screen, stars)
    pygame.display.flip()
    time.sleep(0.5)