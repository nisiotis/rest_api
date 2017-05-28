from django.test import TestCase

# Create your tests here.

from .models import Book

class ModelTestCase(TestCase):

    """This class defines the test suite for the book model."""


    def setUp(self):
        """Define the test client and other test variables."""
        self.book_name = "Write world class code"
        self.book = Book(name=self.book_name)



    def test_model_can_create_a_book(self):

        """Test the book model can create a book."""

        old_count = Book.objects.count()

        self.book.save()

        new_count = Book.objects.count()

        self.assertNotEqual(old_count, new_count)
