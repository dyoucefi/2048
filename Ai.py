import numpy as np
import random
import matplotlib.pyplot as plt
from Game import *

""" Fonctions auxiliares qui servent à choisir le coup suiviant """

""" --- Brutus joue dans l'ordre 3,2,1,0 --- """

def brutus_moves(jeu):
    while True:
        moves = [3,2,1,0]
        i = 0
        while i <= 3:
            state = jeu.play(moves[i])
            if not(state) and i == 3:
                return sum(sum(jeu.board))
            elif state:
                i = 4
            elif not(state):
                i += 1

def brutus_move(jeu):
    moves = [3,2,1,0]
    i = 0
    while i <= 3:
        state = jeu.play(moves[i])
        if not(state) and i == 3:
            return False
        elif state:
            i = 4
        elif not(state):
            i += 1
    return True
""" --- """

""" Choisit et joue le prochain coup en fonction du score obtenu au coup suivant --- """

def next_move(jeu):
    temp = game()
    res = []
    for i in range(4):
        temp.board = np.copy(jeu.board)
        #print("Simulating move : ",i)
        temp.simulate(i)
        #print(temp.board)
        res.append((score_board2(temp),i))
        
    res = sorted(res)
        
    i = 0
    while i<= 3 and not(jeu.play(res[3-i][1])):
        i+=1
    if i<= 3:
        return True,i
    else:
        return False,i
"""---"""

""" Essai de donner un score à la grille pour jouer comme un humain """
    
def score_board2(jeu):
    tot_order = 0
    tot_double = 0
    tot_empty = 0
    #lignes
    #print("---")
    for i in range(len(jeu.board)):
        l = jeu.board[i,:]
        if (sorted(l) == l).all():
            tot_order += 1
            
    for j in range(len(jeu.board[0])):
        c = jeu.board[:,j]
        if (sorted(c) == c).all():
            tot_order += 1

    for i in range(len(jeu.board)):
        for j in range(len(jeu.board[0])-1):
            if jeu.board[i,j] == 2*jeu.board[i,j+1]:
                tot_double += 1
    for j in range(len(jeu.board[0])):
        for i in range(len(jeu.board)-1):
            if jeu.board[i,j] == 2*jeu.board[i+1,j]:
                tot_double += 1
                           
    
    tot_empty = sum(sum(jeu.board == 0))
    return tot_empty,tot_order,tot_double

""" --- Comme monte carlo mais tronqué : on ne va pas jusqu'au bout --- """

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
    for i in jeu.liste_playable:
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
    return res[-1][1]
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
    
  

