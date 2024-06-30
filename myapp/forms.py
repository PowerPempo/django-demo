from django import forms
from .models import email

class email_form(forms.ModelForm):
    class Meta:
        model = email 
        fields = ['email']