import os
from .common import * # noqa


DEBUG = True
INSTALLED_APPS = Common.INSTALLED_APPS # noqa
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
# Site
# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ("gunicorn", )

# Mail
EMAIL_HOST = 'smtp.mailgun.com'
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Social
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True


# Celery
BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
