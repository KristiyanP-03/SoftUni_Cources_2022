with open("words.txt", 'w') as word_writer:
    word_writer.write(input())

with open("input.txt", 'w') as input_text:
    pass
# how to read multiple lines ???


file_with_words_reader = open("words.txt", 'r')
dict_of_words_and_counts = {}
list_of_words = file_with_words_reader.read().split(" ")
for word in list_of_words:
    dict_of_words_and_counts[word] = 0
file_with_words_reader.close()

input_reader = open("input.txt", 'r')
input_string = input_reader.read()
print(input_string)
for word in dict_of_words_and_counts.keys():
    dict_of_words_and_counts[word] = input_string.count(word)
input_reader.close()

print(dict_of_words_and_counts)

