from os import remove
from pathlib import Path
from shutil import copy

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


def pytest_unconfigure():
    # Remove the copied template files after test
    remove("django_invoicing/django_invoicing/templates/base.html")
