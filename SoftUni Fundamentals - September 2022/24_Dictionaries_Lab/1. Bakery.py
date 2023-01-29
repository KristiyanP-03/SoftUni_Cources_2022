list_of_products = input().split(" ")
bakery = {}
for index in range(0, len(list_of_products)):
    if index== 0 or index % 2 == 0:
        key = list_of_products[index]
    else:
        value = int(list_of_products[index])
        bakery[key] = value
print(bakery)