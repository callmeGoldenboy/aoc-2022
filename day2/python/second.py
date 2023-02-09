

point_mapping = {
    "rock": 1,
    "paper": 2,
    "scissors" : 3
}

play_mapping = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

def read_file():
    with open("../input.txt", "r") as f:
        count = 0
        for line in f.readlines():
            current_line = line.strip().split(" ")
            opponent, me = play_mapping[current_line[0]], current_line[1]
            round_result, my_play = get_round_result(opponent, me)
            count += round_result + point_mapping[my_play]
    
    print(f"Total points {count}")

def get_round_result(opponent,me):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    if me == "X" and opponent == rock:
        return 0, scissors
    elif me == "X" and opponent == paper:
        return 0, rock
    elif me == "X" and opponent == scissors:
        return 0, paper
    elif me == "Y":
        return 3, opponent
    elif me == "Z" and opponent == rock:
        return 6, paper 
    elif me == "Z" and opponent == paper:
        return 6, scissors
    elif me == "Z" and opponent == scissors:
        return 6, rock


def main():
    read_file()

if __name__ == "__main__":
    main()