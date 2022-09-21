# zad 1
# num = float(input())
# if num > 0:
#     if num < 1:
#         print("small positive")
#     elif 1 < num <= 100000:
#         print("positive")
#     else:
#         print("large positive")
# elif num == 0:
#     print("zero")
# elif num < 0:
#     num = abs(num)
#     if num < 1:
#         print("small negative")
#     elif 1 < num <= 100000:
#         print("negative")
#     else:
#         print("large negative")

# zad 2
# import sys
# biggest = -sys.maxsize
# n_1 = int(input())
# n_2 = int(input())
# n_3 = int(input())
# if n_1 > biggest:
#     biggest = n_1
# if n_2 > biggest:
#     biggest = n_2
# if n_3 > biggest:
#     biggest = n_3
# print(biggest)

# zad 3
# word = input()
# reversed_word = ""
# lenght = len(word)
# for i in range(lenght - 1, -1, -1):
#     reversed_word += word[i]
# print(reversed_word)

# zad 4
# inputs = int(input())
# for i in range(inputs):
#     num = int(input())
#     if num % 2 == 1:
#         print(f"{num} is odd!")
#         break
# else:
#     print("All numbers are even.")

# zad 5
# while True:
#     num = float(input())
#     if 1 <= num <= 100:
#         print(f"The number {num} is between 1 and 100")
#         break

# zad 6
# budget = int(input())
# bill = 0
# while True:
#     buy = input()
#     if buy == "End":
#         print("You bought everything needed.")
#         break
#     else:
#         buy = float(buy)
#     bill += buy
#     if bill > budget:
#         print("You went in overdraft!")
#         break

# zad 7
# num = int(input())
# for r in range(1, num + 1, 1):
#     for c in range(0, r):
#         print("*", end="")
#     print()
# for i in range(num - 1, -1, -1):
#     for j in range(i - 1, -1, -1):
#         print("*", end="")
#     print()