# Django settings for whatitdo project.
import os
try:
    from localsettings import *
except ImportError:
    pass

# Settings defined in environment variables:
# EMAIL_HOST_PASSWORD
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY
# AWS_STORAGE_BUCKET_NAME
#   (local development)
#   DEBUG
#   DB_PASSWORD
#   (only for local development on Mac):
#   PGHOST = localhost

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

DEBUG = bool(os.environ.get('DEBUG', False))

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('kyle', 'ksanderspdx@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['whatitdo.herokuapp.com']
if DEBUG:
    ALLOWED_HOSTS = ['']

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'whatitdo.bot@gmail.com'
try:
    EMAIL_HOST_PASSWORD
except NameError:
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']


TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Local database settings for dev. Overridden by Heroku db settings at bottom.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wid_db',
        'USER': 'whatitdo',
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': '',
        'PORT': '5432',
    }
}

# Amazon S3 settings for static and media files
AWS_QUERYSTRING_AUTH = False
try:
    AWS_ACCESS_KEY_ID
except NameError:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
try:
    AWS_SECRET_ACCESS_KEY
except NameError:
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
try:
    AWS_STORAGE_BUCKET_NAME
except NameError:
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_FILE_OVERWRITE = True
AWS_LOCATION = '/media'

STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
STATIC_S3_PATH = 'static'
DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = 'media'
MEDIA_URL = '//s3.amazonaws.com/{}/media/'.format(AWS_STORAGE_BUCKET_NAME)
STATIC_URL = '//s3.amazonaws.com/{}/static/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_ROOT = '/{}/'.format(DEFAULT_S3_PATH)
STATIC_ROOT = '/{}/'.format(STATIC_S3_PATH)

STATICFILES_DIRS = (
    'whatitdo/static/',
)

#switches to local static files during development
if DEBUG == True:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'static'),)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'abtg(xgidmdcnq!k3+8d)gi&amp;o%so!3$0x(0n-c)r_+@0y-s^(#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'whatitdo.urls'

WSGI_APPLICATION = 'whatitdo.wsgi.application'

TEMPLATE_DIRS = (
	os.path.join(SITE_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'registration',
    'storages',
    's3_folder_storage',
    'easy_thumbnails',
    'tastypie',
    'south',
    'items',
    'whatitdo',
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


APPEND_SLASH = True

LOGIN_URL = '/accounts/login/'

AUTH_PROFILE_MODULE = 'items.userprofile'

# -- Heroku database setting: ---
# Parse database configuration from $DATABASE_URL
import dj_database_url
try:  
   if os.environ['DATABASE_URL']:
        DATABASES['default'] =  dj_database_url.config()
except KeyError: 
   pass

