list_of_stringed_numbers = input().split()
def sorting_function(list_of_strings):
    sorted_list = []
    for element in list_of_strings:
        number = int(element)
        sorted_list.append(number)
    return sorted(sorted_list)
print(sorting_function(list_of_stringed_numbers))