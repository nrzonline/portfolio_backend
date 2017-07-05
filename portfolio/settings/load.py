from django.core.exceptions import ImproperlyConfigured
import os


def required_settings_files_exist(settings_files):
    for settings_file in settings_files:
        settings_file_path = os.path.join('settings', '%s.py' % settings_file)
        settings_file_path_from_root = os.path.join('portfolio', settings_file_path)

        if not os.path.exists(settings_file_path_from_root):
            raise ImproperlyConfigured(
                "Settings file '%s' does not exist" % settings_file_path_from_root)
    return True


DEVELOPMENT = 'development'
PRODUCTION = 'production'
TEST = 'test'

LOAD_SETTINGS = DEVELOPMENT

settings_files_to_load = [
    'secret',
    LOAD_SETTINGS
]

if required_settings_files_exist(settings_files_to_load):
    from .base import *

if LOAD_SETTINGS == DEVELOPMENT:
    from .development import *
elif LOAD_SETTINGS == TEST:
    from .test import *
elif LOAD_SETTINGS == PRODUCTION:
    from .production import *

