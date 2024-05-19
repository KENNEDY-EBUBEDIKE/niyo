#!/bin/bash

# Start Gunicorn for WSGI server
echo "Starting Gunicorn..."
gunicorn --bind 0.0.0.0:8000 --workers 3 config.wsgi:application &

# Start Daphne for ASGI server
echo "Starting Daphne..."
daphne -b 0.0.0.0 -p 8001 config.asgi:application