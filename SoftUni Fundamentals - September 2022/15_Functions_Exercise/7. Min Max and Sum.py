list_of_str_numbers = input().split()
def min_max_and_sum(list_of_str_nums):
    list_of_int_nubers = []
    sum_of_numbers = 0
    for num in list_of_str_nums:
        number = int(num)
        list_of_int_nubers.append(number)
        sum_of_numbers += number
    max_number = max(list_of_int_nubers)
    min_number = min(list_of_int_nubers)
    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_of_numbers}")
min_max_and_sum(list_of_str_numbers)