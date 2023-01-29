nums_of_wagons = int(input())
train = [0] * nums_of_wagons
command = input()
while command != "End":
    if "add" in command:
        people = int("".join([number for number in command if number.isdigit()]))
        train[-1] += people
    elif "insert" in command:
        wagon = int(command[6:9])
        people = int(command[9::])
        train[wagon] += people
    elif "leave" in command:
        wagon = int(command[5:8])
        people = int(command[8::])
        train[wagon] -= people
    command = input()
print(train)