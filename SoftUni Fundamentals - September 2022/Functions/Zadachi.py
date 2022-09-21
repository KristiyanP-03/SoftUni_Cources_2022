# zad 1
# list_of_nums = []
# def change_nums(string_of_nums):
#     list_of_str = (string_of_nums.split(" "))
#     for e in list_of_str:
#         list_of_nums.append(abs(float(e)))
#     return list_of_nums
# print(change_nums(input()))

# zad 2
# def grade_me(grade):
#     if grade < 3.00:
#         print("Fail")
#     elif 3.00 <= grade < 3.50:
#         print("Poor")
#     elif 3.50 <= grade < 4.50:
#         print("Good")
#     elif 4.50 <= grade < 5.50:
#         print("Very Good")
#     elif 5.50 <= grade:
#         print("Excellent")
# my_grade = float(input())
# grade_me(my_grade)

# zad 3
# def add_function(a, b):
#     return a + b
# def subtract_function(a, b):
#     return a - b
# def multiply_function(a, b):
#     return a * b
# def divide_function(a, b):
#     return int(a / b)
#
# operator = input()
# num1 = int(input())
# num2 = int(input())
#
# if operator == "add":
#     print(add_function(num1, num2))
# elif operator == "subtract":
#     print(subtract_function(num1, num2))
# elif operator == "multiply":
#     print(multiply_function(num1, num2))
# elif operator == "divide":
#     print(divide_function(num1, num2))

# zad 4
# def word_repeater(word, n):
#     for i in range(n):
#         print(word, end="")
#     print()
# word_repeater(input(), int(input()))

# zad 4 s lambda
# word_repeater = lambda word, n: word * n
# print(word_repeater(input(), int(input())))

# zad 5
# def cash_register(product, count):
#     if product == "coffee":
#         price = count * 1.50
#         print(f"{price:.2f}")
#     elif product == "water":
#         price = count * 1.00
#         print(f"{price:.2f}")
#     elif product == "coke":
#         price = count * 1.40
#         print(f"{price:.2f}")
#     elif product == "snacks":
#         price = count * 2.00
#         print(f"{price:.2f}")
# cash_register(input(), int(input()))

# zad 6
# def rectangle_calculator(width, heigh):
#     return width * heigh
# print(rectangle_calculator(width = int(input()), heigh = int(input())))

# zad 7
# def rounding_function(list_of_int):
#     final_list = []
#     for e in list_of_int:
#         current_e = round(float(e))
#         final_list.append(current_e)
#     print(final_list)
# rounding_function(input().split(" "))


