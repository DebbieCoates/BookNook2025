from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from book.models import Book
from .models import WishList

# Model Tests
class WishListModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='testpass')
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            synopsis='Test Synopsis',
            uploadedby=user,
        )
        WishList.objects.create(user=user, book=book)

    def test_wishlist_str(self):
        wishlist = WishList.objects.get(id=1)
        expected_object_name = f'{wishlist}'
        self.assertEqual(expected_object_name, 'testuser - Test Book')

# View Tests
class WishListViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        cls.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            synopsis='Test Synopsis',
            uploadedby=cls.user,
        )
        cls.wishlist = WishList.objects.create(user=cls.user, book=cls.book)

    def setUp(self):
        self.client.login(username='testuser', password='testpass')

    def test_wishlist_view(self):
        response = self.client.get(reverse('wishlist_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_add_to_wishlist_view(self):
        new_book = Book.objects.create(
            title='New Test Book',
            author='New Test Author',
            synopsis='New Test Synopsis',
            uploadedby=self.user,
        )
        response = self.client.get(reverse('add_to_wishlist', args=[new_book.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after adding to wishlist
        self.assertTrue(WishList.objects.filter(book=new_book).exists())

    def test_remove_from_wishlist_view(self):
        response = self.client.get(reverse('remove_from_wishlist', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after removing from wishlist
        self.assertFalse(WishList.objects.filter(book=self.book).exists())
