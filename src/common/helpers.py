from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from src.common.tasks import send_email_task


class EmailHelper:
    FROM = 'noreply@somehost.local'

    @staticmethod
    def send_mail(context, template, subject, to):
        if isinstance(to, str):
            to = [to]

        email_html_message = render_to_string(f'emails/{template}.html', context)
        email_plaintext_message = render_to_string(f'emails/{template}.txt', context)

        if not settings.TESTING:
            send_email_task.delay(subject, to, EmailHelper.FROM, email_plaintext_message, email_html_message)
            return

        msg = EmailMultiAlternatives(subject, email_plaintext_message, EmailHelper.FROM, to)
        msg.attach_alternative(email_html_message, "text/html")
        return msg.send()
