from django import forms
from .models import email , Contact

class email_form(forms.ModelForm):
    class Meta:
        model = email 
        fields = ['email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'comment']
