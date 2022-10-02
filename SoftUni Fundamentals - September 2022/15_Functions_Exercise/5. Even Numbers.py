list_of_str = input().split()
list_of_numbers = []
for num in list_of_str:
    number = int(num)
    list_of_numbers.append(number)
def check_even(number):
    if number % 2 == 0:
          return True
    return False
even_numbers_iterator = filter(check_even, list_of_numbers)
even_numbers = list(even_numbers_iterator)
print(even_numbers)
