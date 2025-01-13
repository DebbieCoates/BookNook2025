from django.contrib import admin
from .models import Book

# Allow the Admin site to appear in the admin site
admin.site.register(Book)