import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from star import Star


def run_game():
    # intialize pygame, settings and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Star Grid")
    star = Star(settings, screen)
    stars = Group()

    gf.create_grid(settings, screen, stars)
    while True:
        gf.check_events()
        gf.update_screen(settings, screen, stars)


run_game()