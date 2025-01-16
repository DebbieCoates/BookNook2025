

from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review
from .models import Book
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404



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




class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'book/review_form.html'

    def form_valid(self, form):
        # Assign the logged-in user to the review
        form.instance.author = self.request.user

        # Assign the book using the GET parameter 'book_id'
        book_id = self.request.GET.get('book_id')
        if book_id:
            form.instance.book = get_object_or_404(Book, id=book_id)

        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the book's detail page after creating a review
        return reverse_lazy('single_book_listing', kwargs={'pk': self.object.book.id})

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['body', 'rating']
    template_name = 'book/review_form.html'

    def get_success_url(self):
        # Redirect back to the book's detail page after updating the review
        return reverse_lazy('single_book_listing', kwargs={'pk': self.object.book.id})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'book/confirm_delete.html'

    def get_success_url(self):
        # Redirect to the associated book's detail page after deletion
        return reverse_lazy('single_book_listing', kwargs={'pk': self.object.book.id})

