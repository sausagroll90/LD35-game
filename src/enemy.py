import pygame
import math

class Enemy:
    def __init__(self, start):
        self.start = start
        if self.start == "left":
            self.x = 0
            self.y = 280
            self.dx = 50
            self.dy = 0
        elif self.start == "right":
            self.x = 560
            self.y = 280
            self.dx = -50
            self.dy = 0
        elif self.start == "top":
            self.x = 280
            self.y = 0
            self.dx = 0
            self.dy = 50
        elif self.start == "bottom":
            self.x = 280
            self.y = 560
            self.dx = 0
            self.dy = -50
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def update(self, dt, time):
        self.x += self.dx * (dt / 1000) * ((time + 2) / 2)
        self.y += self.dy * (dt / 1000) * ((time + 2) / 2)
        self.rect = pygame.Rect(self.x, self.y, 40, 40)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 40, 40))