# members/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Member
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['bio', 'location', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }


