class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

class BookTrackerLogic:
    def __init__(self):
        self.books = []
        self.factory = BookStatusFactory()

    def add_book(self, title, author, status_type):
        status = self.factory.create_status(status_type)
        if status:
            book = Book(title, author, status.status())
            self.books.append(book)
            return book
        else:
            print("Invalid status")

    def get_books(self):
        return self.books
