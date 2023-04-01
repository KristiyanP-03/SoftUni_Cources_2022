#  --- Just Solved / solution 1 --- Решение по условие.
# numbers_dictionary = {}
#
# line = input()
# while line != "Search":
#     number_as_string = line
#     try:
#         number = int(input())
#         numbers_dictionary[number_as_string] = number
#     except ValueError:
#         print("The variable number/value must be an integer")
#     line = input()
#
# # input string to find a equal key in dictionary   |   "Remove" - end searching keys in dictionary
# line = input()
# while line != "Remove":
#     searched = line
#     try:
#         print(numbers_dictionary[searched])
#     except KeyError:
#         print("Number is not found in dictionary")
#     line = input()
#
# line = input()
# while line != "End":
#     searched = line
#     try:
#         del numbers_dictionary[searched]
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# print(numbers_dictionary)

# --- Solved and Modified / solution 2 --- Лектор-колегата Марио Захариев, предложи да се излезе от контекста.
numbers_dictionary = {}

class FirstNumberNotStr(Exception):
    """"Number must be string"""

# input key and value to dictionary -> str(key): int(value)   |   "Search" - stop loop adding
line = input()
while line != "Search":
    # str(key):
    try:
        if line.isdigit():
            raise FirstNumberNotStr
        else:
            number_as_string = line
    except FirstNumberNotStr:
        print("The variable number/key must be a string")
        print("Try new str(key): ")
        line = input()
        continue
    # : int(value)
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number/value must be an integer")
        print("Try new str(key): int(value)   |   \"Search\" to stop adding")
    line = input()


# input string to find a equal str(key) in dictionary   |   "Remove" - end searching keys in dictionary
line = input()
while line != "Remove":
    # input str(key) to search
    try:
        if line.isdigit():
            raise FirstNumberNotStr
        else:
            searched = line
    except FirstNumberNotStr:
        print("The variable number/key must be a string")
        print("Input new number/key   |   \"Remove\" to stop searching")
        line = input()
        continue

    # check for equal key
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number is not found in dictionary")
    line = input()


# imput to remove existing str(key) in dictionary   |   "End" - stop removing items in dictionary
line = input()
while line != "End":
    # input str(key) to remove key: value
    try:
        if line.isdigit():
            raise FirstNumberNotStr
        else:
            to_remove = line
    except FirstNumberNotStr:
        print("The variable number/key must be a string")
        print("Input new number/key   |   \"End\" to stop removing")
        line = input()
        continue

    # check for equal str(key)
    try:
        del numbers_dictionary[to_remove]
    except KeyError:
        print("Number does not exist in dictionary")
        print("Input new number/key   |   \"End\" to stop removing")
    line = input()

print(numbers_dictionary)
