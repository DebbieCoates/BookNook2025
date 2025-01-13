

from django.views import generic
from .models import Book

class BookList(generic.ListView):
    model = Book
    template_name = "book_list.html"
    
    # Filter queryset to only include featured books
    queryset = Book.objects.filter(featured=True)
    


class AllBooks(generic.ListView):
    model = Book
    template_name = "book_list.html"
    
    # Include All Books
    queryset =Book.objects.all()