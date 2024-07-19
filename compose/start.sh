#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

# migrate
python manage.py migrate

# collect static files
python manage.py collectstatic --no-input

# run app
uvicorn adventure_time.asgi:application --host 0.0.0.0 --reload --reload-include '*.py,*.html,*.css'
