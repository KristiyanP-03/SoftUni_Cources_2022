n = int(input())
for num in range(1, n + 1):
    sum_of_d = 0
    d = num
    while d > 0:
        sum_of_d += d % 10
        d = int(d / 10)
    if(sum_of_d == 5) or (sum_of_d == 7) or (sum_of_d == 11):
       print(f'{num} -> True')
    else:
       print(f'{num} -> False')