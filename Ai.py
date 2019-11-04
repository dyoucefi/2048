import numpy as np
import random
import matplotlib.pyplot as plt
from Game import *




    

def chose_move_simulation(jeu,n_sim,profondeur):
    res = []
    for m in [0,1,2,3]:
        score_m = 0
        for n in range(n_sim):
            temp = game()
            temp.board = np.copy(jeu.board)
            temp.score = jeu.score
            temp.play(m)
            
            for p in range(profondeur):
                rand_move = random.randint(0,4)
                temp.play(rand_move)
            score_m += (temp.score/(profondeur+1))
        res.append([score_m,m])
        
    return res
        
        
def play_move_simulation(jeu):
    res = chose_move_simulation(jeu,100,5)
    
    res = sorted(res)
    #print(res)
    #print(res[3][-1])
        
    i = 0
    while i<= 3 and not(jeu.play(res[3-i][-1])):
        i+=1
    if i<= 3:
        return True,i
    else:
        return False,i
    

def stupid_strat(jeu):
    for i in range(4):
        if jeu.playable(i):
            return i
    raise "Pas de coup possible"

""" --- Stratégie monte carlo --- """

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
            while not(cp.game_over()):
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

def play_monte_carlo(nsim=100,aff=True):
    jeu = game()
    while not(jeu.game_over()):
        if aff:
            print(jeu.board)
        decision = monte_carlo(jeu,nsim) # VALID DECISION
        jeu.play(decision)
    if aff:
        print(jeu.board)
        print(jeu.score)
    
  

