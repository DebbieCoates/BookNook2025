

from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review
from .models import Book
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .forms import ApprovalForm

@login_required
def pending_approval(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            book_id = form.cleaned_data['book_id']
            approval_status = form.cleaned_data['approved']
            book = Book.objects.get(id=book_id)
            book.approved = approval_status
            book.save()
            return redirect('pending_approval')
    else:
        books = Book.objects.filter(approved=False)
        form = ApprovalForm()
    return render(request, 'book/pending_approval.html', {'books': books, 'form': form})



from django.contrib import messages

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploadedby = request.user  # Set the current user as the uploader
            book.save()
            messages.success(request, f'Book "{book.title}" added successfully and is now pending admin approval.')
            return redirect('all_books')  # Redirect to 'all_books' after successful addition
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})



@login_required
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Change 'book_list' to your desired redirect URL
    else:
        form = BookForm(instance=book)
    return render(request, 'book/update_book.html', {'form': form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Change 'book_list' to your desired redirect URL
    return render(request, 'book/delete_book.html', {'book': book})


# def your_view(request):
#     review = {
#         'rating': 3,  # Example rating
#     }
#     return render(request, 'your_template.html', {'review': review})



def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})


# FEATURED BOOKS ON MAIN PAGE
class BookList(generic.ListView):
    template_name = "book/book_list.html"
    queryset = Book.objects.filter(featured=True).order_by('id')[:3]

# ALL BOOKS
class AllBooks(generic.ListView):
    template_name = "book/all_books.html"
    # queryset = Book.objects.all()
    paginate_by = 6  # Show 6 books per page

    def get_queryset(self):
        return Book.objects.filter(approved=True)  # Filter to only include approved books

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

