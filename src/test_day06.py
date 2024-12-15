
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

        #board = process_input(input)
        #graph = generate_board_graph(board)
        #visited = walk_path(graph,find_guard(board))
        #print_board(board, visited)
        #print(part1(input))
        #print(grab_adjacent_tiles_to_path(board, visited))
        #graph = add_barrier_to_graph(graph, Point(3,6))
        #print(walk_path_seeking_loop(graph,Point(4,6)))

        #print_board(board,new)
        #print(part2(input))
        #self.assertTrue(check_for_loop(board,[4,6], "<"))
        #self.assertTrue(check_for_loop(board,[6,6], "<"))
        #self.assertTrue(check_for_loop(board,[6,7], "v"))
        #self.assertTrue(check_for_loop_case2(board,[2,8], "<"))
        #self.assertTrue(check_for_loop_case2(board,[4,8], "<"))
        pass


if __name__ == "__main__":
    unittest.main()
