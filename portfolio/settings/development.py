from portfolio.settings import secret
from django.conf import settings
import raven
import sys
import os


globals().update(vars(sys.modules['portfolio.settings.base']))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(settings.BASE_DIR, 'db.sqlite3'),
        'USER': secret.DB_USER,
        'PASSWORD': secret.DB_PASSWORD,
        'HOST': secret.DB_HOST,
        'PORT': secret.DB_PORT,
    }
}

RAVEN_CONFIG = {
    'dsn': secret.SECRET_RAVEN_DNS,
}
