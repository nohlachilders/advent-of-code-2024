#todays is really gross and not worth reading tbh lmfao

def check_for_word_start(input, word):
    offsets = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            offsets.append([i,j])
    offsets.remove([0,0])
    
    occurrences = 0
    loops = 0
    for x in range(0,len(input)):
        for y in range(0,len(input)):
            for offset in offsets:
                result = search_recursive(input, word, x, y, offset)
                occurrences += result
                loops +=1
    #print(loops)
    return occurrences

def search_recursive(input, word, x, y, offset):
    if word == "" or word == input[x][y]:
        #print(f"word empty or last letter matches. assuming match found. return true")
        return 1
    if word[0] != input[x][y]:
        #print(f"{word[0]} does not match {input[x][y]}. returning false")
        return 0
    
    in_bounds_x = 0 <= x + offset[0] <= len(input)-1
    in_bounds_y = 0 <= y + offset[1] <= len(input)-1
    if in_bounds_y and in_bounds_x:
        #print(f"recurring with {word} at {(x,y)} with offset {offset}")
        return search_recursive(input, word[1:], x+offset[0], y+offset[1], offset)
    else:
        #print(f"word {word} at {(x,y)} not in bounds with offset {offset}. returning false.")
        return 0

def detect_x_of_mas(input, x, y):
    in_bounds_x = 0 < x < len(input)-1
    in_bounds_y = 0 < y < len(input)-1
    if not (in_bounds_y) or not (in_bounds_x):
        return 0

    offsets = [[1,1], [1,-1]]
    for offset in offsets:
        letters = "MS"
        if input[x+offset[0]][y+offset[1]] in letters:
            letters = "".join([i for i in letters if i != input[x+offset[0]][y+offset[1]]])
        else:
            return 0
        if input[x+-1*offset[0]][y+-1*offset[1]] in letters:
            letters = "".join([i for i in letters if i != input[x+-1*offset[0]][y+-1*offset[1]]])
        else:
            return 0
    return 1

def count_x_of_mas(input):
    count = 0
    for x in range(0, len(input)):
        for y in range(0, len(input)):
            if input[x][y]== "A":
                count += detect_x_of_mas(input,x,y)
    return count

def main(input):
    print(input_info(input))
    print(check_for_word_start(input, "XMAS"))
    print(count_x_of_mas(input))
