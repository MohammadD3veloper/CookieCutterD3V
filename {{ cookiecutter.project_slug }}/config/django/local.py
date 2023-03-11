from .base import *


# Debug should be True in local mode
DEBUG = True


# Allowed hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

{%- if cookiecutter.use_prometheus %}
# Database in local with Sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


# Local-Memory caching
CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
{%- else %}
# Database in local with Sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
}


# Local-Memory caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
{%- endif %}

CACHE_TTL = 60 * 15
