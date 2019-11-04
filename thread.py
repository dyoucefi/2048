import numpy as np
import random
import matplotlib.pyplot as plt
import importlib
from Game import *
from Ai import *
from threading import Thread
import time

""" Monte Carlo optimisé mais pas vraiment plus rapide """

class Calculateur(Thread):
    """ Calcul les mouvements selon 1 diredction """
    def __init__(self, firstMove=0, jeu=0, n_sim=100, profondeur=5):
        super(Calculateur,self).__init__()
        self.firstMove = firstMove
        self.jeu = jeu
        self.n_sim = n_sim
        self.profondeur = profondeur
        self.res = [0,firstMove]

    def run(self):
        score = 0
        temp = game()
        for n in range(self.n_sim):
            temp.board = np.copy(self.jeu.board)
            temp.score = self.jeu.score
            temp.play(self.firstMove)
            
            for p in range(self.profondeur):
                rand_move = random.randint(0,4)
                temp.play(rand_move)
            score += (temp.score/(self.profondeur+1))
        self.res = [score,self.firstMove]

def compute_thread(li_thread):
    for i in range(4):
        li_thread[i].start()

    for i in range(4):
        li_thread[i].join()

    res = []

    for i in range(4):
        res.append(li_thread[i].res)

    return res

def play_move_simulation_threaded(jeu,li_thread):
    for i in range(4):
        li_thread[i].jeu = jeu
    res = compute_thread(li_thread)
    
    res = sorted(res)        
    i = 0
    while i<= 3 and not(jeu.play(res[3-i][-1])):
        i+=1
    if i<= 3:
        return True,i
    else:
        return False,i

def jouer():

    g = game()
    
    play = True

    while play:
        li_thread = []
        for i in range(4):
            li_thread.append(Calculateur(firstMove=i,jeu=g,n_sim=1000,profondeur=5))
        play = play_move_simulation_threaded(g,li_thread)[0]
        print(g.board)

def compare():
    g1 = game()
    g2 = game()
    play = True
    t_n = []
    t_t = []

    while play:

        
        
        t0 = time.time()
        li_thread = []
        for i in range(4):
            li_thread.append(Calculateur(firstMove=i,jeu=g1,n_sim=100,profondeur=6))
        play = play_move_simulation_threaded(g1,li_thread)[0]
        
        t1 = time.time()

        t2 = time.time()
        play = play_move_simulation(g2)[0]
        t3 = time.time()


        g2.board = g1.board
        g2.score = g1.score

        t_n.append(t3-t2)
        t_t.append(t1-t0)

        
        print(g1.board)

    print(t_n)
    print(t_t)
    print((np.array(t_n)).mean())
    print((np.array(t_t)).mean())
    
"""
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
        
        

"""



"""

jeu = game()

play = True
while play:
    play = play_move_simulation(jeu)[0]
    print(np.max(jeu.board))


print(jeu.board)"""
