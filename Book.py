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
        # The Book class is now complete, and we can create subclasses to represent different types of books.
         
# Book class subclasses 
# PhysicalBook class inheriting from Book

class PhysicalBook(Book):
    def __init__(self, title, author, condition="Good"):
        super().__init__(title, author)
        self.condition = condition

    # Return the book type
    def book_type(self):
        return "Physical Book"
    #The PhysicalBook class inherits from the Book class and defines a condition attribute to represent the physical condition of the book.

    # Physical books can only be borrowed if in good condition
    def borrow_book(self):
        if self.condition == "Good":
            super().borrow_book()
        else:
            raise Exception(f"'{self.title}' is not in good condition for borrowing.")
        #Adds the condition attribute to represent the physical state of the book.
    #The borrow_book() method is overridden in the PhysicalBook class to check the condition of the book before borrowing it.

# EBook class inheriting from Book
class EBook(Book):
    def __init__(self, title, author, format="PDF", file_size = "2MB"):
        super().__init__(title, author)
        self.format = format
        self.file_size = file_size
        #The EBook class inherits from the Book class and defines format and file_size attributes to represent the digital format and file size of the book.

    # Return the book type
    def book_type(self):
        return "E-Book"
    #The book_type() method is overridden in the EBook class to return the book type as “E-Book”.
    #The borrow_book() method is not overridden in the EBook class, so it will use the implementation from the Book class to borrow the book if it is available.

    # Ebooks don't depend on physical availability, but simulate borrowing
    def borrow_book(self):
        print(f"'{self.title}' has been downloaded as an e-book.")
        #This class simulates downloading the book without affecting availability (e-books can be “borrowed” anytime).

# AudioBook class inheriting from Book
class AudioBook(Book):
    def __init__(self, title, author, duration="5 hours"):
        super().__init__(title, author)
        self.duration = duration
        #The AudioBook class inherits from the Book class and defines duration attribute to represent the length of the audio book.

    # Return the book type
    def book_type(self):
        return "Audio Book"
    #The book_type() method is overridden in the AudioBook class to return the book type as “Audio Book”.
    #The borrow_book() method is not overridden in the AudioBook class, so it will use the implementation from the Book class to borrow the book if it is available.

    # Audio books can be borrowed for a specific duration of time
    def borrow_book(self):
        print(f"'{self.title}' has been borrowed for {self.duration}.")
        #This class simulates borrowing the book for a specific duration of time.

#The AudioBook class inherits from the Book class and defines a duration attribute to represent the length of the audio book.
#The borrow_book() method is overridden in the AudioBook class to specify the duration of time the book has been borrowed for.
#The Book class and its subclasses are now complete, and we can create instances of each subclass to represent different types of books.