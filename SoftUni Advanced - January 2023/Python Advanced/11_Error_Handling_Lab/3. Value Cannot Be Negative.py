class NegativeNumbersHater(Exception):
    """I hate negative numbers"""

for _ in range(5):
        number = int(input())
        if number < 0:
            raise NegativeNumbersHater
else:
    print("Very yes")
