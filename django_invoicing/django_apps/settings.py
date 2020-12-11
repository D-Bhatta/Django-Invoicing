"""
Django settings for django_apps project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path
from socket import gethostname

import django_heroku
import dotenv
from django_apps import utils

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Retrieve the environment variables
try:
    path_env = os.path.join(BASE_DIR.parent, ".env")
    dotenv.read_dotenv(path_env)
except (EnvironmentError, FileNotFoundError):
    print("Couldn't retrieve the environment variables")

try:
    path_env = os.path.join(BASE_DIR.parent, ".env")
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
except (KeyError, FileNotFoundError):
    path_env = os.path.join(BASE_DIR.parent, ".env")
    utils.generate_secret_key(path_env)
    dotenv.read_dotenv(path_env)
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Find out what environment we are running in
# Get the hostname
try:
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
    DJANGO_HOST_NAME = os.environ["DJANGO_HOST_NAME"]
    DBNAME = os.environ["DBNAME"]
    DBUSER = os.environ["DBUSER"]
    DBPASSWORD = os.environ["DBPASSWORD"]
    DBHOST = os.environ["DBHOST"]
    DBPORT = os.environ["DBPORT"]
    DBTEST = os.environ["DBTEST"]

except KeyError:
    path_env = os.path.join(BASE_DIR.parent, ".env")
    dotenv.read_dotenv(path_env)
    DJANGO_ENVIRONMENT = os.environ["DJANGO_ENVIRONMENT"]
    DJANGO_HOST_NAME = os.environ["DJANGO_HOST_NAME"]
    DBNAME = os.environ["DBNAME"]
    DBUSER = os.environ["DBUSER"]
    DBPASSWORD = os.environ["DBPASSWORD"]
    DBHOST = os.environ["DBHOST"]
    DBPORT = os.environ["DBPORT"]
    DBTEST = os.environ["DBTEST"]

if DJANGO_ENVIRONMENT == "PRODUCTION":
    ALLOWED_HOSTS = [
        DJANGO_HOST_NAME,
    ]
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "django_apps/static/django_apps"),
        # os.path.join(BASE_DIR, "django_invoicing/static/django_invoicing"),
    ]
    STATICFILES_STORAGE = (
        "whitenoise.storage.CompressedManifestStaticFilesStorage"
    )
elif DJANGO_ENVIRONMENT == "DEVELOPMENT":
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "django_apps\\static\\django_apps"),
        # os.path.join(BASE_DIR, "django_invoicing\\static\\django_invoicing"),
    ]
    ALLOWED_HOSTS = ["*"]
else:
    pass


# Application definition

INSTALLED_APPS = [
    "users",
    "django_invoicing",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_apps.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "django_apps/templates/"),
        ],  ## Add base templates directory
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_apps.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#
# Settings for PostgreSQL
#
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DBNAME,
        "USER": DBUSER,
        "PASSWORD": DBPASSWORD,
        "HOST": DBHOST,
        "PORT": DBPORT,
        "TEST": {
            "NAME": DBTEST,
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = "invoicing:home"

# LOGOUT_REDIRECT_URL = "dashboard"

# Keep this at the end

if DJANGO_ENVIRONMENT == "PRODUCTION":
    django_heroku.settings(locals())
