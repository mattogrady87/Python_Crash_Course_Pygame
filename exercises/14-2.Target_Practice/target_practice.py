import pygame
from pygame.sprite import Group

from stats import Stats
from settings import Settings
from target import Target
from ship import Ship
from button import Button
from bullet import Bullet
import game_functions as gf


def run_game():
    """initialize pygame, settings and screen object."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Target Practice")

    stats = Stats(settings)
    ship = Ship(screen, settings)
    target = Target(screen, settings)
    play_button = Button(settings, screen, "Play")
    bullets = Group()

    while True:
        gf.check_events(settings, screen, ship, bullets,stats, play_button)

        if stats.game_running:
            if len(bullets) == 0:
                stats.update_stats()
                print(stats.points)
                bullet = Bullet(screen, settings, ship)
                bullets.add(bullet)


            ship.update(settings)
            ship.blitme()

            bullets.update(ship)
            bullet.load_bullet(ship, settings)
            bullet.shoot_bullet(ship, bullets, settings)
            bullet.blitme()

            gf.check_bullet_target_collisions(settings, screen, bullets,
                target, stats)


            target.update()
            target.draw_target()

            pygame.display.flip()
            screen.fill(settings.bg_color)

run_game()