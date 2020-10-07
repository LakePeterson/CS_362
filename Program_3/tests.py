import random
import unittest
from credit_card_validator import credit_card_validator


class TestCase(unittest.TestCase):

    def testOne(self):
        for i in range(0, 100000):
            cardNumber = random.randint(4000000000000000, 4999999999999999)
            credit_card_validator(cardNumber)

    def testTwo(self):
        for i in range(0, 10000):
            cardNumber = random.randint(5100000000000000, 5599999999999999)
            credit_card_validator(cardNumber)

    def testThree(self):
        for i in range(0, 10000):
            cardNumber = random.randint(2221000000000000, 2720999999999999)
            credit_card_validator(cardNumber)

    def testFour(self):
        for i in range(0, 1000):
            cardNumber = random.randint(340000000000000, 379999999999999)
            credit_card_validator(cardNumber)

    def testFive(self):
        for i in range(0, 250):
            cardNumber = random.randint(0000000000000000, 9999999999999999)
            credit_card_validator(cardNumber)


if __name__ == '__main__':
    unittest.main()
