from django.test import TestCase
from django.template.exceptions import TemplateDoesNotExist

from ..helpers import EmailHelper


class TestEmailHelper(TestCase):
    subject = 'subject line'
    to = 'to@example.com'

    def test_raise_exception_when_template_does_not_exist(self):
        with self.assertRaises(TemplateDoesNotExist):
            EmailHelper.create_mail({'name': 'test'},
                                    'template_does_not_exist', 'subject line',
                                    'to@example.com')

    def test_create_mail(self):
        msg = EmailHelper.create_mail({}, 'user_reset_password', self.subject,
                                      self.to)
        self.assertEqual(msg.to, [self.to])
        self.assertEqual(msg.from_email, EmailHelper.FROM)
        self.assertEqual(msg.subject, self.subject)

    def test_send_mail(self):
        assert EmailHelper.send_mail({}, 'user_reset_password', self.subject,
                                     self.to) == 1
