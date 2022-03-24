
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, settings):
        super().__init__()
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def update(self, settings):
        delta = settings.alien_speed_factor * settings.alien_direction
        self.x += delta
        self.rect.x = self.x

    def check_edges(self, settings):
        s = settings.screen.get_rect()
        if self.rect.right >= s.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False
