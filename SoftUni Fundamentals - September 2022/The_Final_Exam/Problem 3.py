notebook = {}

str_word_and_def = input()
list_word_and_def = str_word_and_def.split(" | ")
for word_and_def in list_word_and_def:
    key, value = word_and_def.split(": ")
    if key not in notebook.keys():
        notebook[key] = [value]
    else:
        notebook[key].append(value)

words_given_by_the_teacher = input()
test = words_given_by_the_teacher.split(" | ")

teacher_says = input()
if teacher_says == "Test":
    for word in test:
        if word in notebook.keys():
            print(f"{word}:")
            for meaning in notebook[word]:
                print(f" -{meaning}")

elif teacher_says == "Hand Over":
    my_list_with_words = []
    for key in notebook.keys():
        my_list_with_words.append(key)
    print(" ".join(my_list_with_words))