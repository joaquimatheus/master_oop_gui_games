import pygame
from pygame.locals import *
import sys
import pygwidgets
from SimpleSprite import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)

pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

oWaterAnimation = SimpleSprite(window, (22, 140),
                                             'images/water_003.png',
                                             5, 50, 192, 192, .05)

oPlayButton = pygwidgets.TextButton(window, (60, 320), 'Play')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oWaterAnimation.play()

    oWaterAnimation.update()

    window.fill(BGCOLOR)

    oWaterAnimation.draw()
    oPlayButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
