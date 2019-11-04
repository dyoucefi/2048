import pygame
from pygame.locals import *
import numpy as np
import random
import matplotlib.pyplot as plt

class game:
    
    def __init__(self):
        #Initialise la partie
        #Variables
        self.board = np.zeros((4,4),dtype=int)
        self.spawnNumber()
        self.score = 0
        
    #def gameOver(self):
    #    return not((self.board != 0).any())
        
    def spawnNumber(self):
        #Spawn 2 or 4 in a rand spot
        
        #Number
        # 1 2 3 4
        # 5 6 7 8
        # 9 10 11 12
        # 13 14 15 16
        empty_spot = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    empty_spot.append((i,j))
        
        #Choose the empty spot
        spot = random.choice(empty_spot)
                    
        #Choose 2 or 4
        n = 2
        if random.random() > 0.9:#90 chance of getting 2
            n = 4
        
        self.board[spot] = n
        
    def move_up(self):
        #Stack all number up
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
        #Stack all number down
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
        #True if you can add numbers
        a = li[0]
        for i in range(1,len(li)):
            b = li[i]
            if a == b:
                return True
            a = b
        return False
    def add(self,li):
        res = []
        to_delete = -1
        for i in range(len(li)-1):
            if li[i] == li[i+1] and i != to_delete:
                res.append(2*li[i])
                to_delete = i+1
            elif i!= to_delete:
                res.append(li[i])
        if to_delete != len(li)-1:
            res.append(li[-1])
        return res

    def add_modified(self,li):
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
        #if self.gameOver():
        #    return (sum(sum(self.board)))
        #else:
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
        #if self.gameOver():
        #    return (sum(sum(self.board)))
        #else:
        if move == 0:
            self.move_left()
        elif move == 1:
            self.move_up()
        elif move == 2:
            self.move_right()
        elif move == 3:
            self.move_down()


#Parameters
square_size = 100
border_size = 10

def compute_im(value):
    im = pygame.Surface((square_size,square_size))# Initialisation sqaure
    if value >= 0 and value <= 2048:
        v = np.log(value)/np.log(2048)
        im.fill((int(55*v)+200,int(220-200*v),int(220-200*v)))
        return im
    else:
        return def_im

def compute_text(value):
    if value < 10:
        myfont = pygame.font.SysFont('Book Antiqua', 90)
    elif value < 100:
        myfont = pygame.font.SysFont('Book Antiqua', 70)
    elif value < 1000:
        myfont = pygame.font.SysFont('Book Antiqua', 55)
    else:
        myfont = pygame.font.SysFont('Book Antiqua', 40)
    textsurface = myfont.render(str(value), True, (0, 0, 0))
    return textsurface
    
    

def update_aff(jeu):
    fenetre.blit(fond, (0,0))
    for i in range(len(jeu.board)):
        for j in range(len(jeu.board[0])):
            if jeu.board[i,j] != 0 :
                fenetre.blit(compute_im(jeu.board[i,j]), (j*(border_size+square_size)+border_size,
                                      i*(border_size+square_size)+border_size))

                text = compute_text(jeu.board[i,j])
                
                
                fenetre.blit(text, (j*(border_size+square_size)+border_size+20,
                                      i*(border_size+square_size)+border_size))
            else:
                fenetre.blit(def_im, (j*(border_size+square_size)+border_size,
                                      i*(border_size+square_size)+border_size))
        pygame.display.update()

def brutus_moves(jeu):
    while True:
        moves = [3,2,1,0]
        i = 0
        while i <= 3:
            state = jeu.play(moves[i])
            if not(state) and i == 3:
                return sum(sum(jeu.board))
            elif state:
                i = 4
            elif not(state):
                i += 1

def brutus_move(jeu):
    moves = [3,2,1,0]
    i = 0
    while i <= 3:
        state = jeu.play(moves[i])
        if not(state) and i == 3:
            return False
        elif state:
            i = 4
        elif not(state):
            i += 1
    return True

def score_board2(jeu):
    tot_order = 0
    tot_double = 0
    tot_empty = 0
    #lignes
    #print("---")
    for i in range(len(jeu.board)):
        l = jeu.board[i,:]
        if (sorted(l) == l).all():
            tot_order += 1
            
    for j in range(len(jeu.board[0])):
        c = jeu.board[:,j]
        if (sorted(c) == c).all():
            tot_order += 1

    for i in range(len(jeu.board)):
        for j in range(len(jeu.board[0])-1):
            if jeu.board[i,j] == 2*jeu.board[i,j+1]:
                tot_double += 1
    for j in range(len(jeu.board[0])):
        for i in range(len(jeu.board)-1):
            if jeu.board[i,j] == 2*jeu.board[i+1,j]:
                tot_double += 1
                           
    
    tot_empty = sum(sum(jeu.board == 0))
    return tot_empty,tot_order,tot_double

def next_move(jeu):
    temp = game()
    res = []
    for i in range(4):
        temp.board = np.copy(jeu.board)
        #print("Simulating move : ",i)
        temp.simulate(i)
        #print(temp.board)
        res.append((score_board2(temp),i))
        
    res = sorted(res)
        
    i = 0
    while i<= 3 and not(jeu.play(res[3-i][1])):
        i+=1
    if i<= 3:
        return True,i
    else:
        return False,i


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

def chose_move_simulation_f(jeu,n_sim,profondeur):
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
        
        
def play_move_simulation(jeu):
    res = chose_move_simulation(jeu,100,4)
    #100,5
    
    res = sorted(res)
    #print(res)
    #print(res[3][-1])
        
    i = 0
    while i<= 3 and not(jeu.play(res[3-i][-1])):
        i+=1
    if i<= 3:
        return True,i
    else:
        return False,i

def play_move_simulation_moded(jeu):
    if(np.max(jeu.board)>=2048):
        res = chose_move_simulation(jeu,1000,10)
    elif np.max(jeu.board)>=1024:
        res = chose_move_simulation(jeu,200,5)
    elif np.max(jeu.board)>=256:
        res = chose_move_simulation(jeu,100,3)
    else:
        res = chose_move_simulation(jeu,50,2)
    #100,5
    
    res = sorted(res)
    #print(res)
    #print(res[3][-1])
        
    i = 0
    while i<= 3 and not(jeu.play(res[3-i][-1])):
        i+=1
    if i<= 3:
        return True,i
    else:
        return False,i
    


#Main

#Initialisation de l'interface
pygame.init()
fond = pygame.Surface((4*square_size+6*border_size,4*square_size+6*border_size))
fond.fill((0, 0, 0))
fenetre = pygame.display.set_mode(fond.get_size())
fenetre.blit(fond, (0,0))
pygame.display.update() 

def_im = pygame.Surface((square_size,square_size))# Initialisation sqaure
def_im.fill((255,255,255))

pygame.font.init() # Init font


jeu = game()
update_aff(jeu)

continuer = True
brutus = False
play_score = False
play_simulate = False

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                jeu.play(3)
            if event.key == K_UP:
                jeu.play(1)
            if event.key == K_LEFT:
                jeu.play(0)
            if event.key == K_RIGHT:
                jeu.play(2)
            
            if event.key == K_t:
                jeu.board = np.array([[0,2,4,8],
                                      [16,32,64,128],
                                      [256,512,1024,2048],
                                      [4096,0,0,0]])
            if event.key == K_b:
                brutus = not(brutus)
            if event.key == K_r:
                jeu = game()
            if event.key == K_s:
                play_score = not(play_score)

            if event.key == K_n:
                next_move(jeu)

            if event.key == K_o:
                play_move_simulation(jeu)
            if event.key == K_p:
                play_simulate = not(play_simulate)
            if event.key == K_c:
                print(chose_move_simulation(jeu,100,0))
            if event.key == K_m:
                print(jeu.score)
            if event.key == K_i:
                print("---")
                for p in [1,3]:
                    for n in [1,10,100,1000]:
                        print(sorted(chose_move_simulation(jeu,n,p))[-1])
                

            update_aff(jeu)
            #print(jeu.score)

    if brutus:
        brutus = brutus_move(jeu)
        update_aff(jeu)
        pygame.time.wait(20)
    if play_score:
        play_score = next_move(jeu)[0]
        update_aff(jeu)
        pygame.time.wait(20)
    if play_simulate:
        play_simulate = play_move_simulation_moded(jeu)[0]
        update_aff(jeu)
        #pygame.time.wait(20)
        
            #print(jeu.board)

pygame.quit()
