from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User  # Import the User model
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Define choices for the BooleanField
YES_NO_CHOICES = [(True, 'Yes'), (False, 'No')]

CATEGORY_CHOICES = (
    ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
)

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    synopsis = models.TextField()
    # genre = models.TextField()
    slug = models.SlugField(max_length=250, blank=True)  # No jls_extract_var
    book_cover = CloudinaryField('image', default='placeholder')
    part_of_series = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    ISBN = models.CharField(max_length=20, null=True, blank=True)
    featured = models.BooleanField(default=False)
    approved = models.BooleanField(choices=YES_NO_CHOICES, default=False) 
    uploadedby = models.ForeignKey(User, on_delete=models.CASCADE) 
    uploadedOn = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Fiction') 
    

    # Creates a slug if one is not supplied
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate the slug if not supplied
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    approved = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator ],default=5)