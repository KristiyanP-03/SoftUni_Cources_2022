def shopping_cart(*args):
    args = list(args)

    shopping_cart = {}

    for elements in args:
        if elements == "Stop":
            if shopping_cart == {}:
                print("No products in the cart!")
            else:
                for meal, products in sorted(shopping_cart.items(), key=lambda x: (-len(x[1]), x[0])):
                    sorted_products = sorted(products)
                    print(f"{meal}:")
                    for product in sorted_products:
                        print(f" - {product}")

            return ""

        if elements[0] in shopping_cart.keys():
            if len(shopping_cart[elements[0]]) < 4 and elements[0] == "Pizza":
                if elements[1] not in shopping_cart[elements[0]]:
                    shopping_cart[elements[0]].append(elements[1])

            elif len(shopping_cart[elements[0]]) < 2 and elements[0] == "Dessert":
                if elements[1] not in shopping_cart[elements[0]]:
                    shopping_cart[elements[0]].append(elements[1])

            elif len(shopping_cart[elements[0]]) < 3 and elements[0] == "Soup":
                if elements[1] not in shopping_cart[elements[0]]:
                    shopping_cart[elements[0]].append(elements[1])
        else:
            shopping_cart[elements[0]] = [elements[1]]


print(shopping_cart(('Pizza', 'ham'),('Soup', 'carrots'),('Pizza', 'cheese'),('Pizza', 'flour'),('Dessert', 'milk'),
                    ('Pizza', 'mushrooms'),('Pizza', 'tomatoes'),'Stop',))

print(shopping_cart(('Pizza', 'ham'), ('Dessert', 'milk'), ('Pizza', 'ham'), 'Stop',))

print(shopping_cart('Stop',('Pizza', 'ham'),('Pizza', 'mushrooms'),))