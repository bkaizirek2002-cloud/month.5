from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def add(x, y):
    print(f"---------->args {x} and {y}-------------->")
    #from time sleep
    #sleep(15)
    return x + y

@shared_task
def send_otp_mail():
    print("sending" * 10)
    send_mail(
        subject="You otp code",
        message=f"otp code: {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[mail],
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
            "azi.99kg.tls@gmail.com",
            "riszav.01@gmail.com",
            "abdillaevamedina6@gmail.com",
        ],
        fail_silently=False,
    )
    return "OK"