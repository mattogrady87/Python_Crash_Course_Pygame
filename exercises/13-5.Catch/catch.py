import pygame
from pygame.sprite import Group

from settings import Settings
from glove import Glove
from baseball import Baseball
import game_functions as gf
from score import Score


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Catch")

    # Make a glove
    score = Score(settings)
    glove = Glove(screen, settings)

    baseball = Baseball(screen, settings)
    baseballs = Group()
    #baseballs.add(baseball)
    

    while True:
        gf.check_events(settings, screen, glove, score)
        glove.update()
        gf.update_baseballs(settings, baseballs, glove, screen, score)
        gf.update_screen(settings, screen, glove, baseballs)

run_game()
