from cp2048 import *
from Ai import *
import random

jeu = Game2048()
while (not(jeu.gameover())):
    d = my_strategy(jeu.game,jeu.state,jeu.moves)
    jeu.play(d)
    jeu.next_turn()
    print(jeu.game)


    



