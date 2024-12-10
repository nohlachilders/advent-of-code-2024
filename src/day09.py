from dataclasses import dataclass
## part 1
# we want to return a checksum for a formatted disk.
# we can render out the disk given its description into a string.
# we then format the disk by iterating backwards, and if the given element is
# a data block, swap it with the first free space, found by iterating forwards.
# calculating the checksum of the formatted disk is then sum(i * element)
def process_input(input):
    output = ""
    for string in input:
        output += string
    return output

def render_disk_image(input):
    disk = []
    id = 0
    for i in range(0,len(input)):
        if i % 2 == 0:
            for i in range(0,int(input[i])):
                disk.append(str(id))
            id += 1
        else:
            for i in range(0,int(input[i])):
                disk.append(".")
    return disk

def format_disk(disk):
    formatted = []
    j = 0
    for char in disk:
        formatted.append(char)
    for i in range(len(formatted)-1,0,-1):
        if formatted[i] != ".":
            flag = True
            while flag:
                if j >= len(formatted)-1 or j >= i:
                    flag = False
                else:
                    if formatted[j] == "." and j < i:
                        formatted[i], formatted[j] = formatted[j], formatted[i]
                        #break while
                        flag = False
                    j = min(len(formatted)-1, j + 1)
    return formatted

def calculate_checksum(formatted):
    sum = 0
    for i in range(0, len(formatted)):
        if formatted[i] != ".":
            sum += int(formatted[i]) * i
    return sum

def part1(input):
    input = process_input(input)
    disk = render_disk_image(input)
    formatted = format_disk(disk)
    #print(formatted)
    return calculate_checksum(formatted)


## part 2
# now, we must move entire files, which are sections of blocks with the same id.
# we must fit these into the leftmost contiguous section of empty space that will
# fit it.

@dataclass
class File:
    id: int
    size: int

def render_disk_image_with_whole_files(input):
    disk = []
    id = 0
    for i in range(0,len(input)):
        if i % 2 == 0:
            disk.append(File(id = id, size = int(input[i])))
            id += 1
        else:
            for i in range(0,int(input[i])):
                disk.append(".")
    return disk

def find_last_file(input,pointer):
    last_file_pointer = pointer
    for i in range(pointer,0,-1):
        if input[i] != ".":
            last_file_pointer = i
            break
    return last_file_pointer

def find_first_empty_space(input,pointer):
    first_empty_space = pointer
    for j in range(pointer,len(input)):
        if input[j] == ".":
            first_empty_space = j
            break
    return first_empty_space

def find_empty_stretch_at_pointer(input, pointer):
    length = 0
    while pointer + length < len(input)-1:
        if input[pointer + length] != ".":
            break
        length += 1
    return length

def format_last_file(disk, right_pointer):
    formatted = disk
    right_pointer = find_last_file(disk, right_pointer)
    #print(disk[right_pointer])
    left_pointer =  find_first_empty_space(disk, 0)
    file_size = formatted[right_pointer].size
    while left_pointer < right_pointer:
        length = find_empty_stretch_at_pointer(formatted, left_pointer)
        if length >= file_size:
            formatted[right_pointer:right_pointer+1], formatted[left_pointer:left_pointer+file_size] = formatted[left_pointer:left_pointer+file_size], formatted[right_pointer:right_pointer+1]
            return formatted, right_pointer - 1
        left_pointer = find_first_empty_space(formatted, left_pointer+1)
        #print_part2_board(formatted)
    return formatted, right_pointer - 1

def format_disk_with_whole_files(input):
    count = len([i for i in input if i != "."])
    formatted = input
    right_pointer = len(input)-1
    for i in range(0,count):
        results = format_last_file(formatted, right_pointer)
        formatted = results[0]
        right_pointer = results[1]
    return formatted

def print_part2_board(input):
    string = ""
    for i in input:
        if i == ".":
            string += "."
        else:
            string += str(i.id)
    print(string)

def render_part2_disk(input):
    disk = []
    for i in input:
        if i == ".":
            disk.append(".")
        else:
            for j in range(0, i.size):
                disk.append(i.id)
    return disk

def part2(input):
    input = process_input(input)
    disk = render_disk_image_with_whole_files(input)
    disk = format_disk_with_whole_files(disk)
    disk = render_part2_disk(disk)
    return calculate_checksum(disk)


## main
def main(input):
    print(part1(input))
    print(part2(input))
