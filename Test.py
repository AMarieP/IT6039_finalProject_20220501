#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self): #Sets up the tests
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        '''
        Tests a gutter game - a game where every ball gutters and no points are scored.

        args: 
        arg 1: Bowling Game  

        Returns True if the score from self.game equals zero.
        '''
        self.rollMany(0, 20)
        self.assertEqual(self.game.score(), 0, "Should be 0")

    def testAllOnes(self):
        '''
        Test score if every roll is a one

        args: 
        arg 1: self

        Returns True if score from self.game equals 20.
        '''
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20, "Should be 20")

    def testOneSpare(self):
        '''
        Test score if there is one spare rolled in the game, and
        no other points are scored except for the spare and the doubled point roll. 

        args:
        arg 1: self

        Returns True if score from self.game equals 16.
        '''
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        self.assertEqual(self.game.score(), 16, "Should be 16")

    def testOneStrike(self):
        '''
        Test score if there is one strike rolled in the game, and no other
        points are scored except the strike and the two double point rolls. 

        args: 
        arg 1: self

        Returns True if score from self.game equals 24.
        '''
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24, "Should be 24")

    def testAllStrike(self):
        '''
        Test result if player runs a perfect game of all strikes

        args:
        arg 1: self

        Returns True if score from self.game equals 300
        '''
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300, "Should be 300")

    def testAllSpare(self):
        '''
        Test score if player rolls a game of all spares.

        args:
        arg 1: self

        Returns True if self.game is equal to 150.
        '''
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150, "Should be 150")

    def rollMany(self, pins, rolls): #does the rolls for the tests
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()