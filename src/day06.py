# after a revision and rewrite, it is now almost correct. unfortunate.
# i learned a lot however.
# i cant really isolate where the issue is here.


import collections


def process_input(input):
    output = []
    for i in range(0, len(input)):
        output.append([])
        for char in input[i]:
            output[i].append(char)
    return output

Point = collections.namedtuple("Point", [ "x", "y"])
PointDirectionPair = collections.namedtuple("PointDirectionPair", ["point", "direction"])

transition_rule = {"^":">",
              ">":"v",
              "v":"<",
              "<":"^"
              }
movement_rule = {
            "^": Point(0,-1),
            ">": Point(1,0),
            "v": Point(0,1),
            "<": Point(-1,0)
            }


def is_point_in_bounds(point, board):
    x = point.x in range(0,len(board[0]))
    y = point.y in range(0,len(board))
    return x and y

def generate_board_graph(board):
    map = {}
    for y in range(0,len(board)):
        for x in range(0,len(board[0])):
            for direction in movement_rule.keys():
                map[PointDirectionPair(Point(x,y), direction)] = None
    for point_direction in map.keys():
        point = point_direction.point
        direction = point_direction.direction
        offset = movement_rule[direction]
        next_point = Point(point.x + offset.x, point.y + offset.y)
        if is_point_in_bounds(next_point, board):
            if board[next_point.y][next_point.x] == "#":
                direction = transition_rule[direction]
                offset = movement_rule[direction]
                next_point = Point(point.x + offset.x, point.y + offset.y)
                map[point_direction] = PointDirectionPair(next_point, direction)
            else:
                map[point_direction] = PointDirectionPair(next_point, direction)
    return map



def find_guard(input):
    for y in range(0,len(input)):
        for x in range(0,len(input[0])):
            if input[y][x] in transition_rule:
                return Point(x,y)
    return None

def walk_path(graph, starting_point):
    starting = PointDirectionPair(starting_point, "^")
    pointer = starting
    visited = [starting]
    while True:
        if pointer == None or pointer.point == None:
            break
        if pointer not in visited:
            visited.append(pointer)
        pointer = graph[pointer]
        #print(graph[pointer])
    return visited

def print_board(board, visited):
    for pointd in visited:
        point = pointd.point
        board[point.y][point.x] = "X"
    #print(visited)
    print("---------------")
    for i in board:
        print(i)
    print("---------------")

def add_barrier_to_graph(graph, point):
    old_keys = {}
    for incoming in graph.keys():
        if graph[incoming] != None:
            if point == graph[incoming].point:
                old_keys[incoming] = graph[incoming]
                direction = transition_rule[incoming.direction]
                offset = movement_rule[direction]
                next_point = Point(incoming.point.x + offset.x, incoming.point.y + offset.y)
                graph[incoming] = PointDirectionPair(next_point, direction)
    return old_keys

def walk_path_seeking_loop(graph, starting, visited):
    pointer = starting
    while True:
        if visited[pointer] == False:
            visited[pointer] = True
        pointer = graph[pointer]
        if pointer == None or pointer.point == None:
            break
        if visited[pointer] != False:
            return True
    return False

def part1(input):
    board = process_input(input)
    graph = generate_board_graph(board)
    visited = walk_path(graph,find_guard(board))
    points = list(set([i.point for i in visited]))
    return len(points)

def part2(input):
    board = process_input(input)
    graph = generate_board_graph(board)
    starting_point = find_guard(board)
    print("finding initial path")
    visited = walk_path(graph,starting_point)
    print("path found")
    sum = 0
    index = 0
    visited_map = {}
    for i in graph:
        visited_map[i] = False
    for y in range(0, len(board)):
        for x in range(0, len(board[0])):
            index +=1
            point = Point(x, y)
            print(f"loop entered, entry {index} of {len(board) * len(board[0])}")
            oldkeys = add_barrier_to_graph(graph, point)
            print("barrier added")
            print(f"scanning at {point}")
            if walk_path_seeking_loop(graph, PointDirectionPair(starting_point,"^"), visited_map):
                sum += 1
                print("loop found")
            graph.update(oldkeys)
            for j in graph:
                visited_map[j] = False
    return sum


def main(input):
    #print(part1(input))
    print(part2(input))
    pass
