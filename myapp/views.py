from django.shortcuts import render , redirect
from .forms import email_form , ContactForm
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
        email = request.POST['email']
        if form.is_valid():
            form.cleaned_data['email']
            send_mail(
                'success, noreply',
                'Thank you for using our site, hope you enjoy features we did! ',
                'webstudio910@gmail.com',
                [email],
                fail_silently=False,
            )
            form.save()
            return redirect('success') 
    else:
        form = email_form()
    return render(request, 'developers.html', {'form': form})



def success(request):
    return render(request , 'success.html')
    


@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request'})



def send(request):
    return render(request, 'send.html')