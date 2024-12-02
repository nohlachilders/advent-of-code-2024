import sys

def main(arg):
    day = int(arg)
    input = []
    with open(f"inputs/{day:02d}.txt") as file:
        for line in file:
            input.append(line.strip())

    problem = __import__(f"day{day:02d}")
    problem.main(input)


main(sys.argv[1])
