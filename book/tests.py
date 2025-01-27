from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Review

# Model Tests
class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='testpass')
        Book.objects.create(
            title='Test Book',
            author='Test Author',
            synopsis='Test Synopsis',
            uploadedby=user,
        )

    def test_book_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title}'
        self.assertEqual(expected_object_name, 'Test Book')

    def test_book_author(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.author}'
        self.assertEqual(expected_object_name, 'Test Author')

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='testuser', password='testpass')
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            synopsis='Test Synopsis',
            uploadedby=user,
        )
        cls.review = Review.objects.create(
            book=book,
            author=user,
            body='Test Review',
            rating=5,  # Add the rating value
        )

    def test_review_body(self):
        review = Review.objects.get(body='Test Review')
        expected_object_name = f'{review.body}'
        self.assertEqual(expected_object_name, 'Test Review')

    def test_review_approved_default(self):
        review = Review.objects.get(body='Test Review')
        self.assertFalse(review.approved)

# View Tests
class BookViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        cls.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            synopsis='Test Synopsis',
            uploadedby=cls.user,
            approved=True,
        )
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            body='Test Review',
            rating=5,
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_list.html')

    def test_single_book_listing_view(self):
        response = self.client.get(reverse('single_book_listing', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/single_book_listing.html')

    def test_add_book_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('add_book'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/add_book.html')

    def test_update_book_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('update_book', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/update_book.html')

    def test_delete_book_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete_book', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deletion

