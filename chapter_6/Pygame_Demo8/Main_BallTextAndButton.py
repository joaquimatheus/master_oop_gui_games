import pygame
from pygame.locals import *
import sys
import random
from Ball import *
from SimpleText import *
from SimpleButton import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (60, 20),
                              'Program has run throught this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (200, 60), 'images/restartUp.png', 'images/restartDown.png')
frameCounter = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):
            frameCounter = 0

    oBall.update()
    frameCounter = frameCounter + 1
    oFrameCountDisplay.setValue(str(frameCounter))

    window.fill(BLACK)

    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
