
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
    
    counter = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if is_visible(matrix, row, col):
                counter += 1
    
    print(counter)


    
def is_visible(matrix, row, col):
    # check if its an edge tree
    if row == 0 or row == len(matrix) -1 or col == 0 or col==len(matrix) -1:
        return True
    
    value = matrix[row][col]
    current_row = matrix[row]
    # print("row index:", row, "col index:", col, current_row)
    current_col = []
    for i in range(len(matrix)):
        current_col.append(matrix[i][col])
    left_row, right_row = current_row[:col], current_row[col+1:]
    top_col, bot_col = current_col[:row], current_col[row+1:]
    max_left,max_right = max(left_row), max(right_row)
    max_top,max_bot= max(top_col), max(bot_col)
    if value > max_left or value > max_right or value > max_bot or value > max_top:
        return True
    else:
        return False
    





main()