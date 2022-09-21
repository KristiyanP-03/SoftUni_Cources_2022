# num = int(input())
# for i in range(1, num + 1, 3):
#     print(i)

# n = int(input())
# num = 1
# for i in range(0, n + 1, 2):
#     print(num)
#     num = num * 2 * 2

# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# text = input()
# lenght = len(text)
# for i in range(0, lenght, 1):
#     print(text[i])

# zad 1
# for i in range(1, 101):
#     print(i)

# zad 2
# n = int(input())
# for i in range(1, n + 1, 3):
#     print(i)

# zad 3
# n = int(input())
# stepen = 1
# for i in range(1, n + 2, 2):
#     print(stepen)
#     stepen = stepen * 2 * 2

# zad 4
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)

# zad 5
# text = input()
# for i in range(0, len(text)):
#     print(text[i])

# zad 6
# text = input()
# n = 0
# for i in range(0, len(text)):
#     if text[i] == 'a':
#         n += 1
#     elif text[i] == 'e':
#         n += 2
#     elif text[i] == 'i':
#         n += 3
#     elif text[i] == 'o':
#         n += 4
#     elif text[i] == 'u':
#         n += 5
# print(n)

# zad 7
# count_of_numbers = int(input())
# sum_numbers = 0
# for i in range(0, count_of_numbers):
#     number = int(input())
#     sum_numbers += number
# print(sum_numbers)

# zad 8
# import sys
# count_of_numbers = int(input())
# smallest = sys.maxsize
# biggest = -sys.maxsize
# for i in range(count_of_numbers):
#     number = int(input())
#     if number < smallest:
#         smallest = number
#     if number > biggest:
#         biggest = number
# print(f"Max number: {biggest}")
# print(f"Min number: {smallest}")

# zad 9
# sum_count = int(input())
# left_sum = 0
# right_sum = 0
# for i in range(0, sum_count):
#     left_sum += int(input())
# for i in range(0, sum_count):
#     right_sum += int(input())
# if left_sum == right_sum:
#     print(f"Yes, sum = {left_sum}")
# else:
#     diff = abs(right_sum - left_sum)
#     print(f"No, diff = {diff} ")

# zad 10
# count_of_numbers = int(input())
# even = 0
# odd = 0
# for i in range(count_of_numbers):
#     number = int(input())
#     if i % 2 == 0:
#         even += number
#     else:
#         odd += number
# if even == odd:
#     print("Yes")
#     print(f"Sum = {even}")
# else:
#     print("No")
#     sum = abs(even - odd)
#     print(f"Diff = {sum}")
