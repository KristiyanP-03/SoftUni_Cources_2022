def forecast(*args):
    list_with_sunny_places = []
    list_with_cloudy_places = []
    list_with_rainy_places = []

    for tupl in args:
        if tupl[1] == "Sunny":
            list_with_sunny_places.append(tupl[0])

        elif tupl[1] == "Cloudy":
            list_with_cloudy_places.append(tupl[0])

        elif tupl[1] == "Rainy":
            list_with_rainy_places.append(tupl[0])


    list_with_rainy_places.sort()
    list_with_cloudy_places.sort()
    list_with_sunny_places.sort()


    output = ""
    if len(list_with_sunny_places):
        for location in list_with_sunny_places:
            output += f"{location} - Sunny\n"



    if len(list_with_cloudy_places):
        for location in list_with_cloudy_places:
            output += f"{location} - Cloudy\n"



    if len(list_with_rainy_places):
        for location in list_with_rainy_places:
            output += f"{location} - Rainy\n"


    return output

# Tests
print(forecast(("Sofia", "Sunny"),("London", "Cloudy"),("New York", "Sunny")))

print(forecast(("Beijing", "Sunny"),("Hong Kong", "Rainy"),("Tokyo", "Sunny"),
               ("Sofia", "Cloudy"),("Peru", "Sunny"),("Florence", "Cloudy"),("Bourgas", "Sunny")))

