# i gave up on part 2




# move the pointer character, leaving X behind until
# moving would place on top of collision. then rotate clockwise 90 degrees
# and continue until moving would place out of bounds.

def process_input(input):
    output = []
    for i in range(0, len(input)):
        output.append([])
        for char in input[i]:
            output[i].append(char)
    return output

transition_rule = {"^":">",
              ">":"v",
              "v":"<",
              "<":"^"
              }
movement_rule = {
            "^": [0,-1],
            ">": [1,0],
            "v": [0,1],
            "<": [-1,0]
            }

def find_guard(input):
    for y in range(0,len(input)):
        for x in range(0,len(input[0])):
            if input[y][x] in transition_rule:
                return [x,y]
    return None

def move_guard(board, pointer):
    x = pointer[0]
    y = pointer[1]
    offset = movement_rule[board[y][x]]
    dx = offset[0]
    dy = offset[1]


    is_in_bounds = 0 <= x + dx <= len(board[0])-1 and 0 <= y+dy <= len(board)-1
    if is_in_bounds and board[y+dy][x+dx] == "#":
        board[y][x] = transition_rule[board[y][x]]
        return (board, pointer)

    if not is_in_bounds:
        board[y][x] = "X"
        return (board, pointer)

    board[y+dy][x+dx] = board[y][x]
    pointer = [x+dx,y+dy]
    board[y][x] = "X"
    return (board, pointer)

def part1(input):
    pointer = find_guard(input)
    board = input
    while pointer != None:
        move_guard(input, pointer)
        pointer = find_guard(input)

    sum = 0
    for row in board:
        for char in row:
            if char == "X":
                sum += 1
    return sum

# for every place in the sim loop, scan ahead for an obstacle based on the offset
# rules. if succeeds, rotate and scan again. after third, see if ends up in initial
# position, then there is a loop
def check_for_loop_case1(iboard, pointer, state):
    # scan ahead.
    initial = pointer
    x0 = initial[0]
    y0 = initial[1]
    offset = movement_rule[state]
    board = iboard

    i = 1
    while True:
        scan_results = scan_for_obstacle(board, pointer, state)
        if scan_results == None:
            return False
        new_pointer = scan_results[1]
        state = scan_results[2]
        offset = movement_rule[state]
        print(f"{initial}, {pointer}, {new_pointer}")
        print_board(board)
        if i >= 4:
            in_range_x = pointer[0] <= x0 <= new_pointer[0] or pointer[0] >= x0 >= new_pointer[0]
            in_range_y = pointer[1] <= y0 <= new_pointer[1] or pointer[1] >= y0 >= new_pointer[1]
            if in_range_y and in_range_x:
                return True
        pointer = new_pointer
        i += 1
    return False

def check_for_loop_case2(board, pointer, state):
    # scan ahead.
    initial = pointer
    x0 = initial[0]
    y0 = initial[1]
    state = transition_rule[state]
    offset = movement_rule[state]

    i = 1
    while True:
        scan_results = scan_for_obstacle(board, pointer, state)
        if scan_results == None:
            return False
        new_pointer = scan_results[1]
        state = scan_results[2]
        offset = movement_rule[state]
        print(f"{initial}, {pointer}, {new_pointer}")
        print_board(board)
        if i == 4:
            in_range_x = pointer[0] <= x0 <= new_pointer[0] or pointer[0] >= x0 >= new_pointer[0]
            in_range_y = pointer[1] <= y0 <= new_pointer[1] or pointer[1] >= y0 >= new_pointer[1]
            if in_range_y and in_range_x:
                return True
        pointer = new_pointer
        i += 1
    return False



def scan_for_obstacle(board, initial, state): 
    x = initial[0]
    y = initial[1]
    offset = movement_rule[state]
    dx = offset[0]
    dy = offset[1]
    pointer = [x+dx,y+dy]
    step_is_in_bounds = (0 <= pointer[1]+dy <= len(board[0])-1) and (0 <= pointer[0]+dx <= len(board)-1)

    loop = True
    while loop:
        if step_is_in_bounds:
            if board[pointer[1]+dy][pointer[0]+dx] != "#":
                board[pointer[1]][pointer[0]] = "X" #clear me
                pointer = [pointer[0]+dx, pointer[1]+dy]
                board[pointer[1]][pointer[0]] = "X" #clear me
                step_is_in_bounds = (0 <= pointer[1]+dy <= len(board[0])-1) and (0 <= pointer[0]+dx <= len(board)-1)
            elif board[pointer[1]+dy][pointer[0]+dx] == "#":
                loop = False
        else:
            loop = False

    return (board, pointer, transition_rule[state])

    
def part2(input):
    pointer = find_guard(input)
    board = input
    sum = 0

    while pointer != None:
        print_board(board)
        if check_for_loop(board, pointer, board[pointer[1]][pointer[0]]):
            sum += 1
        move_guard(input, pointer)
        pointer = find_guard(input)
        print(f"pointer at {pointer}")
    return sum

def print_board(board):
    print("---------------")
    for i in board:
        print(i)
    print("---------------")


def main(input):
    board = process_input(input)
    print(part1(board))
    pass
