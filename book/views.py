

from django.views import generic
from .models import Book

# FEATURED BOOKS ON MAIN PAGE
class BookList(generic.ListView):
    template_name = "book/book_list.html"
    queryset = Book.objects.filter(featured=True).order_by('id')[:3]

# ALL BOOKS
class AllBooks(generic.ListView):
    template_name = "book/all_books.html"
    queryset = Book.objects.all()
    paginate_by = 6  # Show 10 books per page

# SINGLE BOOK LISTING
class SingleBookListing(generic.DetailView):
    model = Book
    template_name = 'book/single_book_listing.html'  # Specify your template here
    context_object_name = 'book'  # This defines the context variable that will be used in the template
