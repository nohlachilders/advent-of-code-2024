import unittest

from day11 import *

class TestDay11(unittest.TestCase):
    def testDefault(self):
        input = ["125 17"]
        #stones = process_input(input)
        #test = list(itertools.chain.from_iterable([[0],[1,2],[3,4]]))
        #print(blink(stones))
        print(part1(input))
        test = ["0"]
        print(blink_recursive((125, 17), 4))
        print(blink_recursive((125, 17), 5))
        print(len(blink_recursive((125, 17), 75)))
        pass

if __name__ == "__main__":
    unittest.main()
