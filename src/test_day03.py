
import unittest

from day03 import *

class TestDay02(unittest.TestCase):
    def testInputParse(self):
        self.assertEqual(parse_input(["hello", "world"]), "helloworld")

    def testMulSum(self):
        input = "mul(,3)mul(1,3)mul(1,4)14"
        #print(re.findall(r"\d+",input))
        self.assertEqual(find_muls(input),7)

    def testPart2(self):
        input = "dont()do()dont()mul(1,2)do()mul(1,3)"
        instructions = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(dont\(\))",input)
        tup = ('','','this')
        #print(filter_regex_tuple(tup))
        #print(filter_regex_tuple(instructions))
        #print(find_muls_with_prefixes(input))

if __name__ == "__main__":
    unittest.main()
