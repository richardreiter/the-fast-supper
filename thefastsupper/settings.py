"""
Django settings for thefastsupper project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""

from pathlib import Path
import os
import dj_database_url
# import messages to assign tags to them
from django.contrib.messages import constants as messages
# env.py not in production, conditional below to avoid app throwing an error.
if os.path.isfile('env.py'):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')  # templates loc


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')  # environment variable

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# heroku and local host
ALLOWED_HOSTS = ['the-fast-supper.herokuapp.com', 'localhost']

# to prevent 500 errors when login on deployed site
ACCOUNT_EMAIL_VERIFICATION = 'none'

"""
Many thanks to Matt Rudge and CI's 'I Think Therefore I Blog'
Walkthrough project - a great reference, inspiration and example:
https://github.com/Code-Institute-Solutions/Django3blog
"""
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',  # allauth package
    'allauth.account',  # allauth package
    'allauth.socialaccount',  # allauth package
    'cloudinary_storage',  # cloudinary library
    'django.contrib.staticfiles',
    'cloudinary',  # cloudinary library
    'django_summernote',  # summernote library
    'crispy_forms',  # crispy forms package
    'fastblog',
]

# to handle multiple sites using one db
SITE_ID = 1

# redirect to home when login/out
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# tags for bootstrap classes to indicate category of message
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# crispy to use bootstrap classes for formatting
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'thefastsupper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],  # point to templates var
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

WSGI_APPLICATION = 'thefastsupper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    # Get DB env var from env/Heroku
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# from cloudinary lib
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
# static files directories
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# unused, written for good practice
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
