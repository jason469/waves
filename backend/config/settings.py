import os
import dj_database_url

from pathlib import Path

from django.contrib import messages
from dotenv import load_dotenv
from django.urls import reverse_lazy

# load_dotenv("../env/dev.env")
# load_dotenv("../env/prod.env")

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', '0').lower() in ['true', 't', '1']
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', "").split(' ')

INTERNAL_IPS = [
    "localhost"
    "127.0.0.1",
]

PROJECT_NAME = "waves"

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
    'django_htmx',

    # Development
    'debug_toolbar'
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
    "backend.website.base.middleware.HtmxMessagesMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
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
    'default': dj_database_url.parse(os.getenv('DATABASE_URL')),
}

# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
#         'NAME': os.environ.get('DB_NAME', 'waves-db'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#         'USER': os.environ.get('DB_USER', 'waves-user'),
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

# Sets the minimum message level that will be recorded by the messages framework
MESSAGE_LEVEL = messages.DEBUG

# This sets the mapping of message level to message tag, which is typically rendered as a CSS class in HTML.
MESSAGE_TAGS = {
    messages.DEBUG: "bg-light",
    messages.INFO: "text-white bg-primary",
    messages.SUCCESS: "text-white bg-success",
    messages.WARNING: "text-dark bg-warning",
    messages.ERROR: "text-white bg-danger",
}


def show_toolbar(request):
    if DEBUG:
        return True
    else:
        return False


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}

try:
    from backend.api.settings import *
    from backend.website.base import *
    from backend.website.search import *
    from backend.website.playlist import *
except ImportError:
    raise Exception()
