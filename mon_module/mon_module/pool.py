import random
from Game import *
from Ai import *
from multiprocessing import Pool
from statistics import mean


def monteCarloPoolMove(jeu,nsim,pool):
    #pool sur les parties random
    averages = [0,0,0,0]
    test = game()
    for firstMove in range(4):
        test.copyGame(jeu)
        if not(test.gameOver()):
            test.play(firstMove)
            li_test = [test]*nsim
            li_res = pool.map(auxPool, li_test)
            averages[firstMove] += mean(li_res)
       
    attempt = 0
    im = 0
    sucess = False
    while (attempt <=4 and sucess == False):
        for i in range(4):
            if averages[i] > averages[im]:
                im = i
        averages[im] = 0
        attempt += 1
        sucess = jeu.play(im)

def auxPool(jeu):
    g = game();
    g.copyGame(jeu)
    return playRandom(g,-1)

def main():
    jeu = game()
    i = 0
    pool = Pool()
    while not(jeu.gameOver()):
        
        monteCarloPoolMove(jeu,1000,pool)
        #if i%10 == 0:
        jeu.show()
        i+=1
    return jeu.score
    pool.close()

if __name__== '__main__':
    main()
