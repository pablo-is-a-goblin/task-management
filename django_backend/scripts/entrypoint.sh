#!/bin/sh

exec python3 /django/manage.py runserver 0.0.0.0:${BACKEND_PORT}