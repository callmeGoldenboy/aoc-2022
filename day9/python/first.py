from pprint import pprint
def read_input():
    with open("../input.txt","r") as f:
        return f.read().splitlines()




def check_distance():
    pass

test_input = [
    "R 2",
    "L 2",
    "U 2",
    "D 1",
    "L 2"
]

def main():
    lines = read_input()
    matrix = [[ "*" for _ in range(5)] for _ in range(5)]
    start_row, start_col = int(len(matrix)/2), int(len(matrix[0])/2)
    head_row, head_col = start_row, start_col
    tail_row, tail_col = start_row, start_col

    matrix[start_row][start_col] = "#"
    for value in test_input:
        input = value.split(" ")
        direction, length = input[0], int(input[1])
        print(f"{direction=},{length=}")
        for step in range(length):
            prev_head_row, prev_head_col = head_row, head_col
            if direction == "R":
                head_col += 1
                if abs(head_col - tail_col) > 1:
                    print("increase tail to the right")
                    tail_col += 1
            elif direction == "L":
                head_col -= 1
                if abs(head_col - tail_col) > 1:
                    tail_col -= 1
            elif direction == "D":
                head_row += 1
                if abs(head_row - tail_row) > 1:
                    tail_row += 1
            elif direction == "U":
                head_row -= 1
                if abs(head_row - tail_row) > 1:
                    tail_row -= 1
            matrix[prev_head_row][prev_head_col] = "*" 
            matrix[head_row][head_col] = "H"
            matrix[tail_row][tail_col] = "#"
            pprint(matrix)

main()