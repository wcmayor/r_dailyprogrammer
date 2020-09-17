import unittest

from challenges.challenge_379 import tax

class TestTax(unittest.TestCase):

    def testValidNumbers(self):
        self.assertEqual(tax(0), 0)
        self.assertEqual(tax(10000), 0)
        self.assertEqual(tax(10009), 0)
        self.assertEqual(tax(10010), 1)
        self.assertEqual(tax(12000), 200)
        self.assertEqual(tax(56789), 8697)
        self.assertEqual(tax(1234567), 473326)
        self.assertEqual(tax(100000000), 39979500)

    def testNonNumeric(self):
        with self.assertRaises(ValueError):
            tax("abc")
        with self.assertRaises(ValueError):   
            tax([123, 456])

    def testValueOutsideRange(self):
        with self.assertRaises(ValueError):
            tax(100000001)
        