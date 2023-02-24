import os
import dj_database_url

from pathlib import Path
from dotenv import load_dotenv
from django.urls import reverse_lazy

# load_dotenv("../env/dev.env")
load_dotenv("../env/prod.env")

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', "").split(' ')

PROJECT_NAME = "music-app"

INSTALLED_APPS = [
    # Default apps installed by Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # API
    'rest_framework',
    'backend.api',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',

    # Django Website
    'backend.website.base',
    'backend.website.playlist',
    'backend.website.search',

    'widget_tweaks',
    'django_extensions',
    'django_htmx'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
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

WSGI_APPLICATION = 'backend.config.wsgi.application'

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')),
}
# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
#         'NAME': os.environ.get('DB_NAME', 'music-app'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#         'USER': os.environ.get('DB_USER', 'music-app-user'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'T47CGcJXj40ME0pHs'),
#     }
# }

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
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # Uncomment in production

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = reverse_lazy('website__base:login')
LOGIN_REDIRECT_URL = reverse_lazy('website__base:index')
LOGOUT_REDIRECT_URL = reverse_lazy('website__base:login')

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')
REDIS_LOCATION = f"{REDIS_HOST}:{REDIS_PORT}"

try:
    from backend.api.settings import *
    from backend.website.base import *
    from backend.website.search import *
    from backend.website.playlist import *
except ImportError:
    raise Exception()
