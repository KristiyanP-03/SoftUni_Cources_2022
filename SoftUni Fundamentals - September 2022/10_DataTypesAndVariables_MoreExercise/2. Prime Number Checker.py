number = int(input())
factors = []
if number <= 1:
    print("False")
else:
    for factor in range(2, number):
        if number % factor == 0:
            factors.append(factor)
    if len(factors) == 0:
        print("True")
    else:
        print("False")