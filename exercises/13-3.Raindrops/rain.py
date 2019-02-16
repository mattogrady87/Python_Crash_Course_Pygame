import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf
from raindrop import Raindrop


def run_game():
    # initialize pygame, settings and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Rain Drops")
    #raindrop = Raindrop(settings, screen)
    raindrops = Group()

    while True:
        gf.check_events()
        gf.update_screen(settings, screen, raindrops)

run_game()

