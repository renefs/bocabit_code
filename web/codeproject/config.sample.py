import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'O\xe2\xfcg\x87F\x16\x14\xadQ\xdf\xd5\xfaP7\xf3\xb5\xb0\xc6#\x16\x8c\xdd%'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ["SOCIAL_AUTH_GOOGLE_OAUTH2_KEY"]
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ["SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET"]

LOG_DEBUG_PATH = os.environ["LOG_DEBUG_PATH"]

ALLOWED_HOSTS = []

DEBUG = False

STATIC_ROOT = '../static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
