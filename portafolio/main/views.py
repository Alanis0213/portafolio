from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"De: {name} <{email}>\n\nMensaje:\n{message}"

        send_mail(
            subject="Nuevo mensaje de contacto",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['alanisdeavilat@gmail.com'],
        )

        # Puedes mostrar un mensaje o redirigir
        return render(request, 'index.html', {'success': True})

    return render(request, 'index.html')

def indexEn(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"De: {name} <{email}>\n\nMensaje:\n{message}"

        send_mail(
            subject="Nuevo mensaje de contacto",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['alanisdeavilat@gmail.com'],
        )

        # Puedes mostrar un mensaje o redirigir
        return render(request, 'indexEn.html', {'success': True})

    return render(request, 'indexEn.html')


def contacto(request):
    return render(request,'contactame.html')
def contactoEn(request):
    return render(request,'contactameEn.html')


def portafolio(request):
    return render(request,'portafolio.html')

def portafolioEn(request):
    return render(request,'portafolioEn.html')
