product_name = input()
count_of_products = int(input())
def cash_register(product, count):
    price = 0.00
    if product == "coffee":
        price = 1.50 * count
    elif product == "water":
        price = 1.00 * count
    elif product == "coke":
        price = 1.40 * count
    elif product == "snacks":
        price = 2.00 * count
    print(f"{price:.2f}")
cash_register(product_name, count_of_products)

