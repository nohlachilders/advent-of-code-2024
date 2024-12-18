import unittest

from day17 import *

class TestDay17(unittest.TestCase):
    def testDefault(self):
        test_input = [
                "Register A: 729",
                "Register B: 0",
                "Register C: 0",
                "",
                "Program: 0,1,5,4,3,0",
                ]
        test_input_2 = [
                "Register A: 117440",
                "Register B: 0",
                "Register C: 0",
                "",
                "Program: 0,3,5,4,3,0",
                ]
        #print(process_input(test_input))
        print(part1(test_input))
        print(part1(test_input_2))
        print(part2(test_input_2))
        pass

if __name__ == "__main__":
    unittest.main()
