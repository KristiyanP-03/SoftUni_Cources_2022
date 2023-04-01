symbols_list = ["-", ",", ".", "!", "?"]

file = open("1/text.txt", 'r')

is_even_line = True
for line in file:

    if is_even_line:
        for symbol in symbols_list:
            if symbol in line:
                line = line.replace(symbol, '@')

        list_line = line.split(" ")
        print(" ".join(list_line[::-1]))
        is_even_line = False


    else:
        is_even_line = True
