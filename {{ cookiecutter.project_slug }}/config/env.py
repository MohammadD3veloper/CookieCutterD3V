from pathlib import Path
import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()


env.read_env(BASE_DIR / '.env/.local.env')