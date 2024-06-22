from django import forms 

 
class email_form(forms.Form): 
    email_field = forms.EmailField(max_length = 200)   