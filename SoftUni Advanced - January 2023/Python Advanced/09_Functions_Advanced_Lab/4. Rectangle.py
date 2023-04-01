def rectangle(length, width):

    def int_or_sth_else(a, b):
        if type(a) is not int or type(b) is not int:
            return exit(print("Enter valid values!"))

    int_or_sth_else(length, width)

    def area(a, b):
        return a * b
    def perimeter(a, b):
        return 2 * (a + b)

    area = area(length, width)
    perimeter = perimeter(length, width)

    return f"Rectangle area: {area}\nRectangle perimeter: {perimeter}"


print(rectangle(2, 10))