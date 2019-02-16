import pygame
from pygame.sprite import Group

from settings import Settings
from rocket import Rocket
import game_functions as gf


def run_game():
    # Initilize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")

    # Make a rocket
    rocket = Rocket(screen, ai_settings)
    # Make a group to store bullets in
    bullets = Group()

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, rocket, bullets)
        rocket.update() 
        gf.update_bullets(bullets, ai_settings)

        gf.update_screen(ai_settings, screen, rocket, bullets)




run_game()
