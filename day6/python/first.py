from collections import deque

def run():
    with open("../input.txt", "r") as f:
        stream = f.read()

    current_chars = []
    first_chars = 0
    counter = 0
    for char in stream: 
        if first_chars <4:
            current_chars.append(char)
            first_chars += 1
        elif check_unique(current_chars):
            print(f"Sequence appears at char count {counter}")
            break
        else:
            current_chars.pop(0)
            current_chars.append(char)
        counter +=1

def check_unique(current_chars):
    return len(set(current_chars)) == 4

run()