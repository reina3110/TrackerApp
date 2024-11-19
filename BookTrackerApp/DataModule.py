class BookHistory:
    def __init__(self):
        self.history = []

    def add_to_history(self, book):
        self.history.append(book)

    def get_history(self):
        return self.history
