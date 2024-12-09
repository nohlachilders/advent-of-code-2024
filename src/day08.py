## part 1
# we want a set of valid coordinates. first, we want to have a list of all
# the antennas for each frequency and their location. then, we can create
# associated antinode locations based off of them.
# then we can take the total list of all antinodes, subtract ones that are out
# of bounds, and then subtract ones that overlap with an antenna
def process_input(input):
    output = []
    for i in range(0, len(input)):
        output.append([])
        for char in input[i]:
            output[i].append(char)
    return output

def get_locations_hashmap(input) -> dict:
    locations = {}
    for y in range(0, len(input)):
        for x in range(0, len(input[0])):
            char = input[y][x]
            if char not in locations:
                locations[char] = [[x,y]]
            else:
                locations[char].append([x,y])
    return locations

# for each antenna type, for each element in the locations,
# and for each remaining element in the suffix,
# calculate the dx,dy between the two, and the antinodes will be at
# element1-dx,dy and element1+2dx,2dy
def generate_antinode_locations(locations):
    antinodes = []
    for key in locations.keys():
        if key != ".":
            for i in range(0, len(locations[key])):
                pointer = locations[key][i]
                suffix_list = locations[key][i+1:]
                for suffix in suffix_list:
                    dx = suffix[0] - pointer[0]
                    dy = suffix[1] - pointer[1]
                    node1 = [pointer[0]-dx, pointer[1]-dy]
                    if node1 not in antinodes:
                        antinodes.append(node1)
                    node2 = [pointer[0]+2*dx, pointer[1]+2*dy]
                    if node2 not in antinodes:
                        antinodes.append(node2)
    return antinodes

def reprint_board(input, antinodes):
    copy = input
    for y in range(0,len(input)):
        for x in range(0, len(input[0])):
            if [x,y] in antinodes:
                copy[y][x] = "X"
    for row in copy:
        print(row)

def bound_antinode_locations(input, antinodes):
    x = len(input[0]) - 1
    y = len(input) - 1
    bounded = []
    for node in antinodes:
        if 0 <= node[0] <= x and 0 <= node[1] <= y:
            bounded.append(node)
    return bounded

def part1(input):
    map = process_input(input)
    locations = get_locations_hashmap(map)
    antinodes = bound_antinode_locations(input, generate_antinode_locations(locations))
    print(len(antinodes))


## part2
# so now, instead of making two nodes, we now have the more general case
# of making nodes along the same line, with the same calculated general offset.
# we now make nodes in a loop while the node is still in bounds. also, we must
# only generate new nodes if theres at least one other, but i think that happens
# already.
def generate_antinode_locations_with_harmonics(input, locations, antinodes):
    x = len(input[0]) 
    y = len(input) 
    for key in locations.keys():
        if key != ".":
            for i in range(0, len(locations[key])):
                pointer = locations[key][i]
                suffix_list = locations[key][i+1:]
                for suffix in suffix_list:
                    dx = suffix[0] - pointer[0]
                    dy = suffix[1] - pointer[1]
                    latest_node = [pointer[0],pointer[1]]
                    while latest_node[0] in range(0,x) and latest_node[1] in range(0,y):
                        if latest_node not in antinodes:
                            antinodes.append(latest_node)
                        latest_node = [latest_node[0] + dx, latest_node[1] + dy]

                    latest_node = [pointer[0],pointer[1]]
                    while latest_node[0] in range(0,x) and latest_node[1] in range(0,y):
                        if latest_node not in antinodes:
                            antinodes.append(latest_node)
                        latest_node = [latest_node[0] - dx, latest_node[1] - dy]
    return antinodes

def part2(input):
    map = process_input(input)
    locations = get_locations_hashmap(map)
    antinodes = generate_antinode_locations(locations)
    antinodes = bound_antinode_locations(map, antinodes)
    antinodes = generate_antinode_locations_with_harmonics(input, locations, antinodes)
    print(len(antinodes))


##
def main(input):
    part1(input)
    part2(input)
    pass
