import random
from cp2048 import Game2048
from math import log

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
    #return jeu.score() #+ log(sum(sum((jeu.game == 0) + 1)))*2.7 #+ progressiveScore(jeu)*0.3
          
def progressiveScore(jeu):
    for i in range(3):
        for j in range(3):
            s1 = (log(jeu.game[i][j] + 1) - log(jeu.game[i][j+1]+1))/log(2)
            s2 = (log(jeu.game[i][j+1] + 1) - log(jeu.game[i][j]+1))/log(2)
            s3 = (log(jeu.game[i][j] + 1) - log(jeu.game[i+1][j]+1))/log(2)
            s4 = (log(jeu.game[i+1][j] + 1) - log(jeu.game[i][j+1]+1))/log(2)

    return max(s1,s2) + max(s3,s4)

def strategy_2048(game,state,move):
    averages = [0,0,0,0]
    jeu = Game2048(game)
    for firstMove in range(4):
        for i in range(100):
            test = jeu.copy()
            if not(test.gameover()):
                test.play(firstMove)
                averages[firstMove] += playRandomModed(test,6)/100
            
    im = 0
    for i in range(4):
        if averages[i] > averages[im]:
            im = i
    return im



    
