from abc import ABC, abstractmethod

# Base class for all types of books
class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_available = True  # Encapsulated attribute to manage availability
    

    # Abstract method to force subclasses to define book type
    @abstractmethod
    def book_type(self):
        pass
    # ABC module to enforce implementation of the book_type() method in subclasses.
    

    # Method to check if the book is available
    def check_availability(self):
        return self.__is_available
    #The __is_available attribute is private, ensuring that only borrow_book() and return_book() can modify the book’s availability.
    

    # Borrow the book if available, otherwise raise an exception
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
    
# PhysicalBook class inheriting from Book
class PhysicalBook(Book):
    def __init__(self, title, author, condition="Good"):
        super().__init__(title, author)
        self.condition = condition
    
    # Return the type of book
    def book_type(self):
        return "Physical Book"
    
    # Physical books can only be borrowed if in good condition
    def borrow_book(self):
        if self.condition == "Good":
            super().borrow_book()
        else:
            raise Exception(f"'{self.title}' is not in good condition for borrowing.")
        #Adds the condition attribute to represent the physical state of the book.
    #The borrow_book() method is overridden in the PhysicalBook class to check the condition of the book before borrowing it.

# Ebook class inheriting from Book
class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    # Return the type of book
    def book_type(self):
        return "E-Book"
    
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

# LibraryUser class to represent a library member
class LibraryUser:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    #Represents a library user and manages the user's borrowed books. 

    # Borrow a book and handle errors
    def borrow_book(self, book):
        try:
            book.borrow_book()
            self.borrowed_books.append(book)
        except Exception as e:
            print(f"Error: {e}")
    
    # Return a book and handle errors
    def return_book(self, book):
        try:
            book.return_book()
            self.borrowed_books.remove(book)
        except Exception as e:
            print(f"Error: {e}")
            #. It has methods borrow_book() and return_book() that handle exceptions such as trying to return a book that hasn't been borrowed.


# Library class to manage book collection
class Library:
    def __init__(self):
        self.books = []  # List to hold books in the library
    #Manages the library's collection of books. 
    # Add a book to the library
    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")
    
    # Display all available books in the library
    def show_available_books(self):
        print("\nAvailable Books in the Library:")
        for book in self.books:
            if book.check_availability():
                print(f" - {book.title} ({book.book_type()}) by {book.author}")
        print()  # Newline for better formatting
        #Users can add books and display available books.

# Main interaction function
def main():
    library = Library()
    user = LibraryUser("Alice")

    # Adding some books to the library
    library.add_book(PhysicalBook("The Catcher in the Rye", "J.D. Salinger"))
    library.add_book(Ebook("To Kill a Mockingbird", "Harper Lee", 1.2))
    library.add_book(PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", condition="Good"))
    library.add_book(PhysicalBook("Harry Porter and the Philosopher's Stone", "J.K. Rowling"))
    

    while True:
        # Menu for user interaction
        print("\nLibrary System:")
        print("1. Show Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            # Show available books
            library.show_available_books()
        
        elif choice == '2':
            # Borrow a book
            library.show_available_books()
            book_title = input("Enter the title of the book to borrow: ")
            found_book = None
            for book in library.books:
                if book.title.lower() == book_title.lower():
                    found_book = book
                    break
            
            if found_book:
                user.borrow_book(found_book)
            else:
                print(f"Book '{book_title}' not found in the library.")
        
        elif choice == '3':
            # Return a book
            if user.borrowed_books:
                print("\nBorrowed Books:")
                for idx, book in enumerate(user.borrowed_books):
                    print(f"{idx + 1}. {book.title} ({book.book_type()})")
                book_idx = int(input("Enter the number of the book to return: ")) - 1
                
                if 0 <= book_idx < len(user.borrowed_books):
                    user.return_book(user.borrowed_books[book_idx])
                else:
                    print("Invalid selection.")
            else:
                print("You have not borrowed any books.")
        
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice, please select from 1 to 4.")

if __name__ == "__main__":
    main()
#Provides a user-friendly interface where users can:
# View available books.
# Borrow books by entering the book title.
# Return books by selecting from a list of borrowed books.
# Exit the system.