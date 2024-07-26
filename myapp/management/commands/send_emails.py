# send_emails.py

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from myapp.models import email

class Command(BaseCommand):
    help = 'Send test emails to all subscribers'

    def handle(self, *args, **kwargs):
        subscribers = email.objects.all()
        subject = 'Test Email'
        message = 'This is a test email.'

        for subscriber in subscribers:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [subscriber.email],
                fail_silently=False,
            )

        self.stdout.write(self.style.SUCCESS('Emails sent successfully'))
