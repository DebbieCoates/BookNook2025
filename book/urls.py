
from django.urls import path
from . import views

from .views import ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('all/', views.AllBooks.as_view(), name='all_books'),
    path('books/<int:pk>/', views.SingleBookListing.as_view(), name='single_book_listing'),
    path('reviews/add/', ReviewCreateView.as_view(), name='review_add'),
    path('reviews/edit/<int:pk>/', ReviewUpdateView.as_view(), name='review_edit'),
    path('reviews/delete/<int:pk>/', ReviewDeleteView.as_view(), name='review_delete'),
]


