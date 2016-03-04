# -*- coding: utf-8 -*-
# import os
import sys
import pygame
from pygame.locals import *
from local_settings import *
from color import *
from characters import Player
from engine import GameObject


class Game(object):
    def __init__(self):
        pygame.init()
        self. display = pygame.display.Info()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE,
                                              0,
                                              self.display.bitsize)

        self.player = Player(100, 100, "player.bmp")
    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000.0
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            GameObject.sprite_group.draw(self.screen)
            self.player.update(dt)

            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
