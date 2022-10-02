def smallest_of_three():
    list_of_numbers = []
    for one_of_the_number in range(3):
        number = int(input())
        list_of_numbers.append(number)
    smallest_number_is = min(list_of_numbers)
    return smallest_number_is
print(smallest_of_three())