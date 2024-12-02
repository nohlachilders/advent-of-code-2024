import unittest

from day01 import *

class TestDay01(unittest.TestCase):
    def testSplit(self):
        list = ["1 1", "2    2", "2323 3232"]
        self.assertEqual(split_lists(list), [["1","2","2323"],["1","2","3232"]])

    def testDistance(self):
        list1 = [0, 1, 1, 0]
        list2 = [0, 1, 3, 0]
        print(distance(list1,list2))

if __name__ == "__main__":
    unittest.main()
