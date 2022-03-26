# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:49:41 2022

@author: smtur
"""

import pygame
from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import AlienFleet, Alien


class GameFunctions():

    def check_events(self, ship, settings):
        for ev in pygame.event.get():

            # print('in event loop ' + str(ev.type))
            if ev.type == pygame.QUIT:
                # print('quit key')
                return False

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_q:
                    # print('quit key')
                    return False
                self.check_keydown_events(ev, ship, settings)
            elif ev.type == pygame.KEYUP:
                self.check_keyup_events(ev, ship)
        return True

    def check_keydown_events(self, ev, ship, settings):
        if ev.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif ev.key == pygame.K_LEFT:
            ship.moving_left = True
        elif ev.key == pygame.K_UP:
            ship.moving_up = True
        elif ev.key == pygame.K_DOWN:
            ship.moving_down = True
        elif ev.key == pygame.K_SPACE:
            bullets = ship.bullets
            if len(bullets) < settings.ship_settings.max_bullets:
                new_bullet = Bullet(ship, settings)
                bullets.add(new_bullet)

    def check_keyup_events(self, ev, ship):
        if ev.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif ev.key == pygame.K_LEFT:
            ship.moving_left = False
        elif ev.key == pygame.K_UP:
            ship.moving_up = False
        elif ev.key == pygame.K_DOWN:
            ship.moving_down = False

    def update_screen(self, ship, settings, alien_fleet):
        settings.screen.fill(settings.game_settings.bg)
        ship.draw_bullets()
        ship.draw()
        alien_fleet.draw()
        pygame.display.flip()
        # print('flip')

    def collision_update(self, ship, alien_fleet):
        b = ship.bullets
        a = alien_fleet.aliens
        collisions = pygame.sprite.groupcollide(b, a, True, True)
        if len(a) == 0:
            b.empty()
            return True
        else:
            return False
        


        
