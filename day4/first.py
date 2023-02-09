

def read_input():
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        input = line.strip().split(",")
        left, right = input[0], input[1]
        left_input = left.split("-")
        right_input = right.split("-")
        left_start, left_end = int(left_input[0]), int(left_input[1])
        right_start, right_end = int(right_input[0]), int(right_input[1])
        if left_start <= right_start and left_end >= right_end or right_start <= left_start and right_end >= left_end:
            count += 1
    
    print("Tot", count)


def main():
    read_input()


if __name__ == "__main__":
    main()