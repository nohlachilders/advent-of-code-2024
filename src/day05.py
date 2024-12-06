# we want to identify which lines follow ordering rules
# we want to find the middle element of those lines
# we want to give the sum of the middle element of the correctly ordered lines
import re

def process_input(input):
    # return a list of pairs of ints (the ordering rules)
    pairs = []

    # return a list of lists of ints (the sequences)
    sequences = []

    for line in input:
        if re.fullmatch(r"\d+\|\d+", line):
            pairs.append([int(i) for i in line.split("|")])
        if re.fullmatch(r"(\d+,)+\d+", line):
            sequences.append([int(i) for i in line.split(",")])

    return (pairs, sequences)

def make_ordering_rules(pairs):
    #rules are value-after-key, value-before-key. if key is in after, values come after key
    before = {}
    after = {}
    for pair in pairs:
        if pair[0] not in after:
            after[pair[0]] = [pair[1]]
        else:
            after[pair[0]].append(pair[1])

        if pair[1] not in before:
            before[pair[1]] = [pair[0]]
        else:
            before[pair[1]].append(pair[0])
    return (before,after)

def is_sequence_valid(rules, sequence):
    before = rules[0]
    after = rules[1]

    for i in range(0,len(sequence)):
        pointer = sequence[i]
        prefix = sequence[:i]
        suffix = sequence[i+1:]
        for element in prefix:
            if pointer in after:
                if element in after[pointer]:
                    #print(f"{element} was found before {pointer} in {sequence} despite before {before}")
                    return False
        for element in suffix:
            if pointer in before:
                if element in before[pointer]:
                    #print(f"{element} was found after {pointer} in {sequence} despite after {after}")
                    return False
    return True

def part1(input):
    processed = process_input(input)
    rules = make_ordering_rules(processed[0])
    sequences = processed[1]
    sum = 0
    for i in sequences:
        if is_sequence_valid(rules, i):
            sum += i[len(i) // 2]
    return sum

def sort_sequence(rules, sequence):
    # its quicksort but instead of using normal greater than/less than rules we are given them
    if sequence == []:
        return sequence
    before = rules[0]
    after = rules[1]
    pointer = sequence[0]
    prefix = []
    suffix = []
    for i in sequence[1:]:
        if pointer in after:
            if i in after[pointer]:
                suffix.append(i)
        if pointer in before:
            if i in before[pointer]:
                prefix.append(i)
    return sort_sequence(rules, prefix) + [pointer] + sort_sequence(rules, suffix)

def part2(input):
    processed = process_input(input)
    rules = make_ordering_rules(processed[0])
    sequences = processed[1]
    sum = 0
    for i in sequences:
        if not is_sequence_valid(rules, i):
            sorted = sort_sequence(rules, i)
            sum += sorted[len(sorted) // 2]
    return sum


def main(input):
    print(part1(input))
    print(part2(input))
