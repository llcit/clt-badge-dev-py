"""
Django settings for badges project.

This application is the upgrade version from django 1.7.x on python 2.7
to Django 1.11.x on Python 3.6.x

For more information on this file, see 
https://github.com/llcit/clt-analytics-dev-py
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from configparser import RawConfigParser
config = RawConfigParser()

#Copy the server.conf.eaxmple to server.conf and add server's information
config.read(os.path.join(BASE_DIR,'badgeproject/settings/server.conf'))

# Secret key stored in your local environment variable not here.
SECRET_KEY = config.get('secrets', 'SECRET_KEY')

"""
Use the DEBUG option to check it is production or not
If the DEBUG is True, then it is not production server.
Check and configure the debug section of 'server.conf' file correctly.
"""
DEBUG = config.get('debug', 'DEBUG')

ALLOWED_HOSTS = [config.get('hosts', 'HOST1'),]

SITE_ROOT = config.get('site', 'SITE_ROOT')
SITE_HOST = config.get('site', 'SITE_HOST')

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_cas_ng',
    'crispy_forms',
    'braces',
    'badge_site',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'badgeproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # Added to allow access to SITE_ROOT parameter in templates
                'badgeproject.context_processors.site_root',
            ],
        },
    },
]

WSGI_APPLICATION = 'badgeproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   os.path.join(BASE_DIR,'badgeproject/cltbadgedb'),
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
TIME_ZONE = 'Pacific/Honolulu'

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Project staticfiles directory
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/cltbadgesite'),]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

ISSUER_REPO = 'badge-docs/issuer'
BADGES_REPO = 'badge-docs/badges'
AWARDS_REPO = 'badge-docs/earned'
REVOKE_REPO = 'badge-docs/revoke'

STATIC_URL = '/static/cltbadgesite/'
MEDIA_URL = '/media/cltbadgesite/'

STATIC_ROOT = config.get('static_root', 'STATIC_ROOT')
MEDIA_ROOT = config.get('static_root', 'MEDIA_ROOT')

EMAIL_HOST = config.get('email', 'EMAIL_HOST')
EMAIL_PORT = config.get('email', 'EMAIL_PORT')
EMAIL_HOST_USER = config.get('email', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('email', 'EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config.get('email', 'EMAIL_USE_TLS')

# NEXT THREE LINES ENABLE CAS LOGIN AT UH
LOGIN_URL = os.path.join(SITE_ROOT,'/accounts/login/')
LOGOUT_URL = os.path.join(SITE_ROOT,'/logout')
LOGIN_REDIRECT_URL = SITE_ROOT
CAS_SERVER_URL = config.get('cas', 'CAS_SERVER_URL')
CAS_REDIRECT_URL = config.get('cas', 'CAS_REDIRECT_URL')
CAS_VERSION = config.get('cas', 'CAS_VERSION')

