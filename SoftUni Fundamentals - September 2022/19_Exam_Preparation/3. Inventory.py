inventory = input().split(", ")
while True:
    command = input()
    if command == "Craft!":
        break
    elif "Collect" in command:
        collect_list = command.split(" - ")
        collectable = collect_list[1]
        if collectable not in inventory:
            inventory.append(collectable)
    elif "Drop" in command:
        drop_list = command.split(" - ")
        droppable = drop_list[1]
        if droppable in inventory:
            inventory.remove(droppable)
    elif "Combine Items" in command:
        combo_list = command.split(" - ")
        old_item, new_item = combo_list[1].split(":")
        if old_item in inventory:
            put_here = inventory.index(old_item)
            inventory.insert(put_here + 1, new_item)
    elif "Renew" in command:
        renew_list = command.split(" - ")
        thing = renew_list[1]
        if thing in inventory:
            inventory.remove(thing)
            inventory.append(thing)
print(", ".join(inventory))



