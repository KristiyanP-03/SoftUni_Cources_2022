number = int(input())
def perfect_num(num):
    perfect_sum = 0
    not_perfect = False
    for i in range(1, num):
        if num % i == 0:
            perfect_sum += i
    if perfect_sum != num:
        not_perfect = True
    if not_perfect:
        print("It's not so perfect.")
    else:
        print("We have a perfect number!")
perfect_num(number)