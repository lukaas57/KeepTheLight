import random

import item
from utils import *
import tileManager

class Source(item.Item):

    def __init__(self, image, x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, size=64):
        super().__init__(image, x, y, size)

    def update(self, player, counter, game_map, game_map_layer2, light_intensity):

        if player.get_rect().colliderect(self.get_rect()):
            counter.count += 1
            if light_intensity.value < -10:
                light_intensity.value += 80
            self.respawn(game_map, game_map_layer2)

    def respawn(self, game_map, game_map_layer2, max_attempts=1000):
        rows = len(game_map)
        cols = len(game_map[0])

        for _ in range(max_attempts):
            x_tile = random.randint(0, cols - 1)
            y_tile = random.randint(0, rows - 1)

            if (int(game_map[y_tile][x_tile]) not in tileManager.collide_tiles and
                    int(game_map_layer2[y_tile][x_tile]) not in tileManager.collide_tiles):

                self.x = x_tile * TILE_SIZE + TILE_SIZE // 2
                self.y = y_tile * TILE_SIZE + TILE_SIZE // 2
                self.get_rect()
                return

        raise Exception("Could not find valid spawn tile after many attempts.")
