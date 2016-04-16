import pygame
import src.player
import src.enemy

pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BeatBox")
clock = pygame.time.Clock()
font = pygame.font.Font("res/thefont.ttf", 20)
titlefont = pygame.font.Font("res/thefont.ttf", 80)
background = pygame.image.load("res/background.png")

player1 = src.player.Player()

spawns1 = [
    [1, "left"],
    [2, "right"],
    [3, "top"],
    [3, "bottom"]
]

spawns2 = [
    [1, "left"],
    [2, "top"],
    [3, "right"],
    [4, "bottom"] 
]

spawns3 = [
    [0.5, "left"],
    [1, "left"],
    [1.5, "left"],
    [2, "left"],
    [2.5, "right"],
    [3, "right"],
    [3.5, "right"],
    [4, "right"],
]

spawnslist = [spawns1, spawns2, spawns3]