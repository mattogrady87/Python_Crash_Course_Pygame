import sys
import pygame

# Keyboard events
def check_keydown_events(event, settings, screen, ship, 
    bullets):
    if event.key == pygame.K_q:
        sys.exit()
    
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    
    elif event.key == pygame.K_SPACE:
        for bullet in bullets:
            if bullet.need_reload == False:
                bullet.shooting_bullet = True

    elif event.key == pygame.K_r:
        bullets.empty()


def check_keyup_events(event, settings, screen, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(settings, screen, ship, bullets, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, 
                bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, screen, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, play_button, ship,
                bullets, mouse_x, mouse_y)

def check_bullet_target_collisions(settings, screen, bullets,
        target, stats):
    if pygame.sprite.spritecollideany(target, bullets):
        stats.target_hit = True
        stats.reset_tries()
        bullets.empty()


def start_game(settings, screen, stats, ship, bullets):
    """Start the game"""
    pygame.mouse.set_visible(False)
    stats.reset_tries()
    stats.game_running = True


def check_play_button(settings, screen, stats, play_button, ship, bullets, mouse_x,
     mouse_y):
     """ Start a new game when the player clicks play."""
     button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
     if button_clicked and not stats.game_running:
         start_game(settings, screen, stats, ship, bullets)

