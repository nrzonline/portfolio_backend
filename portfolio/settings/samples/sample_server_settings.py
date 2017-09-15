from portfolio.settings import secret
from django.conf import settings
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

""" PRODUCTION SUGGESTIONS

DEBUG = FALSE

RAVEN_CONFIG = {
    'dsn': secret.SECRET_RAVEN_DNS,
}

REST_FRAMEWORK = settings.REST_FRAMEWORK + {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

STATIC_ROOT = "/public_html/static/"
"""
