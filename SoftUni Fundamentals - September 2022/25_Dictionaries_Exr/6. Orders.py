store = {}
while True:
    command = input()
    if command == 'buy':
        break
    product, price, count = command.split(' ')
    price, count = float(price), int(count)
    quantity_left = 0
    if product not in store:
        store[product] = {}
        store[product][price] = 0
    else:
        quantity_left = list(store[product].values())
        quantity_left = quantity_left[0]
        store[product].clear()
        store[product] = {}
        store[product][price] = 0
    store[product][price] += count + quantity_left
for item in store:
    for key, value in store[item].items():
        result = key * value
        print(f"{item} -> {result:.2f}")

