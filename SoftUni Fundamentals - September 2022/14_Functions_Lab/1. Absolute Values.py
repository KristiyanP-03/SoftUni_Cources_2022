list_of_numbers = input().split(" ")
converted_list = []
def absolute_values(imputed_list):
    for element in imputed_list:
        current_number = float(element)
        current_number = abs(current_number)
        converted_list.append(current_number)
    return converted_list
print(absolute_values(list_of_numbers))