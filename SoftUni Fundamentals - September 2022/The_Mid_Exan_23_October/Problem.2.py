route = input().split("||")
fuel = int(input())
ammo = int(input())

no_fuel = False

for command in route:

    if len(command.split(" ")) == 2:
        #valid command
        current_command, value = command.split(" ")
        value = int(value)
    elif len(command.split(" ")) == 1:
        # command is Titan so program ends
        print("You have reached Titan, all passengers are safe.")
        break

    if current_command == "Travel":
        if fuel >= value:
            fuel -= value
            print(f"The spaceship travelled {value} light-years.")
        else:
            no_fuel = True
            print("Mission failed.")
        if no_fuel:
            break
    elif current_command == "Enemy":
        if ammo >= value:
            ammo -= value
            print(f"An enemy with {value} armour is defeated.")
        elif ammo <= value:
            damaged_enemy_chaser = value - ammo
            fuel -= 2 * damaged_enemy_chaser
            if fuel < 0:
                no_fuel = True
                print("Mission failed.")
            elif fuel > 0:
                ammo = 0
                print(f"An enemy with {damaged_enemy_chaser} armour is outmaneuvered.")
        if no_fuel:
            break
    elif current_command == "Repair":
        ammo_amout = 2 * value
        ammo += ammo_amout
        print(f"Ammunitions added: {ammo_amout}.")
        fuel += value
        print(f"Fuel added: {value}.")