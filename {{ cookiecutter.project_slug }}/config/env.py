from django.conf import settings

from pathlib import Path

import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()


if env("SETTINGS_DEBUG") is True:
    env.read_env(os.path.join(BASE_DIR, '.env/.local.env'))
elif env("SETTINGS_DEBUG") is False:
    env.read_env(os.path.join(BASE_DIR, '.env/.production.env'))
