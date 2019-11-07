import random
from Game import *


def randomMove(jeu):
    move = random.randint(0,3)
    while not(jeu.play(move)):
        move = random.randint(0,3)

def playRandom(jeu):
    while not(jeu.gameOver()):
        randomMove(jeu)
    return jeu.score

def playRandom(jeu,maxMove=-1):
    i = 0
    while not(jeu.gameOver()) and (i <= maxMove or maxMove < 0):
        randomMove(jeu)
        i += 1
    return jeu.score

def monteCarloMove(jeu,nsim,prof):
    averages = [0,0,0,0]
    test = game()
    for firstMove in range(4):
        for i in range(nsim):
            test.copyGame(jeu)
            if not(test.gameOver()):
                test.play(firstMove)
                averages[firstMove] += playRandom(test,prof)/nsim
            
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
def playMonteCarlo(jeu,nsim=100,prof=-1,aff=True):
    while not(jeu.gameOver()):
        if aff:
            jeu.show()
            print(jeu.score)
        monteCarloMove(jeu,nsim,prof)
    return jeu.score
    
