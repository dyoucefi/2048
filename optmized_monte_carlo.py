""" Optimized Monte Carlo """
from Game import *

def main():
    jeu = game()
    jeu.show()


def create_pool(size):
    """ Create pool to test move given the size """
    p = []
    for direction in range(4):
        li = []
        for n in range(size):
            li.append(game())
        p.append(li)
    return p

def copy_state_pool(p,jeu):
    """ set the state """
    for sp in p:
        for g in sp:
            g.copy(jeu)

def simulate_k_round(p,k):
    """ simulate random play """
    for sp in p:
        for g in sp:
            moves = np.random.randint
        
    
    
