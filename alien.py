
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

from settings import Settings


# Singleton, please
class AlienFleet():

    def __init__(self, settings):
        self.settings = settings
        self.aliens = Group()
        test_alien = Alien(self.settings)
        alien_width = test_alien.rect.w
        alien_height = test_alien.rect.h
        for row in range(self.settings.alien_fleet_settings.num_rows_of_aliens):
            for col in range(self.settings.alien_fleet_settings.num_aliens_per_row):
                alien = self.create_alien(alien_width, alien_height, row, col)
                self.aliens.add(alien)

    def num_rows_of_aliens(self, ship_height, alien_height):
        h2 = alien_height * 2
        h3 = alien_height * 3
        avail_space = self.settings.screen_settings.h - h3 - ship_height
        num_rows = int(avail_space / h2)
        return num_rows

    def num_aliens_per_row(self, w):
        w2 = w * 2
        avail_space = self.settings.screen_settings.w - w2
        num_aliens = int(avail_space / w2)
        return num_aliens

    def create_alien(self, w, h, row, col):
        w2 = w * 2
        h2 = h * 2
        alien = Alien(self.settings)
        alien.x = w + w2 * col
        alien.rect.x = alien.x
        alien.rect.y = h + h2 * row
        return alien

    def update(self):
        self.aliens.update()

    def check_alien_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.reverse_alien_fleet()
                break

    def reverse_alien_fleet(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_fleet_settings.drop_speed_factor
        self.settings.alien_fleet_settings.direction *= -1
        
    def draw(self):
        self.check_alien_fleet_edges()
        self.aliens.draw(self.settings.screen)


class Alien(Sprite):

    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    # def draw(self,screen):
    #    screen.blit(self.image, self.rect)

    def update(self):
        sf = self.settings.alien_fleet_settings.speed_factor
        d = self.settings.alien_fleet_settings.direction
        delta = sf * d
        self.x += delta
        self.rect.x = self.x

    def check_edges(self):
        w = self.settings.game_settings.w
        if self.rect.right >= w:
            return True
        elif self.rect.left <= 0:
            return True
        return False
