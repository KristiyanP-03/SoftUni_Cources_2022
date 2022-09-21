# zad 1
# number1 = int(input())
# number2 = int(input())
# number3 = int(input())
# number4 = int(input())
# sum_of_nums = int((number2 + number1) / number3) * number4
# print(sum_of_nums)

# zad 2
# char1 = input()
# char2 = input()
# char3 = input()
# output = ""
# output += char1
# output += char2
# output += char3
# print(output)

# zad 3
# dudes = int(input())
# capcility = int(input())
# courses = dudes // capcility
# left_dudes = dudes % capcility
# if left_dudes != 0:
#     courses += 1
# print(courses)

# zad 4
# n = int(input())
# total_sum = 0
# for i in range(n):
#     char = input()
#     total_sum += ord(char)
# print("The sum equals: " + str(total_sum))

# zad 5
# start = int(input())
# end = int(input())
# for i in range(start, end + 1):
#     print(chr(i), end=" ")

# zad 6
# characters = int(input())
# for i in range(characters):
#     for j in range(characters):
#         for g in range(characters):
#             print(chr(i + 97), end="")
#             print(chr(j + 97), end="")
#             print(chr(g + 97))

# zad 7
# tank = 255
# total_took = 0
# pour = int(input())
# for i in range(pour):
#     take = int(input())
#     if total_took + take > tank:
#         print("Insufficient capacity!")
#         i += 1
#         continue
#     total_took += take
# print(total_took)
