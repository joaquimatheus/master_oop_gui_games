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

