from pygame.locals import *
import pygwidgets
import sys
import pyhame
from BallonMgr import *

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                                       'Score: 0', textColor=BLACK,
                                       backgroundColor=None, width=140, fontSize=24)

oStatusDisplay = pygwidgets.DisplayText(window, (100, USABLE_WINDOW_HEIGHT + 15),
                                        '', textColor=BLACK, backgroundColor=None,
                                        width=300, fontSize=24)
oStartButton = pygwidgets.TextButton(window,
                                     (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'Start')

oBallonMgr = BallonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False

while True:
    nPointsEarned = 0
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            oBallonMgr.handleEvent(event)
            theScore = oBallonMgr.getScore()
            oScoreDisplay.setValue('Score ' + str(theScore))

        elif oStartButton.handleEvent(event):
            oBallonMgr.start()
            oScoreDisplay.setValue('Score: 0')
            playing = True

    if playing:
        oBallonMgr.update()
        nPopped = oBalloonMgr.getCountPopped()
        nMissed = oBalloonMgr.getCountMissed()
        oStatusDisplay.setValue('Popped: ' + str(nPopped) +
                                '  Missed: ' + str(nMissed) +
                                '  Out of: ' + str(N_BALLONS))

        if (nPopped + nMissed) == N_BALLONS:
            playing = False
            oStartButton.enable()

    window.fill(BACKGROUND_COLOR)

    if playing:
        oBalloonMgr.draw()
    
    pygame.draw.rect(window, GRAY, pygame.Rect(0,
                                               USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))

    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)

