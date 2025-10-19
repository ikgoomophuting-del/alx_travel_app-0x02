from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_payment_confirmation_email(email, booking_reference, amount, status):
    subject = f"Payment {status}: {booking_reference}"
    message = f"Your payment of {amount} ETB for booking {booking_reference} is {status.lower()}."
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
    return f"Email sent to {email}"

