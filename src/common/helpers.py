from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailHelper:
    from_email = 'noreply@somehost.local'

    @staticmethod
    def create_mail(context, template, subject, to):
        # render email text
        email_html_message = render_to_string(f'emails/{template}.html',
                                              context)
        email_plaintext_message = render_to_string(f'emails/{template}.txt',
                                                   context)

        msg = EmailMultiAlternatives(subject, email_plaintext_message,
                                     EmailHelper.from_email, to)
        msg.attach_alternative(email_html_message, "text/html")
        return msg

    @staticmethod
    def send_mail(context, template, subject, to):
        mail = EmailHelper.create_mail(context, template, subject, to)
        mail.send()
