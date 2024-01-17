import pygame

class Player:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
        self.color = (0, 255, 0)
        self.Rect = pygame.Rect(self.pos, self.size)
    def draw(self, screen):
        self.Rect = pygame.Rect(self.pos, self.size)
        pygame.draw.rect(screen, self.color, self.Rect)
    def update(self):
        return 0