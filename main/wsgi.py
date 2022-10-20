"""
WSGI config for main project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root="/static")
application.add_files("/static", prefix="more-files/")
/home/abbas/Workspace/django_blog/static