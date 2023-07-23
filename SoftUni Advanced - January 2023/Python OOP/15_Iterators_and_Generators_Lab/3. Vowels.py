vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']

class vowels:
    def __init__(self, string):
        self.string = ''.join([char for char in string if char.lower() in vowels_list])
        self.index = 0
        self.length = len(self.string)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.length:
            raise StopIteration
        else:
            current_char = self.string[self.index]
            self.index += 1
            return current_char

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)