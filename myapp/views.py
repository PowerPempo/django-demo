from django.shortcuts import render , HttpResponse , redirect
from .forms import email_form

def main(request):
    return render(request , 'main.html')

def index(request):
    return render(request , 'main')

def portfolio(request):
    return render(request , 'portfolio.html')

def portfolio_2(request):
    return render(request , 'portfolio')

def developers(request):
    return render(request , 'developers.html')

def developers_2(request):
    return render(request, 'developers')


def save_email(request):
    if request.method == 'POST':
        form = email_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = email_form()
    return render(request, 'developers.html', {'form': form})



def success(request):
    return render(request , 'success.html')
    