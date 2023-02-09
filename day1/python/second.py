
def read_line():
    with open("../input.txt", "r") as f:
        lines = f.readlines()
        current_max = 0
        current_index = 0
        current_calories = []
        elfs_calories = [0,0,0]
        for line in lines:
            if line != "\n":
                current_calories.append(int(line.strip()))
            else: 
                current_index +=1
                current_elf_calories = sum(current_calories)
                current_calories = []
                add_if_greater(elfs_calories, current_elf_calories)
        total = sum(elfs_calories)
        print(f"Max calories {total}")

def add_if_greater(elfs_calories, current_elf_calories):
    min_index = elfs_calories.index(min(elfs_calories))
    if current_elf_calories > elfs_calories[min_index]:
        elfs_calories[min_index] = current_elf_calories

def main():
    read_line()

if __name__ == "__main__":
    main()
