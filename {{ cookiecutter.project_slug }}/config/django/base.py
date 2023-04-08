"""
Django settings for {{ cookiecutter.project_slug }} project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from config.env import BASE_DIR, env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# website domain name
DOMAIN_NAME = env("DOMAIN_NAME")


# DEBUG
DEBUG = env("SETTINGS_DEBUG")

# Application definition
LOCAL_APPS = [
    "{{ cookiecutter.project_slug }}.authentication.apps.AuthenticationConfig",
    "{{ cookiecutter.project_slug }}.core.apps.CoreConfig",
    "{{ cookiecutter.project_slug }}.utils.apps.UtilsConfig",
]

THIRD_PARTY_APPS = [
    {%- if cookiecutter.use_celery != "n" %}
    "django_celery_results",
    "django_celery_beat",
    {%- endif %}
    {%- if cookiecutter.api_framework == "RestFramework" %}
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "corsheaders",
    {%- elif cookiecutter.api_framework == "GrapheneDjango" %}
    "graphene_django",
    {%- elif cookiecutter.api_framework == "DjangoGrpcFramework" %}
    "django_grpc_framework",
    {%- elif cookiecutter.api_framework == "BasicHTML" %}
    "django-crispy-forms",
    "crispy-bootstrap5",
    {%- endif %}
    {%- if cookiecutter.use_debug_toolbar %}
    "debug_toolbar",
    {%- endif %}
    {%- if cookiecutter.use_prometheus != "n" %}
    "django_prometheus",
    {%- endif %}
    "docs",
]


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    {%- if cookiecutter.use_channels != "n" %}
    "daphne",
    {%- endif  %}
    'django.contrib.staticfiles',
]


INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    {%- if cookiecutter.use_prometheus != "n" %}
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    {%- endif %}
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    {%- if cookiecutter.api_framework == "RestFramework" %}
    'corsheaders.middleware.CorsMiddleware',
    {%- endif %}
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    {%- if cookiecutter.use_debug_toolbar != "n" %}
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    {%- endif %}
    {%- if cookiecutter.use_prometheus != "n" %}
    'django_prometheus.middleware.PrometheusAfterMiddleware',    
    {%- endif %}
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Wsgi application declaration
WSGI_APPLICATION = 'config.wsgi.application'


{%- if cookiecutter.use_channels != "n" %}
# ASGI Application declaration
ASGI_APPLICATION = 'config.asgi.application'

{%- endif %}


# Custom authentication user model
AUTH_USER_MODEL = "authentication.User"


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
{%- if cookiecutter.use_persian_django != "n" %}
LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True
{%- else %}
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
{%- endif %}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static/'

STATICFILES_DIR = [
    BASE_DIR / 'static/'
]


# Media files (Uploaded Images, Uploaded files)
MEDIA_ROOT = 'media/'
MEDIA_URL = 'media/'


# Documents Root
DOCS_ROOT = "documents/build/html/"
DOCS_ACCESS = "superuser"


{%- if cookiecutter.use_debug_toolbar != "n" %}
INTERNAL_IPS = [
    "127.0.0.1",
]
{%- endif %}
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

{%- if cookiecutter.api_framework == "RestFramework" %}
# Rest Framework Settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

{%- elif cookiecutter.api_framework == "DjangoGrpcFramework" %}
GRPC_FRAMEWORK = {
    'ROOT_HANDLERS_HOOK': 'config.urls.grpc_handlers',
}

{%- elif cookiecutter.api_framework == "GrapheneDjango" %}
# Graphene & GrapheneJWT Configurations
AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

GRAPHENE = {
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
    "ATOMIC_MUTATIONS": True,
}

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_ALLOW_ANY_CLASSES": [
            "graphql_auth.mutations.Register",
            "graphql_auth.mutations.VerifyAccount",
            "graphql_auth.mutations.ResendActivationEmail",
            "graphql_auth.mutations.SendPasswordResetEmail",
            "graphql_auth.mutations.PasswordReset",
            "graphql_auth.mutations.ObtainJSONWebToken",
            "graphql_auth.mutations.VerifyToken",
            "graphql_auth.mutations.RefreshToken",
            "graphql_auth.mutations.RevokeToken",
            "graphql_auth.mutations.VerifySecondaryEmail",
        ],
    # optional
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
}
{%- endif %}


# You can remove the files from settings if you dont need them.
{%- if cookiecutter.use_celery != "n" %}
from config.settings.celery import *
{%- endif %}
{%- if cookiecutter.api_framework != "RestFramework" %}
from config.settings.cors import *
from config.settings.spectacular import *
{%- endif %}
from config.settings.email import *
{%- if cookiecutter.use_prometheus != "n" %}
from config.settings.prometheus import *
{%- endif %}
