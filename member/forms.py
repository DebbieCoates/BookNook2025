# members/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Member

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['bio', 'location', 'birth_date']
