from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Secret Key (production-க்கு change செய்யலாம் later in environment variables)
SECRET_KEY = 'django-insecure-change-me-please'

# ⚙️ Debug off in production
DEBUG = False

# 🌐 Allow Render & localhost
ALLOWED_HOSTS = ['*']

# ✅ CSRF trusted origins (Render domain)
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']

# 📦 Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wasteapp',
]

# 🧱 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌍 Project URLs
ROOT_URLCONF = 'smartwaste.urls'

# 🎨 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'wasteapp' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 WSGI
WSGI_APPLICATION = 'smartwaste.wsgi.application'

# 🗃 Database (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔒 Password validators (optional)
AUTH_PASSWORD_VALIDATORS = []

# 🌏 Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# 📁 Static files setup (for Render)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'wasteapp' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 📸 Media files (optional, if you plan to upload images)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🔑 Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'