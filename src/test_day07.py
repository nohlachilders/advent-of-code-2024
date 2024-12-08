import unittest
import re

from day07 import *

class TestDay07(unittest.TestCase):
    def testInput(self):
        input = [
                "190: 10 19",
                "3267: 81 40 27",
                "83: 17 5",
                "156: 15 6",
                "7290: 6 8 6 15",
                "161011: 16 10 13",
                "192: 17 8 14",
                "21037: 9 7 18 13",
                "292: 11 6 16 20"
                ]
        self.assertEqual(3749, part1(input))

        concatenated = int(str(123)+str(456))
        #print(concatenated)
        self.assertEqual(11387, part2(input))
        pass

if __name__ == "__main__":
    unittest.main()
