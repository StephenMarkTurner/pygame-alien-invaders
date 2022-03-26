

import pygame
from pygame.sprite import Sprite
from settings import Settings


class Bullet(Sprite):

    def __init__(self, ship, settings):
        super().__init__()
        self.screen = settings.screen
        bs = settings.bullet_settings
        self.sf = settings.bullet_settings.speed_factor
        self.fg = settings.bullet_settings.fg
        self.rect = pygame.Rect(0, 0, bs.w, bs.h)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Store as float, for better resolution.
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.sf
        self.rect.y = self.y

    # No self.image, so cannot use Group draw() functionality.
    def draw(self):
        pygame.draw.rect(self.screen, self.fg, self.rect)
