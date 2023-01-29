longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = [str_of_numbers.split(",") for str_of_numbers in input().split("-")]

    first_range = set(range(int(first_range[0]), int(first_range[1]) + 1))
    second_range = set(range(int(second_range[0]), int(second_range[1]) + 1))

    current_intersection = first_range.intersection(second_range)

    if len(longest_intersection) < len(current_intersection):
        longest_intersection = current_intersection


print(f"Longest intersection is "
      f"[{', '.join(str(number) for number in longest_intersection)}] "
      f"with length {len(longest_intersection)}")