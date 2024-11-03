import pygame 
from os.path import join 
from os import walk
from os.path import join, dirname, abspath

ASSETS_DIR = join(dirname(dirname(abspath(__file__))), "images")

WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720 
TILE_SIZE = 64
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))