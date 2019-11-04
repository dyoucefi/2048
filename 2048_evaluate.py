#import pygame
#from pygame.locals import *
import numpy as np
import random
import matplotlib.pyplot as plt
import importlib
from Game import *
from Ai import *




jeu = game()

play = True
while play:
    play = play_move_simulation(jeu)[0]
    print(np.max(jeu.board))


print(jeu.board)
