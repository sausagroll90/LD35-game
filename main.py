import pygame
from src.setup import *
import src.gameloop

mainloop = src.gameloop.Gameloop(screen, False, clock, player1, spawnslist, font, titlefont, background)

mainloop.run_current_state()

pygame.quit()