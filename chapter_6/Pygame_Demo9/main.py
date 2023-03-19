import pygame
from pygame.locals import *
from SimpleButton import *
import sys

GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

def myCallBackFunction():
    print('User pressed Button B, called myCallBackFunction')

class CallBackTest():
    def __init__(self):
        pass

    def myMethod(self):
        print('User presssed Button C, called myMethod of the CallBackTest object')

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oCallBackTest = CallBackTest()
oButtonA = SimpleButton(window, (25, 30),
                        'images/buttonAUp.png',
                        'images/buttonBDown.png')

oButtonB = SimpleButton(window, (150, 30),
                        'images/buttonBUp.png',
                        'images/buttonBDown.png',
                        callBack=myCallBackFunction)

oButtonC = oButtonC = SimpleButton(window, (275, 30),
                                   'images/buttonCUp.png',
                                   'images/buttonCDown.png',
                                   callBack=oCallBackTest.myMethod)

counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButtonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')

        oButtonB.handleEvent(event)
        oButtonC.handleEvent(event)

    counter = counter + 1

    window.fill(GRAY)

    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)


