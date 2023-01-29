string = input()
tuple_of_characters = tuple([character for index, character in enumerate(string)])

elements_collector = {}
for element in tuple_of_characters:
    elements_collector[element] = tuple_of_characters.count(element)

elements_collector = dict(sorted(elements_collector.items()))

for char, count in elements_collector.items():
    print(f"{char}: {count} time/s")