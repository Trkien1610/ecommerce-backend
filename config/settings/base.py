"""
Cấu hình chung cho mọi môi trường (dev, test, prod).

Không dùng trực tiếp file này: dev.py / test.py / prod.py import nó rồi ghi đè
phần khác biệt. Mọi secret đều đọc từ biến môi trường (hoặc file .env).
"""

from pathlib import Path

import environ

# base.py nằm ở config/settings/base.py -> cần lùi 3 cấp để về thư mục gốc dự án.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
# Đọc file .env nếu có. Biến đã tồn tại trong hệ điều hành (ví dụ do Docker truyền vào)
# sẽ KHÔNG bị file .env ghi đè.
environ.Env.read_env(BASE_DIR / ".env")

# --- Bảo mật cơ bản --------------------------------------------------------
SECRET_KEY = env("SECRET_KEY")  # Bắt buộc, không có giá trị mặc định.
DEBUG = False  # An toàn mặc định; chỉ dev.py bật lên True.
ALLOWED_HOSTS: list[str] = []

# --- Ứng dụng ----------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "corsheaders",
]

LOCAL_APPS: list[str] = [
    # Các app trong apps/ sẽ được thêm dần từ Phase 3.
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Custom User model phải khai báo TRƯỚC lần migrate đầu tiên (Phase 3).
# AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # CorsMiddleware phải đứng trước CommonMiddleware để kịp gắn header CORS.
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --- Database -----------------------------------------------------------------
# Ví dụ: postgres://user:password@localhost:5432/dbname
DATABASES = {"default": env.db("DATABASE_URL")}
# Giữ kết nối DB tối đa 60 giây thay vì mở/đóng mới mỗi request.
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Mật khẩu -----------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- Ngôn ngữ & thời gian -----------------------------------------------------
LANGUAGE_CODE = "vi"
TIME_ZONE = "Asia/Ho_Chi_Minh"
USE_I18N = True
USE_TZ = True  # Lưu thời gian dạng UTC trong DB, hiển thị theo TIME_ZONE.

# --- File tĩnh & file upload -------------------------------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# --- CORS ---------------------------------------------------------------------
# Danh sách domain Frontend được phép gọi API, ví dụ http://localhost:3000
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])