from djangoappengine.settings_base import *

import os

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

LANGUAGE_CODE = 'ru'

USE_I18N = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'markup_deprecated',
    'djangotoolbox',
    'djangoappengine',
    'captcha',
    'mathfilters',
    'myfilter',
    'filetransfers',
    'upload',
    'my',
    'mynews',
    'posts',
    'songs',
    'books',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',    
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

LOGIN_REDIRECT_URL = '/'

PROJECT_ROOT = os.path.dirname(__file__)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

ROOT_URLCONF = 'urls'

DEBUG = False

ALLOWED_HOSTS = '*'
