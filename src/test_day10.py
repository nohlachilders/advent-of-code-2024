import unittest

from day10 import *

class TestDay10(unittest.TestCase):
    def testDefault(self):
        input = [
                "89010123",
                "78121874",
                "87430965",
                "96549874",
                "45678903",
                "32019012",
                "01329801",
                "10456732"]
        matrix = process_input(input)
        nodes = make_nodegraph(matrix)
        #print(find_trail_for_node(nodes, Coordinate(2,0)))
        self.assertEqual(36,part1(input))
        self.assertEqual(81,part2(input))
        pass


if __name__ == "__main__":
    unittest.main()
