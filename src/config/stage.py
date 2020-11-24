from .common import * # noqa


# Site
# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ("gunicorn", ) # noqa

# Social
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
