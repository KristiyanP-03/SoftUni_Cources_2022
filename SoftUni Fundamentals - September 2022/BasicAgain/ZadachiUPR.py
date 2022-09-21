# zad 1
# name = input()
# if name == "Johnny":
#     print(f"Hello, my love!")
# else:
#     print(f"Hello, {name}!")

# zad 2
# age = int(input())
# if age <= 14:
#     print("drink toddy")
# elif 14 < age <= 18:
#     print("drink coke")
# elif 18 < age <= 21:
#     print("drink beer")
# elif age > 21:
#     print("drink whisky")

# zad 3
# n = int(input())
# for i in range(n):
#     code = int(input())
#     if code == 88:
#         print("Hello")
#     elif code == 86:
#         print("How are you?")
#     elif code < 88 and code != 86:
#         print("GREAT!")
#     elif code > 88:
#         print("Bye.")

# zad 4
# divisor = int(input())
# boundary = int(input())
# for i in range(boundary, -1, -1):
#     if i % divisor == 0:
#         print(i)
#         break

# zad 5
# orders = int(input())
# price = 0
# total_money = 0
# for i in range(orders):
#     price_per_capsule = float(input())
#     days = int(input())
#     capsules = int(input())
#     if (price_per_capsule < 0.01 or price_per_capsule > 100.00) or (days < 1 or days > 31) or \
#         (capsules < 1 or capsules > 2000):
#         continue
#     price = (price_per_capsule * capsules) * days
#     print(f"The price for the coffee is: ${price:.2f}")
#     total_money += price
# print(f"Total: ${total_money:.2f}")

# # zad 6
# inputs = int(input())
# for each_input in range(inputs):
#     word = input()
#     if "," in word or "." in word or "_" in word:
#         print(f"{word} is not pure!")
#     else:
#         print(f"{word} is pure.")

# zad 7
# while True:
#     word = input()
#     if word == "End":
#         break
#     if word == "SoftUni":
#         continue
#     new_word = ""
#     for i in range(len(word)):
#         new_word += 2 * word[i]
#     print(new_word)

# zad 8
# coffe_counter = 0
# while True:
#     event = input()
#     if event == "END":
#         break
#     elif event == "coding" or event == "dog" or event == "cat" or event == "movie":
#         coffe_counter += 1
#     elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
#         coffe_counter += 2
# if coffe_counter > 5:
#     print("You need extra sleep")
# else:
#     print(coffe_counter)

# zad 9
while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
