#zad 1
# numbers = input()
# list_of_nums = ''.join(sorted(numbers))
# print(list_of_nums[::-1])

#zad 2
# string = input()
# list_of_uppercases = []
# for i, v in enumerate(string):
#     if v.isupper():
#         list_of_uppercases.append(i)
#     elif v.islower():
#         continue
# print(list_of_uppercases)

#zad 3
# farm = input()
# list_of_animals = farm.split(", ")
# list_of_animals.reverse()
# for animal in list_of_animals:
#     if list_of_animals.index(animal) == 0 and animal == "wolf":
#         print("Please go away and stop eating my sheep")
#         break
#     if animal == "wolf":
#         print(f"Oi! Sheep number {list_of_animals.index(animal)}! You are about to be eaten by a wolf!")

#zad 4
# string = input().lower()
# sand_item_count = string.count("sand")
# water_item_count = string.count("water")
# fish_item_count = string.count("fish")
# sun_item_count = string.count("sun")
# total_items = sand_item_count + water_item_count + fish_item_count + sun_item_count
# print(total_items)
