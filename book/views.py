

from django.views import generic
from .models import Book
from .forms import ReviewForm
from django.shortcuts import render

def your_view(request):
    review = {
        'rating': 3,  # Example rating
    }
    return render(request, 'your_template.html', {'review': review})


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
# views.py
class SingleBookListing(generic.DetailView):
    model = Book
    template_name = 'book/single_book_listing.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.all()

        # Add a range list to the context
        context['range'] = range(1, 6)

        for review in reviews:
            review.stars = ['fas' if i < review.rating else 'far' for i in range(5)]

        context['reviews'] = reviews
        return context

