words_separated_by_a_single_space = input()
palindrome_to_search = input()
list_of_palindromes = words_separated_by_a_single_space.split(" ")
list_of_palindromes = [word for word in list_of_palindromes if word == word[::-1]]
number_of_your_palindrome_found = list_of_palindromes.count(palindrome_to_search)
print(list_of_palindromes)
print(f"Found palindrome {number_of_your_palindrome_found} times")