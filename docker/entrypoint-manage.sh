#!/bin/bash

set -e

./manage.py migrate
./manage.py collectstatic --noinput

exec tail -f /dev/null