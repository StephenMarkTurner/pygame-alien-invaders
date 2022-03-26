# -*- coding: utf-8 -*-
"""
"""


class Settings():
    def __init__(self):
        # I wasn't sure where wlse to put this var.
        # Set this!
        self.screen = None
        
        self.game_settings = GameSettings()
        self.ship_settings = ShipSettings()
        self.bullet_settings = BulletSettings()
        self.alien_fleet_settings = AlienFleetSettings()


class GameSettings():
    def __init__(self):
        self.caption = "Alien Invaders"
        self.w = 800
        self.h = 600
        self.bg = (230, 230, 230)


class ShipSettings():
    def __init__(self):
        self.speed_factor = 0.4
        self.max_bullets = 3


class BulletSettings():
    def __init__(self):
        self.speed_factor = 2
        #self.w = 3
        self.w = 100
        self.h = 15
        self.fg = (60, 60, 60)


class AlienFleetSettings():
    def __init__(self):
        self.speed_factor = 0.2
        self.drop_speed_factor = 1
        self.num_aliens_per_row = 5
        self.num_rows_of_aliens = 3
        # Right is 1, left is -1
        self.direction = 1
