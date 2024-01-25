# ref: https://blog.devgenius.io/django-tailwind-setup-made-easy-36043adda97c

# First, we create a virtual environment
python -m venv venv

# Activate the environment

## windows
source venv/Scripts/activate

## linux
source venv/bin/activate

# Install Django
python -m pip install django

# Start project
django-admin startproject django_project .

# Create your app
python manage.py startapp main