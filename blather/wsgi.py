"""
WSGI config for blather project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blather.settings")
sys.path.append('/var/www/geoffcox77.com/blather/blat/')
sys.path.append('/var/www/geoffcox77.com/blather/rockmeout/')
sys.path.append('/var/www/geoffcox77.com/blather/')

application = get_wsgi_application()
