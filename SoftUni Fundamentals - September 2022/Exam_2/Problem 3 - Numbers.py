list_of_numbers = list(map(int, input().split(" ")))
list_with_top_five = []
average_value = 0.00
numbers_counter = 0

for number in list_of_numbers:
    average_value += number
    numbers_counter += 1
average_value = average_value / numbers_counter
numbers_counter = 0
list_of_numbers.sort()
list_of_numbers.reverse()
for num in list_of_numbers:
    if num > average_value:
        list_with_top_five.append(num)
        numbers_counter += 1
        if numbers_counter == 5:
            break
if numbers_counter > 0:
    list_with_top_five.sort()
    list_with_top_five.reverse()
    print(" ".join([str(num) for num in list_with_top_five]))
else:
    print("No")
