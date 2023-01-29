treasure_chest_space = input().split("|")
list_to_print = []
sum_the_value = 0
while True:
    command = input()
    if command == "Yohoho!":
        if len(treasure_chest_space) == 0:
            print("Failed treasure hunt.")
        else:
            for item in treasure_chest_space:
                sum_the_value += len(item)
            sum_the_value = sum_the_value / len(treasure_chest_space)
            print(f"Average treasure gain: {sum_the_value:.2f} pirate credits.")
        break
    if "Loot" in command:
        list_with_loot = command.split(" ")
        list_with_loot.remove("Loot")
        for each_loot in list_with_loot:
            if each_loot not in treasure_chest_space:
                treasure_chest_space.insert(0, each_loot)
    elif "Drop" in command:
        list_for_ext_index = command.split(" ")
        index = int(list_for_ext_index[1])
        if index < len(treasure_chest_space):
            moving_the_loot = treasure_chest_space[index]
            treasure_chest_space.pop(index)
            treasure_chest_space.append(moving_the_loot)
    elif "Steal" in command:
        list_with_stolen_loots = command.split(" ")
        if int(list_with_stolen_loots[1]) < len(treasure_chest_space):
            for loot in range(int(list_with_stolen_loots[1])):
                stolen_loot = treasure_chest_space.pop(-1)
                list_to_print.append(stolen_loot)
            list_to_print.reverse()
        else:
            for loot in range(len(treasure_chest_space) - 1):
                stolen_loot = treasure_chest_space.pop(-1)
                list_to_print.append(stolen_loot)
            list_to_print.reverse()
        print(", ".join(list_to_print))
        list_to_print.clear()



