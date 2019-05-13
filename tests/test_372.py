import unittest

from challenges.challenge_372 import balanced, balanced_bonus

class TestChallenge372(unittest.TestCase):

    def test_balanced_function(self):
        self.assertTrue(balanced("xxxyyy"))
        self.assertTrue(balanced("yyyxxx"))
        self.assertFalse(balanced("xxxyyyy"))
        self.assertTrue(balanced("yyxyxxyxxyyyyxxxyxyx"))
        self.assertFalse(balanced("xyxxxxyyyxyxxyxxyy"))
        self.assertTrue(balanced(""))
        self.assertFalse(balanced("x"))

    def test_balanced_bonus_function(self):
        self.assertTrue(balanced_bonus("xxxyyyzzz"))
        self.assertTrue(balanced_bonus("abccbaabccba"))
        self.assertFalse(balanced_bonus("xxxyyyzzzz"))
        self.assertTrue(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))
        self.assertFalse(balanced_bonus("pqq"))
        self.assertFalse(balanced_bonus("fdedfdeffeddefeeeefddf"))
        self.assertTrue(balanced_bonus("www"))
        self.assertTrue(balanced_bonus("x"))
        self.assertTrue(balanced_bonus(""))

if __name__ == "__main__":
    unittest.main()
