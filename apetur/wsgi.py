"""
WSGI config for apetur project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import sys
sys.path.append('/home/ubuntu/django/apetur')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apetur.settings")

application = get_wsgi_application()
