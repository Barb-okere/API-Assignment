# Library class to manage book collection
class Library:
    def __init__(self):
        self.books = []  # List to hold books in the library
    #Manages the library's collection of books.
    #The books attribute is a list to store the books available in the library.
    
    # The Library class has methods to add books to the collection, remove books, and display the available books.
    # Add a book to the library collection
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")
    