import sys
biggest = -sys.maxsize
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
if n_1 > biggest:
    biggest = n_1
if n_2 > biggest:
    biggest = n_2
if n_3 > biggest:
    biggest = n_3
print(biggest)