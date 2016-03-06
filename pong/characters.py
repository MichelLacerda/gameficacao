# -*- coding: utf-8 -*-
import pygame
from engine import GameObject


class Player(GameObject):
    """Class Base for Player."""
    sprite_group = pygame.sprite.Group()

    def __init__(self, screen, x, y, image_src):
        GameObject.__init__(self, screen, x, y, image_src)
        Player.sprite_group.add(self)
        self.keyboard = {
            'UP': pygame.K_UP,
            'DOWN': pygame.K_DOWN,
        }

    def draw(self, screen):
        super(Player, self).draw(screen)
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         ((self.rect.x, self.rect.y), (16, 64)))

    def update(self, dt):
        key = pygame.key.get_pressed()
        if key[self.keyboard.get('UP')]:
            self.rect.y -= 300 * dt
        elif key[self.keyboard.get('DOWN')]:
            self.rect.y += 300 * dt

