import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from abc import ABC, abstractmethod

class Balloon(ABC):
    popSoundLoaded = False
    popSound = None

    @abstractmethod
    def __init__(self, window, maxWidth, maxHeight, ID,
                 oImage, size, nPoints, speedY):
        self.window = window
        self.ID = ID
        self.balloonImage = oImage
        self.size = size
        self.nPoints = nPoints
        self.speedY = speedY

        if not Balloon.popSoundLoaded:
            Balloon.popSoundLoaded = True
            Balloon.popSound = pygame.mixer.Sound('sounds/balloonPop.wav')

        balloonRect = self.balloonImage.getRect()
        self.width = balloonRect.width
        self.height = balloonRect.height

        self.x = random.randrange(maxWidth - self.width)
        self.y = maxHeight + random.randrange(75)
        self.balloonImage.setLoc((self.x, self.y))

    def clickedInside(self, mousePoint):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return True, self.nPoints
        else:
            return False, 0

    def update(self):
        self.y = self.y - self.speedY
        self.balloonImage.setLoc((self.x, self.y))
        if self.y < -self.height:
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        self.balloonImage.draw()

    def __del__(self):
        print(self.size, 'Balloon', self.ID, 'is going away')

class BalloonSmall(Balloon):
    balloonImage = pygame.image.load('images/redBalloonSmall.png')
    
    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonSmall.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID,
                         oImage, 'Small', 30, 3.1)

class BalloonMedium(Balloon):
    balloonImage = pygame.image.load('images/redBalloonMedium.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonMedium.balloonImage)

        super().__init__(window, maxWidth, maxHeight, ID, oImage, 'Medium', 20, 2.2)

class BalloonLarge(Balloon):
    balloonImage = pygame.image.load('images/redBalloonMedium.png')
    def __init__(self, window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0, 0),
                                  BalloonLarge.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID, oImage, 'Large', 10, 1.5)
