def process_input(input):
    # turn list of strings into list of lists of ints
    output = [i.split() for i in input]
    for row in output:
        for i in range(0, len(row)):
            row[i] = int(row[i])
    return output

def is_safe(arr):
    # initialize the increment direction based off of the first index.
    # if theres a mismatch, it wasnt safe anyway.
    positivity = 1
    if arr[1]-arr[0] < 0:
        positivity = -1
    if arr[1]-arr[0] == 0:
        return 0

    for i in range(1, len(arr)):
        delta = arr[i] - arr[i-1]
        if delta * positivity not in [1,2,3]:
            return 0
    return 1

def is_safe_with_tolerance(arr):
    # same as the tolerance function, but if theres an issue, we can try to
    # remove one of three indicies: the two with an increment issue, or the
    # first index, which we were using to initialize the increment direction.
    # inefficient but idc
    positivity = 1
    if arr[1]-arr[0] < 0:
        positivity = -1

    for i in range(1, len(arr)):
        delta = arr[i] - arr[i-1]
        if delta * positivity not in [1,2,3]:
            return max(is_safe(arr[:i-1]+arr[i:]), is_safe(arr[:i]+arr[i+1:]), is_safe(arr[1:]))
    return 1

def main(input):
    levels = process_input(input)

    print(sum([is_safe(i) for i in levels]))
    print(sum([is_safe_with_tolerance(i) for i in levels]))


