import pygame
import src.player
import src.enemy

pygame.mixer.pre_init(22050, -16, 2, 512)

pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BeatBox")
clock = pygame.time.Clock()

font = pygame.font.Font("res/thefont.ttf", 20)
titlefont = pygame.font.Font("res/thefont.ttf", 80)
background = pygame.image.load("res/background.png")
lflash = pygame.image.load("res/whitesquare.png").convert()
rflash = pygame.image.load("res/whitesquare.png").convert()
tflash = pygame.image.load("res/whitesquare.png").convert()
bflash = pygame.image.load("res/whitesquare.png").convert()
redflash = pygame.image.load("res/red.png").convert()
redflash.set_alpha()
pimg = pygame.image.load("res/particle.png").convert()

hit = pygame.mixer.Sound("res/hit.wav")
hit.set_volume(0.5)
miss = pygame.mixer.Sound("res/miss.wav")
miss.set_volume(0.4)

player1 = src.player.Player(redflash, pimg, hit, miss)

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