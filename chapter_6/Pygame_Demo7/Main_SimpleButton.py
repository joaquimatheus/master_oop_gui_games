import pygame
from pygame.locals import *
from SimpleButton import *
import sys

GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINOOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINOOW_HEIGHT))
clock = pygame.time.Clock()

oButton = SimpleButton(window, (150, 30),
                       'images/buttonUp.png',
                       'images/buttonDown.png')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButton.handleEvent(event):
            print('User has clicked the button')

    window.fill(GRAY)

    oButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
