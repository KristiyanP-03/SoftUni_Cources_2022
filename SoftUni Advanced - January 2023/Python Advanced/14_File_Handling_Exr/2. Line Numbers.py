file = open("1/text.txt", 'r')
punctuation_marks_list = ["-", ",", ".", "!", "?", "'"]
chars_counter = 0
punctuation_marks_counter = 0

for i, line in enumerate(file):
    line = line.replace('\n', ' ')

    for char in line:
        if char in punctuation_marks_list:
            punctuation_marks_counter += 1
        elif char not in punctuation_marks_list and char != ' ':
            chars_counter += 1

    line = f"Line {i + 1}: " + line + f"({chars_counter})({punctuation_marks_counter})"
    print(line)

    chars_counter = 0
    punctuation_marks_counter = 0