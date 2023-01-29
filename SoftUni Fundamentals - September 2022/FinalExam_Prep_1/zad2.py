import re

data = input()
list_of_places = []
points = 0

pattern = r"(=|\/)[A-Z][A-Za-z]{2,}\1"
verify_places = re.finditer(pattern, data)

for place in verify_places:
    place = re.split('=|\/', place.group())[1]
    points += len(place)
    list_of_places.append(place)

print(f"Destinations: {', '.join(list_of_places)}")
print(f"Travel Points: {points}")





