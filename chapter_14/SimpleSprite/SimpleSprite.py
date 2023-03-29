import pygame
import time

class SimpleSpriteSheetAnimation():

    def __init__(self, window, loc, imagePath, nImages, width, height, durationPerImage):
        self.window = window
        self.loc = loc
        self.nImages = nImages
        self.imagesList = []

        spritesSheetImage = pygame.image.load(imagePath)
        spritesSheetImage = pygame.Surface.convert_alpha(spriteSheetImage)

        nCols = spriteSheetImage.get_width() // width

        row = 0
        col = 0

        for imageNumber in range(nImages):
            x = col * height
            y = row * width

            subsurfaceRect = pygame.Rect(x, y, width, height)
            image = spriteSheetImage.subsurface(subsurfaceRect)
            self.images

            col = col + 1
            if col == nCols:
                col = 0
                row = row + 1

        self.durationPerImage = durationPerImage
        self.playing = False
        self.index =0

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
