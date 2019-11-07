import random
from math import log

""" Contient toute la logique du jeu 2048 """

class game:
    """classe pour un instance du jeu 2048"""
    
    def __init__(self):
        """ Initialise la partie """
        self.board = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        self.copy = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        self.spawn()
        self.score = 0

    def copyGame(self,game_to_copy):
        """ Copy the state of an other game """
        for i in range(4):
            for j in range(4):
                self.board[i][j] = game_to_copy.board[i][j]
        self.score = game_to_copy.score

    def copyBoard(self):
        for i in range(4):
            for j in range(4):
                self.copy[i][j] = self.board[i][j]

    def setCopyAsBoard(self):
        for i in range(4):
            for j in range(4):
                self.board[i][j] = self.copy[i][j]

    def boardEqualCopy(self):
        for i in range(4):
            for j in range(4):
                if self.copy[i][j] != self.board[i][j]:
                    return False
        return True

    def show(self):
        for i in range(4):
            print(self.board[i])
        print('\n')
        

    def spawn(self):
        x = random.randint(0,3)
        y = random.randint(0,3)
        while self.board[x][y] != 0:
            x = random.randint(0,3)
            y = random.randint(0,3)

        n = 2
        if random.random() > 0.8:
            n = 4
        self.board[x][y] = n

    def moveUp(self):
        for j in range(4):
            newColone = [0,0,0,0]
            idNewColone = 0
            tampon = self.board[0][j]
            fusionAllowed = True
            for i in range(1,4):
                if tampon != 0 and tampon == self.board[i][j] and fusionAllowed:
                    newColone[idNewColone] = 2*tampon
                    idNewColone += 1
                    self.score += 2*tampon
                    tampon = -1
                    fusionAllowed = False
                elif tampon>0 and self.board[i][j] != 0:
                    newColone[idNewColone] = tampon
                    idNewColone += 1
                    tampon = self.board[i][j]
                elif tampon>0 and self.board[i][j] == 0:
                    tampon = tampon
                elif tampon <= 0:
                    tampon = self.board[i][j]
            if tampon > 0:
                newColone[idNewColone] = tampon
            for i in range(4):
                self.board[i][j] = newColone[i]

    def moveDown(self):
        for j in range(4):
            newColone = [0,0,0,0]
            idNewColone = 0
            tampon = self.board[3][j]
            fusionAllowed = True
            for i in [2,1,0]:
                if tampon != 0 and tampon == self.board[i][j] and fusionAllowed:
                    newColone[idNewColone] = 2*tampon
                    idNewColone += 1
                    self.score += 2*tampon
                    tampon = -1
                    fusionAllowed = False
                elif tampon>0 and self.board[i][j] != 0:
                    newColone[idNewColone] = tampon
                    idNewColone += 1
                    tampon = self.board[i][j]
                elif tampon>0 and self.board[i][j] == 0:
                    tampon = tampon
                elif tampon <= 0:
                    tampon = self.board[i][j]
            if tampon > 0:
                newColone[idNewColone] = tampon
            for i in [3,2,1,0]:
                self.board[i][j] = newColone[3-i]

    def moveLeft(self):
        for i in range(4):
            newColone = [0,0,0,0]
            idNewColone = 0
            tampon = self.board[i][0]
            fusionAllowed = True
            for j in range(1,4):
                if tampon != 0 and tampon == self.board[i][j] and fusionAllowed:
                    newColone[idNewColone] = 2*tampon
                    idNewColone += 1
                    self.score += 2*tampon
                    tampon = -1
                    fusionAllowed = False
                elif tampon>0 and self.board[i][j] != 0:
                    newColone[idNewColone] = tampon
                    idNewColone += 1
                    tampon = self.board[i][j]
                elif tampon>0 and self.board[i][j] == 0:
                    tampon = tampon
                elif tampon <= 0:
                    tampon = self.board[i][j]
            if tampon > 0:
                newColone[idNewColone] = tampon
            for j in range(4):
                self.board[i][j] = newColone[j]


    def moveRight(self):
        for i in range(4):
            newColone = [0,0,0,0]
            idNewColone = 0
            tampon = self.board[i][3]
            fusionAllowed = True
            for j in [2,1,0]:
                if tampon != 0 and tampon == self.board[i][j] and fusionAllowed:
                    newColone[idNewColone] = 2*tampon
                    idNewColone += 1
                    self.score += 2*tampon
                    tampon = -1
                    fusionAllowed = False
                elif tampon>0 and self.board[i][j] != 0:
                    newColone[idNewColone] = tampon
                    idNewColone += 1
                    tampon = self.board[i][j]
                elif tampon>0 and self.board[i][j] == 0:
                    tampon = tampon
                elif tampon <= 0:
                    tampon = self.board[i][j]
            if tampon > 0:
                newColone[idNewColone] = tampon
            for j in [3,2,1,0]:
                self.board[i][j] = newColone[3-j]

                
        
    def play(self,move):
        """ Play the move, spawn the number and return True if the move is legit """
        self.copyBoard()
        if move == 0:
            self.moveLeft()
        elif move == 1:
            self.moveUp()
        elif move == 2:
            self.moveRight()
        elif move == 3:
            self.moveDown()

        if self.boardEqualCopy():
            return False

        self.spawn()
        #self.updateScore()
        return True

    
    def gameOver(self):
        """ Return True if game over """
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return False
                
        self.copyBoard()
        self.moveLeft()
        if not(self.boardEqualCopy()):
            self.setCopyAsBoard()
            return False
        self.moveRight()
        if not(self.boardEqualCopy()):
            self.setCopyAsBoard()
            return False
        self.moveUp()
        if not(self.boardEqualCopy()):
            self.setCopyAsBoard()
            return False
        self.moveDown()
        if not(self.boardEqualCopy()):
            self.setCopyAsBoard()
            return False

        return True

    def updateScore(self):
        """ Modifie le score, pas encore utilisée """
        self.score = 0
        m = max(max(self.board))

        defaultScore = 0
        for i in range(4):
            for j in range(4):
                if self.board[i][j] > 2:
                        defaultScore += (log(self.board[i][j],2)-1)*(self.board[i][j])
                
        orderScore = 0
        for i in range(4):
            for j in range(4):
                if i%2 == 0:
                    orderScore += (self.board[i][j])*(16-(j+4*i))*(1/16)*(1/16)/m
                if i%2 == 1:
                    orderScore += (self.board[i][j])*(16-(4*(i+1))+j)*(1/16)*(1/16)/m

        self.score = defaultScore + orderScore*defaultScore*0.0005
                        
        diffScore = 0
        
        for i in range(3):
            for j in range(3):
                diffScore += (self.board[i][j] - self.board[i+1][j])
                diffScore += (self.board[i][j] - self.board[i][j+1])

        self.score = defaultScore + orderScore*defaultScore*0.0005 + defaultScore*diffScore*0.000001 #*0.00001
        
