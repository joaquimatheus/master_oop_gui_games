import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *

class SceneB(pyghelpers.Scene):

    def __init__(self, window):
        self.window = window

        self.messageField = pygwidgets.DisplayText(self.window,
                            (15, 25), 'This is Scene B', fontSize=50,
                            textColor=WHITE, width=610, justified='center')

        self.gotoAButton = pygwidgets.TextButton(self.window,
                                                 (100, 100), 'Go to Scene A')

        self.gotoBButton = pygwidgets.TextButton(self.window,
                                                 (250, 100), 'Go to Scene B')

        self.gotoCButton = pygwidgets.TextButton(self.window,
                                                 (400, 100), 'Go to Scene C')

        self.gotoAButton.disable()


    def getSceneKey(self):
        return SCENE_B

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.gotoBButton.handleEvent(event):
                self.goToScene(SCENE_B)
            if self.gotoBButton.handleEvent(event):
                self.goToScene(SCENE_C)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.send(SCENE_B, SEND_MESSAGE,
                              'Sending message to Scene B')

                if event.key == pygame.K_c:
                    self.send(SCENE_C, SEND_MESSAGE,
                              'Sending message to Scene C')

                if event.key == pygame.K_1:
                    answer = self.request(SCENE_A, GET_DATA)
                    print('Received data from Scene A')
                    print('Answer was:', answer)

                if event.key == pygame.K_3:
                    answer = self.request(SCENE_C, GET_DATA)
                    print('Received data from Scene C')
                    print('Answer was:', answer)

                if event.key == pygame.K_x:
                    self.sendAll(SEND_MESSAGE,
                                 'Sending message to All Scenes')

    def draw(self):
        self.window.fill(GRAYB)
        self.messageField.draw()
        self.gotoAButton.draw()
        self.gotoBButton.draw()
        self.gotoCButton.draw()

    def receive(self, receiveID, data):
        print('In B')
        print('Received a message of type:', receiveID)
        print('The data received was:', data)

    def respond(self, requestId):
        if requestID == GET_DATA:
            return 'Here is data from scene B'
