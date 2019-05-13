import unittest

from challenges.challenge_374 import getAdditivePersistence

class TestAddiditvePersistence(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(getAdditivePersistence(13), 1)
        self.assertEqual(getAdditivePersistence(1234), 2)
        self.assertEqual(getAdditivePersistence(9876), 2)
        self.assertEqual(getAdditivePersistence(199), 3)

if __name__ == "__main__":
    unittest.main()