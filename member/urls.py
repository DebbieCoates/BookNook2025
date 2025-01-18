
from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_member, name='update_member'),
    path('profile/', views.member_profile, name='member_profile'),
]
