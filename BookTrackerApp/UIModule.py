class BookTrackerUI:
    @staticmethod
    def display_book_info(book):
        print(f"Title: {book.title}, Author: {book.author}, Status: {book.status}")

    @staticmethod
    def get_user_input():
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        status = input("Enter book status (to-read/reading/completed): ")
        return title, author, status
