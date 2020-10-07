import unittest
from contrived_func import contrived_func


class TestCase(unittest.TestCase):

    def testOne(self):
        self.assertEqual(contrived_func(5), True)

    def testTwo(self):
        self.assertEqual(contrived_func(145), True)

    def testThree(self):
        self.assertEqual(contrived_func(555), True)

    def testFour(self):
        self.assertEqual(contrived_func(6), False)

    def testFive(self):
        self.assertEqual(contrived_func(161), False)

    def testSix(self):
        self.assertEqual(contrived_func(75), True)

    def testSeven(self):
        self.assertEqual(contrived_func(49), False)

if __name__ == '__main__':
    unittest.main()
