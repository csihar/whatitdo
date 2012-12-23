# Django settings for whatitdo project.
import os

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('kyle', 'ksanderspdx@gmail.com'),
)

MANAGERS = ADMINS

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'whatitdo.bot@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] #'w4t1td0b0t'

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
        'PASSWORD': 'w4t1td0',
        'HOST': '',
        'PORT': '',
    }
}

# Amazon S3 settings for static and media files
AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID'] #'AKIAJ7PXE26XGHMH4RUQ'
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY'] #'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'
AWS_STORAGE_BUCKET_NAME = 'whatitdo'
AWS_S3_FILE_OVERWRITE = True
AWS_LOCATION = '/media'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = 'http://s3.amazonaws.com/whatitdo/media/'
STATIC_URL = 'http://s3.amazonaws.com/whatitdo/static/'
MEDIA_ROOT = '/media/'
STATIC_ROOT = '/static/'

STATICFILES_DIRS = (
    '/static/',
)

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
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
    'easy_thumbnails',
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
DATABASES['default'] =  dj_database_url.config()



# Settings defined in environment variables:
# EMAIL_HOST_PASSWORD
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY
