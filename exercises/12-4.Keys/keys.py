import pygame
from settings import Settings
import game_functions as gf
from keyholder import Keyholder


def run_game():
    # init
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Show me the Keys")

    keyholder = Keyholder(screen, None)

    while True:
        gf.check_events(keyholder)
        gf.print_event(screen, keyholder)

run_game()

