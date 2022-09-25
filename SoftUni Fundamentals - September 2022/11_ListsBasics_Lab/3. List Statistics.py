count_of_inputs = int(input())
postitive_number_list = []
negative_number_list = []
count_of_positive_numbers = 0
sum_of_negative_numbers = 0
for each_input in range(count_of_inputs):
    number = int(input())
    if number >= 0:
        postitive_number_list.append(number)
        count_of_positive_numbers += 1
    else:
        negative_number_list.append(number)
        sum_of_negative_numbers += number
print(postitive_number_list)
print(negative_number_list)
print(f"Count of positives: {count_of_positive_numbers}")
print(f"Sum of negatives: {sum_of_negative_numbers}")