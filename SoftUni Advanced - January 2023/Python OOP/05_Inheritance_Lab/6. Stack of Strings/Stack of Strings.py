class Stack:

    def __init__(self):
        self.data = list()

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        return '[' + ', '.join(self.data[::-1]) + ']'