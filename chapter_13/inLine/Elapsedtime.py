import pygame
from pygame.locals import *
import sys
import pygwidgets
import time

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
WHITE = (255, 255, 255)
FRAMES_PER_SECOND = 30
TIMER_LENGTH = 2.5

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Click "Start" to start a ' +
                                       str(TIMER_LENGTH) + ' second time:',
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)

startButton = pygwidgets.TextButton(window, (200, 100), 'Start')
clickMeButton = pygwidgets.TextButton(window, (320, 100), 'Click me')
timerMessage = pygwidgets.DisplayText(window, (0, 100), 'Message showing during time',
                                      fontSize=36, justified='center', width=WINDOW_WIDTH)

timerMessage.hide()
timerRunning = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):
            timeStarted = time.time()
            startButton.disable()
            timerMessage.show()
            print('Starting timer')
            timerRunning = True

        if clickMeButton.handleEvent(event):
            print('Other button was clicked')

    if timerRunning:
        elapsed = time.time()
        if elapsed >= TIMER_LENGTH:
            startButton.enable()
            timerMessage.hide()
            print('Timer ended by elapsed time')
            timerRunning = False

    window.fill(WHITE)

    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
