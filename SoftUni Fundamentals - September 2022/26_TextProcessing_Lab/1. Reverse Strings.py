while True:
    your_string = input()
    if your_string == "end":
        break
    your_string_reversed = your_string[::-1]
    print(f"{your_string} = {your_string_reversed}")