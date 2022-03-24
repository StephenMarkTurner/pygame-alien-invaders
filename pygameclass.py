# -*- coding: utf-8 -*-
"""
"""

import pygame
from settings import Settings


class Pygame():
    def __init__(self, settings):
        print('init game')
        pygame.init()
        pygame.display.set_caption(settings.caption)
        settings.screen = pygame.display.set_mode((settings.w, settings.h))

    def quit_game(self):
        print('quit game')
        pygame.quit()
