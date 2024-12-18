import re
import itertools
import collections
# we need to write a parser for a specified programming language.
# we have a few functions, a basic evaluation loop, three addresses of memory,
# an output, and a pointer for where in the program we are.

def process_input(input):
    ints = []
    for line in input:
        ints.append([int(i) for i in re.findall(r"\d+", line)])
    return list(itertools.chain.from_iterable(ints))

def part1(input):
    ints = process_input(input)
    program = ChronospatialParser(ints[3:],ints[0], ints[1], ints[2])
    return program.run_program()

# defeated out of lazyness
def part2(input):
    ints = process_input(input)
    program = ints[3:]
    print(program)
    case = []
    index = 8 ** 15
    increases = []
    matches = collections.defaultdict(int)
    while case != program:
        index += 32768
        thisprogram = ChronospatialParser(ints[3:],index, ints[1], ints[2])
        next_case = thisprogram.run_program()
        if len(next_case) > len(case):
            increases.append(index)
        case = next_case
        matching = 0
        for i in range(0,len(case)):
            if case[i] == program[i]:
                matching += 1
        matches[matching] += 1
        print(index, len(case), matching, increases, matches)
    return index

## main
def main(input):
    print(part2(input))
# ideas:
# store language level instructions in a map. this implies i should use oop
# since theres a part 2, having global variables might get annoying.
# so for now i will use oop.

class ChronospatialParser():
    def __init__(self, program:list, a:int,b:int,c:int):
        self.program = tuple(program)
        self.a = a
        self.b = b
        self.c = c
        self.pointer = 0
        self.operand = 1
        self.output = []

    def run_program(self):
        while self.pointer in range(0,len(self.program)-1):
            match self.do_instruction(self.program[self.pointer]):
                case 0:
                    self.pointer += 2
                    self.operand += 2
                case _:
                    # in this case the pointer got reassigned
                    self.operand = self.pointer+1
        return self.output
        
    
    def get_operand(self, operand):
        operands = {
                0:0,
                1:1,
                2:2,
                3:3,
                4:self.a,
                5:self.b,
                6:self.c,
                7:-1
                }
        return operands[self.program[operand]]
        
    def do_instruction(self, instruction):
        instructions = {
                0:self.adv,
                1:self.bxl,
                2:self.bst,
                3:self.jnz,
                4:self.bxc,
                5:self.out,
                6:self.bdv,
                7:self.cdv,
                }
        return instructions[instruction]()

    def get_description(self, instruction):
        descriptions = {
                0:"a/2^o into a",
                1:"b xor ol into b",
                2:"o % 8 into b",
                3:"jump to ol",
                4:"b xor c into b",
                5:"o mod 8 into out",
                6:"a/2^o into b",
                7:"a/2^0 into c"
                }
        print(descriptions[instruction])


    def adv(self):
        self.a = self.a // (2 ** self.get_operand(self.operand))
        return 0

    def bxl(self):
        self.b = self.b ^ self.program[self.operand]
        return 0

    def bst(self):
        self.b = self.get_operand(self.operand) % 8
        return 0

    def jnz(self):
        if self.a == 0:
            return 0
        else:
            self.pointer = self.program[self.operand]
            return 1

    def bxc(self):
        self.b = self.b ^ self.c
        return 0

    def out(self):
        self.output.append(self.get_operand(self.operand) % 8)
        return 0

    def bdv(self):
        self.b = self.a // (2 ** self.get_operand(self.operand))
        return 0

    def cdv(self):
        self.c = self.a // (2 ** self.get_operand(self.operand))
        return 0

