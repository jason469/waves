#!/usr/bin/env bash

set -o errexit  # exit on error
pip install --upgrade pip
pip install -r backend/requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py waves__createsuperuser