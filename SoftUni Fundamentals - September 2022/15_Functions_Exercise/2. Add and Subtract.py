first_number = int(input())
second_number = int(input())
third_number = int(input())
def sum_numbers(a, b):
    return a + b
add_function_result = sum_numbers(first_number, second_number)
def subtract(c):
    return add_function_result - c
subtract_function_result = subtract(third_number)
def add_and_subtract():
    print(subtract_function_result)
add_and_subtract()
