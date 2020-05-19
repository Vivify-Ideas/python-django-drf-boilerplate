from django.test import TestCase
from django.template.exceptions import TemplateDoesNotExist

from src.common.helpers import EmailHelper


class TestEmailHelper(TestCase):
    subject = 'subject line'
    to = 'to@example.com'

    def test_raise_exception_when_template_does_not_exist(self):
        with self.assertRaises(TemplateDoesNotExist):
            EmailHelper.send_mail({}, 'template_does_not_exist', self.subject, self.to)

    def test_send_mail(self):
        assert EmailHelper.send_mail({}, 'user_reset_password', self.subject, self.to) == 1
