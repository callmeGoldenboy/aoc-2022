
from pprint import pprint
def main():
    with open("../input.txt", "r") as f:
        lines = f.read().splitlines()
    
    size = len(lines)
    matrix = [[0 for col in range(size)] for row in range(size)]
    for i in range(len(matrix)):
        line = lines[i]
        for col in range(len(matrix)):
            matrix[i][col] = int(line[col])
    
    max_score = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            current_score = calc_score(matrix, row, col)
            if current_score >max_score:
                max_score = current_score
    
    print("max score", max_score)


    
def calc_score(matrix, row, col):
    
    value = matrix[row][col]
    current_row = matrix[row]
    if row == 0 or row == len(matrix) -1 or col == 0 or col==len(matrix) -1:
        return 0
    current_col = []
    for i in range(len(matrix)):
        current_col.append(matrix[i][col])
    left_row, right_row = current_row[:col], current_row[col+1:]
    top_col, bot_col = current_col[:row], current_col[row+1:]
    view_left, view_right, view_top, view_bot = 0,0,0,0
    for i in reversed(left_row):
        if i < value:
            view_left += 1
        elif i == value:
            view_left += 1
            break
        else:
            break
    for v in right_row:
        if v < value:
            view_right += 1
        elif v == value:
            view_right += 1
            break
        else:
            break
    for v in reversed(top_col):
        if v < value:
            view_top += 1
        elif v == value:
            view_top += 1
            break
        else:
            break
    for v in bot_col:
        if v < value:
            view_bot += 1
        elif v == value:
            view_bot += 1
            break
        else:
            break
    return view_bot * view_top * view_left * view_right

main()