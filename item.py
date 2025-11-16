import math

from utils import *


class Item:

    def __init__(self, image, x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, size=64):
        self.x = x
        self.y = y

        self.size = size

        self.image = pygame.transform.scale(pygame.image.load(resource_path(image)).convert_alpha(), (size, size))

    def get_rect(self, camera_offset=(0,0)):
        return self.image.get_rect(center=(self.x + camera_offset[0], self.y +camera_offset[1]))

    def draw(self, screen, camera_offset=(0,0)):
        screen.blit(self.image, self.get_rect(camera_offset))

    def get_distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
