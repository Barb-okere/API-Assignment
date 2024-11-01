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
            self.borrowed_books.remove(book)
        except Exception as e: # error handling
            print(f"Error: {e}")
    #The borrow_book() method borrows a book and adds it to the user's borrowed_books list.
    #If an exception is raised during borrowing, it is caught and displayed as an error message.

    # Return a book and remove it from the user's borrowed books list
    def return_book(self, book):
        try:
            book.return_book()
            self.borrowed_books.remove(book)
        except Exception as e: # error handling
            print(f"Error: {e}")
            #The return_book() method returns a book and removes it from the user's borrowed_books list
            #If an exception is raised during returning, it is caught and displayed as an error message.
            #The LibraryUser class has methods borrow_book() and return_book() that handle exceptions such as trying to return a book that hasn't been borrowed.
    #The LibraryUser class is now complete, and we can create instances of LibraryUser to represent library members.
    #The LibraryUser class manages the borrowing and returning of books for a library user, handling exceptions that may occur during the process.
# Create instances of LibraryUser
user1 = LibraryUser("Alice")
user2 = LibraryUser("Bob")

