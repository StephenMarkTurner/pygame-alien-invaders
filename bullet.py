from wsgiref.util import shift_path_info
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ship, settings):
        super().__init__()
        w = settings.bullet_width
        h = settings.bullet_height
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Store as float, for better resolution.
        self.y = float(self.rect.y)
        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update_position(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw(self, settings):
        pygame.draw.rect(settings.screen, self.color, self.rect)
