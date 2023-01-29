parts_price = input()
tax = 0.2

end_flag = False
sum_without_taxes = 0.00
taxes_sum = 0.00
total_sum = 0.00

while True:
    if (parts_price == "special" or parts_price == "regular") and sum_without_taxes > 1:
        break
    elif (parts_price == "special" or parts_price == "regular") and sum_without_taxes == 0.00:
        print("Invalid order!")
        end_flag = True
        break
    elif float(parts_price) < 0:
        print("Invalid price!")
    elif float(parts_price) > 0:
        parts_price = float(parts_price)
        sum_without_taxes += parts_price
    else:
        print("Invalid price!")
    parts_price = input()
taxes_sum = sum_without_taxes * tax
if parts_price == "special":
    total_sum = 0.9 * (sum_without_taxes + taxes_sum)
elif parts_price == "regular":
    total_sum = sum_without_taxes + taxes_sum
if not end_flag:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum_without_taxes:.2f}$")
    print(f"Taxes: {taxes_sum:.2f}$")
    print("-----------")
    print(f"Total price: {total_sum:.2f}$")