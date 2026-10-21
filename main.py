inventory = {}
RESOURCES = ["iron_ore", "copper_ore", "stone", "coal"]
RECIPES = {
    "iron_plate": {"iron_ore": 2},
    "copper_plate": {"copper_ore": 2},
    "circuit": {"iron_plate": 2, "copper_plate": 2},
}
resource_display = ", ".join(RESOURCES)
while True:
    p_input = input("> ")
    parts = p_input.split()
    target = None
    if len(parts) == 0:
        continue
    elif len(parts) == 1:
        action = parts[0]
    else:
        action = parts[0]
        target = parts[1]

    #mine
    if action == "mine":
        if target is None:
            print("What do you want to mine?")
        elif target in RESOURCES:
            print(f"{target} mined")
            inventory[target] = inventory.get(target, 0) + 1
        else:
            print(f"Try mining these instead: {resource_display}")
        #inventory
    elif action == "inventory":
        if not inventory:
            print("Inventory is empty")
        else:
            for item, count in inventory.items():
                print(f"{item}: {count}")
        #crafting
    elif action == "craft":
        if target is None:
            print("What do you want to craft?")
        elif target in RECIPES:
            recipe = RECIPES[target]
            can_craft = True
            for ingredient, amount in recipe.items():
                have = inventory.get(ingredient, 0)
                if have < amount:
                    print(f"You don't have enough {ingredient}")
                    can_craft = False
                    break
            if can_craft is True:
                for ingredient, amount in recipe.items():
                    inventory[ingredient] = inventory[ingredient] - amount
                inventory[target] = inventory.get(target, 0) + 1
                print(f"{target} crafted")   
        else:
            print("Unknown recipe") 
    elif action == "quit":
        break
    else:
        print("Invalid command")
