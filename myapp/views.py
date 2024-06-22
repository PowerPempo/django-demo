from django.shortcuts import render , HttpResponse , redirect
from .forms import email_form
from .models import email_model
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
    #email_view = email_model.objects.get(id=id)
    context = {}
    context['form'] = email_form()

    if request.method == 'POST':
        forma = email_form(request.POST)
        if forma.is_valid():
            forma.save()

    else:
        forma = email_form()

    context['form'] = forma

    return render(request , 'developers.html' , context )

# ,{'email_view':email_view} 