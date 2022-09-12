#!/bin/bash 

python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py populate_db food_compare 
python manage.py populate_db food_fact
python manage.py populate_db food_labeler
python manage.py populate_db image_caption
python manage.py populate_db sentiment
python manage.py populate_db translation_validator

python manage.py runserver 0.0.0.0:8000