import unittest

from challenges.challenge_381 import yahtzee_upper, yahtzee_upper_large

class TestYahtzee(unittest.TestCase):
    
    def testNormalRolls(self):
        self.assertEqual(yahtzee_upper([2, 3, 5, 5, 6]), 10)
        self.assertEqual(yahtzee_upper([1, 1, 1, 1, 3]), 4)
        self.assertEqual(yahtzee_upper([1, 1, 1, 3, 3]), 6)
        self.assertEqual(yahtzee_upper([1, 2, 3, 4, 5]), 5)
        self.assertEqual(yahtzee_upper([6, 6, 6, 6, 6]), 30)
    
    def testLargeRolls(self):
        self.assertEqual(yahtzee_upper_large(), 996579199996579199996579199996579199996579199996579199996579199996579199996579199996579199996579199996579199996579199996579199996579199996579199996579199)