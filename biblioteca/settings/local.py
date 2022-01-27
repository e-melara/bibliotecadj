import os
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbbiblioteca',
        'USER': 'postgres',
        'PASSWORD': 'Godmylove061990@',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

STATIC_URL = '/static/'

DEBUG = True

ALLOWED_HOSTS = []
