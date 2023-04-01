class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page
        return f"You are on page {page} right now."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:              #self.book - <__obj__>     How to fix?
            if book.title == title:
                return f"You found your \"{title}\"!"
        else:
            return f"No such book found..."


my_book = Book("The Great Gatsby", "Francise Scott Fidgeralt")
Library().add_book(my_book)
print(Library().find_book("The Great Gatsby"))
print(my_book.turn_page(45))