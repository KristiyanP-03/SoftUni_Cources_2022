number_of_compounds = int(input())

compound_destroier = set()

for _ in range(number_of_compounds):
    elements_list = input().split()

    for element in elements_list:
        compound_destroier.add(element)

print(*compound_destroier, sep="\n")