import unittest

from day04 import *

class TestDay04(unittest.TestCase):
    def testSampleInput(self):
       input = ["MMMSXXMASM",
       "MSAMXMSMSA",
       "AMXSXMAAMM",
       "MSAMASMSMX",
       "XMASAMXAMM",
       "XXAMMXXAMA",
       "SMSMSASXSS",
       "SAXAMASAAA",
       "MAMMMXMMMM",
       "MXMXAXMASX"]
       #print(input_info(input))
       self.assertEqual(18, check_for_word_start(input,"XMAS"))
       #print(search_recursive(input,"XMAS",9,3,[-1,-1]))
       print(count_x_of_mas(input))

if __name__ == "__main__":
    unittest.main()
