"""Settings khi chạy pytest."""

# ruff: noqa: F403, F405
from .base import *

DEBUG = False

# Hash mật khẩu chuẩn (PBKDF2, 1.000.000 vòng lặp) cố ý chậm để chống dò mật khẩu.
# Trong test ta tạo hàng trăm user, nên dùng MD5 cho nhanh. CHỈ dùng trong test!
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Email lưu trong bộ nhớ (django.core.mail.outbox) để test kiểm tra được.
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"