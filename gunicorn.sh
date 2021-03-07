#!/bin/sh
#gunicorn --chdir app main:app -w 2 --threads 2 -b 0.0.0.0:8000
gunicorn 'app.main:create_app("dev")' --workers 4 -b 0.0.0.0:8000