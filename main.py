import pygame
from src.setup import *
import src.gameloop

mainloop = src.gameloop.Gameloop(screen, False, clock, player1, spawnslist, font)

mainloop.run_current_state()

pygame.quit()