from abc import ABC, abstractmethod

class ReaderBlueprint(ABC):

    @abstractmethod
    def reader_login(self, username: str, password: str):
        pass

    def change_reader_details(self, reader_id: int):
        pass

    @abstractmethod
    def reader_logout(self, reader_id: int):
        pass