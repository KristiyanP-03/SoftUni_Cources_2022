list_of_numbers = list(map(int, input().split(" ")))
while True:
    command = input()
    if command == "end":
        break
    elif "swap" in command:
        com, index1, index2 = command.split(" ")
        index1 = int(index1)
        index2 = int(index2)
        list_of_numbers[index1], list_of_numbers[index2] = list_of_numbers[index2], list_of_numbers[index1]

    elif "multiply" in command:
        com, index1, index2 = command.split(" ")
        index1 = int(index1)
        index2 = int(index2)

        multiplayed_sum = list_of_numbers[index1] * list_of_numbers[index2]
        list_of_numbers[index1] = multiplayed_sum
    elif "decrease" in command:
        list_of_numbers = [element - 1 for element in list_of_numbers]

print(", ".join([str(number) for number in list_of_numbers]))
