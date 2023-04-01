def negative_and_postitive_numbers_sum(sequence_of_numbers):
    list_of_numbers = list(map(int, sequence_of_numbers.split(' ')))

    sum_of_positive_numbers = 0
    sum_of_negative_numbers = 0

    for number in list_of_numbers:
        if number >= 0:
            sum_of_positive_numbers += number
        else:
            sum_of_negative_numbers += number

    print(sum_of_negative_numbers)
    print(sum_of_positive_numbers)

    if sum_of_positive_numbers > abs(sum_of_negative_numbers):
        return "The positives are stronger than the negatives"
    elif sum_of_positive_numbers < abs(sum_of_negative_numbers):
        return "The negatives are stronger than the positives"


print(negative_and_postitive_numbers_sum(sequence_of_numbers=input()))