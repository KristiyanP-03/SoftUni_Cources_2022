is_not_file_exist = False

try:
    file = open("text.txt", 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")
    is_not_file_exist = True

# bonus
if is_not_file_exist:
    question = input("Do you want to create one [y/n]: ")
    if question == 'y':
        creating_file = open("text.txt", 'w')
        creating_file.write("This is some random line\n")
        creating_file.write("This is the second line\n")
        creating_file.write("And this is the third one")
        print("File succsesfully created!")
    else:
        exit("Program ends here! LoL")