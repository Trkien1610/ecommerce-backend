"""Settings cho server production. Hoàn thiện thêm ở Phase 13."""

# ruff: noqa: F403, F405
from .base import *

DEBUG = False

# Bắt buộc khai báo domain thật, ví dụ: api.myshop.vn
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[])

# Chạy sau Nginx có HTTPS: tin header X-Forwarded-Proto do Nginx gửi vào.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS: bắt trình duyệt luôn dùng HTTPS. Để 0 cho đến khi HTTPS chạy ổn định.
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=0)