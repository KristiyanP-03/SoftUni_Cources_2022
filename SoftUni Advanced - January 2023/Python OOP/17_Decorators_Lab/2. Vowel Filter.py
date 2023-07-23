vowels = ["a", "e", "i", "u", "y", "o"]

def vowel_filter(function):

    def wrapper():
        list_with_chars = function()
        new_list = [char for char in list_with_chars if char in vowels]
        return new_list

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())