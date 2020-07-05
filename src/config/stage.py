from .common import * # noqa


INSTALLED_APPS = Common.INSTALLED_APPS # noqa

# Site
# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ("gunicorn", )

# Social
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
