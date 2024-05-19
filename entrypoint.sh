#!/bin/bash


# Run database migrations
echo "Creating migrations..."
python3 manage.py makemigrations

# Run database migrations
echo "Applying migrations..."
python3 manage.py migrate

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Start Gunicorn for WSGI server
echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application &

# Start Daphne for ASGI server
echo "Starting Daphne..."
daphne -b 0.0.0.0 -p 8001 config.asgi:application