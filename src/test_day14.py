import unittest

from day14 import *

class TestDay14(unittest.TestCase):
    def testDefault(self):
        input = [
                "p=0,4 v=3,-3",
                "p=6,3 v=-1,-3",
                "p=10,3 v=-1,2",
                "p=2,0 v=2,-1",
                "p=0,0 v=1,3",
                "p=3,0 v=-2,-2",
                "p=7,6 v=-1,-3",
                "p=3,0 v=-1,-2",
                "p=9,3 v=2,3",
                "p=7,3 v=-1,2",
                "p=2,4 v=2,-3",
                "p=9,5 v=-3,-3"
                ]
        vectors = process_input(input)
        positions = vectors[0]
        velocities = vectors[1]
        test_p = positions[10]
        test_v = velocities[10]
        steps = 5
        #print([take_step(11,7, test_p, test_v, i) for i in range(0,steps+1)])
        new_postitions = find_new_positions(11,7, positions, velocities, 100)
        factor = find_score(11,7, new_postitions)
        #print(factor)
        pass

if __name__ == "__main__":
    unittest.main()
