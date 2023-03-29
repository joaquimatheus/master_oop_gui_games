import pygame
import pyghelpers
from SceneA import *
from SceneB import *
from SceneC import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 180
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

scenesList = [SceneA(window),
              SceneB(window),
              SceneC(window)]

oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)
oSceneMgr.run()
