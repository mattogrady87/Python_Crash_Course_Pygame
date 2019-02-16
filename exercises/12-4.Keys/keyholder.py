import pygame


class Keyholder():
    def __init__(self, screen, currentkey):
        """This class will hold the key event until processed"""
        self.currentkey = currentkey
        self.basicfont = pygame.font.SysFont('Ubuntu', 48)
