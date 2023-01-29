float_tuple = tuple(map(float, input().split(" ")))
numbers_and_counts = {}

for number in float_tuple:
    numbers_and_counts[number] = float_tuple.count(number)

for key in numbers_and_counts:
    print(f"{key} - {numbers_and_counts[key]} times")
