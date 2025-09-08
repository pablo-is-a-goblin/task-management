#!/bin/sh

# migrations
python3 /django/manage.py makemigrations tasks
python3 /django/manage.py makemigrations
python3 /django/manage.py migrate

celery -A config worker -l info &

# run server
exec python3 /django/manage.py runserver 0.0.0.0:${BACKEND_PORT}