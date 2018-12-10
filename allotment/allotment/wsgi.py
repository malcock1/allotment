"""
WSGI config for allotment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "allotment.settings")

application = get_wsgi_application()

# This application object is used by the development server
# as well as any WSGI server configured to use this file.
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()