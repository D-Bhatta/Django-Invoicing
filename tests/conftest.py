from os import path, remove
from pathlib import Path
from shutil import copy, rmtree

import dotenv
from django_apps.utils import get_logger

lg = get_logger()

# Build paths inside the project like this: PROJ_DIR / 'subdir'.
PROJ_DIR = Path(__file__).resolve().parent.parent


def pytest_configure():
    # Copy the template files which pytest can't see
    copy(
        "django_invoicing/django_apps/templates/base.html",
        "django_invoicing/django_invoicing/templates/",
    )
    # Set test env vars
    try:
        path_env = path.join(PROJ_DIR, "env\\test.env")
        dotenv.read_dotenv(path_env)
    except (EnvironmentError, FileNotFoundError):
        print("Couldn't retrieve the environment variables")


def pytest_unconfigure():
    # Remove the copied template files after test
    remove("django_invoicing/django_invoicing/templates/base.html")
