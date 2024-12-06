import unittest

from day05 import *

class TestDay05(unittest.TestCase):
    def testInputProcessing(self):
        string = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
        input = string.split("\n")
        #print(process_input(input))
        processed = process_input(input)
        rules = make_ordering_rules(processed[0])
        sequences = processed[1]
        #print(sequences)
        for i in sequences:
            #print(is_sequence_valid(rules, i))
            if not is_sequence_valid(rules,i):
                #print(sort_sequence(rules, i))
                pass



if __name__ == "__main__":
    unittest.main()
