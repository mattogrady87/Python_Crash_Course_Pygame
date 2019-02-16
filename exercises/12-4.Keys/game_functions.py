import pygame
import sys


def check_events(keyholder):
    """Respone to keypresses and most events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            keyholder.currentkey = event.key

def print_event(screen, keyholder):
    text = keyholder.basicfont.render("hello world",
        True, (255, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.fill((230, 0, 0))
    screen.blit(text, textrect)