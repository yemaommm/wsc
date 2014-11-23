"""
WSGI config for wsc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
# import sys

# # #Calculate the path based on the location of the WSGI script.
# apache_configuration= os.path.dirname(__file__)
# project = os.path.dirname(apache_configuration)
# workspace = os.path.dirname(project)
# sys.path.append(workspace)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
