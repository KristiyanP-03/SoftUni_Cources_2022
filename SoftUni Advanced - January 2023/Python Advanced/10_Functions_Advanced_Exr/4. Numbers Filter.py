def even_odd_filter(**kwargs):

    for key, values in kwargs.items():

        if key == "even":
            kwargs[key] = [num for num in values if num % 2 == 0]

        elif key == "odd":
            kwargs[key] = [num for num in values if num % 2 != 0]

    sorted_kwargs = dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))

    return sorted_kwargs


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))
