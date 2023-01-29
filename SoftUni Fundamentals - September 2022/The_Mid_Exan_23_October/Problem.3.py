shelf_with_books = input().split("&")

while True:
    command = input()
    if command == "Done":
        print(", ".join(shelf_with_books))
        break
    if "Add" in command:
        current_command, book_name = command.split(" | ")
        if book_name not in shelf_with_books:
            shelf_with_books.insert(0, book_name)
    elif "Take Book" in command:
        current_command, book_name = command.split(" | ")
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)
    elif "Swap Books" in command:
        current_command, book_1, book_2 = command.split(" | ")
        if book_1 and book_2 in shelf_with_books:
            book1_index = shelf_with_books.index(book_1)
            book2_index = shelf_with_books.index(book_2)
            shelf_with_books[book1_index], shelf_with_books[book2_index] = shelf_with_books[book2_index], \
                                                                           shelf_with_books[book1_index]
    elif "Insert Book" in command:
        current_command, book_name = command.split(" | ")
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)
    elif "Check Book" in command:
        current_command, index = command.split(" | ")
        index = int(index)
        if index < len(shelf_with_books):
            print(shelf_with_books[index])

















