def fibonacci():
    first_num = 0
    second_num = 1

    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num


generator1 = fibonacci()
for i in range(5):
    print(next(generator1))
generator2 = fibonacci()
for i in range(1):
    print(next(generator2))