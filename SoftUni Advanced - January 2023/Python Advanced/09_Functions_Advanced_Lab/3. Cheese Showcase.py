def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    cheeses = []

    for cheese, pieces_count in sorted_cheeses:
        cheeses.append(cheese)
        quantities = sorted(pieces_count, reverse=True)
        cheeses += quantities

    return '\n'.join([str(cheese) for cheese in cheeses])

print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430],Mozzarella=[50, 125],))
