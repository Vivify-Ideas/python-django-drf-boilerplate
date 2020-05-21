import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from six import python_2_unicode_compatible
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from easy_thumbnails.fields import ThumbnailerImageField
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

from src.common.helpers import EmailHelper


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args,
                                 **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    """
    # send an e-mail to the user
    context = {
        'username':
        reset_password_token.user.username,
        'email':
        reset_password_token.user.email,
        'reset_password_url':
        "{}{}?token={}".format(
            settings.SITE_URL,
            reverse('password_reset:reset-password-request'),
            reset_password_token.key)
    }

    EmailHelper.send_mail(context, 'user_reset_password', 'Password Reset',
                          [reset_password_token.user.email])


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_picture = ThumbnailerImageField('ProfilePicture',
                                            upload_to='profile_pictures/',
                                            blank=True,
                                            null=True)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


saved_file.connect(generate_aliases_global)
