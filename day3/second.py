

def read_input():
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    unique_items = []
    for i  in range(0, len(lines), 3):
        first = lines[i].strip()
        second = lines[i+1].strip()
        third = lines[i+2].strip()
        common_item  = set(first).intersection(second).intersection(third)
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