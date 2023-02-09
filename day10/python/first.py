from pprint import pprint

def read_input():
    with open("../input.txt", "r") as f:
        lines = f.read().splitlines()
        return lines

register_values = {
    20: 0,
    60:0,
    100: 0,
    140: 0,
    180: 0,
    220: 0
}
def main():
    instructions = read_input()
    cycle = 1
    current_register_value = 1
    for current_instruction in instructions:
        # finish once we reach cycle 220
        if current_instruction == "noop":
            cycle += 1
            set_cycle_values(register_values, cycle, current_register_value)
        elif current_instruction.startswith("addx"):
            value = int(current_instruction.split(" ")[1])
            cycle += 1
            set_cycle_values(register_values, cycle, current_register_value)
            current_register_value += value
            cycle += 1
            set_cycle_values(register_values, cycle, current_register_value)
    print(sum_values(register_values))

def set_cycle_values(register_values, current_cycle, current_register_value):
    register_values [current_cycle] = current_register_value


def sum_values(register_values):
    wanted_cycles = [20, 60, 100, 140, 180, 220]
    values = [value*key for key,value in register_values.items() if key in wanted_cycles ]
    return sum(values)

main()