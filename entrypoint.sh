#!/bin/sh

set -e

./manage.py migrate
./manage.py collectstatic --noinput
# newrelic-admin run-program gunicorn --bind 0.0.0.0:8000 --access-logfile - src.wsgi:application
gunicorn --bind 0.0.0.0:8000 --access-logfile - src.wsgi:application

