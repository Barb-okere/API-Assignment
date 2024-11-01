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
    
    # Remove a book from the library collection
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book.title}' has been removed from the library.")
        else:
            print(f"'{book.title}' is not in the library.")

    # Display the available books in the library
    def show_available_books(self):
        if self.books:
            print("Available books in the library:")
            for book in self.books:
                if book.check_availability():
                 print(f"'{book.title}' {book.book_type()} by {book.author}")
            else:
                    print("No books available in the library.")
                    print()
    #The Library class has methods to add books to the collection, remove books, and display the available books.   
    #The show_available_books() method displays the available books in the library with their titles, authors, and types.
# Create an instance of the Library class
library = Library()
#The Library class is now complete, and we can create an instance of Library to represent a library.
#The library instance can be used to manage the collection of books in the library.
#The Library class manages the collection of books in the library, providing methods to add, remove, and display available books.
#The Library class is now complete, and we can create an instance of Library to represent a library.

