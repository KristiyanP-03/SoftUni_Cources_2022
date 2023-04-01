def draw_upper_half(n):
    for i in range(n):
        spaces = n - 1 - i
        stars = i + 1
        print(' ' * spaces + '* ' * stars)


def draw_lower_half(n):
    for i in range(n):
        spaces = i + 1
        stars = n - i - 1
        print(' ' * spaces + '* ' * stars)

n = int(input())

draw_upper_half(n)
draw_lower_half(n)

