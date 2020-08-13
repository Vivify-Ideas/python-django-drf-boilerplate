from src.config.common import *  # noqa

# Testing
INSTALLED_APPS += ('django_nose', )  # noqa
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['-s', '--nologcapture', '--with-progressive', '--with-fixture-bundling']
