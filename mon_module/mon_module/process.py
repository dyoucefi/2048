from multiprocessing import Process
from Ai import *
from Game import *

result = [0]*10

def aux(i):
    jeu = Game()
    result[i] = playMonteCarlo(jeu,100,10,True)

for i in range(10):
    p = Process(target=aux,args=(i,))
    p.start()

for i in range(10):
    p.join()

print(result)
