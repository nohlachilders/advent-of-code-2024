# Todays problem is linear algebra related.
# We are given two points, and are asked to find
# a linear combination that results in the desired point.
# However, we can easily test to see if these points
# form a basis of the space of 2d integer vectors.
# if they do, then the combination is necessarily unique.
# if they do not, then the combination cannot exist.

import numpy as np
import re
## part 1
def process_input(input):
    vectors_a = []
    vectors_b = []
    vectors_prize = []
    for line in input:
        if "Button A" in line:
            l = list(map(int, re.findall(r"\d+", line)))
            vectors_a.append(np.array(l, dtype=np.int64))
        if "Button B" in line:
            l = list(map(int, re.findall(r"\d+", line)))
            vectors_b.append(np.array(l, dtype=np.int64))
        if "Prize" in line:
            l = list(map(int, re.findall(r"\d+", line)))
            vectors_prize.append(np.array(l, dtype=np.int64))
    return (vectors_a, vectors_b, vectors_prize)

# then simply solve the system of linear equations.
# i tried for a long time to get it to work with floating point math
# since its just one np function, but i had to capitulate
# and look up the way to do it algorithmically. bc i dont remember any math.
# in this case cramers rule.
# applied math degree btw
def solve_for_combination(vector_a, vector_b, prize):
    a = np.column_stack((vector_a, vector_b))
    det_a = a[0][0]*a[1][1] - a[0][1] * a[1][0]
    solution = []
    for i in [0,1]:
        vecs = [vector_a, vector_b]
        vecs[i] = prize
        ai = np.column_stack(tuple(vecs))
        det_ai = ai[0][0]*ai[1][1] - ai[0][1] * ai[1][0]
        solution.append(det_ai / det_a)
    return np.array(solution, dtype=np.int64)

def get_token_cost(vector_a, vector_b, prize):
    solution = solve_for_combination(vector_a, vector_b, prize)
    if (int(np.round(solution[0])) * vector_a + int(np.round(solution[1])) * vector_b == prize).all():
       return int(solution[0]) * 3 + int(solution[1])
    else:
        return 0

def part1(input):
    vectors = process_input(input)
    a = vectors[0]
    b = vectors[1]
    prize = vectors[2]
    sum = 0
    for i in range(0, len(vectors[0])):
        #print(solve_for_combination(a[i], b[i], prize[i]))
        sum += get_token_cost(a[i], b[i], prize[i])
    return sum

## part 2
# the position of the given prizes must now be offset by 10000000000000.
# should already be fine.

def process_input_part2(input):
    vectors_a = []
    vectors_b = []
    vectors_prize = []
    for line in input:
        if "Button A" in line:
            l = list(map(int, re.findall(r"\d+", line)))
            vectors_a.append(np.array(l, dtype=np.int64))
        if "Button B" in line:
            l = list(map(int, re.findall(r"\d+", line)))
            vectors_b.append(np.array(l, dtype=np.int64))
        if "Prize" in line:
            l = list(map(int, re.findall(r"\d+", line)))
            offset = lambda x: x + 10000000000000
            l = list(map(offset, l))
            vectors_prize.append(np.array(l, dtype=np.int64))
    return (vectors_a, vectors_b, vectors_prize)

def part2(input):
    vectors = process_input_part2(input)
    a = vectors[0]
    b = vectors[1]
    prize = vectors[2]
    sum = 0
    for i in range(0, len(vectors[0])):
        #print(solve_for_combination(a[i], b[i], prize[i]))
        sum += get_token_cost(a[i], b[i], prize[i])
    return sum

## main
def main(input):
    print(part1(input))
    print(part2(input))
    pass
