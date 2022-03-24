# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 20:49:41 2022

@author: smtur
"""

import pygame
from ship import Ship
from alien import Alien
from settings import Settings
from bullet import Bullet
from alien import Alien


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
            if len(bullets) < settings.bullets_allowed:
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

    def update_screen(self, ship, aliens, settings):
        screen = settings.screen
        screen.fill(settings.bg)
        self.draw_bullets(ship, settings)
        ship.draw()
        self.draw_aliens(settings, aliens)
        pygame.display.flip()
        # print('flip')

    def draw_bullets(self, ship, settings):
        # Iterate a copy, since may be deleting item.
        bullets = ship.bullets
        bullets_copy = ship.bullets.copy()
        for bullet in bullets_copy:
            bullet.update_position()
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
            else:
                bullet.draw(settings)

    def create_alien_fleet(self, ship, settings, aliens):
        screen = settings.screen
        test_alien = Alien(screen)
        alien_w = test_alien.rect.width
        alien_h = test_alien.rect.height
        cols = self.num_aliens_per_row(settings, alien_w)
        rows = self.num_rows_of_aliens(settings, ship.rect.height, alien_h)
        for row in range(rows):
            for col in range(cols):
                alien = self.create_alien(settings, alien_w, alien_h, row, col)
                aliens.add(alien)

    def num_rows_of_aliens(self, settings, ship_h, h):
        h2 = h * 2
        h3 = h * 3
        avail_space = settings.h - h3 - ship_h
        num_rows = int(avail_space / h2)
        return num_rows

    def num_aliens_per_row(self, settings, w):
        w2 = w * 2
        avail_space = settings.w - w2
        num_aliens = int(avail_space / w2)
        return num_aliens

    def create_alien(self, settings, w, h, row, col):
        w2 = w * 2
        h2 = h * 2
        alien = Alien(settings)
        alien.x = w + w2 * col
        alien.rect.x = alien.x
        alien.rect.y = h + h2 * row
        return alien

    def check_alien_fleet_edges(self, settings, aliens):
        for alien in aliens.sprites():
            if alien.check_edges(settings):
                self.reverse_alien_fleet(settings, aliens)
                break

    def reverse_alien_fleet(self, settings, aliens):
        for alien in aliens.sprites():
            alien.rect.y += settings.alien_drop_speed_factor
        settings.alien_direction *= -1

    def draw_aliens(self, settings, aliens):
        self.check_alien_fleet_edges(settings, aliens)
        screen = settings.screen
        for alien in aliens:
            alien.draw(screen)
        
