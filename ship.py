# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:44:53 2022

@author: smtur
"""

import pygame
from settings import Settings
from pygame.sprite import Group


class Ship():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.settings = Settings()
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.bullets = Group()

        print(self)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.settings.speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.settings.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.speed
        # TBD Truncate to integer?
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def draw(self):
        self.screen.blit(self.image, self.rect)
