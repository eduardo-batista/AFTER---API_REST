from abc import ABC, abstractmethod

class AuthProvider(ABC):
    @abstractmethod
    def sign_up(self, email: str, password: str) -> str:
        pass

    @abstractmethod
    def sign_in(self, email: str, password: str) -> str:
        pass