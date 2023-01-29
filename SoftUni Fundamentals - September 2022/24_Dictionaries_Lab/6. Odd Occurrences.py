list_with_random_words = [word.lower() for word in input().split(" ")]
dict_with_counted_words = {}
list_with_odd_words = []
for current_word in list_with_random_words:
    if current_word not in dict_with_counted_words:
        dict_with_counted_words[current_word] = 1
    else:
        dict_with_counted_words[current_word] += 1
for the_word in dict_with_counted_words.keys():
    if dict_with_counted_words[the_word] % 2 == 1:
        list_with_odd_words.append(the_word)
print(" ".join(list_with_odd_words))
