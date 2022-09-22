farm = input()
list_of_animals = farm.split(", ")
list_of_animals.reverse()
for animal in list_of_animals:
    if list_of_animals.index(animal) == 0 and animal == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if animal == "wolf":
        print(f"Oi! Sheep number {list_of_animals.index(animal)}! You are about to be eaten by a wolf!")
