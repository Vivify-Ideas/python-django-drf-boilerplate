#!/bin/sh

set -e

celery -A src.config worker --loglevel=debug --concurrency=4
