import os

from celery import Celery

from .env import env


# Set the default Django settings module for the 'celery' program.
if env("SETTINGS_DEBUG") is True:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.local')
elif env("SETTINGS_DEBUG") is False:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.production')


app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
