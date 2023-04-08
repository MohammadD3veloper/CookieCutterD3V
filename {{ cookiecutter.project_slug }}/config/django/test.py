from .base import *


# Debug should be True in local mode
DEBUG = env("SETTINGS_DEBUG")


# Allowed hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


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
        'BACKEND': 'django.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

CACHE_TTL = 60 * 15
