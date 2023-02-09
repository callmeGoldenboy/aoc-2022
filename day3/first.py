

def read_input():
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    unique_items = []
    for line in lines:
        filtered_line = line.strip()
        middle_index = int(len(filtered_line) / 2)
        left_part, right_part = filtered_line[0:middle_index], filtered_line[middle_index:]
        common_item  = set(left_part).intersection(right_part)
        unique_items.append(common_item)
    
    indexes = ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    tot = 0
    for item in unique_items:
        element:str = item.pop()
        try:
            value = indexes.index(element)
        except ValueError:
            value = indexes.index(element.lower()) + 26
        
        tot += value
    print("Total is", tot)

def main():
    read_input()

if __name__  == "__main__":
    main()