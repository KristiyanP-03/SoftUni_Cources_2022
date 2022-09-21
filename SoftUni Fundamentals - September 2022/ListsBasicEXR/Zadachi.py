# zad 4
# sums_list_as_strings = input().split(",")
# count_of_beggars = int(input())
# final_list = []
# counter_of_index = 0
# sums_list_as_digits = []
# for element in sums_list_as_strings:
#     sums_list_as_digits.append(int(element))
# while counter_of_index < count_of_beggars:
#     sum_for_current_beggar = 0
#     for current_index in range(counter_of_index, len(sums_list_as_digits), count_of_beggars):
#         sum_for_current_beggar += sums_list_as_digits[current_index]
#     counter_of_index += 1
#     final_list.append(sum_for_current_beggar)
# print(final_list)

# zad 5
# string = input()
# shuffles = int(input())
# list_string = string.split(' ')
# for _ in range(shuffles):
#     first_half = list_string[:len(list_string) // 2]
#     second_half = list_string[len(list_string) // 2:]
#     list_string = [letter for pair in zip(first_half, second_half) for letter in pair]
# print(list_string)

# zad 6
# import sys
# smallest = sys.maxsize
# list_of_new_str_nums = []
# string_of_nums = input()
# remove_n_times = int(input())
# removed_times = 0
# list_of_str_nums = string_of_nums.split(" ")
# list_of_nums = []
# for el in list_of_str_nums:
#     list_of_nums.append(int(el))
# while removed_times != remove_n_times:
#     for element in list_of_nums:
#         if element < smallest:
#             smallest = element
#     list_of_nums.remove(smallest)
#     smallest = 9999999
#     removed_times += 1
# for el in list_of_nums:
#     list_of_new_str_nums.append(str(el))
# print(", ".join(list_of_new_str_nums))
