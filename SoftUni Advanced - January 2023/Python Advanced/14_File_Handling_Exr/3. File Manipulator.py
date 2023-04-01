import os




def create_file(name):
    file = open(name, 'w')
    return file.close()

def add_to_file(name, string):
    file = open(name, 'a')
    file.write(string)
    file.write('\n')
    return file.close()

def replace_strings(name, old_string, new_string):
    try:
        file = open(name, 'r')
        line = file.read()
        file.close()

        for char in line:
            line = line.replace(old_string, new_string)

        file = open(name, 'w')
        file.write(line)
        return file.close()
    except FileNotFoundError:
        print("An error occurred")
        return

def delete_file(name):
    try:
        os.remove(name)
    except FileNotFoundError:
        print("An error occurred")
    return






while True:
    command_line = input()
    if command_line == "End":
        break
    try:
        command, *other_parts_of_the_comand_line = command_line.split('-')
    except IndexError:
        print("Command is not complete and the program do not understand")


    if command == "Create":
        file_name = other_parts_of_the_comand_line[0]
        create_file(file_name)

    elif command  == "Add":
        file_name, content = other_parts_of_the_comand_line
        add_to_file(file_name, content)

    elif command == "Replace":
        file_name, old_content, new_content = other_parts_of_the_comand_line
        replace_strings(file_name, old_content, new_content)

    elif command == "Delete":
        file_name = other_parts_of_the_comand_line[0]
        delete_file(file_name)


    else:
        print("This command is unknown for the program")