# Django settings for whatitdo project.
import os
from localsettings import *

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('kyle', 'ksanderspdx@gmail.com'),
)
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

MEDIA_ROOT = '/media/'
STATIC_ROOT = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'abtg(xgidmdcnq!k3+8d)gi&amp;o%so!3$0x(0n-c)r_+@0y-s^(#'

# List of callables that know how to import templates from various sources.
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

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'whatitdo.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'C:/www/whatitdo/templates',
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

APPEND_SLASH = True

LOGIN_URL = '/accounts/login/'
AUTH_PROFILE_MODULE = 'items.userprofile'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

# Settings defined in localsettings:
#	EMAIL_USE_TLS = 
#	EMAIL_HOST = ''
#	EMAIL_PORT = 
#	EMAIL_HOST_USER = ''
#	EMAIL_HOST_PASSWORD = ''
#
#	DATABASES = {
#	    'default': {
#	        'ENGINE': '',                    # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#	        'NAME': '',                      # Or path to database file if using sqlite3.
#	        'USER': '',                      # Not used with sqlite3.
#	        'PASSWORD': '',                  # Not used with sqlite3.
#	        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#	        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#	    }
#	}
#	
#	AWS_QUERYSTRING_AUTH = 
#	AWS_ACCESS_KEY_ID = ''
#	AWS_SECRET_ACCESS_KEY = ''
#	AWS_STORAGE_BUCKET_NAME = ''
#	AWS_S3_FILE_OVERWRITE = 
#	AWS_LOCATION = ''
#	
#	STATICFILES_STORAGE = ''
#	DEFAULT_FILE_STORAGE = ''
#	MEDIA_URL = ''
#	STATIC_URL = ''
