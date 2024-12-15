import numpy as np
import collections
import re
# part 1
# we are given several points and velocities. they exist in a grid.
# they advance by the given velocity each step. they wrap around the grid.
# ergo their positiion can just be modulod by the size of the grid.
def process_input(input):
    positions = []
    velocities = []
    for line in input:
        numbers = [int(i) for i in re.findall(r"[-]*\d+", line)]
        positions.append(np.array((numbers[0],numbers[1])))
        velocities.append(np.array((numbers[2],numbers[3])))
    return [positions, velocities]

def take_step(x, y, position, velocity, steps):
    new = position + (velocity * steps)
    new_bounded = np.array([new[0] % x, new[1] % y])
    return new_bounded

def find_new_positions(x, y, positions, velocities, steps):
    new = []
    for i in range(0, len(positions)):
        new.append(take_step(x,y,positions[i], velocities[i], steps))
    return new

def find_score(x,y,positions):
    midpoint = [x//2, y//2]
    # first quadrant is less than midpoint for axis
    quadrant_scores = [0,0,0,0]
    for i in positions:
        if i[0] < midpoint[0] and i[1] < midpoint[1]:
            quadrant_scores[0] += 1
        elif i[0] > midpoint[0] and i[1] < midpoint[1]:
            quadrant_scores[1] += 1
        elif i[0] < midpoint[0] and i[1] > midpoint[1]:
            quadrant_scores[2] += 1
        elif i[0] > midpoint[0] and i[1] > midpoint[1]:
            quadrant_scores[3] += 1
    print(quadrant_scores)
    return np.prod(np.array(quadrant_scores))






def part1(input):
    vectors = process_input(input)
    positions = vectors[0]
    velocities = vectors[1]
    steps = 100
    x = 101
    y= 103
    new_postitions = find_new_positions(x,y, positions, velocities, 100)
    factor = find_score(x,y, new_postitions)
    print(factor)
    pass

# part 2
# if the image is wierdly dense in a reigon then it probably forms an image.
# i dont know and dont care about testing for this.
# slow and bruteforced but works
def part2(input):
    vectors = process_input(input)
    position = vectors[0]
    velocities = vectors[1]
    steps = 100
    x = 101
    y= 103
    max_score = 0
    step_this_happened_on = 0
    sum_of_scores = 0
    scores = [[],[],[]]
    for i in range(1,10000):
        positions = find_new_positions(x,y, position, velocities, i)
        score = look_for_a_big_vertical_line_or_something(positions)
        sum_of_scores += score
        if score > max_score:
            max_score = score
            step_this_happened_on = i
            scores += [[step_this_happened_on, score]]
        print("loop", i, score, scores[-1], scores[-2], scores[-3])
    print(max_score)
    print(step_this_happened_on)
    print(sum_of_scores/1000)

def look_for_a_big_vertical_line_or_something(points):
    maybe_score = 0
    for i in range(0,len(points)//2):
        y = points[i][1]
        x = points[i][0]
        for j in range(0,5):
            is_in_points= lambda point : np.any(np.all(point == points, axis=1))
            if is_in_points(np.array([x,y+j])) or is_in_points(np.array([x,y-j])):
                maybe_score += 1
            else:
                break
        for j in range(0,5):
            is_in_points= lambda point : np.any(np.all(point == points, axis=1))
            if is_in_points(np.array([x+j,y])) or is_in_points(np.array([x-j,y])):
                maybe_score += 1
            else:
                break
    return maybe_score


# main
def main(input):
    print(part1(input))
    part2(input)
    pass
