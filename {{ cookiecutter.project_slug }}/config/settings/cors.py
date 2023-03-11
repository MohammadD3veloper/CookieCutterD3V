# Cors configurations
CORS_ALLOWED_ORIGINS = [
    f"http://{DOMAIN_NAME}",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

CSRF_TRUSTED_ORIGINS = [
    f"http://{DOMAIN_NAME}",
    "http://localhost:8000",
    "http://127.0.0.1:9000",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
