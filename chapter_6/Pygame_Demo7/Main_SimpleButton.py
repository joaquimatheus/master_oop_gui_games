import pygame
from pygame.locals import *
from SimpleButton import *
import sys

GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINOOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.clock()
