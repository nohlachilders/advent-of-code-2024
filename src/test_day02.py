import unittest

from day02 import *

class TestDay02(unittest.TestCase):
    def testInputParse(self):
        input = ["1 1 1 1","2 2 2 2"]
        output = [[1,1,1,1],[2,2,2,2]]
        self.assertEqual(process_input(input), output)

    def testSafety(self):
        input = [[1,2,3,4],
                 [1,3,4,5],
                 [5,4,3,2],
                 [1,1,2,3],
                 [1,5,6,7],
                 [1,2,1,2],
                 [1,2,3,3]]
        self.assertEqual([1,1,1,0,0,0,0], [is_safe(i) for i in input])

    def testToleranceEdgeCases(self):
        input = [[48,46,47,49,51,54,56],
                 [1,1,2,3,4,5],
                 [1,2,3,4,5,5],
                 [5,1,2,3,4,5],
                 [1,4,3,2,1],
                 [1,6,7,8,9],
                 [1,2,3,4,3],
                 [9,8,7,6,7],
                 [7,10,8,10,11],
                 [29,28,27,25,26,25,22,20]]
        self.assertEqual([1 for i in range(0,10)],[is_safe_with_tolerance(i) for i in input])

    def testToleranceFalsePositive(self):
        input = [1,2,3,3,3]
        self.assertEqual(0, is_safe_with_tolerance(input))

if __name__ == "__main__":
    unittest.main()
