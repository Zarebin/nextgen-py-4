#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput
python manage.py populate_db food_compare 
python manage.py populate_db food_fact
python manage.py populate_db food_labeler
python manage.py populate_db image_caption
python manage.py populate_db sentiment
python manage.py populate_db translation_vlidator
