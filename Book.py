from abc import ABC, abstractmethod

# Base class for all book types
class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_available = True  # Encapsulated attribute to manage availability

    # Abstract method to force subclasses to define book type
    @abstractmethod
    def book_type(self):
        pass
    # ABC module to enforce implementation of the book_type() method in subclasses.

    # Method to check availablity of the book 
    def check_availability(self):
        return self.__is_available
    #The __is_available attribute is private, to ensure that only borrow_book() and return_book() can modify the book’s availability.

    # Borrow the book if available, else raise an exception
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"'{self.title}' has been borrowed.")
        else:
            raise Exception(f"'{self.title}' is currently not available.")
    
    # Return the book if it's borrowed, otherwise raise an exception
    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"'{self.title}' has been returned.")
        else:
            raise Exception(f"'{self.title}' was not borrowed.")
        #Exception handling is implemented in borrow_book() and return_book() to prevent borrowing an unavailable book or returning a book that hasn’t been borrowed.
    