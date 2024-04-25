# contact/views.py
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Message

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')
        Message.objects.create(name=name, email=email, message=message_content)

        # Send confirmation email
        send_mail(
            'Confirmation Email',
            'Thank you for your message. We will get back to you soon!',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Message received successfully'})
    return JsonResponse({'error': 'Invalid request method'})
