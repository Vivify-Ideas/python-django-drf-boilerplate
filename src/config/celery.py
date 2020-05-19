from __future__ import absolute_import

import os
import sys
import dotenv

from celery import Celery
from django.conf import settings

TESTING = sys.argv[1:2] == ['test']
if not TESTING:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dotenv.read_dotenv(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.local")

app = Celery('src.config')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# tasks can be added below
