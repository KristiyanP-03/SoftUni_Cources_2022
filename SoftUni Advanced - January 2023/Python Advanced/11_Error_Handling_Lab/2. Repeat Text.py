txt = input()

try:
    multiplier = int(input())

    print(txt * multiplier)

except ValueError:
    print("Variable times must be an integer")
