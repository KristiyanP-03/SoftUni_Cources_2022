def age_assignment(*args, **kwargs):

    people_ages = []

    for letter, ages in kwargs.items():

        for name in args:
            if name[0] == letter:
                people_ages.append(f"{name} is {ages} years old.")

    return '\n'.join(sorted(people_ages))