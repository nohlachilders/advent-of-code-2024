from dataclasses import dataclass
import itertools
import collections
## part 1
# we are given a matrix of integers.
def process_input(input):
    matrix = []
    for row in input:
        thisrow = [int(i) for i in row]
        matrix.append(thisrow)
    return matrix

# we want to build a hashmap of connections between spots on the grid.
# a node is connected to an adjacent node2 iff val(node) = val(node2-1).
# we can associate each coordinate on the grid with a structure containing its
# value and any connected nodes.
@dataclass
class Node():
    value: int
    connections: []

Coordinate = collections.namedtuple("Coordinate",["x","y"])

def make_nodegraph(matrix):
    nodes = {}
    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            # make the dict entry for this coordinate, and add any adjacent nodes
            coordinate = Coordinate(x,y)
            node = Node(matrix[y][x], [])
            node.connections = check_for_connections(matrix,coordinate)
            nodes[coordinate] = node
    return nodes

def check_for_connections(matrix, coordinate):
    connections = []
    bounds_x = len(matrix[0]) -1
    bounds_y = len(matrix) -1
    for offset in [Coordinate(1,0), Coordinate(0,1), Coordinate(-1,0), Coordinate(0,-1)]:
        x2 = coordinate.x + offset.x
        y2 = coordinate.y + offset.y
        if 0 <= x2 <= bounds_x and 0 <= y2 <= bounds_y:
            if matrix[y2][x2] == matrix[coordinate.y][coordinate.x] + 1:
                connections.append(Coordinate(x2,y2))
    return connections

# now, we can perform a depth first search on each node to generate the trail that starts from it.
# any given branch of the tree terminates when we reach a node that has no connections.
def find_trail_for_node(nodes, coordinate):
    return depth_first_search(nodes, coordinate)

def depth_first_search(nodes, coordinate):
    head = nodes[coordinate]
    search = [coordinate]
    if head.connections == []:
        return search
    else:
        for child in head.connections:
            search += depth_first_search(nodes, child)
        return list(set(search))

def part1(input):
    matrix = process_input(input)
    nodes = make_nodegraph(matrix)
    sum = 0
    for coordinate in nodes.keys():
        if nodes[coordinate].value == 0:
            trail = depth_first_search(nodes, coordinate)
            #print_trail(matrix, trail)
            for i in trail:
                if nodes[i].value == 9:
                    sum += 1
            #print(sum)
    return sum

def print_trail(matrix, trail):
    board = []
    for y in range(0, len(matrix)):
        board.append([])
        for x in range(0,len(matrix[0])):
            if Coordinate(x,y) in trail:
                board[y].append(str(matrix[y][x]))
            else:
                board[y].append(".")
        print(board[y])


## part 2
# we now want to, in our depth-first-search, get all paths from 0 nodes to
# 9 nodes.
# if we do another depth-first-search, and we return true if endpoints end in
# a 9, then every recursive path that is a unique path should return true.
def depth_first_search_part2(nodes, coordinate):
    head = nodes[coordinate]
    search = [coordinate]
    sum = 0
    if head.value == 9:
        sum += 1
    if head.connections == []:
        return sum
    else:
        for child in head.connections:
            sum += depth_first_search_part2(nodes, child)
        return sum

def part2(input):
    matrix = process_input(input)
    nodes = make_nodegraph(matrix)
    sum = 0
    for coordinate in nodes.keys():
        if nodes[coordinate].value == 0:
            sum += depth_first_search_part2(nodes, coordinate)
    return sum

## main
def main(input):
    print(part1(input))
    print(part2(input))
    pass
