
import unittest

from day06 import *

class TestDay06(unittest.TestCase):
    def testInputProcessing(self):
        input = [
                "....#.....",
                ".........#",
                "..........",
                "..#.......",
                ".......#..",
                "..........",
                ".#..^.....",
                "........#.",
                "#.........",
                "......#..."
                ]

        board = process_input(input)
        #print(part2(board))
        #self.assertTrue(check_for_loop(board,[4,6], "<"))
        #self.assertTrue(check_for_loop(board,[6,6], "<"))
        #self.assertTrue(check_for_loop(board,[6,7], "v"))
        #self.assertTrue(check_for_loop_case2(board,[2,8], "<"))
        #self.assertTrue(check_for_loop_case2(board,[4,8], "<"))
        pass


if __name__ == "__main__":
    unittest.main()
