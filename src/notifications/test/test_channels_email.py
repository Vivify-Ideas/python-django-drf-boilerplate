from django.test import TestCase
from django.template.exceptions import TemplateDoesNotExist

from src.notifications.channels.email import EmailChannel


class TestEmailChannel(TestCase):
    subject = 'subject line'
    to = 'to@example.com'

    def test_raise_exception_when_template_does_not_exist(self):
        with self.assertRaises(TemplateDoesNotExist):
            EmailChannel.send({}, 'template_does_not_exist', self.subject, self.to)

    def test_send_mail(self):
        assert EmailChannel.send({}, 'emails/user_reset_password.html', self.subject, self.to) == 1
