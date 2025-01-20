from django import forms
from .models import Review, Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, HTML

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'synopsis', 'category', 'book_cover', 'part_of_series', 'ISBN']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('title'),
            Field('author'),
            Field('synopsis'),
            Field('category'),
            Field('book_cover'),
            Field('part_of_series'),
            Field('ISBN'),
            Submit('submit', 'Save Book')
        )

class ApprovalForm(forms.Form):
    book_id = forms.IntegerField(widget=forms.HiddenInput())
    approved = forms.ChoiceField(choices=[(True, 'Approve'), (False, 'Reject')])

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Review
        fields = ['body', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('body'),
            Field('rating'),
            Submit('submit', 'Submit Review')
        )
