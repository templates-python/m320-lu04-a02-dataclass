from dataclasses import dataclass


@dataclass
class Book:
    """
    A book in a library.

    Attributes
    ----------
    title: str
    author: str
    available: bool
    """


if __name__ == '__main__':
    # Testen
    book1 = Book(title="Python Programmierung", author="Guido van Rossum")

    print(book1.available)
    book1.available = False
    print(book1.available)
