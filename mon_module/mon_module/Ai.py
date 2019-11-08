import random
from .cp2048 import Game2048
from math import log
from .Game import *

""" Game de Xavier Dupré """

def randomMoveModed(jeu):
    move = random.randint(0,3)
    jeu.play(move)
    jeu.next_turn()


def playRandomModed(jeu,maxMove=-1):
    i = 0
    while not(jeu.gameover()) and (i <= maxMove or maxMove < 0):
        randomMoveModed(jeu)
        i += 1
    return computeScore(jeu)

def computeScore(jeu):
    defaultScore = 0
    for i in range(4):
        for j in range(4):
            if jeu.game[i][j] > 2:
                defaultScore += (log(jeu.game[i][j],2)-1)*(jeu.game[i][j])
    return defaultScore
          


def strategy_2048(game,state,move):
    averages = [0,0,0,0]
    jeu = Game2048(game)
    for firstMove in range(4):
        for i in range(250):
            test = jeu.copy()
            if not(test.gameover()):
                test.play(firstMove)
                averages[firstMove] += playRandomModed(test,-1)/250
            
    im = 0
    for i in range(4):
        if averages[i] > averages[im]:
            im = i
    return im

""" Vrai 2048 """

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

    
