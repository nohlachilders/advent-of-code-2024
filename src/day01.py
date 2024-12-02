def split_lists(input):
    splitted = [[],[]]
    for line in input:
        words = line.split()
        for i in range(0, len(words)):
            splitted[i].append(words[i])
    return splitted

def main(input):
    print(input)

