import random
import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def testOne(self):
        password = '12345'
        self.assertFalse(check_pwd(password))

    def testTwo(self):
        password = 'abcdefghi'
        self.assertFalse(check_pwd(password))

    def testThree(self):
        password = 'ABCDEFGHI'
        self.assertFalse(check_pwd(password))

    def testFour(self):
        password = 'abcdEFGHI'
        self.assertFalse(check_pwd(password))

    def testFive(self):
        password = 'abcdEFGH1234'
        self.assertFalse(check_pwd(password))

if __name__ == '__main__':
    unittest.main()
