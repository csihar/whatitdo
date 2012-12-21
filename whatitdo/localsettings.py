ADMINS = (
    ('kyle', 'ksanderspdx@gmail.com'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'whatitdo.bot@gmail.com'
EMAIL_HOST_PASSWORD = 'w4t1td0b0t'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wid_db',                      # Or path to database file if using sqlite3.
        'USER': 'whatitdo',                      # Not used with sqlite3.
        'PASSWORD': 'w4t1td0',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = 'AKIAJ7PXE26XGHMH4RUQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'whatitdo'
AWS_S3_FILE_OVERWRITE = True
AWS_LOCATION = '/media'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = 'http://s3.amazonaws.com/whatitdo/media/'
STATIC_URL = 'http://s3.amazonaws.com/whatitdo/static/'
