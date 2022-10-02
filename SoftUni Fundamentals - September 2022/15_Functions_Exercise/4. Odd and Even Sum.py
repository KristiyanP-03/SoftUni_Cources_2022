single_number = input()
def odd_and_even_digit_sum(str_number):
    odd_sum = 0
    even_sum = 0
    for current_str_digit in str_number:
        digit = int(current_str_digit)
        if digit % 2 == 1:
            odd_sum += digit
        else:
            even_sum += digit
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
odd_and_even_digit_sum(single_number)