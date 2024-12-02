def split_lists(input):
    splitted = [[],[]]
    for line in input:
        words = line.split()
        for i in range(0, len(words)):
            splitted[i].append(words[i])
    return splitted

def quicksort(arr):
    # i dont think this is the right way to write this but whatever it works lol
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return quicksort(left) + middle + quicksort(right)

def get_distances(arr1, arr2):
    distances = [abs(i - j) for i,j in zip(arr1, arr2)]
    return sum(distances)

def get_similarity(arr1, arr2):
    # put the number of times an element of the first list appears in the second
    # in a hashmap, so that we only need to count it once and can look it up
    # quickly if it appears again
    counts = {}
    total_score = 0
    for i in arr1:
        if i not in scores:
            scores[i] = len([j for j in arr2 if j == i])
        total_score += scores[i] * i
    return total_score

def main(input):
    # split our input array of "rows" into two lists by "column", delimited by spaces
    input_lists = split_lists(input)

    # sort the lists so we can do the given distance calculation simply
    list1 = [int(i) for i in input_lists[0]]
    list1 = quicksort(list1)
    list2 = [int(i) for i in input_lists[1]]
    list2 = quicksort(list2)

    print(get_distances(list1, list2))
    print(get_similarity(list1, list2))


