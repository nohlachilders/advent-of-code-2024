import re
## part 1
# given an input and a list of strings, we want to find whether it can be made
# with the operations * and +.

class PuzzleEntry:
    goal: int
    elements: list
    def __init__(self, goal, elements):
        self.goal = goal
        self.elements = elements

    def __str__(self):
        return f"goal: {self.goal}, elements: {self.elements}"

def process_input(input):
    entries = []
    for i in input:
        nums = [int(i) for i in re.findall(r"\d+", i)]
        entries.append(PuzzleEntry(goal = nums[0], elements = nums[1:]))
    return entries

# if the length of the list is 1, return list[0]==goal
# if the length of the list is > 1, we can run two recursive cases, one for each operator
# so return check([list[0]+list[1]] + list[2:], goal) or check([list[0]*list[1]] + list[1:], goal)
def check_for_combination_recursive(goal, elements, flag = False):
    if len(elements) == 1:
        return elements[0] == goal

    check_concatenation = False
    if flag:
        concatenated = int(str(elements[0])+str(elements[1]))
        check_concatenation = check_for_combination_recursive(goal, [concatenated] + elements[2:], flag)

    check_addition = check_for_combination_recursive(goal, [elements[0]+elements[1]] + elements[2:], flag)
    check_multiplication = check_for_combination_recursive(goal, [elements[0]*elements[1]] + elements[2:], flag)
    return check_addition or check_multiplication or check_concatenation

def part1(input):
    input = process_input(input)
    total = 0
    for i in input:
        if check_for_combination_recursive(i.goal, i.elements):
            #print(True, i.goal, i.elements)
            #print(sum(i.elements))
            total += i.goal
    return total

## part 2
# the same as the previous algorithm, but with a third recursive case:
# we now also check the digits added together. the above algorithm has been modified.

def part2(input):
    input = process_input(input)
    total = 0
    for i in input:
        if check_for_combination_recursive(i.goal, i.elements, True):
            #print(True, i.goal, i.elements)
            #print(sum(i.elements))
            total += i.goal
    return total

## main
def main(input):
    print(part1(input))
    print(part2(input))
    pass
