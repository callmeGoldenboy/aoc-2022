current_dir = "/root"

dir_sizes = {}
with open("../input.txt", "r") as f:
    lines = f.read().splitlines()

counter = 0
while counter < len(lines):
    try:
        line = lines[counter]
        if line.startswith("$"):
            is_command = True
            formatted_line = line.strip().replace("$","").strip().split(" ")
            if formatted_line[0] == "cd":
                arg = formatted_line[1]
                if arg == "..":
                    current_dir = current_dir[:current_dir.rfind("/")]
                elif arg == "/":
                    current_dir = "/root"
                else:
                    current_dir = current_dir + "/" + arg
            elif formatted_line[0] == "ls":
                while True:
                    new_line = lines[counter + 1]
                    if new_line.startswith("$"):
                        break
                    else:
                        output = new_line.split(" ")
                        if output[0] == "dir":
                            path = current_dir + "/" + output[1]
                            dir_sizes[path] = 0
                        else:
                            size = int(output[0])
                            dir_sizes[current_dir] = dir_sizes.get(current_dir, 0) + size
                        counter +=1
        counter += 1
    except Exception:
        break

# update parent directories sizes 
for dir, size in dir_sizes.items():
    dirs = dir.split("/")
    for i in range(len(dirs)-1,1, -1):
        new_dir = dirs[1:i]
        if len(new_dir) == 1:
            path = "/" + new_dir[0]
        else:
            path = "/".join(new_dir)
            path = "/" + path
        dir_sizes[path] += size



# Filter the directories with total size at most 100000 and calculate
# the sum of their sizes
small_dirs = {k: v for k, v in dir_sizes.items() if v <= 100000}
result = sum(small_dirs.values())
print(result)