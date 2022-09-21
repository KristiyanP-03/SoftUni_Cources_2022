# zad 1
# cpu_price = float(input())
# cpu_price_bgn = cpu_price * 1.57
# videocard_price = float(input())
# videocard_price_bgn = videocard_price * 1.57
# ram_price = float(input())
# ram_price_bgn1 = ram_price * 1.57
# count_ram = int(input())
# ram_price_bgn1 = ram_price_bgn1 * count_ram
# discount = float(input())
# cpu_price_bgn *= 1 - discount
# videocard_price_bgn *= 1 - discount
# money = cpu_price_bgn + videocard_price_bgn + ram_price_bgn1
# print(f"Money needed - {money:.2f} leva.")

# zad 2
# days = 5
# saved_money = 0
# money = float(input())
# daily_income = float(input())
# bill = float(input())
# gift_price = float(input())
# saved_money += days * money
# saved_money += days * daily_income
# saved_money -= bill
# if saved_money >= gift_price:
#     print(f"Profit: {saved_money:.2f} BGN, the gift has been purchased.")
# elif saved_money < gift_price:
#     needed_money = gift_price - saved_money
#     print(f"Insufficient money: {needed_money:.2f} BGN.")

# zad 3
# kg = float(input())
# type_do = input()
# km = int(input())
# kg_price_per_km = 0
# if type_do == "standard":
#     if kg < 1.00:
#         kg_price_per_km = km * 0.03
#     elif 1.00 <= kg < 10.00:
#         kg_price_per_km = km * 0.05
#     elif 10.00 <= kg < 40.00:
#         kg_price_per_km = km * 0.10
#     elif 40.00 <= kg < 90.00:
#         kg_price_per_km = km * 0.15
#     elif 90.00 <= kg < 150.00:
#         kg_price_per_km = km * 0.20
# elif type_do == "express":
#     if kg < 1.00:
#         kg_price_per_km = km * 0.03
#         kg_price_per_km += km * (kg * (0.03 * 0.80))
#     elif 1.00 <= kg < 10.00:
#         kg_price_per_km = km * 0.05
#         kg_price_per_km += km * (kg * (0.05 * 0.40))
#     elif 10.00 <= kg < 40.00:
#         kg_price_per_km = km * 0.10
#         kg_price_per_km += km * (kg * (0.10 * 0.05))
#     elif 40.00 <= kg < 90.00:
#         kg_price_per_km = km * 0.15
#         kg_price_per_km += km * (kg * (0.15 * 0.02))
#     elif 90.00 <= kg < 150.00:
#         kg_price_per_km = km * 0.20
#         kg_price_per_km += km * (kg * (0.20 * 0.01))
# print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {kg_price_per_km:.2f} lv.")

# zad 4
# days = int(input())
# total_liters = 0
# total_degrees  = 0
# for d in range(days):
#     liters = float(input())
#     degrees = float(input())
#     total_liters += liters
#     total_degrees += liters * degrees
# print(f"Liter: {total_liters:.2f}")
# avr = total_degrees / total_liters
# print(f"Degrees: {avr:.2f}")
# if avr < 38:
#     print("Not good, you should baking!" )
# elif 38 <= avr <= 42:
#     print("Super!")
# elif avr > 42:
#     print("Dilution with distilled water!")

# zad 5
# import sys
# head_trick = False
# highest_score = -sys.maxsize
# winner = ""
# goals = 0
# while True:
#     name = input()
#     if name == "END":
#         break
#     goals = int(input())
#     if goals >= 10:
#         winner = name
#         head_trick = True
#         break
#     if goals >= 3:
#         head_trick = True
#     if goals > highest_score:
#         highest_score = goals
#         winner = name
# print(f"{winner} is the best player!")
# if head_trick:
#     print(f"He has scored {goals} goals and made a hat-trick !!!")
# else:
#     print(f"He has scored {goals} goals.")

# zad 6
# n = int(input())
# is_first = False
# for a in range(1, 10):
#     for b in range(9, a + 1, -1):
#         for c in range(0, 10):
#             for d in range(8, c, -1):
#                 divide = a * b * c * d
#                 collect = a + b + c + d
#                 if divide // collect == 3 and n % 3 == 0 and is_first == False:
#                     print(f"{d}", end="")
#                     print(f"{c}", end="")
#                     print(f"{b}", end="")
#                     print(f"{a}")
#                     is_first = True
#                 if divide == collect and n % 10 == 5  and is_first == False:
#                     print(f"{a}", end="")
#                     print(f"{b}", end="")
#                     print(f"{c}", end="")
#                     print(f"{d}")
#                     is_first = True
# if not is_first:
#     print("Nothing found")


# 5 zad again
# import sys
# head_trick = False
# highest_score = -sys.maxsize
# winner = ""
# goals = 0
# while True:
#     name = input()
#     if name == "END":
#         break
#     goals = int(input())
#     if goals >= 10:
#         winner = name
#         highest_score = goals
#         head_trick = True
#         break
#     if goals >= 3:
#         head_trick = True
#     else:
#         head_trick = False
#     if 0 < goals > highest_score:
#         highest_score = goals
#         winner = name
# if winner != "":
#     print(f"{winner} is the best player!")
# if head_trick:
#     print(f"He has scored {highest_score} goals and made a hat-trick !!!")
# else:
#     print(f"He has scored {highest_score} goals.")
