operator = input()
first_number = int(input())
second_number = int(input())
def function_working_with_operators(opr, a, b):
    if opr == "add":
        return a + b
    elif opr == "subtract":
        return a - b
    elif opr == "multiply":
        return a * b
    elif opr == "divide":
        return int(a / b)
print(function_working_with_operators(operator, first_number, second_number))