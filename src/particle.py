import pygame
import random

class Particle:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        random.seed()
        self.dx = random.randint(-150, 150)
        self.dy = random.randint(-150, 150)
        self.orientation = random.random() * 360
        self.dr = random.randint(-180, 180)
        self.img = img
        self.alpha = 255

    def update(self, dt):
        self.x += self.dx * (dt / 1000)
        self.y += self.dy * (dt / 1000)
        self.orientation += self.dr * (dt / 1000)
        self.dx -= self.dx * 0.5 * (dt / 1000)
        self.dy -= self.dy * 0.5 * (dt / 1000)
        self.dr -= self.dr * 0.5 * (dt / 1000)
        self.alpha -= dt * 0.15
        self.img.set_alpha(self.alpha)

    def draw(self, screen):
        screen.blit(pygame.transform.rotate(self.img, self.orientation), (self.x, self.y))