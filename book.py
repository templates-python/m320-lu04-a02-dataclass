"""
Creates a book using dataclass and post_init
"""

from dataclasses import dataclass


@dataclass
class Book:
    """
    A book in a library.
    """
    title: str
    author: str
    available: bool = True

    def __post_init__(self):
        if not self.title:
            raise ValueError('title must not be empty')
        if not self.author:
            raise ValueError('author must not be empty')

    @property
    def title(self):
        """
        Gets the title.
        :return:
        """
        return self._title

    @title.setter
    def title(self, value):
        """
        Sets the title.
        :param value:
        :return:
        """
        self._title = value

    @property
    def author(self):
        """
        Gets the author.
        :return:
        """
        return self._author

    @author.setter
    def author(self, value):
        """
        Sets the author.
        :param value:
        :return:
        """
        self._author = value

    @property
    def available(self):
        """
        Gets the availability
        :return:
        """
        return self._available

    @available.setter
    def available(self, value):
        """
        Sets the availability
        :param value:
        :return:
        """
        self._available = value


if __name__ == '__main__':
    # Testen
    book1 = Book(title="Python Programmierung", author="Guido van Rossum")

    print(book1.available)
    book1.available = False
    print(book1.available)
