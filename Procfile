release: python manage.py migrate
web: gunicorn allotment.wsgi:application --pythonpath ./allotment --log-file -

