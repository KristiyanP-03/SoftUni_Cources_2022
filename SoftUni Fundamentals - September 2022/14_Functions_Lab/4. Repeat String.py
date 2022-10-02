text = input()
how_many_times = int(input())
def str_repeater(string, times):
    new_word = ""
    for i in range(times):
        new_word += string
    return new_word
print(str_repeater(text, how_many_times))
