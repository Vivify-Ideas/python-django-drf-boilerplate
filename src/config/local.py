from src.config.common import *  # noqa

# Testing
INSTALLED_APPS += ('django_nose',)  # django_nose is a third-party Django test runner and Nose plugin that provides additional features and improvements over Django's built-in test runner.
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['-s', '--nologcapture', '--with-progressive', '--with-fixture-bundling']
