import numpy as np
import random
import matplotlib.pyplot as plt
from Game import *

""" Fonctions auxiliares qui servent à choisir le coup suiviant """

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
    
 def case_vide(jeu):
    mat=jeu.board
    res=0
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                res+=1
    return res
    
  

