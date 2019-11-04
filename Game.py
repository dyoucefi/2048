import numpy as np
import random

""" Contient toute la logique du jeu 2048 """

class game:
    """classe pour un instance du jeu 2048"""
    
    def __init__(self):
        """ Initialise la partie """
        self.board = np.zeros((4,4),dtype=int)
        self.spawnNumber()
        self.score = 0

    def copy(self,game_to_copy):
        """ Copy the state of an other game """
        self.board = np.copy(game_to_copy.board)
        self.score = game_to_copy.score

    def show(self):
        print(self.board)
        
    def spawnNumber(self):
        """ Spawn 2 or 4 in a rand spot """
        empty_spot = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    empty_spot.append((i,j))
        
        #Choose the empty spot
        spot = random.choice(empty_spot)
                    
        #Choose 2 or 4
        n = 2
        if random.random() > 0.8:#90 chance of getting 2
            n = 4
        
        self.board[spot] = n
        
    def move_up(self):
        """ Stack all number up """
        for j in range(len(self.board[0])):
            new_c = []
            for i in range(len(self.board)):
                if self.board[i,j] != 0:
                    new_c.append(self.board[i,j])
                    self.board[i,j] = 0

            new_c = self.add_modified(new_c)
            
            for i in range(len(new_c)):
                self.board[i,j] = new_c[i]
                
    def move_down(self):
        """Stack all number down"""
        for j in range(len(self.board[0])):
            new_c = []
            for i in range(len(self.board)-1,-1,-1):
                if self.board[i,j] != 0:
                    new_c.append(self.board[i,j])
                    self.board[i,j] = 0
                    
            new_c = self.add_modified(new_c)
            
            for i in range(len(new_c)):
                self.board[len(self.board)-i-1,j] = new_c[i]
                
    def move_left(self):
        """ Stack all number left """
        for i in range(len(self.board)):
            new_l = []
            for j in range(len(self.board[0])):
                if self.board[i,j] != 0:
                    new_l.append(self.board[i,j])
                    self.board[i,j] = 0
                    
            new_l = self.add_modified(new_l)
            
            for j in range(len(new_l)):
                self.board[i,j] = new_l[j]
                
    def move_right(self):
        """ Stack all number rifht """
        for i in range(len(self.board)):
            new_l = []
            for j in range(len(self.board[0])-1,-1,-1):
                if self.board[i,j] != 0:
                    new_l.append(self.board[i,j])
                    self.board[i,j] = 0
                    
            new_l = self.add_modified(new_l)
            
            for j in range(len(new_l)):
                self.board[i,len(self.board[0])-1-j] = new_l[j]
                
    def addable(self,li):
        """True if you can add numbers"""
        a = li[0]
        for i in range(1,len(li)):
            b = li[i]
            if a == b:
                return True
            a = b
        return False

    def add_modified(self,li):
        """ Add lines or colonnes """
        res = []
        if len(li) >= 1:
            tampon = li[0]
            for i in range(1,len(li)):
                if tampon == -1:
                    tampon = li[i] 
                elif tampon == li[i]:
                    res.append(2*tampon)
                    self.score += 2*tampon
                    tampon = -1
                else:
                    res.append(tampon)
                    tampon = li[i]
            if tampon != -1:
                res.append(tampon)
        return res
    
    def play(self,move):
        """ Play the move, spawn the number and return True if the move is legit """
        before_board = np.copy(self.board)
        if move == 0:
            self.move_left()
        elif move == 1:
            self.move_up()
        elif move == 2:
            self.move_right()
        elif move == 3:
            self.move_down()

        if (before_board == self.board).all():
            return False

        self.spawnNumber()
        return True

    def simulate(self,move):
        """ Move and no spawn """
        if move == 0:
            self.move_left()
        elif move == 1:
            self.move_up()
        elif move == 2:
            self.move_right()
        elif move == 3:
            self.move_down()

    def playable(self,c):
        """ Check if the move is playable """
        cp = game()
        cp.board = np.copy(self.board)
        return cp.play(c)
