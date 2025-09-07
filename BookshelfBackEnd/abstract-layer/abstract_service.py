from abc import ABC, abstractmethod
from entities.reader import Reader


class ApplicationServices(ABC):

    @abstractmethod
    def register_reader(self, first_name: str, email: str, password: str) -> Reader:
        pass
