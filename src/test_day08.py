import unittest

from day08 import *

class TestDay08(unittest.TestCase):
    def testInput(self):
        input = [
                "............",
                "........0...",
                ".....0......",
                ".......0....",
                "....0.......",
                "......A.....",
                "............",
                "............",
                "........A...",
                ".........A..",
                "............",
                "............"]
        input = process_input(input)
        #print(input)
        locations = get_locations_hashmap(input)
        #print(locations["0"])
        #print(generate_antinode_locations(locations))
        antinodes = bound_antinode_locations(input, generate_antinode_locations(locations))
        #reprint_board(input,antinodes)
        self.assertEqual(14,len(antinodes))
        harmonics = generate_antinode_locations_with_harmonics(input, locations, antinodes)
        harmonics = bound_antinode_locations(input, harmonics)
        #reprint_board(input, harmonics)
        self.assertEqual(34,len(antinodes))
        pass

if __name__ == "__main__":
    unittest.main()
