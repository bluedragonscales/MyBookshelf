from abc import ABC, abstractmethod
from entities.reader import Reader


class ReaderBlueprint(ABC):

    @abstractmethod
    def register_reader(self, reader: Reader) -> Reader:
        pass

    @abstractmethod
    def reader_login(self, username: str, password: str):
        pass

    def change_reader_details(self, reader_id: int):
        pass

    @abstractmethod
    def reader_logout(self, reader_id: int):
        pass