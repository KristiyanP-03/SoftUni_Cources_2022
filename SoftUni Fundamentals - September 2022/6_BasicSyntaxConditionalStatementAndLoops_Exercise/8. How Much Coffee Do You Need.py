coffe_counter = 0
while True:
    event = input()
    if event == "END":
        break
    elif event == "coding" or event == "dog" or event == "cat" or event == "movie":
        coffe_counter += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        coffe_counter += 2
if coffe_counter > 5:
    print("You need extra sleep")
else:
    print(coffe_counter)