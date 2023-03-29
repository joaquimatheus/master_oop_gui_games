import pygame
from pygame.locals import *
import pygwidgets
import random
import sys

GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'

STATE_SPLASH = 'Splash'
STATE_PLAYER_CHOICE = "PlayerChoice"
STATE_SHOW_RESULTS = "ShowResults"

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

messageField = pygwidgets.DisplayText(window, (15, 25), "Welcome to Rock, Paper, Scissors!",
                                      fontSize=50, textColor = WHITE, width= 610, justified = 'center')

rockImage = pygwidgets.Image(window, (25, 120), 'images/Rock.png')
paperImage = pygwidgets.Image(window, (255, 120), 'images/Paper.png')
scissorsImage = pygwidgets.Image(window, (425, 120), 'images/Scissors.png')

startbutton = pygwidgets.CustomButton(window, (210, 300),
                                      up='images/startButtonDown.png',
                                      down='images/startButtonDown.png',
                                      over='images/startButtonHighlight.png')

rockButton = pygwidgets.CustomButton(window, (25, 120),
                                     up = 'images/Rock.png',
                                     over = 'images/Scissors.png')

startButton = pygwidgets.CustomButton(window, (210, 300),
                                      up='images/startButtonUp.png',
                                      down='images/startButtonDown.png',
                                      over='images/startButtonHighlight.png')

rockButton = pygwidgets.CustomButton(window, (25, 120),
                                     up = 'images/Rock.png',
                                     over = 'images/RockOver.png',
                                     down = 'images/RockDown.png')

paperButton = pygwidgets.CustomButton(window, (255, 120),
                                      up = 'images/Paper.png',
                                      over = 'images/ScissorsOver.png',
                                      down = 'images/ScissorsDown.png')

scissorButton = pygwidgets.CustomButton(window, (425, 120),
                                        up = 'images/Scissors.png',
                                        over = 'images/ScissorsOver.png',
                                        down = 'images/ScissorsDown.png')

chooseText = pygwidgets.DisplayText(window, (15, 395), "Choose!",
                                    fontSize=50, textColor = WHITE, width = 610, justified = 'center')

resultsField = pygwidgets.DisplayText(window, (20, 275), '', \
                                    fontSize=50, textColor=WHITE, width=610, justified='center')

rpsCollectionPlayer = pygwidgets.ImageCollection(window, (50, 62),
                                                 {ROCK: 'images/Rock.png', PAPER: 'images/Paper.png', SCISSORS: 'images/Scissors.png'}, '')

rpsCollectionComputer = pygwidgets.ImageCollection(window, (350, 62),
                                                   {ROCK: 'images/Rock.png', PAPER: 'images/Paper.png', SCISSORS: 'images/Scissors.png'}, '')

restartButton = pygwidgets.CustomButton(window, (220, 310),
                                        up = 'images/restartButtonUp.png',
                                        down = 'images/restartButtonDown.png',
                                        over = 'images/restartButtonHighlight.png')

playerScoreCounter = pygwidgets.DisplayText(window, (15, 315), 'Player Score:',
                                            fontSize=50, textColor = WHITE)

computerScoreCounter = pygwidgets.DisplayText(window, (300, 315), 'Computer Score',
                                            fontSize=50, textColor = WHITE)

winnerSound = pygame.mixer.Sound('sounds/ding.wav')
tieSound    = pygame.mixer.Sound('sounds/push.wav')
loserSound  = pygame.mixer.Sound('sounds/buzz.wav')

playerScore = 0
computerScore = 0
state = STATE_SPLASH

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == STATE_SPLASH:
            if startButton.handleEvent(event):
                state = STATE_PLAYER_CHOICE

        elif state == STATE_PLAYER_CHOICE:
            playerChoice = ''
            if rockButton.handleEvent(event):
                playerChoice = ROCK
                rpsCollectionPlayer.replace(ROCK)

            elif paperButton.handleEvent(event):
                playerChoice = PAPER
                rpsCollectionPlayer.replace(PAPER)

            elif scissorButton.handleEvent(event):
                playerChoice = SCISSORS
                rpsCollectionPlayer.replace(SCISSORS)

            if playerChoice != '':
                rps = (ROCK, PAPER, SCISSORS)
                computerChoice = random.choice(rps)
                rpsCollectionComputer.replace(computerChoice)

                if playerChoice == ROCK and computerChoice == SCISSORS:
                    resultsField.setValue('Rock breaks Scissors. You win!')
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == ROCK and computerChoice == SCISSORS:
                    resultsField.setValue('Rock breaks Scissors. You win!')
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == ROCK and computerChoice == PAPER:
                    resultsField.setValue('Rock is covered by Paper. You lose.')
                    computerScore = computerScore + 1
                    loserSound.play()
                   
                elif playerChoice == SCISSORS and computerChoice == PAPER:
                    resultsField.setValue('Scissors cuts Paper. You win!')
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == SCISSORS and computerChoice == ROCK:
                    resultsField.setValue('Scissors crushed by Rock. You lose.')
                    computerScore = computerScore + 1
                    loserSound.play()

                elif playerChoice == PAPER and computerChoice == ROCK:
                    resultsField.setValue('Paper covers Rock. You win!')
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == PAPER and computerChoice == SCISSORS:
                    resultsField.setValue('Paper is cut by Scissors. You lose.')
                    computerScore = computerScore + 1
                    loserSound.play()

                playerScoreCounter.setValue('Your Score: ' + str(playerScore))
                computerScoreCounter.setValue('Computer Score: ' + str(computerScore))

                state = STATE_SHOW_RESULTS

        elif state == STATE_SHOW_RESULTS:
            if restartButton.handleEvent(event):
                state = STATE_PLAYER_CHOICE

        else:
            raise ValueError('Unknown value for state: ', state)


    if state == STATE_PLAYER_CHOICE:
        messageField.setValue('       Rock             Paper         Scissors')
    elif state == STATE_SHOW_RESULTS:
        messageField.setValue('You                     Computer')

    window.fill(GRAY)

    messageField.draw()

    if state == STATE_SPLASH:
        rockImage.draw()
        paperImage.draw()
        scissorsImage.draw()
        startButton.draw()

    elif state == STATE_PLAYER_CHOICE:
        rockButton.draw()
        paperButton.draw()
        scissorButton.draw()
        chooseText.draw()

    elif state == STATE_SHOW_RESULTS:
        resultsField.draw()
        rpsCollectionPlayer.draw()
        rpsCollectionComputer.draw()
        playerScoreCounter.draw()
        computerScoreCounter.draw()
        restartButton.draw()

    else:
        raise ValueError('Unknown value for state:', state)

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
