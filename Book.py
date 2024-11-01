from abc import ABC, abstractmethod

# Base class for all book types
class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass