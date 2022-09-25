lines_of_sentences = int(input())
key_word = input()
not_filtered_list = []
filtered_list = []
for each_sentence in range(lines_of_sentences):
    sentence = input()
    not_filtered_list.append(sentence)
    if key_word in sentence:
        filtered_list.append(sentence)
print(not_filtered_list)
print(filtered_list)