import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.screenSize = [700, 700]
        self.screen = pygame.display.set_mode(self.screenSize, vsync=1)
        self.isRunning = True
    def handleEvents(self):
        for event in pygame.get_event():
            if event.type == QUIT:
                self.isRunning = False
        return 0
    def update(self):
        return 0
    def render(self):
        pygame.display.update()
        return 0
    def Exit(self):
        pygame.quit()
        return 0