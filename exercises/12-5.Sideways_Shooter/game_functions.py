import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, rocket, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_UP:
       rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    elif event.key ==pygame.K_SPACE:
        fire_bullet(ai_settings, screen, rocket, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, rocket):
    """ Respond to key releases"""
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    if event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(ai_settings, screen, rocket, bullets):
    """Respond to keypresses and most events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)

def update_screen(ai_settings, screen, rocket, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets, ai_settings):
    """ Update position of bullets and get rid of old bullets"""
    # Update bullets positions
    bullets.update()
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.left >= ai_settings.screen_width:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, rocket, bullets):
    """ Fire a bullet if limit not reached yet"""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, rocket)
        bullets.add(new_bullet)