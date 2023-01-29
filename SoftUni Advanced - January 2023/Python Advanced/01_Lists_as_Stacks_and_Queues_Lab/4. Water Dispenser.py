from _collections import deque

water_in_the_dispenser = int(input())
queue = deque([])
while True:
    name = input()
    if name == "Start":
        break
    else:
        queue.append(name)
while True:
    command = input()
    if command == "End":
        break
    elif command.isdigit():
        if int(command) <= water_in_the_dispenser:
            water_in_the_dispenser -= int(command)
            print(f"{queue[0]} got water")
            queue.popleft()
        else:
            print(f"{queue[0]} must wait")
            queue.popleft()
    elif "refill" in command:
        add_l = command.split(" ")[1]
        water_in_the_dispenser += int(add_l)
print(f"{water_in_the_dispenser} liters left")
