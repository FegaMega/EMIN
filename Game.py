import player
import Object
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.screenSize = [700, 700]
        self.screen = pygame.display.set_mode(self.screenSize, vsync=1)
        self.isRunning = True
        self.player = player.Player([50, 50], [50, 50])
        self.objects = [Object.Objects([100, 150], [200, 30])]
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.isRunning = False
        return 0
    def update(self):
        self.player.update()
        for object in self.objects:
            object.update()
        return 0
    def render(self):
        for object in self.objects:
            object.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.time.Clock().tick(60)
        return 0
    def Exit(self):
        pygame.quit()
        return 0