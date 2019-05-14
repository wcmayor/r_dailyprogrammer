import unittest

from challenges.challenge_364 import roll_dice

class TestChallenge364(unittest.TestCase):

    def test_sum_output(self):
        self.assertLessEqual(roll_dice("1d2"), 2)
        self.assertLessEqual(roll_dice("3d12"), 36)
        self.assertLessEqual(roll_dice("100d100"), 10000)
        self.assertGreaterEqual(roll_dice("1d2"), 1)
        self.assertGreaterEqual(roll_dice("3d12"), 3)
        self.assertGreaterEqual(roll_dice("100d100"), 100)
    
    def test_string_output(self):
        output = roll_dice("6d6", True)

        self.assertIsInstance(output, str)

        output = output.split(": ")
        sum_of_rolls = int(output[0])
        list_of_rolls = output[1]

        self.assertLessEqual(sum_of_rolls, 36)
        self.assertGreaterEqual(sum_of_rolls, 6)
        self.assertEqual(sum_of_rolls, sum([int(roll) for roll in list_of_rolls.split(" ")]))
    
    def test_rolls_out_of_range(self):
        with self.assertRaises(ValueError):
            roll_dice("0d2")
        with self.assertRaises(ValueError):
            roll_dice("101d2")

    def test_sides_out_of_range(self):
        with self.assertRaises(ValueError):
            roll_dice("1d1")
        with self.assertRaises(ValueError):
            roll_dice("1d101")

if __name__ == "__main__":
    unittest.main()