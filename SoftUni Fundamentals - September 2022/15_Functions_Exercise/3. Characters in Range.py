start_char = input()
end_char = input()
def char_range(first_char, second_char):
    start = ord(first_char)
    end = ord(second_char)
    for current_character in range(start + 1, end, + 1):
        character = chr(current_character)
        print(character, end=" ")
    print()
char_range(start_char, end_char)