list_with_numbers = input().split(" ")
def list_rounding_function(list_with_nums):
    rounded_list = []
    for element in list_with_nums:
        num = float(element)
        rounded_num = round(num)
        rounded_list.append(rounded_num)
    print(rounded_list)
list_rounding_function(list_with_numbers)