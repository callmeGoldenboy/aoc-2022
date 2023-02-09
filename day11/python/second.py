from pprint import pprint

monkeys = {
    0: {"items": [57,58],
        "operation": lambda old_worry : old_worry * 19,
        "test": lambda old_worry: 2 if old_worry % 7 == 0 else 3,
        "item_count": 0
        },
        
    1: {"items": [66,52,59,79,94,73],
        "operation": lambda old_worry : old_worry + 1,
        "test": lambda old_worry: 4 if old_worry % 19 == 0 else 6,
        "item_count": 0
        },

    2: {"items": [80],
         "operation": lambda old_worry : old_worry + 6,
        "test": lambda old_worry: 7 if old_worry % 5 == 0 else 5,
        "item_count": 0
        },

    3: {"items": [82, 81, 68, 66, 71, 83, 75, 97],
        "operation": lambda old_worry : old_worry + 5,
        "test": lambda old_worry: 5 if old_worry % 11 == 0 else 2,
        "item_count": 0
        },

    4: {"items": [55, 52, 67, 70, 69, 94, 90],
        "operation": lambda old_worry : old_worry * old_worry,
        "test": lambda old_worry: 0 if old_worry % 17 == 0 else 3,
        "item_count": 0
        },

    5: {"items": [69, 85, 89, 91],
        "operation": lambda old_worry : old_worry + 7,
        "test": lambda old_worry: 1 if old_worry % 13 == 0 else 7,
        "item_count": 0
        },

    6: {"items": [75, 53, 73, 52, 75],
        "operation": lambda old_worry : old_worry * 7,
        "test": lambda old_worry: 0 if old_worry % 2 ==  0 else 4,
        "item_count": 0
        },

    7: {"items": [94, 60, 79],
        "operation": lambda old_worry : old_worry + 2,
        "test": lambda old_worry: 1 if old_worry % 3 ==  0 else 6,
        "item_count":0
        },
}

def main():
    worry_level = 0
    mod_number = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 
    for round in range(10000):
        for current_monkey in range(8):
            monkey = monkeys[current_monkey]
            items = monkey["items"].copy()
            fn = monkey["operation"]
            next_monkey_fn = monkey["test"]
            for worry_level in items:
                worry_level = fn(worry_level) # during inspection
                worry_level = worry_level % mod_number
                next_monkey = next_monkey_fn(worry_level)
                monkey["item_count"] += 1
                monkey["items"].pop(0)
                monkeys[next_monkey]["items"].append(worry_level)

    sorted_item_counts = sorted([val["item_count"] for _,val in monkeys.items()], reverse=True)
    pprint(sorted_item_counts[0] * sorted_item_counts[1])

main()



        