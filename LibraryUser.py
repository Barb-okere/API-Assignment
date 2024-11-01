# LibraryUser class to represent a library member
class LibraryUser:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    #Represents a library user and manages the user's borrowed books. 