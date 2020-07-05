import os
import sys

from src.config.common import * # noqa


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TESTING = sys.argv[1:2] == ['test']


# Testing
INSTALLED_APPS += ('django_nose', ) # noqa
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    BASE_DIR, '-s', '--nologcapture', '--with-coverage',
    '--with-progressive', '--cover-package=src'
]
