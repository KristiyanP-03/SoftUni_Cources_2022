def reverse_text(string):
    string = string[::-1]
    for char in string:
        yield char

for char in reverse_text("step"):
    print(char, end='')