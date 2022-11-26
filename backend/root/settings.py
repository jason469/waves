import os
from datetime import timedelta
from pathlib import Path

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
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend.api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.root.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
        'NAME': os.environ.get('DB_NAME', 'postgres'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
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


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
