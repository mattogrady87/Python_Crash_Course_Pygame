import sys
import pygame
from raindrop import Raindrop
from time import sleep
from random import randint

def check_keydown_events(event):
    if event.key == pygame.K_q:
        sys.exit()
    
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)

def create_rain(settings, screen, raindrops, x):
    """Create a raindrop an place it"""
    raindrop = Raindrop(settings, screen)
    raindrop.rect.x = x
    raindrops.add(raindrop)
    print(len(raindrops))

def drop_rain(settings, screen, raindrops):
    """When we get ~20 raindrops, we'll drop them"""
    if len(raindrops) >= 20:
        print("were in here")
        raindrops.update()

def remove_rain(settings, screen, raindrops):
    """Delete rain when it gets below screen"""
    for raindrop in raindrops:
        if raindrop.rect.y >= settings.screen_height:
            raindrops.remove(raindrop)


def create_grid(settings, screen, raindrops):
    """Call create_rain with updated x value"""
    x = randint(0, settings.screen_width)
    create_rain(settings, screen, raindrops, x)

def update_screen(settings, screen, raindrops):
    screen.fill(settings.bg_color)
    create_grid(settings, screen, raindrops)
    raindrops.update()
    #drop_rain(settings, screen, raindrops)
    remove_rain(settings, screen, raindrops)
    raindrops.draw(screen)
    
    pygame.display.flip()
    sleep(settings.rain_make_rate)


