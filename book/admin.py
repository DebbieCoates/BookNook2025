from django.contrib import admin
from .models import Book
from .models import Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author')
    search_fields = ['title']
    list_filter = ('author',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('synopsis',)





# Allow the Admin site to appear in the admin site
# admin.site.register(Book)
admin.site.register(Review)
