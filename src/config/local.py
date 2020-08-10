import sys
from src.config.common import *  # noqa

TESTING = sys.argv[1:2] == ['test']

# Testing
INSTALLED_APPS += ('django_nose', )  # noqa
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['-s', '--nologcapture', '--with-progressive', '--with-fixture-bundling']
