import pygame.font

from utils import *


class Counter:

    def __init__(self, x, y, text='', color='black', size=45 ):
        self.x = x
        self.y = y

        self.size = size

        self.text = text

        self.count = 0

        self.color = color

        self.font = pygame.font.Font(resource_path('assets/fonts/PressStart2P.ttf'), self.size)
        self.surface = self.font.render(f'{self.text}{int(self.count)}', False, self.color)


    def update(self):
        self.surface = self.font.render(f'{self.text}{int(self.count)}', False, self.color)


    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))


    def reset(self):
        self.count = 0
        self.surface = self.font.render(f'{self.text}{int(self.count)}', False, self.color)



