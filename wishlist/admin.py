from django.contrib import admin
from .models import WishList

# Allow the Admin site to appear in the admin site
# admin.site.register(Book)
admin.site.register(WishList)
