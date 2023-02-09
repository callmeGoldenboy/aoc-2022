
def read_line():
    with open("../input.txt", "r") as f:
        lines = f.readlines()
        current_max = 0
        current_index = 0
        current_calories = []
        for line in lines:
            if line != "\n":
                current_calories.append(int(line.strip()))
            else: 
                current_index +=1
                current_elf_calories = sum(current_calories)
                current_calories = []
                if current_elf_calories > current_max:
                    current_max = current_elf_calories

        print(f"Max calories {current_max}")

def main():
    read_line()

if __name__ == "__main__":
    main()
