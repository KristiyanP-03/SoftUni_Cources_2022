# zad 1
# Naem = int(input())
# awards = Naem * 0.70
# food = awards * 0.85
# sound = food / 2
# final_price = Naem + awards + food + sound
# print(f"{final_price:.2f}")

# zad 2
# budget = float(input())
# dudes = int(input())
# dudes_dress_price = float(input())
# design = budget * 0.10
# if dudes > 150:
#     dudes_dress_price = dudes_dress_price - (dudes_dress_price * 0.10)
# price = dudes * dudes_dress_price + design
# if budget >= price:
#     money_left = budget - price
#     print("Action!")
#     print(f"Wingard starts filming with {money_left:.2f} leva left.")
# else:
#     needed_money = price - budget
#     print("Not enough money!")
#     print(f"Wingard needs {needed_money:.2f} leva more.")

# zad 3
# name = input()
# zala = input()
# bileti = int(input())
# price = 0.00
# if name == "A Star Is Born":
#     if zala == "normal":
#         price = 7.50
#     elif zala == "luxury":
#         price = 10.50
#     elif zala == "ultra luxury":
#         price = 13.50
# elif name == "Bohemian Rhapsody":
#     if zala == "normal":
#         price = 7.35
#     elif zala == "luxury":
#         price = 9.45
#     elif zala == "ultra luxury":
#         price = 12.75
# elif name == "Green Book":
#     if zala == "normal":
#         price = 8.15
#     elif zala == "luxury":
#         price = 10.25
#     elif zala == "ultra luxury":
#         price = 13.25
# elif name == "The Favourite":
#     if zala == "normal":
#         price = 8.75
#     elif zala == "luxury":
#         price = 11.55
#     elif zala == "ultra luxury":
#         price = 13.95
# income = price * bileti
# print(f"{name} -> {income:.2f} lv.")

# zad 4
# money = int(input())
# tickets = 0
# price = 0
# products = 0
# while True:
#     name = input()
#     if name == "End":
#         break
#     if len(name) > 8:
#         price += ord(name[0]) + ord(name[1])
#         if price > money:
#             break
#         tickets += 1
#     else:
#         price += ord(name[0])
#         if price > money:
#             break
#         products += 1
# print(tickets)
# print(products)

# zad 5
# import sys
# count = int(input())
# best_name = ""
# worst_name = ""
# highest_rate = -sys.maxsize
# lowest_rate = sys.maxsize
# avg = 0.00
# for c in range(count):
#     name = input()
#     rate = float(input())
#     if rate > highest_rate:
#         best_name = name
#         highest_rate = rate
#     elif rate < lowest_rate:
#         worst_name = name
#         lowest_rate = rate
#     avg += rate
# avg = avg / count
# print(f"{best_name} is with highest rating: {highest_rate:.1f}")
# print(f"{worst_name} is with lowest rating: {lowest_rate:.1f}")
# print(f"Average rating: {avg:.1f}")

# zad 6
busy_seats = 0
ticket_count = 0
st_tickets = 0
s_tickets = 0
k_tickets = 0
while True:
    film_name = input()
    if film_name == "Finish":
        break
    free_seats = int(input())
    while True:
        type_ticket = input()
        if type_ticket == "End":
            break
        if type_ticket == "student":
            ticket_count += 1
            busy_seats += 1
            st_tickets += 1
        elif type_ticket == "standard":
            ticket_count += 1
            busy_seats += 1
            s_tickets += 1
        elif type_ticket == "kid":
            ticket_count += 1
            busy_seats += 1
            k_tickets += 1
        if busy_seats == free_seats:
            break
    busy_seats = (busy_seats * 100) / free_seats
    print(f"{film_name} - {busy_seats:.2f}% full.")
    busy_seats = 0
st_tickets = (st_tickets * 100) / ticket_count
s_tickets = (s_tickets * 100) / ticket_count
k_tickets = (k_tickets * 100) / ticket_count
print(f"Total tickets: {ticket_count}")
print(f"{st_tickets:.2f}% student tickets.")
print(f"{s_tickets:.2f}% standard tickets.")
print(f"{k_tickets:.2f}% kids tickets.")
