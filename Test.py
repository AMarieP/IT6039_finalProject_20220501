#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self): #Sets up the self
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score() == 0 #Score should be 6

    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20 #Score should be 20

    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score() == 16 #Score should be 16

    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0, 16)
        assert  self.game.score() == 24 #Score should be 24

    def testPerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300 #Score should be 300

    def testOneSpare(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150 #Score should be 150

    def rollMany(self, pins,rolls): #does the rolls for the tests
        for i in range(rolls):
            self.game.rolls(pins)

if __name__ == '__main__':
    unittest.main()