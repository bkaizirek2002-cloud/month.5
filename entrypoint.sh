#!/bin/sh
python manage.py runserver makemigrations  
python manage.py runserver migrate 
python manage.py collectstatic --noinput
exec gunicorn shop_api.wsgi:application --bind 0.0.0.0:8000

