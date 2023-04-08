from django.conf import settings

from pathlib import Path

import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

DEBUG = os.environ.get("DJANGO_DEBUG")

if DEBUG == "true":
    env.read_env(os.path.join(BASE_DIR, '.env/.local.env'))
elif DEBUG == "false":
    env.read_env(os.path.join(BASE_DIR, '.env/.production.env'))
