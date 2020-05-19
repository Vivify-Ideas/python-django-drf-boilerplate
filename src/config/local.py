import os
import sys

from src.config.common import * # noqa
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TESTING = sys.argv[1:2] == ['test']

DEBUG = True

# Testing
INSTALLED_APPS += ('django_nose', ) # noqa
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    BASE_DIR, '-s', '--nologcapture', '--with-coverage',
    '--with-progressive', '--cover-package=src'
]

# Mail
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Celery
BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
