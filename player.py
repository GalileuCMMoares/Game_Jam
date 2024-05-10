import pygame
from configuraçao import *
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load("").convert_alpha() # espaço para colocar um png
        self.react = self.image.get_react(topleft = pos)

        self.direction = pygame.math.Vector2()

        def input(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
            else:
                self.direction.x = 0

        def update(self):
            self.input()