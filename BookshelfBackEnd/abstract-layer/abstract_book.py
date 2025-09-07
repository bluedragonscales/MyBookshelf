from abc import ABC, abstractmethod
from entities.book import Book

class BookBluprint(ABC):

    @abstractmethod
    def create_book (self):
        pass

    @abstractmethod
    def edit_book_details(self):
        pass

    @abstractmethod
    def list_books(self) -> list[Book]:
        pass

    @abstractmethod
    def delete_book(self):
        pass
