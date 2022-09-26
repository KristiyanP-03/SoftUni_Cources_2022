stringed_list_of_numbers = input().split(" ")
count_of_numbers_to_remove = int(input())
inted_list_of_numbers = []
for num in stringed_list_of_numbers:
    number = int(num)
    inted_list_of_numbers.append(number)
for element in range(count_of_numbers_to_remove):
    smallest_number = min(inted_list_of_numbers)
    inted_list_of_numbers.remove(smallest_number)
new_stringed_list_of_numbers = []
for num in inted_list_of_numbers:
    number = str(num)
    new_stringed_list_of_numbers.append(number)
print(", ".join(new_stringed_list_of_numbers))