inventory = {}

while True:
    p_input = input("> ")
    parts = p_input.split()
    target = None
    if len(parts) == 1:
        action = parts[0]
    else:
        action = parts[0]
        target = parts[1]

    if action == "mine":
        print(f"{target} mined")
        inventory[target] = inventory.get(target, 0) + 1
        print(inventory)
    elif action == "inventory":
        for items, count in inventory.items():
            print(f"{items}: {count}")
    elif action == "quit":
        break
    
