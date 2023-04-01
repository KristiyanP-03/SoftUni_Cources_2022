def recursive_power(n, power):
    if power == 1:
        return n
    return n * recursive_power(n, power - 1)

print(recursive_power(2, 10))