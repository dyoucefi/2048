import pygame
from pygame.locals import *
import numpy as np
import random
import matplotlib.pyplot as plt
import importlib
from Game import *
from Ai import *
from time import time

#test temps pour finir une partie
t0 = time()
jeu = game()
t1 = time()
moves = np.random.randint(0,4,1000)
t2 = time()

temps = []
coups = []
for n in range(100):
    jeu = game()
    t3 = time()
    i = 0
    while (jeu.board == 0).any() and i < 1000:
        jeu.play(moves[i])
        i += 1
    t4 = time()
    temps.append(t4-t3)
    coups.append(i)
print(t1-t0,t2-t1,np.mean(temps),np.mean(coups))
