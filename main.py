# -*- coding: utf-8 -*-
"""
"""

import sys
import pygame
from pygameclass import Pygame
from pygame.sprite import Group

from ship import Ship
from alien import Alien
from settings import Settings
from game_functions import GameFunctions


def game_loop(settings):
    game_functions = GameFunctions()
    screen = settings.screen
    ship = Ship(screen)
    aliens = Group()
    game_functions.create_alien_fleet(ship, settings, aliens)
    keep_going = True
    while keep_going:
        keep_going = game_functions.check_events(ship, settings)
        ship.update()
        aliens.update(settings)
        game_functions.update_screen(ship, aliens, settings)

        pygame.time.delay(5)


print('starting program')
settings = Settings()
pg = Pygame(settings)
game_loop(settings)
pg.quit_game()

print('finished program, calling sys.exit()')
sys.exit()
