import os
import json

from datetime import timedelta
from pathlib import Path
from dotenv import dotenv_values, load_dotenv
from django.urls import reverse_lazy

load_dotenv("../env/dev.env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-c4d(@251p0j9wkiqle^r976*xnq3&ed(+qpcp)#@-=t=j+2q6!')

DEBUG = os.environ.get('DEBUG_MODE', True)

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', "localhost").split(" ")

PROJECT_NAME = "PROJECT NAME"

FASTAPI_ROOT_PATH = os.environ.get('FASTAPI_ROOT_PATH', '')

AUTH_JWT_SECRET_KEY = os.environ.get("AUTH_JWT_SECRET_KEY", SECRET_KEY)
AUTH_JWT_ACCESS_EXPIRY = timedelta(minutes=int(os.environ.get("AUTH_JWT_ACCESS_EXPIRY_MINUTES", 30)))
AUTH_JWT_REFRESH_EXPIRY = timedelta(days=int(os.environ.get("AUTH_JWT_REFRESH_EXPIRY_DAYS", 1)))

INSTALLED_APPS = [

    # Default apps installed by Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # FastAPI
    'backend.api',

    # Django Website
    'backend.website.base',
    'backend.website.playlist',
    'backend.website.search',

    'widget_tweaks',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'website/templates')],
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

WSGI_APPLICATION = 'backend.config.asgi.application'
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
        'NAME': os.environ.get('DB_NAME', 'music-app'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
        'USER': os.environ.get('DB_USER', 'music-app-user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'T47CGcJXj40ME0pHs'),
    }

}

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_LOCATION = f"{REDIS_HOST}:{REDIS_PORT}"

AUTH_CACHE_NAME = 'auth'
AUTH_CACHE_DATABASE = '1'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis:{REDIS_LOCATION}/0',
    },
    AUTH_CACHE_NAME: {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis:{REDIS_LOCATION}/{AUTH_CACHE_DATABASE}',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # Uncomment in production

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = reverse_lazy('website__base:index')
LOGOUT_REDIRECT_URL = reverse_lazy('website__base:login')