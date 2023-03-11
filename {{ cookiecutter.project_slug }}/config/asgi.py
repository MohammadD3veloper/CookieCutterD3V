"""
ASGI config for {{ cookiecutter.project_slug }} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
{%- if cookiecutter.use_channels %}
from channels.routing import ProtocolTypeRouter


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.production')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
})

{%- else %}
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.django.production')

application = get_asgi_application()
{%- endif %}
