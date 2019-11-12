import unittest
from cp2048 import *
from Ai import *
class AITest(unittest.TestCase):



    def test_play_random_moveinfini(self):
        jeu = Game2048()
        print(type(jeu))
        playRandomModed(jeu,-1)
        self.assertTrue(jeu.gameover())
        
    def test_play_random_move(self):
        jeu=Game2048()
        li=[]
        for j in range(4):
            g= jeu.copy()
            g.play(j)
            li.append(g.game)
        playRandomModed(jeu.game,1)
        self.assertIn(jeu.game,li)
    #On teste si im ne varie pas entre 2 essais pour être sur de faire le bon choixaa
    def test_strat_2048(self):
        averages = [0,0,0,0]
        jeu = Game2048(numpy.array([[0,0,2,8],[0,0,2,4],[0,0,0,0],[0,0,0,0]]))
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
        i2= strategy_2048(jeu.game,jeu.state,jeu.moves)
        self.assertEqual(i2,im)

    def test_compute_score():
         jeu= Game2048()
         jeu.game(numpy.array([[0,0,2,8],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
         test= 0#valeuràtrouver
         i=compute_score(jeu)
         self.assertEqual(i,test)

        

if __name__== '__main__':
    unittest.main()
