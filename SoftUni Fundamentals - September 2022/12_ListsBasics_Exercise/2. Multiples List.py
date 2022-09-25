factor = int(input())
count = int(input())
multiples_list = []
for number in range(factor, count * factor + 1, factor):
    multiples_list.append(number)
print(multiples_list)