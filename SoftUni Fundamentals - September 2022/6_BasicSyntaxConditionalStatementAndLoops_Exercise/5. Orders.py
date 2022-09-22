orders = int(input())
price = 0
total_money = 0
for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if (price_per_capsule < 0.01 or price_per_capsule > 100.00) or (days < 1 or days > 31) or \
        (capsules < 1 or capsules > 2000):
        continue
    price = (price_per_capsule * capsules) * days
    print(f"The price for the coffee is: ${price:.2f}")
    total_money += price
print(f"Total: ${total_money:.2f}")