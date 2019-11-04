import pygame
from pygame.locals import *
import numpy as np
import random
import matplotlib.pyplot as plt
import importlib
from Game import *
from Ai import *
from time import time

jeu = game()

def game_over(jeu):
    if (jeu.board == 0).any():
        return False
    cp = game()
    cp.board = np.copy(jeu.board)
    return not(cp.play(0) or cp.play(1) or cp.play(2) or cp.play(3))

def stupid_strat(jeu):
    for i in range(4):
        if jeu.playable(i):
            return i
    raise "Pas de coup possible"

def monte_carlo(jeu,nsim):
    res = []
    for i in range(4):
        cp = game()
        cp.board = np.copy(jeu.board)
        scores = []
        for n in range(nsim):
            cp.board = np.copy(jeu.board)
            coups = np.random.randint(0,4,1000)
            c = 0
            while not(game_over(cp)):
                cp.play(coups[c%1000])
                c += 1
            scores.append(cp.score)
        res.append((np.mean(scores),i))
    res = sorted(res)
    print(res)
    for i in range(4):
        if jeu.playable(res[-i-1][1]):
            print(res[-i-1][1])
            return res[-i-1][1]
    raise "Pas jouable"

def play_monte_carlo():
    jeu = game()
    while not(game_over(jeu)):
        print(jeu.board)
        decision = monte_carlo(jeu,250) # VALID DECISION
        jeu.play(decision)
    print(jeu.board)
    print(jeu.score)

play_monte_carlo()

"""
while not(game_over(jeu)):
    print(jeu.board)
    decision = stupid_strat(jeu) # VALID DECISION OR NOT ?
    jeu.play(decision)

print(jeu.score)
print(jeu.board)

    
    
"""
