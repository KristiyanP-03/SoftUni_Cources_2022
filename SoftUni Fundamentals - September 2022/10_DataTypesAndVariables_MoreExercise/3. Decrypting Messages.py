key = int(input())
number_of_chars = int(input())
secret_word = ""
for n in range(number_of_chars):
    current_char = input()
    current_char_in_number = ord(current_char)
    secret_char_in_number = current_char_in_number + key
    secret_char = chr(secret_char_in_number)
    secret_word += secret_char
print(secret_word)