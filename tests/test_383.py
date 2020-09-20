import unittest

from challenges.challenge_383 import same_necklace, repeats, bonus2

class TestSameNecklace(unittest.TestCase):

    def testTrueNecklaces(self):
        self.assertTrue(same_necklace("nicole", "icolen"))
        self.assertTrue(same_necklace("nicole", "lenico"))
        self.assertTrue(same_necklace("aabaaaaabaab", "aabaabaabaaa"))
        self.assertTrue(same_necklace("x", "x"))
        self.assertTrue(same_necklace("", ""))

    def testFalseNecklaces(self):
        self.assertFalse(same_necklace("nicole", "coneli"))
        self.assertFalse(same_necklace("abc", "cba"))
        self.assertFalse(same_necklace("xxyyy", "xxxyy"))
        self.assertFalse(same_necklace("xyxxz", "xxyxz"))
        self.assertFalse(same_necklace("x", "xx"))
        self.assertFalse(same_necklace("x", ""))
    
    def testRepeats(self):
        self.assertEqual(repeats("abc"), 1)
        self.assertEqual(repeats("abcabcabc"), 3)
        self.assertEqual(repeats("abcabcabcx"), 1)
        self.assertEqual(repeats("aaaaaa"), 6)
        self.assertEqual(repeats("a"), 1)
        self.assertEqual(repeats(""), 1)
    
    def testBonus2(self):
        results = ['estop', 'pesto', 'stope', 'topes']
        self.assertEqual(bonus2("https://raw.githubusercontent.com/dolph/dictionary/master/enable1.txt"), results)