from django import forms 
  
  
class email_form(forms.Form): 
    geeks_field = forms.EmailField(max_length = 200) 