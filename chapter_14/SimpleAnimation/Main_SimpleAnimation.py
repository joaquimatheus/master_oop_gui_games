import pygame
from pygame.locals import *
import sys
import pygwidgets
from SimpleAnimation import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)

pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

dinosaurAnimTuple = ('images/Dinobike/f1.gif',
                      'images/Dinobike/f2.gif',
                      'images/Dinobike/f3.gif',
                      'images/Dinobike/f4.gif',
                      'images/Dinobike/f5.gif',
                      'images/Dinobike/f6.gif',
                      'images/Dinobike/f7.gif',
                      'images/Dinobike/f8.gif',
                      'images/Dinobike/f9.gif',
                      'images/Dinobike/f10.gif')

oDinosaurAnimation = SimpleAnimation(window, (22, 140),
                                     dinosaurAnimTuple, .1)

oPlayButton = pygwidgets.TextButton(window, (20, 240), 'Play')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oDinosaurAnimation.play()

    oDinosaurAnimation.update()

    window.fill(BGCOLOR)

    oDinosaurAnimation.draw()
    oPlayButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
