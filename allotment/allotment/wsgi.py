"""
WSGI config for allotment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
"""
import os, sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "allotment.settings")

django.setup()


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""

# The following taken from http://mainlydata.kubadev.com/python/django/django-and-heroku-getting-it-working/
import os, sys

#Allows us to see useful stuff in Gunicorn output
sys.stdout = sys.stderr

#Rely upon env var 'DYNO` to determine if we are
#running within Heroku
if 'DYNO' in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "allotment.settings_heroku")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "allotment.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
