import re

def parse_input(input):
    # list of strings to one string
    string = ""
    for i in input:
        string += i
    return string

def find_muls(input):
    # find instances of "mul(x,y)" in a string and return the sum of the products
    muls_raw = re.findall(r"mul\(\d+,\d+\)",input)
    sum = 0
    for i in muls_raw:
        digits = [int(digit) for digit in re.findall(r"\d+",i)]
        product = 1
        for j in digits:
            product *= j
        sum += product
    return sum

def filter_regex_tuple(tup):
    # pull the first nonempty string from a tuple since the re.findall() below
    # returns a tuple
    # with all the different groups instead of just a raw string of the matching
    # characters
    for i in tup:
        if i != '':
            return i

def find_muls_with_prefixes(input):
    # actually grug mode
    instructions_raw = re.findall(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))",input)
    instructions = [filter_regex_tuple(tup) for tup in instructions_raw]
    to_process = ""

    enabled = True
    for i in instructions:
        match i:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _:
                if enabled:
                    to_process += i
    return find_muls(to_process)

def main(input):
    input = parse_input(input)
    print(find_muls(input))
    print(find_muls_with_prefixes(input))
