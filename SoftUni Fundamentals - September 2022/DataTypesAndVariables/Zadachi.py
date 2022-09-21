# zad 1
# name_1 = input()
# name_2 = input()
# something_between = input()
# print(name_1 + something_between + name_2)

# zad 2
# meters = int(input())
# kilometers = meters / 1000
# print(f"{kilometers:.2f}")

# zad 3
# pound = int(input())
# dolar = pound * 1.31
# print(f"{dolar:.3f}")

# zad 4
# centuries = int(input())
# years = centuries * 100
# days = years * 365.2422
# days = int(days)
# hours = days * 24
# minutes = hours * 60
# print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

# zad 5
# n = int(input())
# for num in range(1, n + 1):
#     sum_of_d = 0
#     d = num
#     while d > 0:
#         sum_of_d += d % 10
#         d = int(d / 10)
#     if(sum_of_d == 5) or (sum_of_d == 7) or (sum_of_d == 11):
#        print(f'{num} -> True')
#     else:
#        print(f'{num} -> False')

# zad 6
# year = int(input())
# happy_year = False
# while not happy_year:
#     year += 1
#     set_year = set()
#     for i in range(len(str(year))):
#         set_year.add(str(year)[i])
#     happy_year = len(set_year) == len(str(year))
# print(year)
