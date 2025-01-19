from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import WishList
from book.models import Book

@login_required
def wishlist_view(request):
    wishlist_items = WishList.objects.filter(user=request.user)
    wishlist_count = wishlist_items.count()
    paginator = Paginator(wishlist_items, 4)  # Show 4 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'wishlist_count': wishlist_count,
    }
    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    wishlist, created = WishList.objects.get_or_create(user=request.user, book=book)
    if created:
        messages.success(request, f'Book "{book.title}" added to wishlist.')
    else:
        messages.info(request, f'Book "{book.title}" is already in your wishlist.')
    return redirect('single_book_listing', pk=book_id)

@login_required
def remove_from_wishlist(request, book_id):
    wishlist_item = get_object_or_404(WishList, user=request.user, book_id=book_id)
    book_title = wishlist_item.book.title
    wishlist_item.delete()
    messages.success(request, f'Book "{book_title}" removed from wishlist.')
    return redirect('wishlist_view')
