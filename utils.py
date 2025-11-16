import os
import sys
import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60
TILE_SIZE = 64
MAP_SIZE = TILE_SIZE*30

def setSize(width, height):
    global SCREEN_WIDTH,SCREEN_HEIGHT
    SCREEN_WIDTH = width
    SCREEN_HEIGHT = height


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


