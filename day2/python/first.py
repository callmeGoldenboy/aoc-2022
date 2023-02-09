

point_mapping = {
    "rock": 1,
    "paper": 2,
    "scissors" : 3
}

play_mapping = {
    "X": "rock",
    "A": "rock",
    "Y": "paper",
    "B": "paper",
    "Z": "scissors",
    "C": "scissors"
}

def read_file():
    with open("../input.txt", "r") as f:
        count = 0
        for line in f.readlines():
            current_line = line.strip().split(" ")
            opponent, me = play_mapping[current_line[0]], play_mapping[current_line[1]]
            round_result = get_round_result(opponent, me)
            count += round_result + point_mapping[me]
    
    print(f"Total points {count}")

def get_round_result(opponent,me):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    if opponent == me:
        return 3
    elif me == rock and opponent == scissors:
        return 6
    elif me == rock and opponent == paper:
        return 0 
    elif me == paper and opponent == rock:
        return 6
    elif me == paper and opponent == scissors:
        return 0
    elif me == scissors and opponent == paper:
        return 6
    elif me == scissors and opponent == rock:
        return 0


def main():
    read_file()

if __name__ == "__main__":
    main()