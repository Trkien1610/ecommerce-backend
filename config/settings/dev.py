"""Settings cho máy lập trình viên. KHÔNG dùng trên server."""

# ruff: noqa: F403, F405
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Dev cho mọi Frontend local gọi API, khỏi khai báo từng cổng.
CORS_ALLOW_ALL_ORIGINS = True

# Email in ra terminal thay vì gửi thật.
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"    