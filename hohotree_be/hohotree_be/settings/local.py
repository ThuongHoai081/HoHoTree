"""
Settings for local development environment.
"""

from .common import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

DEBUG = True

SECRET_KEY = "django-insecure-*$0b8ibx7uzk45cm+fxw7*jj(yzi2ye!l4+!dnyxa-u-nbuz=q"

ALLOWED_HOSTS = ["*"]

HOST = "http://localhost:8000/"

# Database
SUPABASE_URL = "https://kyyiekngpfhpoldvlpmq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt5eWlla25ncGZocG9sZHZscG1xIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM2ODc3NDcsImV4cCI6MjA1OTI2Mzc0N30.SMAfUS7bQ1IyZh54WdJH0mxFEX61LOhsDRq43cDKLDo"


# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "boilerplate",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hohotree',
        'USER': 'root',
        'PASSWORD': '', 
        'HOST': 'localhost',    
        'PORT': '3306', 
    }
}


# CORS
CORS_ALLOWED_ORIGINS = ["http://localhost:8000"]

# Logging
# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "{levelname} {asctime} {filename}:{lineno} >>> {message}",
#             "style": "{",
#         },
#         "simple": {
#             "format": "{levelname} {message}",
#             "style": "{",
#         },
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             "formatter": "verbose",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "INFO",
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": "INFO",
#             "propagate": False,
#         },
#         "django.db": {
#             # database level logging
#             "level": "DEBUG"
#         },
#     },
# }