class sequence_repeat:
    def __init__(self, string, number):
        self.string = string
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        else:
            char = self.string[self.index]
            if self.index + 1 == len(self.string):
                self.index = 0
            else:
                self.index += 1
            self.number -= 1
            return char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')