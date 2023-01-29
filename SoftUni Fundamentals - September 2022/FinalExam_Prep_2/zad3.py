n = int(input())
garage = {}
sell = False

for i in range(n):
    car, mileage, fuel = input().split("|")
    garage[car] = [int(mileage), int(fuel)]

while True:
    command = input()
    if command == "Stop":
        for current_car in garage.keys():
            print(f"{current_car} -> Mileage: {garage[current_car][0]} kms, Fuel in the tank: {garage[current_car][1]} lt.")
        break
    elif "Drive" in command:
        part_of_command, car, distance, fuel = command.split(" : ")

        distance = int(distance)
        fuel = int(fuel)

        if car in garage.keys():

            if garage[car][1] < fuel:
                print("Not enough fuel to make that ride")
            else:
                garage[car][1] -= fuel
                if garage[car][0] < 100000 and garage[car][0] + distance > 100000:
                    sell = True
                garage[car][0] += distance
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                if sell:
                    print(f"Time to sell the {car}!")
                    garage.pop(car)

    elif "Refuel" in command:
        part_of_command, car, fuel = command.split(" : ")
        fuel = int(fuel)

        if car in garage.keys():
            garage[car][1] += fuel
            if garage[car][1] > 75:
                unused_fuel = garage[car][1] - 75
                fuel -= unused_fuel
                garage[car][1] = 75
            print(f"{car} refueled with {fuel} liters")

    elif "Revert" in command:
        part_of_command, car, kilometers = command.split(" : ")
        kilometers = int(kilometers)

        if car in garage.keys():
            garage[car][0] -= kilometers
            if garage[car][0] < 10000:
                garage[car][0] = 10000
            else:
                print(f"{car} mileage decreased by {kilometers} kilometers")


