import pygame

from utils import *

collide_tiles = [21, 22, 23, 33, 41, 43, 50, 51, 61, 62, 63, 101, 102, 104, 106, 109, 110, 111, 113, 121, 122, 126, 129,
                 130, 131, 133, 144, 145, 146, 147, 149, 150, 151, 166]


def load_tiles(tilesheet, tile_width, tile_height):
    tilesheet = pygame.image.load(tilesheet).convert_alpha()
    sheet_width, sheet_height = tilesheet.get_size()
    tiles = []
    for y in range(0, sheet_height, tile_height):
        for x in range(0, sheet_width, tile_width):
            tile = tilesheet.subsurface(pygame.Rect(x, y, tile_width, tile_height))
            tile = pygame.transform.scale(tile, (64, 64))
            tiles.append(tile)
    return tiles


def read_map(map_file):
    game_map = []

    with open(map_file, 'r') as f:
        rows = f.read().split('\n')
        for row in rows:
            row_tiles = row.split(',')
            game_map.append(row_tiles)

    return game_map


def draw_map(game_map, player, screen, tiles):
    x_offset = SCREEN_WIDTH // 2 - player.x
    y_offset = SCREEN_HEIGHT // 2 - player.y

    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            if tile == -1:
                continue

            draw_x = x_offset + x * 64
            draw_y = y_offset + y * 64

            if -64 < draw_x < SCREEN_WIDTH and -64 < draw_y < SCREEN_HEIGHT:
                screen.blit(tiles[int(tile)], (draw_x, draw_y))


def collision(player, game_map, direction, speed):
    half_size = player.size * 0.3
    future_x = player.x
    future_y = player.y

    if direction == 'UP':
        future_y -= speed
    elif direction == 'DOWN':
        future_y += speed
    elif direction == 'LEFT':
        future_x -= speed
    elif direction == 'RIGHT':
        future_x += speed

    corners = [
        (future_x - half_size, future_y - half_size),  # top-left
        (future_x + half_size, future_y - half_size),  # top-right
        (future_x - half_size, future_y + half_size),  # bottom-left
        (future_x + half_size, future_y + half_size),  # bottom-right
    ]

    for corner_x, corner_y in corners:
        tile_x = int(corner_x // TILE_SIZE)
        tile_y = int(corner_y // TILE_SIZE)

        if tile_y < 0 or tile_y >= len(game_map) or tile_x < 0 or tile_x >= len(game_map[0]):
            return True

        if int(game_map[tile_y][tile_x]) in collide_tiles:
            return True

    return False