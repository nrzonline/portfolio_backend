from django.core.exceptions import ImproperlyConfigured
import os


DEVELOPMENT = 'development'
PRODUCTION = 'production'
TEST = 'test'

LOAD_SETTINGS = DEVELOPMENT


def raise_error_on_missing_settings_file(settings_file):
    settings_file_path = os.path.join(
        'portfolio_back', os.path.join('settings', '%s.py' % settings_file))

    if not os.path.exists(settings_file_path):
        raise ImproperlyConfigured(
            "Settings file '%s' does not exist" % settings_file_path)


raise_error_on_missing_settings_file('secret')
raise_error_on_missing_settings_file(LOAD_SETTINGS)
from .base import *

if LOAD_SETTINGS == DEVELOPMENT:
    from .development import *
elif LOAD_SETTINGS == TEST:
    from .test import *
elif LOAD_SETTINGS == PRODUCTION:
    from .production import *

