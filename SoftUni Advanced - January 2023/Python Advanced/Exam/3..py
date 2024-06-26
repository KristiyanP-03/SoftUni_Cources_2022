def shop_from_grocery_list(budget, grocery_list, *products):
    total_prise = 0

    for product, price in products:
        if product in grocery_list:
            if total_prise + price <= budget:
                total_prise += price
                grocery_list.remove(product)
            else:
                return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
    else:
        if grocery_list:
            return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."
        return f"Shopping is successful. Remaining budget: {(budget-total_prise):.2f}."




print(shop_from_grocery_list(100,["tomato", "cola"],("cola", 5.8),("tomato", 10.0),("tomato", 20.45),))

print(shop_from_grocery_list(100,["tomato", "cola", "chips", "meat"],("cola", 5.8),("tomato", 10.0),("meat", 22),))

print(shop_from_grocery_list(100,["tomato", "cola", "chips", "meat", "chocolate"],("cola", 15.8),("chocolate", 30),("tomato", 15.85),("chips", 50),("meat", 22.99),))















# purchased_products = set()
    # total_cost = 0
    #
    # for product, price in products:
    #     if product in grocery_list and product not in purchased_products and price <= budget:
    #         budget -= price
    #         purchased_products.add(product)
    #         total_cost += price
    #
    # if len(purchased_products) == len(grocery_list):
    #     return f"Shopping is successful. Remaining budget: {budget:.2f}."
    # else:
    #     missing_products = set(grocery_list) - purchased_products
    #     return f"You did not buy all the products. Missing products: {', '.join(sorted(missing_products))}."