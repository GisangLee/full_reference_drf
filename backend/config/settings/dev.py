from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

THIRD_PARTY_APPS = ["debug_toolbar"] + THIRD_PARTY_APPS

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = ("127.0.0.1", "::1", "0.0.0.0")

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJ_APPS