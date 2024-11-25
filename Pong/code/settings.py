import pygame
from random import choice, uniform
import os

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
SIZE = {'paddle': (40,100), 'ball': (30,30)}
POS = {'player': (WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2), 'opponent': (50, WINDOW_HEIGHT / 2)}
SPEED = {'player': 500, 'opponent': 250, 'ball': 450}
COLOURS = {
    'paddle': '#ee322c',
    'paddle shadow': '#b12521',
    'ball': '#ee622c',
    'bg': '#002633',
    'bg detail': '#004a63'
}