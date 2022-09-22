number = int(input())
if number % 2 == 0 and number != 2 or number % 3 == 0 and number != 3 or number < 1:
    print("False")
else:
    print("True")
