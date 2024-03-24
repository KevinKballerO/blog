from django.core.mail import send_mail
from django.http import HttpResponse

def send_welcome_email(request):
    subject = 'Bienvenido a Mi Sitio'
    message = '¡Gracias por crear una cuenta!'
    from_email = 'from@example.com'
    recipient_list = ['to@example.com']
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return HttpResponse("Correo enviado exitosamente.")