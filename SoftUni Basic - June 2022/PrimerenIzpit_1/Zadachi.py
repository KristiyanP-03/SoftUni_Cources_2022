# 4b zad
# import sys
# points = 0
# biggest_score = -sys.maxsize
# winner = ""
# name = input()
# while True:
#     for i in name:
#         number = int(number)
#         if chr(number) == True:
#             points += 10
#         else:
#             points += 2
#     if points >= biggest_score:
#         biggest_score = points
#         winner = name
#     points = 0
#     name = input()
#     if name == "Stop":
#         print(f"The winner is {winner} with {biggest_score} points!")
#         break

#zad 5a
# sold_games = int(input())
# h_p = 0
# f_p = 0
# ov_p = 0
# o_p = 0
# for i in range(sold_games):
#     name = input()
#     if name == "Hearthstone":
#         h_p += 1
#     elif name == "Fornite":
#         f_p += 1
#     elif name == "Overwatch":
#         ov_p += 1
#     else:
#         o_p += 1
# if h_p != 0:
#     h_p = (h_p * 100) / sold_games
# if f_p != 0:
#     f_p = (f_p * 100) / sold_games
# if ov_p != 0:
#     ov_p = (ov_p * 100) / sold_games
# if o_p != 0:
#     o_p = (o_p * 100) / sold_games
# print(f"Hearthstone - {h_p:.2f}%")
# print(f"Fornite - {f_p:.2f}%")
# print(f"Overwatch - {ov_p:.2f}%")
# print(f"Others - {o_p:.2f}%")

