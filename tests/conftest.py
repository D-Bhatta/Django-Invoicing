from os import remove
from shutil import copy, rmtree


def pytest_configure():
    copy(
        "django_invoicing/django_apps/templates/base.html",
        "django_invoicing/django_invoicing/templates/",
    )


def pytest_unconfigure():
    remove("django_invoicing/django_invoicing/templates/base.html")
