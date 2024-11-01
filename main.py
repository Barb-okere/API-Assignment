# Define the LibraryUser class
class LibraryUser:
    def __init__(self, name):
        self.name = name

# Define the PhysicalBook class
class PhysicalBook:
    def __init__(self, title, author, condition="New"):
        self.title = title
        self.author = author
        self.condition = condition

# Define the Ebook class
class Ebook:
    def __init__(self, title, author, file_size):
        self.title = title
        self.author = author
        self.file_size = file_size

# Define the AudioBook class
class AudioBook:
    def __init__(self, title, author, duration):
        self.title = title
        self.author = author
        self.duration = duration

# Define the Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

# Main interaction function
def main():
    library = Library()
    user1 = LibraryUser("Alice")

    # Adding some books to the library
    library.add_book(PhysicalBook("The Catcher in the Rye", "J.D. Salinger"))
    library.add_book(Ebook("To Kill a Mockingbird", "Harper Lee", 1.2))
    library.add_book(PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", condition="Good"))
    library.add_book(PhysicalBook("Harry Porter and the Philosopher's Stone", "J.K. Rowling"))
    library.add_book(PhysicalBook("1984", "George Orwell"))
    library.add_book(Ebook("Animal Farm", "George Orwell", 0.8))
    library.add_book(AudioBook("The Hobbit", "J.R.R. Tolkien", "10 hours"))
    library.add_book(AudioBook("The Lord of the Rings", "J.R.R. Tolkien", "50 hours"))
    library.add_book(PhysicalBook("The Hitchhiker's Guide to the Galaxy", "Dou glas Adams"))
    library.add_book(PhysicalBook("The Hitchhiker's Guide to the Galaxy", "Douglas Adams"))
    library.add_book(Ebook("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1.5))
    library.add_book(PhysicalBook("The Hitchhiker's Guide to the Galaxy", "Douglas Adams"))

    # Display available books
    library.show_available_books()
    
    # Alice borrows some books
    user1.borrow_book(library.books[0])
    user1.borrow_book(library.books[1])
    user1.borrow_book(library.books[2])

    # Display available books after borrowing
    library.show_available_books()
    
    # Alice returns a book
    user1.return_book(library.books[0])

    # Display available books after returning
    library.show_available_books()

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
                user1.borrow_book(found_book)
            else:
                print(f"Book '{book_title}' not found in the library.")
        
        elif choice == '3':
            # Return a book
            if user1.borrowed_books:
                print("\nBorrowed Books:")
                for idx, book in enumerate(user1.borrowed_books):
                    print(f"{idx + 1}. {book.title} ({book.book_type()})")
                book_idx = int(input("Enter the number of the book to return: ")) - 1
                
                if 0 <= book_idx < len(user1.borrowed_books):
                    user1.return_book(user1.borrowed_books[book_idx])
                else:
                    print("Invalid selection.")
            else:
                print("You have not borrowed any books.")
        
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice, please select from 1 to 4.")

# Run the main function
if __name__ == "__main__":
    main()
#The main() function creates instances of Library and LibraryUser classes, adds books to the library, and demonstrates borrowing and returning books by a library user.
#The main() function is executed when the script is run, displaying the available books, borrowing some books, returning a book, and displaying the updated list of available books.
#The main() function demonstrates the interaction between the Library and LibraryUser classes, showing how books can be added to the library, borrowed by users, and returned to the library.
#The main() function is executed when the script is run, displaying the available books, borrowing some books, returning a book, and displaying the updated list of available books.
#The main() function demonstrates the interaction between the Library and LibraryUser classes, showing how books can be added to the library, borrowed by users, and returned to the library.
#Provides a user-friendly interface where users can:
# View available books.
# Borrow books by entering the book title.
# Return books by selecting from a list of borrowed books.
# Exit the system.


