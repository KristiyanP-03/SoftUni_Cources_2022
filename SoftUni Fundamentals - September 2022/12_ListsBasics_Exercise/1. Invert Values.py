stringed_numbers = input()
inted_numbers_in_list = []
stringed_numbers_in_list = stringed_numbers.split(" ")
for each_stringed_number in stringed_numbers_in_list:
    number = int(each_stringed_number) * -1
    inted_numbers_in_list.append(number)
print(inted_numbers_in_list)