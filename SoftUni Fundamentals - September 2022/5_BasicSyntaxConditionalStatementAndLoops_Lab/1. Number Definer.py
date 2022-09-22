num = float(input())
if num > 0:
    if num < 1:
        print("small positive")
    elif 1 < num <= 100000:
        print("positive")
    else:
        print("large positive")
elif num == 0:
    print("zero")
elif num < 0:
    num = abs(num)
    if num < 1:
        print("small negative")
    elif 1 < num <= 100000:
        print("negative")
    else:
        print("large negative")
