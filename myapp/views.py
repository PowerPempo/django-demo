from django.shortcuts import render , HttpResponse , redirect

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
