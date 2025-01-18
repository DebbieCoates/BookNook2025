from django.contrib import admin
from .models import Member

# Allow the Admin site to appear in the admin site
# admin.site.register(Book)
admin.site.register(Member)