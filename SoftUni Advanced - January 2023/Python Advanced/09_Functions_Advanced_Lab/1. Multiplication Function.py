def multiply(*args):
    sum = 1
    args = list(args)
    for number in args:
        sum *= number
    return sum

print(multiply(1, 4, 5))