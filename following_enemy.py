import random

import pygame

import entity
from utils import *

class FollowingEnemy(entity.Entity):

    def __init__(self, image, x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, size=64, speed=10):
        super().__init__(image, x, y, size, speed)
        self.offset = random.randint(-15, 15)
        self.offset2 = random.randint(-15, 15)

    def update(self, player, light_intensity):

        if self.x < player.x + self.offset:
            self.x += self.speed

        if self.x > player.x + self.offset:
            self.x -= self.speed

        if self.y < player.y + self.offset2:
            self.y += self.speed

        if self.y > player.y + self.offset2:
            self.y -= self.speed

        if self.get_rect().colliderect(player.get_rect()):
            if light_intensity.value - 8 >= -450:
                light_intensity.value -= 8

