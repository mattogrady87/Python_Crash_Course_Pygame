import sys
import pygame
from baseball import Baseball


def check_keydown_events(event, settings, screen, glove, score):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        glove.moving_right = True
    elif event.key == pygame.K_LEFT:
        glove.moving_left = True
    elif event.key == pygame.K_q:
        print("DUH DUH DUH High Score: {}".format(score.high_score))
        sys.exit()

def check_keyup_events(event, glove):
    """Respond to keys being let go of"""
    if event.key == pygame.K_RIGHT:
        glove.moving_right = False
    elif event.key == pygame.K_LEFT:
        glove.moving_left = False

def catch_ball(settings, baseballs, glove, score):
    for ball in baseballs:
        if ball.rect.colliderect(glove.rect):
            score.increase_score()
            baseballs.remove(ball)
        elif ball.rect.top > settings.screen_height:
            score.decrease_score()
            baseballs.remove(ball)

def respawn_balls(settings, baseballs, screen):
    if len(baseballs) == 0:
        baseball = Baseball(screen, settings)
        baseballs.add(baseball)

def check_events(settings, screen, glove, score):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, glove, score)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, glove)

def update_baseballs(settings, baseballs, glove, screen, score):
    """update the positions of all baseballs in group"""
    baseballs.update(settings)
    catch_ball(settings, baseballs, glove, score)
    respawn_balls(settings, baseballs, screen)

def update_screen(settings, screen, glove, baseballs):
    """update the images on the screen and flip to the new screen"""
    screen.fill(settings.bg_color)
    glove.blitme()
    baseballs.draw(screen)

    pygame.display.flip()
