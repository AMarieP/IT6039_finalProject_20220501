#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self): #Sets up the self
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        '''
        Test a gutter game - a game where every ball gutters and no points are scored. 
        '''
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0, "Should be 0")

    def testAllOnes(self):
        '''
        Test result if every roll is a one
        '''
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20, "Should be 20")

    def testOneSpare(self):
        '''
        Test result if there is one spare rolled in the game
        '''
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        self.assertEqual(self.game.score(), 16, "Should be 16")

    def testOneStrike(self):
        '''
        Test result if there is one strike rolled in the game
        '''
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24, "Should be 24")

    def testPerfectGame(self):
        '''
        Test result if player runs a perfect game
        '''
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300, "Should be 300")

#TODO: figure out what this is supposed to test - all spare?
    def testOneSpare(self):
        '''
        '''
        self.rollMany(5, 21)
        assert self.game.score() == 150 #Score should be 150

    def rollMany(self, pins, rolls): #does the rolls for the tests
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()