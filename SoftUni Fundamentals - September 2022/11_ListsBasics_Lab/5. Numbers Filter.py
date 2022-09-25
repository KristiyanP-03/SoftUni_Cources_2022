lines_of_numbers = int(input())
list_of_numbers = []
filtered_by_command_list = []
for line in range(lines_of_numbers):
    number = int(input())
    list_of_numbers.append(number)
command = input()
for each_number in list_of_numbers:
    if command == "even" and each_number % 2 == 0:
        filtered_by_command_list.append(each_number)
    elif command == "odd" and each_number % 2 != 0:
        filtered_by_command_list.append(each_number)
    elif command == "negative" and each_number < 0:
        filtered_by_command_list.append(each_number)
    elif command == "positive" and each_number >= 0:
        filtered_by_command_list.append(each_number)
print(filtered_by_command_list)