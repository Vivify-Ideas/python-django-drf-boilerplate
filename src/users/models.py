import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken
from easy_thumbnails.fields import ThumbnailerImageField
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from easy_thumbnails.signals import saved_file
from easy_thumbnails.signal_handlers import generate_aliases_global

from src.common.helpers.token import default_token_generator
from src.common.helpers.urls import build_absolute_uri
from src.notifications.services import notify
from src.notifications.notifications import ACTIVITY_USER_CREATED, ACTIVITY_USER_RESETS_PASS


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    """
    reset_password_path = reverse('password_reset:reset-password-confirm')
    context = {
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'link': build_absolute_uri(f'{reset_password_path}?token={reset_password_token.key}'),
    }

    notify(ACTIVITY_USER_RESETS_PASS, context=context, email_to=[reset_password_token.user.email])


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_picture = ThumbnailerImageField('ProfilePicture', upload_to='profile_pictures/', blank=True, null=True)
    is_active = models.BooleanField(default=False,
                                    help_text='Designates whether this user should be treated as active.')

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def __str__(self):
        return self.username


saved_file.connect(generate_aliases_global)


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if not created:
        return

    """
    Handles user created verification process
    """
    # you can pass additional expiry param to make_token method
    token, _ = default_token_generator.make_token(instance)
    verify_account_path = reverse('user-verify_account')
    context = {
        'username': instance.username,
        'email': instance.email,
        'link': build_absolute_uri(f'{verify_account_path}?token={token}'),
    }

    notify(ACTIVITY_USER_CREATED, context=context, email_to=[instance.email])
