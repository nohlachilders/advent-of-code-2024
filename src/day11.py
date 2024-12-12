import re
import collections
import itertools
import functools
## part1
#
# we are given a list of ints.
def process_input(input):
    return map(int, re.findall(r"\d+", input[0]))

# for each int in this list, we want to replace it with the results of the first
# applicable rule of the three
def blink(stones):
    return list(itertools.chain.from_iterable(map(do_stone_step, stones)))

def do_stone_step(stone):
    stringified = str(stone)
    if stone == 0:
        return [1]
    if len(stringified) % 2 == 0:
        left = int(stringified[0:len(stringified) // 2])
        right = int(stringified[len(stringified) // 2:])
        return [left, right]
    return [stone * 2024]

def part1(input):
    stones = process_input(input)
    for i in range(0,25):
        stones = blink(stones)
    return len(stones)



## part2
#
# uh oh
# so brute forcing this is inefficient. however. we can precalulate a lot of this.
# here are some base cases:
# 0: 1
# 1: 2024
# 2: 4048
# 3: 6072
# 4: 8096
# 5: 10120 : 
# 6: 12144
# 7: 14168
# 8: 16192
# 9: 18216
# the first digits result in an even number length, so they decompose into these bases cases.
# the higher digits will decompose after being multiplied by 2024 again.
# this suggests another recursive algorithm, with caching cases in a hashmap as they arise:
# stopping here. filtered.
@functools.cache
def blink_recursive(stones, depth):
    if depth == 10:
        return stones
    if len(stones) == 1:
        stringified = str(stones[0])
        if stones[0] == 0:
            return blink_recursive((1,), 0)
        if len(stringified) % 2 == 0:
            left = int(stringified[0:len(stringified) // 2])
            right = int(stringified[len(stringified) // 2:])
            return blink_recursive((left, right), depth + 1)
        return blink_recursive((stones[0] * 2024,), depth + 1)
    result = tuple(itertools.chain.from_iterable(map(lambda p: blink_recursive((p,), depth), stones)))
    return blink_recursive(result, depth + 1)





# main
def main(input):
    print(part1(input))
    pass
