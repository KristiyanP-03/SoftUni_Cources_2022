plant_discovery = {}
rating = 0
rated = 0

n = int(input())
for i in range(n):
    plant_info = input()
    plant, rarity = plant_info.split("<->")
    if plant in plant_discovery.keys():
        plant_discovery[plant] += [int(rarity), rating, rated]
    else:
        plant_discovery[plant] = [int(rarity), rating, rated]

while True:
    command = input()
    if command == "Exhibition":
        break
    elif "Rate:" in command:
        the_command, info = command.split(": ")
        current_plant, curent_plant_rating = info.split(" - ")
        curent_plant_rating = int(curent_plant_rating)
        if current_plant in plant_discovery.keys():
            plant_discovery[current_plant][1] += curent_plant_rating
            plant_discovery[current_plant][2] += 1
        else:
            print("error")
    elif "Update:" in command:
        the_command, info = command.split(": ")
        current_plant, curent_plant_rarity = info.split(" - ")
        curent_plant_rarity = int(curent_plant_rarity)
        if current_plant in plant_discovery.keys():
            plant_discovery[current_plant][0] = curent_plant_rarity
        else:
            print("error")
    elif "Reset:" in command:
        the_command, current_plant = command.split(": ")
        if current_plant in plant_discovery.keys():
            plant_discovery[current_plant][1] = 0
        else:
            print("error")

print("Plants for the exhibition:")
for (key, value) in plant_discovery.items():
    print(f"- {key}; Rarity: {value[0]}; Rating: {(value[1]/value[2]):.2f}")

