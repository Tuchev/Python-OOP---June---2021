from abc import abstractmethod, ABC


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class MobileFormatter(BaseFormatter):
    def format(self, book: Book):
        return book.content[:20]


class DesktopFormatter(BaseFormatter):
    def format(self, book: Book):
        return book.content[:100]


class Printer:
    def get_book(self, book: Book, formatter: BaseFormatter):
        print("Print...")
        return formatter.format(book)
