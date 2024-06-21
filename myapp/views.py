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


def email_view(request):
    context = {}
    context['form'] = email_form()
    return render(request , 'developers.html' , context)