from .base import *


# Debug should be False in production mode
DEBUG = env("SETTINGS_DEBUG")


# Allowed hosts (Set your domain here)
ALLOWED_HOSTS = [DOMAIN_NAME, f"www.{DOMAIN_NAME}"]


{%- if cookiecutter.use_prometheus != "n" %}
# Database with postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django_prometheus.db.backends.postgresql',
        'NAME': BASE_DIR / 'db.sqlite3',
        'HOST': env('POSTGRESQL_HOST'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASSWORD'),
        'PORT': env('POSTGRESQL_PORT'),
    },
}


# Caching with redis
CACHES = {
    'default': {
        'BACKEND': 'django_prometheus.cache.backends.redis.RedisCache',
        'LOCATION': env("REDIS_URL"),
    }
}
{%- else %}
# Database with postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRESQL_NAME'),
        'HOST': env('POSTGRESQL_HOST'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASSWORD'),
        'PORT': env('POSTGRESQL_PORT'),
    },
}


# Caching with redis
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env("REDIS_URL"),
    }
}
{%- endif %}

CACHE_TTL = 60 * 15

{%- if cookiecutter.use_logging_system != "n" %}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'log/{{ cookiecutter.project_slug }}.log',
            'formatter': 'app',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
    'formatters': {
        'app': {
            'format': [
                "%(asctime)s:[%(levelname)-8s]" "(%(module)s.%(funcName)s): %(message)s"
            ],
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    }
}

{%- endif %}