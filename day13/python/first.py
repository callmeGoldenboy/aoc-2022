from pprint import pprint

def read_input(filepath):
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
        filtered = []
        for line in lines:
            if len(line) != 0:
                filtered.append(eval(line))
    return filtered

def main():
    path = "../input.txt"
    path = "../example.txt"
    lines = read_input(path)
    for i in range(0,len(lines), 2):
        left = lines[i]
        right = lines[i+1]

main()