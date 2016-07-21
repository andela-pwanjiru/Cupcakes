from django.test import TestCase, Client
from models import Book, Category


# Create your tests here.
class InventoryTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='yes')
        self.book = Book.objects.create(title="too good",
                                        author="last night", category=self.category
                                        )

    def test_book_search(self):
        self.assertEqual(Book.objects.count(), 1)
        self.assertIn('too good',
                      Book.objects.get(title='too good').title)

    def test_search_with_wrong_title(self):
        self.assertEqual(Book.objects.filter(title="nothing").count(), 0)
