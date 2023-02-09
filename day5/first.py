
from collections import deque
from pprint import pprint

def read_input():
    col1 = deque(["Z","T","F","R","W","J","G"])
    col2 = deque(["G","W","M"])
    col3 = deque(["J","N","H","G"])
    col4 = deque(["J","R","C","N","W"])
    col5 = deque(["W","F","S","B","G","Q","V","M"])
    col6 = deque(["S","R","T","D","V","W","C"])
    col7 = deque(["H","B","N","C","D","Z","G","V"])
    col8 = deque(["S","J","N","M","G","C"])
    col9 = deque(["G","P","N","W","C","J","D","L"])
    matrix = ["", col1, col2, col3, col4, col5,col6, col7, col8, col9]
    with open("./input.txt", "r") as f:
        lines = f.readlines()
        lines = lines[10:] # skip the crates input

    for line in lines:
        line = line.strip()
        input = line.split(" ")
        number, start, end = int(input[1]), int(input[3]), int(input[5])
        for _ in range(number):
            element = matrix[start].pop()
            matrix[end].append(element)
    final_combination = ""
    for i in range(1, len(matrix)):
        final_combination += matrix[i].pop()
    
    print(final_combination)


def main():
    read_input()

if __name__ == "__main__":
    main()