remove_this = input()
the_string = input()
while remove_this in the_string:
    the_string = the_string.replace(remove_this, "")
print(the_string)