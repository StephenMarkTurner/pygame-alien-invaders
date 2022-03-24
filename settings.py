# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:37:25 2022

@author: smtur
"""

class Settings():
    def __init__(self):
        self.caption = "Alien Invaders"
        self.w = 800
        self.h = 600
        self.bg = (230,230,230)
        self.screen = None
        
        self.speed = 0.5
        self.bullet_speed_factor = 0.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        self.alien_speed_factor = 0.4
        self.alien_drop_speed_factor = 1
        # 1 for right, -1 for left
        self.alien_direction = 1


