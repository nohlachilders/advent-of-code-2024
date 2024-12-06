import sys

def main(arg):
    day = int(arg)
    input = []
    with open(f"inputs/{day:02d}.txt") as file:
        for line in file:
            input.append(line.strip())

    problem = __import__(f"day{day:02d}")
    print(input_info(input))
    problem.main(input)

def input_info(input):
    counts = {}
    for line in input:
        if len(line) not in counts:
            counts[len(line)] = 1
        else:
            counts[len(line)] +=1
    return counts

main(sys.argv[1])
