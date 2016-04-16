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
    [4, "right"]
]

spawns4 = [
    [1, "top"],
    [1.5, "bottom"],
    [2, "right"],
    [2.5, "left"]
]

spawns5 = [
    [1, "top"],
    [2, "bottom"],
    [3, "top"],
    [4, "bottom"]
]

spawns6 = [
    [1, "left"],
    [1, "right"],
    [1.5, "top"],
    [1.5, "bottom"],
    [2, "left"],
    [2, "right"],
    [2.5, "top"],
    [2.5, "bottom"]
]

spawns7 = [
    [1, "left"],
    [1.33, "top"],
    [1.66, "right"],
    [2, "left"],
    [2.33, "top"],
    [2.66, "right"]
]

spawns8 = [
    [0.5, "right"],
    [0.75, "left"],
    [1, "right"],
    [1.25, "left"],
]

spawns9 = [
    [0.5, "top"],
    [1, "top"],
    [1.5, "bottom"],
    [2, "bottom"],
    [2.5, "left"],
    [3, "right"],
    [3.5, "left"],
    [4, "right"],
]

spawns10 = [
    [1, "left"],
    [1.25, "top"],
    [1.5, "left"],
    [1.75, "right"],
    [2, "left"],
    [2.25, "down"],
    [2.5, "left"],
    [2.75, "right"],

]

spawnslist = [spawns1, spawns2, spawns3, spawns4, spawns5, spawns6, spawns7, spawns8, spawns9, spawns10]