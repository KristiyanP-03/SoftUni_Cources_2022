def even_odd(*args):
    args = list(args)
    command = args[-1]
    args.pop(-1)
    filtered_list = []

    if command == "even":
        for index, number in enumerate(args):
            if (index + 1) % 2 == 0:
                filtered_list.append(number)

    elif command == "odd":
        for index, number in enumerate(args):
            if (index + 1) % 2 == 1:
                filtered_list.append(number)

    return filtered_list

print(even_odd(1, 2, 3, 4, 5, 6, "even"))