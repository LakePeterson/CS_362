"""
    My methodology for finding the bugs was mainly oriented around
    guessing and checking, in which I did not utilize the TSLgenerator.
    The reason I found the guess and check method to be the most effective
    was becuase after reading the provied material I was able to target
    areas that a bug could exist when it came to validating credit cards.
    From this the first bug I found was an empty string, second was if
    the card number was too short, third was a valid Visa card, fourth
    was a valid American Express card, fifth was if the card was too long,
    the sixth bug was checking for a valid Mastercard.
"""

import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def testBugOne(self):
        self.assertEqual(credit_card_validator(''), True)

    def testBugTwo(self):
        self.assertEqual(credit_card_validator('452100934314023'), True)

    def testBugThree(self):
        self.assertEqual(credit_card_validator('4521009704314023'), True)

    def testBugFour(self):
        self.assertEqual(credit_card_validator('370600982683046'), True)

    def testBugFive(self):
        self.assertEqual(credit_card_validator('3496626767003111'), True)

    def testBugSix(self):
        self.assertEqual(credit_card_validator('2720995085393011'), True)

if __name__ == '__main__':
    unittest.main()
