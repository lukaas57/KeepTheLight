import random

import tileManager
import pygame
from utils import *
from value_tracker import ValueTracker
from player import Player
from following_enemy import FollowingEnemy
from counter import Counter
from source import Source

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
game_runing = True

icon = pygame.image.load(resource_path('assets/icon.png'))
pygame.display.set_icon(icon)

pygame.display.set_caption('Keep the light')


# Tile manager
tiles = tileManager.load_tiles(resource_path('assets/maps/KeepTheLight_tileset.png'), 16, 16)
game_map = tileManager.read_map(resource_path('assets/maps/forest/untitled._Tile Layer 1.csv'))
game_map_layer2 = tileManager.read_map(resource_path('assets/maps/forest/untitled._trees.csv'))

# objects of the game
player = None
enemies = []
source = None


# fog of war
darkness = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
light_intensity = None

# counter
counter_img = pygame.transform.scale(pygame.image.load(resource_path('assets/item/source.png')).convert_alpha(), (TILE_SIZE, TILE_SIZE))
counter = None

# score
score = None

# lose
lose = False
font = pygame.font.Font(resource_path('assets/fonts/PressStart2P.ttf'), 45)
surface = font.render(f'You lost!', False, 'red')
lost_text = surface.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

def new_game():
    global lose, game_runing, score, counter, player, enemies, source, light_intensity

    lose = False
    game_runing = True
    source = Source(resource_path('assets/item/source.png'))
    source.respawn(game_map, game_map_layer2)
    score = Counter(20, 20, color=(216,60,106), text='score:')
    counter = Counter(80,85, color=(255,130,116))
    player = Player('assets/player/player.png', speed=5, x=MAP_SIZE/2, y=MAP_SIZE/2)
    light_intensity = ValueTracker()

    enemies.clear()

    for i in range(10):
        enemies.append(
            FollowingEnemy(resource_path('assets/enemy/enemy.png'), speed=player.speed * (random.randint(1, 4) / 10),
                           x=random.randint(0, MAP_SIZE), y=random.randint(0, MAP_SIZE)))



def draw_darkness_overlay(screen, darkness, ellipse_size=(250, 200), max_opacity=230):
    darkness.fill((0, 0, 0, max_opacity))

    num_circles = 6
    for i in range(num_circles):
        factor = i / (num_circles - 1)
        size = (
            int(ellipse_size[0] * (1 + factor)),
            int(ellipse_size[1] * (1 + factor))
        )
        opacity = int(max_opacity * (1 - factor))

        ellipse_surface = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.ellipse(ellipse_surface, (0, 0, 0, opacity), (0, 0, *size))

        ellipse_rect = ellipse_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        darkness.blit(ellipse_surface, ellipse_rect, special_flags=pygame.BLEND_RGBA_SUB)

    screen.blit(darkness, (0, 0))

new_game()

light_power = 0.15

def update():
    global game_runing
    player.update(game_map, game_map_layer2)

    for enemy in enemies:
        enemy.update(player, light_intensity)

    source.update(player, counter, game_map, game_map_layer2, light_intensity)

    global light_power
    global lose

    if light_intensity.value - light_power  > -450:

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            light_power = 2
            player.speed = 12
        else:
            player.speed = 5
            light_power = 0.15

        light_intensity.value -= light_power
    else:
        light_intensity.value = -450
        game_runing = False
        lose = True

    counter.update()

    score.count += 1/FPS
    score.update()

def draw(screen):
    camera_offset = (SCREEN_WIDTH // 2 - player.x, SCREEN_HEIGHT // 2 - player.y)

    tileManager.draw_map(game_map, player,screen,tiles)

    player.draw(screen, camera_offset)

    tileManager.draw_map(game_map_layer2, player,screen,tiles)

    for enemy in enemies:
        enemy.draw(screen, camera_offset)

    source.draw(screen, camera_offset)

    # fog of war
    draw_darkness_overlay(screen,darkness, ellipse_size=(500+light_intensity.value, 450+light_intensity.value))

    # counter
    counter.draw(screen)
    screen.blit(counter_img, (10,70))

    #score
    score.draw(screen)

    if lose:
        screen.blit(surface, lost_text)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and game_runing == False:
            new_game()

    screen.fill((123, 24, 60))

    # RENDER YOUR GAME HERE
    if game_runing:
        update()

    draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
