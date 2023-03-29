import pygame
import time

class SimpleAnimation():
    def __init__(self, window, loc, picPaths, durationPerImage):
        self.window = window
        self.loc = loc
        self.imagesList = []

        for picPath in picPaths:
            image = pygame.image.load(picPath)
            image = pygame.Surface.convert_alpha(image)
            self.imagesList.append(image)

        self.playing = False
        self.durationPerImage = durationPerImage
        self.nImages = len(self.imagesList)
        self.index = 0

    def play(self):
        if self.playing:
            return

        self.playing = True
        self.imageStartTime = time.time()
        self.index = 0

    def update(self):
        if not self.playing:
            return

        self.elapsed = time.time() - self.imageStartTime

        if self.elapsed > self.durationPerImage:
            self.index = self.index + 1

            if self.index < self.nImages:
                self.imageStartTime = time.time()
            else:
                self.playing = False
                self.index = 0

    def draw(self):
        
        theImage = self.imagesList[self.index]

        self.window.blit(theImage, self.loc)
