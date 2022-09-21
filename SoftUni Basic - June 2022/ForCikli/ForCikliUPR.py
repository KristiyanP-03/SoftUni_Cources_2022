# zad 1
# for i in range(1, 1001):
#     if i % 10 == 7:
#         print(i)

# zad 2
# import sys
# sum_numbers = 0
# max_num = -sys.maxsize
# n = int(input())
# for i in range(0, n):
#     num = int(input())
#     if num > max_num:
#         max_num = num
#     sum_numbers += num
# sum_numbers -= max_num
# if max_num == sum_numbers:
#     print("Yes")
#     print(f"Sum = {sum_numbers}")
# else:
#     print("No")
#     print(f"Diff = {abs(max_num - sum_numbers)}")

# zad 3
# count_of_numbers = int(input())
# p1 = 0
# c_n1 = 0
# p2 = 0
# c_n2 = 0
# p3 = 0
# c_n3 = 0
# p4 = 0
# c_n4 = 0
# p5 = 0
# c_n5 = 0
# for i in range(count_of_numbers):
#     number = int(input())
#     if number < 200:
#         c_n1 += 1
#     elif 200 <= number <= 399:
#         c_n2 += 1
#     elif 400 <= number <= 599:
#         c_n3 += 1
#     elif 600 <= number <= 799:
#         c_n4 += 1
#     elif number >= 800:
#         c_n5 += 1
# p1 = c_n1 / count_of_numbers * 100
# print(f"{p1:.2f}%")
# p2 = c_n2 / count_of_numbers * 100
# print(f"{p2:.2f}%")
# p3 = c_n3 / count_of_numbers * 100
# print(f"{p3:.2f}%")
# p4 = c_n4 / count_of_numbers * 100
# print(f"{p4:.2f}%")
# p5 = c_n5 / count_of_numbers * 100
# print(f"{p5:.2f}%")

# zad 4
# age = int(input())
# wm_price = float(input())
# toy_price = int(input())
# toy = 0
# money = 0
# for i in range(1, age + 1):
#     if i % 2 != 0:
#         toy += 1
#     else:
#         money_given = i * 5 - 1
#         money += money_given
# money = toy * toy_price + money
# if money >= wm_price:
#     money = money - wm_price
#     print(f"Yes! {money:.2f}")
# else:
#     diff = wm_price - money
#     print(f"No! {diff:.2f}")

# zad 5
# tabs = int(input())
# salary = int(input())
# for i in range(tabs):
#     site = input()
#     if site == "Facebook":
#         salary -= 150
#         if salary == 0:
#             print("You have lost your salary.")
#             break
#     elif site == "Instagram":
#         salary -= 100
#         if salary == 0:
#             print("You have lost your salary.")
#             break
#     elif site == "Reddit":
#         salary -= 50
#         if salary == 0:
#             print("You have lost your salary.")
#             break
# if salary > 0:
#     print(salary)

# zad 6
# name = input()
# points = float(input())
# count_grader = int(input())
#
# for i in range(1, count_grader + 1):
#     grader_name = input()
#     grader_points = float(input())
#     points = points + ((len(grader_name) * grader_points) / 2)
#     if points >= 1250.5:
#         break
#
# if points > 1250.5:
#     print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
# else:
#     diff = 1250.5 - points
#     print(f"Sorry, {name} you need {diff:.1f} more!")

# zad 7
# count_groups = int(input())
# musala_count = 0
# montblanc_count = 0
# kilimanjaro_count = 0
# k2_count = 0
# everest_count = 0
# all_people = 0
# for i in range(1, count_groups + 1):
#     count_people = int(input())
#     all_people = all_people + count_people
#     if count_people <= 5:
#         musala_count = musala_count + count_people
#     elif count_people <= 12:
#         montblanc_count = montblanc_count + count_people
#     elif count_people <= 25:
#         kilimanjaro_count = kilimanjaro_count + count_people
#     elif count_people <= 40:
#         k2_count = k2_count + count_people
#     else:
#         everest_count = everest_count + count_people
# musala_percent = musala_count / all_people * 100
# montblanc_percent = montblanc_count / all_people * 100
# kilimanjaro_percent = kilimanjaro_count / all_people * 100
# k2_percent = k2_count / all_people * 100
# everest_percent = everest_count / all_people * 100
# print(f"{musala_percent:.2f}%")
# print(f"{montblanc_percent:.2f}%")
# print(f"{kilimanjaro_percent:.2f}%")
# print(f"{k2_percent:.2f}%")
# print(f"{everest_percent:.2f}%")

# zad 8
# import math
# tournament_count = int(input())
# init_points = int(input())
# sum_points = 0
# win_count = 0
# for i in range(1, tournament_count + 1):
#     level = input()
#     if level == "W":
#         win_count = win_count + 1
#         sum_points = sum_points + 2000
#     elif level == "F":
#         sum_points = sum_points + 1200
#     elif level == "SF":
#         sum_points = sum_points + 720
# total_points = sum_points + init_points
# print(f"Final points: {total_points}")
# avg_points = math.floor(sum_points / tournament_count)
# print(f"Average points: {avg_points}")
# percent_win = win_count / tournament_count * 100
# print(f"{percent_win:.2f}%")
