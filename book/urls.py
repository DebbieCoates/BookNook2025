
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('all/', views.AllBooks.as_view(), name='all_books'),
    path('books/<int:pk>/', views.SingleBookListing.as_view(), name='single_book_listing'),
]
