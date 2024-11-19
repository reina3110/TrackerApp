if __name__ == "__main__":
    ui = BookTrackerUI()
    logic = BookTrackerLogic()
    history = BookHistory()

    # Add a new book
    title, author, status = ui.get_user_input()
    book = logic.add_book(title, author, status)
    if book:
        history.add_to_history(book)

    # Display all books
    for b in logic.get_books():
        ui.display_book_info(b)
        
    # Display reading history
    print("Reading History:")
    for b in history.get_history():
        ui.display_book_info(b)
