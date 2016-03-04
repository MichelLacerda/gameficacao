# -*- coding: utf-8 -*-
import pygame
from engine import GameObject


class Player(GameObject):
    sprite_group = pygame.sprite.Group()

    def __init__(self, x, y, image_src):
        GameObject.__init__(self, x, y, image_src)
        Player.sprite_group.add(self)

    def update(self, dt):
        self.rect.x += 80 * dt



