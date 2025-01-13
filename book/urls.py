from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('all_books', views.AllBooks.as_view(), name='all_books'),
]
