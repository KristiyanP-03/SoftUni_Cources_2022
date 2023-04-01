sum_of_numbers = 0

file_to_read = open("numbers.txt", 'r')  #'r' is deafult
list_of_numbers_and_new_line_operators = file_to_read.readlines()

for element in list_of_numbers_and_new_line_operators:
    if "\\n" in element:
        element.replace('\\n', '')
        print(element)
    sum_of_numbers += int(element)

print(sum_of_numbers)