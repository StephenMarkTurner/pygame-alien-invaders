# -*- coding: utf-8 -*-
"""
"""

from pickle import FALSE
import sys
import pygame

from ship import Ship
from alien import Alien, AlienFleet
from settings import Settings
from game_functions import GameFunctions


def game_loop(ship, settings, alien_fleet):
    keep_going = True
    while keep_going:
        keep_going = game_functions.check_events(ship, settings)
        ship.update()
        alien_fleet.update()
        if(game_functions.collision_update(ship, alien_fleet)):
            alien_fleet = AlienFleet(settings)
        game_functions.update_screen(ship, settings, alien_fleet)

        pygame.time.delay(5)


def pygame_init(settings):
    print('init game')
    pygame.init()
    gs = settings.game_settings
    pygame.display.set_caption(gs.caption)
    screen = pygame.display.set_mode((gs.w, gs.h))
    return screen


print('starting program')
settings = Settings()
settings.screen = pygame_init(settings)
ship = Ship(settings)
alien_fleet = AlienFleet(settings)
game_functions = GameFunctions()

game_loop(ship, settings, alien_fleet)

print('quit game')
pygame.quit()
sys.exit()
