import pygame
import tileManager
import entity
from utils import *


class Player(entity.Entity):

    def __init__(self, image, x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, size=64, speed=10):
        super().__init__(image, x, y, size, speed)

    def update(self, game_map, game_map_layer2):
        keys = pygame.key.get_pressed()
        speed = self.speed

        if (keys[pygame.K_DOWN] and (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT])) or (
                keys[pygame.K_UP] and (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT])):
            speed = self.speed * 0.7

        if keys[pygame.K_LEFT] and not (
                tileManager.collision(self, game_map, 'LEFT', speed) or tileManager.collision(self, game_map_layer2,
                                                                                              'LEFT', speed)):
            self.x -= speed

        if keys[pygame.K_RIGHT] and not (
                tileManager.collision(self, game_map, 'RIGHT', speed) or tileManager.collision(self, game_map_layer2,
                                                                                               'RIGHT', speed)):
            self.x += speed

        if keys[pygame.K_UP] and not (
                tileManager.collision(self, game_map, 'UP', speed) or tileManager.collision(self, game_map_layer2,
                                                                                            'UP', speed)):
            self.y -= speed

        if keys[pygame.K_DOWN] and not (
                tileManager.collision(self, game_map, 'DOWN', speed) or tileManager.collision(self, game_map_layer2,
                                                                                              'DOWN', speed)):
            self.y += speed
