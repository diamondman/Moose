import os, sys

path = "/opt/Moose/"
sys.path.append(path)
sys.path.append(path+"moose/")
import moose.settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'moose.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()