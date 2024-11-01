# Define the LibraryUser class
class LibraryUser:
    def __init__(self, name):
        self.name = name

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

