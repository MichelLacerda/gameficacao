# -*- coding: utf-8 -*-
import pygame


class GameObject(pygame.sprite.Sprite):
    """Class Base for Sprite in Game."""
    sprite_group = pygame.sprite.Group()

    def __init__(self, x, y, image_src):
        pygame.sprite.Sprite.__init__(self)
        GameObject.sprite_group.add(self)

        self.image = pygame.image.load(image_src)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        self.sprite_group.draw(screen)

    def update(self, dt):
        pass

    def destroy(self, class_name):
        class_name.List.remove(self)
        GameObject.group.remove(self)
        del self
