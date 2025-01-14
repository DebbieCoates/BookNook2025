from django.db import models
from django.utils.text import slugify

# Define choices for the BooleanField
YES_NO_CHOICES = [(True, 'Yes'), (False, 'No')]

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    synopsis = models.TextField()
    genre = models.TextField()
    slug = models.SlugField(max_length=250, blank=True)  # No jls_extract_var
    # book_cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    part_of_series = models.BooleanField(choices=YES_NO_CHOICES, default=False)
    ISBN = models.CharField(max_length=20, null=True, blank=True)
    featured = models.BooleanField(default=False)

    # Creates a slug if one is not supplied
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically generate the slug if not supplied
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title