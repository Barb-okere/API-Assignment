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