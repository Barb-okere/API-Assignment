# LibraryUser class to represent a library member
class LibraryUser:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    #Represents a library user and manages the user's borrowed books. 
    #The borrowed_books attribute is a list to store the books borrowed by the user.

    # Borrow a book and add it to the user's borrowed books list 
    def borrow_book(self, book):
        try:
            book.borrow_book()
            self.borrowed_books.append(book)
        except Exception as e: # error handling
            print(f"Error: {e}")