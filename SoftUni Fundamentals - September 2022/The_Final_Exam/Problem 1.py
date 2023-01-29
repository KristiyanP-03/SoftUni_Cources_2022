string = input()

while True:

    command_line = input()

    if command_line == "End":
        break

    elif "Translate" in command_line:
        command, character , new_character = command_line.split(" ")
        while character in string:
            string = string.replace(character, new_character)
        print(string)

    elif "Includes" in command_line:
        command, substring = command_line.split(" ")
        if substring in string:
            print("True")
        else:
            print("False")

    elif "Start" in command_line:
        command, substring = command_line.split(" ")
        len_of_substring = len(substring)
        if string[:len_of_substring] == substring:
            print("True")
        else:
            print("False")

    elif command_line == "Lowercase":
        string = string.lower()
        print(string)

    elif "FindIndex" in command_line:
        command, char = command_line.split(" ")
        index = string.rfind(char)
        print(index)

    elif "Remove" in command_line:
        command, start_index, count_of_char = command_line.split(" ")
        start_index = int(start_index)
        count_of_char = int(count_of_char)

        end_index = start_index + count_of_char

        string = string[:start_index] + string[end_index:]
        print(string)

