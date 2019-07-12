# development.py & __development.py

from .base import *

# import os

DEBUG = True

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEBUG_TOOLBAR_CONFIG = {
#     'JQUERY_URL': '',
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

