from django import forms
from .models import Review
from .models import Book


# In your forms.py
from django import forms
from .models import Book

class ApprovalForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())
    approved = forms.ChoiceField(choices=[(True, 'Approve'), (False, 'Reject')])


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['body', 'rating']  # Exclude 'book' and 'author'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'synopsis', 'category', 'book_cover', 'part_of_series', 'ISBN']