from celery import task
from django.core.mail import EmailMultiAlternatives


@task(name='SendEmailTask')
def send_email_task(subject, to, default_from, email_plaintext_message, email_html_message):
    msg = EmailMultiAlternatives(subject, email_plaintext_message, default_from, to)
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
