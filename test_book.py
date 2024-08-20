import unittest

from book import Book


class TestBook(unittest.TestCase):
    def test_valid_book_creation(self):
        book = Book(title="Python Programmierung", author="Guido van Rossum")
        self.assertEqual(book.title, "Python Programmierung")
        self.assertEqual(book.author, "Guido van Rossum")
        self.assertTrue(book.available)

    def test_empty_title_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            Book(title="", author="Guido van Rossum")
        self.assertEqual(str(context.exception), 'title must not be empty')

    def test_empty_author_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            Book(title="Python Programmierung", author="")
        self.assertEqual(str(context.exception), 'author must not be empty')

    def test_set_availability(self):
        book = Book(title="Python Programmierung", author="Guido van Rossum")
        self.assertTrue(book.available)
        book.available = False
        self.assertFalse(book.available)

    def test_set_title(self):
        book = Book(title="Old Title", author="Guido van Rossum")
        book.title = "New Title"
        self.assertEqual(book.title, "New Title")

    def test_set_author(self):
        book = Book(title="Python Programmierung", author="Old Author")
        book.author = "New Author"
        self.assertEqual(book.author, "New Author")

