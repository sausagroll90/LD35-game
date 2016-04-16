import pygame
import src.player
import src.enemy

pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("LD35 game")
clock = pygame.time.Clock()

player1 = src.player.Player()

spawns = [
    [1, src.enemy.Enemy("left")],
    [2, src.enemy.Enemy("right")],
    [3, src.enemy.Enemy("top")],
    [3, src.enemy.Enemy("bottom")]
]