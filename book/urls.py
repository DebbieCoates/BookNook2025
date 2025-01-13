from . import views
from django.urls import path

urlpatterns = [
   
    path('all_books', views.AllBooks.as_view(), name='all_books'),
    path('', views.BookList.as_view(), name='home'),
]
