"""
Django settings for clt badge project.

"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from unipath import Path
PROJECT_DIR = Path(__file__).ancestor(3)  # Points to <repository root>

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_cas_ng',
    #'uhauth',
    'crispy_forms',
    'braces',
    'badge_site',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# CAS
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)
# set CAS SERVER FIRST
CAS_SERVER_URL = ''
# set CAS VERSION: default is CAS2
CAS_VERSION = 'CAS_2_SAML_1_0'
# set redirection after login
CAS_REDIRECT_URL = ''

ROOT_URLCONF = 'badgeproject.urls'

WSGI_APPLICATION = 'badgeproject.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Pacific/Honolulu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

TEMPLATE_DIRS = (PROJECT_DIR.child('templates'),)


CRISPY_TEMPLATE_PACK = 'bootstrap3'

ISSUER_REPO = 'badge-docs/issuer'
BADGES_REPO = 'badge-docs/badges'
AWARDS_REPO = 'badge-docs/earned'
REVOKE_REPO = 'badge-docs/revoke'
