string_with_names = input()
list_with_names = string_with_names.split(", ")
list_with_sorted_names = sorted(list_with_names, key=lambda el: (-len(el), el))
print(list_with_sorted_names)