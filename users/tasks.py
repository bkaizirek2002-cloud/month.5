from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def add(x, y):
    print(f"---------->args {x} and {y}-------------->")
    return x + y

@shared_task
def send_otp_mail(email, otp):
    print("sending" * 10)
    send_mail(
        subject="You OTP code",
        message=f"otp code: {otp}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
    return "OK"

@shared_task
def send_report_mail():
    print("sending" * 10)
    send_mail(
        subject="Report data",
        message=f"что то очень важное",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[
            "bkaizirek2002@gmail.com", 
            #"azi.99kg.tls@gmail.com",
            #"riszav.01@gmail.com",
            #"abdillaevamedina6@gmail.com",
        ],
        fail_silently=False,
    )
    return "OK"