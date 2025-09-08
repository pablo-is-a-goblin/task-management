#!/bin/sh

# migrations
python3 /django/manage.py makemigrations tasks
python3 /django/manage.py makemigrations
python3 /django/manage.py migrate

# celery
celery -A config worker -l info &
celery -A config beat &

# run server
exec python3 /django/manage.py runserver 0.0.0.0:${BACKEND_PORT}