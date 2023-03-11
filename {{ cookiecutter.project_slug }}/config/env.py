from django.conf import settings

from pathlib import Path
import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()

if settings.DEBUG:
    env.read_env(BASE_DIR / '.env/.local.env')
else:
    env.read_env(BASE_DIR / '.env/production.env')
