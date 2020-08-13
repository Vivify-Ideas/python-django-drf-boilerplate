from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from src.common.tasks import send_email_task


class EmailChannel:
    @staticmethod
    def send(context, html_template, subject, to):
        if isinstance(to, str):
            to = [to]

        email_html_message = render_to_string(html_template, context)

        if not settings.TESTING:
            send_email_task.delay(subject, to, settings.EMAIL_FROM, email_html_message)
            return

        msg = EmailMultiAlternatives(
            subject,
            email_html_message,
            settings.EMAIL_FROM,
            to,
            alternatives=((email_html_message, 'text/html'), ),
        )
        return msg.send()
